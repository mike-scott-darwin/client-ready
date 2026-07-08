#!/usr/bin/env python3
"""
fal.ai Ad Creative Generator for Client Ready

Generates ad creative / images from the terminal using fal.ai (Flux models) —
the same setup Devon uses on the BookedOutRoofers build ("I am now using fal.ai
for generating images... I've spent 80 cents and generated like 100 ads").

Usage:
    python3 scripts/fal-image.py --prompt "..." [options]
    python3 scripts/fal-image.py --prompt-file path/to/prompt.txt
    python3 scripts/fal-image.py --angle 9-to-5 [--extra "..."]   # on-message
    python3 scripts/fal-image.py --angle all --model schnell      # full set
    python3 scripts/fal-image.py --list-angles

Options:
    --prompt        TEXT   The image prompt (or use --prompt-file / --angle)
    --prompt-file   PATH   Read the prompt from a file
    --angle         KEY    On-message angle from scripts/ad-prompts.json, or 'all'
    --extra         TEXT   Extra detail appended to an --angle prompt
    --list-angles          Print available angle keys and exit
    --model         NAME   schnell | dev | pro | pro-ultra | <full fal model id>
                           (default: dev)
    --size          NAME   feed|1:1 | story|9:16 | landscape|1.91:1 |
                           square_hd | portrait_16_9 | landscape_16_9 | WxH
                           (default: feed)
    --num           N      Number of images to generate (default: 1)
    --format        FMT    jpeg | png (default: jpeg)
    --out           DIR    Output dir (default: outputs/ad-creative)
    --slug          TEXT   Filename slug (default: derived from prompt)
    --dry-run              Print the request and exit without calling fal

Environment (.env in repo root):
    FAL_KEY  - API key from https://fal.ai/dashboard/keys

Each run writes the image(s) plus a sidecar .json (prompt + params + seed)
so the swipe file is reproducible.
"""

import os
import sys
import json
import re
import argparse
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = REPO_ROOT / ".env"
DEFAULT_OUT = REPO_ROOT / "outputs" / "ad-creative"
LOG_FILE = REPO_ROOT / "scripts" / "fal-image.log"
PROMPTS_FILE = Path(__file__).parent / "ad-prompts.json"

FAL_SYNC_BASE = "https://fal.run"

MODEL_ALIASES = {
    "schnell": "fal-ai/flux/schnell",      # fastest / cheapest
    "dev": "fal-ai/flux/dev",              # good default quality
    "pro": "fal-ai/flux-pro/v1.1",         # pro
    "pro-ultra": "fal-ai/flux-pro/v1.1-ultra",
}

# Friendly names -> fal image_size. Meta ad placements mapped to the
# closest supported aspect ratio.
SIZE_ALIASES = {
    "feed": "square_hd",        # 1:1 feed (1080x1080-ish)
    "1:1": "square_hd",
    "square": "square_hd",
    "story": "portrait_16_9",   # 9:16 story / reels
    "reels": "portrait_16_9",
    "9:16": "portrait_16_9",
    "landscape": "landscape_16_9",
    "1.91:1": "landscape_16_9",
}


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except OSError:
        pass


def load_env():
    if not ENV_FILE.exists():
        log(f"ERROR: .env not found at {ENV_FILE}")
        log("Create it with:  FAL_KEY=your_key_from_https://fal.ai/dashboard/keys")
        sys.exit(1)
    env = {}
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


def load_prompts():
    if not PROMPTS_FILE.exists():
        log(f"ERROR: prompt library not found at {PROMPTS_FILE}")
        sys.exit(1)
    return json.loads(PROMPTS_FILE.read_text())


def build_angle_prompt(lib, key, extra=None):
    """Compose a grounded, on-message prompt for an angle key from the library."""
    angle = lib["angles"][key]
    parts = [angle["prompt"]]
    if extra:
        parts.append(extra)
    parts.append(lib.get("headline_space_suffix", ""))
    parts.append(lib.get("quality_suffix", ""))
    return ", ".join(p.strip() for p in parts if p.strip())


def slugify(text, max_len=40):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len] or "creative"


def resolve_size(size):
    """Return the fal `image_size` value: an enum string or a {width,height} dict."""
    key = size.lower()
    if key in SIZE_ALIASES:
        return SIZE_ALIASES[key]
    m = re.match(r"^(\d+)x(\d+)$", key)
    if m:
        return {"width": int(m.group(1)), "height": int(m.group(2))}
    # Assume the caller passed a raw fal enum (e.g. square_hd, portrait_4_3).
    return size


def build_payload(prompt, size, num, fmt):
    return {
        "prompt": prompt,
        "image_size": resolve_size(size),
        "num_images": num,
        "output_format": fmt,
    }


def call_fal(model_id, payload, api_key):
    url = f"{FAL_SYNC_BASE}/{model_id}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", f"Key {api_key}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        log(f"ERROR: fal returned HTTP {e.code}: {body}")
        sys.exit(1)
    except urllib.error.URLError as e:
        log(f"ERROR: could not reach fal: {e.reason}")
        sys.exit(1)


def download(url, dest):
    try:
        with urllib.request.urlopen(url, timeout=120) as resp:
            dest.write_bytes(resp.read())
    except (urllib.error.URLError, OSError) as e:
        log(f"ERROR: failed to download {url}: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate ad creative with fal.ai (Flux)")
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--angle", help="on-message angle key from ad-prompts.json, or 'all'")
    parser.add_argument("--extra", help="extra detail appended to an --angle prompt")
    parser.add_argument("--list-angles", action="store_true")
    parser.add_argument("--model", default="dev")
    parser.add_argument("--size", default="feed")
    parser.add_argument("--num", type=int, default=1)
    parser.add_argument("--format", default="jpeg", choices=["jpeg", "png"])
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--slug")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.list_angles:
        lib = load_prompts()
        print("Available angles (from scripts/ad-prompts.json):\n")
        for key, a in lib["angles"].items():
            print(f"  {key:<24} {a['label']}")
        return

    # Build the work list: [(prompt, slug), ...]
    jobs = []
    if args.angle:
        lib = load_prompts()
        if args.size == "feed":  # library default size unless caller overrode it
            args.size = lib.get("default_size", "feed")
        keys = list(lib["angles"].keys()) if args.angle == "all" else [args.angle]
        for key in keys:
            if key not in lib["angles"]:
                parser.error(f"unknown angle '{key}' — try --list-angles")
            jobs.append((build_angle_prompt(lib, key, args.extra), args.slug or key))
    elif args.prompt_file:
        prompt = Path(args.prompt_file).read_text().strip()
        jobs.append((prompt, args.slug or slugify(prompt)))
    elif args.prompt:
        prompt = args.prompt.strip()
        jobs.append((prompt, args.slug or slugify(prompt)))
    else:
        parser.error("provide --prompt, --prompt-file, or --angle (see --list-angles)")

    model_id = MODEL_ALIASES.get(args.model, args.model)

    if args.dry_run:
        log(f"DRY RUN — would POST {len(jobs)} job(s) to {FAL_SYNC_BASE}/{model_id}")
        for prompt, slug in jobs:
            print(f"\n[{slug}] ({args.size})")
            print(json.dumps(build_payload(prompt, args.size, args.num, args.format), indent=2))
        return

    env = load_env()
    api_key = env.get("FAL_KEY")
    if not api_key or api_key.startswith("your_"):
        log("ERROR: Missing FAL_KEY in .env")
        log("Get one at https://fal.ai/dashboard/keys and add:  FAL_KEY=...")
        sys.exit(1)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    ext = "png" if args.format == "png" else "jpg"
    total = 0

    for prompt, slug in jobs:
        log(f"Generating {args.num} image(s) for '{slug}' with {model_id} ({args.size})...")
        payload = build_payload(prompt, args.size, args.num, args.format)
        result = call_fal(model_id, payload, api_key)
        images = result.get("images", [])
        if not images:
            log(f"  WARNING: no images returned for '{slug}': {json.dumps(result)[:300]}")
            continue

        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        saved = []
        for i, img in enumerate(images, 1):
            suffix = f"-{i}" if len(images) > 1 else ""
            dest = out_dir / f"{stamp}-{slug}{suffix}.{ext}"
            download(img["url"], dest)
            saved.append(str(dest.relative_to(REPO_ROOT)))
            log(f"  saved {dest.relative_to(REPO_ROOT)}")
            total += 1

        # Sidecar for reproducibility / swipe-file provenance.
        sidecar = out_dir / f"{stamp}-{slug}.json"
        sidecar.write_text(json.dumps({
            "prompt": prompt,
            "angle": args.angle if args.angle and args.angle != "all" else slug if args.angle else None,
            "model": model_id,
            "size": args.size,
            "num_images": args.num,
            "format": args.format,
            "seed": result.get("seed"),
            "images": saved,
            "generated_at": stamp,
        }, indent=2))

    log(f"Done. {total} image(s) in {out_dir.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
