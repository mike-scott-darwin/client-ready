#!/usr/bin/env python3
"""
DFY vault seeder — the headless `co-extract` step.

Turns a buyer's short intake (5 merged questions + a price line + uploaded
supporting docs) into a per-buyer Codify vault: four structured context files
(offer, audience, voice, soul) that every deliverable is then generated from.
This is what makes the six deliverables aligned by construction.

Uploaded documents (the buyer's real sales page, testimonials, About page, call
transcripts, screenshots) are fetched and fed to the extractor as native
document/image blocks, so it mines the buyer's ACTUAL language and proof rather
than working from thin text-box answers. Supports PDF, text/markdown/HTML,
images (png/jpg/gif/webp), and .docx (if python-docx is installed).

Two of the four output files ARE deliverables:
    core/audience.md -> Deliverable 1 (Dream Client Blueprint / ICP)
    core/offer.md    -> Deliverable 2 (Your Validated Offer)

Run dfy_build_campaign.py next to produce deliverables 3-6 from this vault.

Usage:
    python3 dfy_seed_vault.py --in intake.json                      # docs from intake["documents"] + *_upload keys
    python3 dfy_seed_vault.py --in intake.json --doc sales.pdf --doc https://site.com/about
    python3 dfy_seed_vault.py --in intake.json --slug acme

Requires:
    pip3 install anthropic          # ANTHROPIC_API_KEY or an `ant auth login` profile
    pip3 install python-docx        # optional — only to read .docx uploads
"""

import argparse
import base64
import json
import mimetypes
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import dfy_generate as core

VAULTS_DIR = core.REPO_ROOT / "outputs" / "dfy-runs"
CORE_FILES = ("offer", "audience", "voice", "soul")

# Stay well under the 32MB request limit per file, and cap extracted text.
MAX_DOC_BYTES = 25 * 1024 * 1024
MAX_TEXT_CHARS = 20000
IMAGE_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
               ".gif": "image/gif", ".webp": "image/webp"}

EXTRACTION_SYSTEM = """\
You are the Client Ready context extractor. Turn a coach or service provider's
intake into four structured Codify context files. You are NOT writing marketing
copy yet — you are building the SUBSTRATE all their deliverables get generated
from, so it must be specific, grounded, and internally consistent.

You may also receive the buyer's own uploaded materials — their sales page,
testimonials, About page, call transcripts, screenshots. MINE THEM: pull the
buyer's real language, real proof, mechanism details, and pricing, and lift
verbatim client quotes for the voice file. Prefer their actual words over
anything generic. Uploaded proof is real proof; do not invent additional
testimonials or income claims — use [bracketed placeholders] where proof is
missing.

Follow the Client Ready method: zone of genius first, one problem / one audience
/ one offer, clarity over hype. Name the mechanism (their process) with a clear,
non-hype name and 3-4 steps. Anchor the ICP on their best-client answer. Derive
the core belief from their story. If an answer is thin, make the strongest
defensible interpretation and keep it tight.

Output EXACTLY four blocks, each markdown (headings, short sections), no
preamble, in this wrapper format and order:

<<<FILE:offer>>>
# Offer
(one-line pitch; The Problem; The Mechanism — named, 3-4 steps; The
Transformation before->after; What's Included; Pricing Recommendation with
reasoning; Guarantee; Objection Handling; The Bridge to a higher-ticket offer)
<<<END>>>
<<<FILE:audience>>>
# Audience — Dream Client Blueprint
(one-line "you help WHO achieve WHAT by HOW"; The Anchor Client from their best
client; Demographics; Psychographics incl. clients' verbatim words; Awareness
Level; Buying Triggers; Where They Hang Out; Disqualifiers)
<<<END>>>
<<<FILE:voice>>>
# Voice
(Tone; Signature moves; Words to USE; Words to AVOID; Client language to mirror
verbatim)
<<<END>>>
<<<FILE:soul>>>
# Soul
(The core belief; The story it comes from; Why it matters)
<<<END>>>
"""

FRONTMATTER = {
    "offer": '---\ntype: reference\nstatus: active\nsource: {src}\ndeliverable: "2 — Your Validated Offer"\n---\n\n',
    "audience": '---\ntype: reference\nstatus: active\nsource: {src}\ndeliverable: "1 — Dream Client Blueprint (ICP)"\n---\n\n',
    "voice": '---\ntype: reference\nstatus: active\nsource: {src}\nnote: "The buyer\'s natural voice, with Michael\'s directness underneath."\n---\n\n',
    "soul": '---\ntype: reference\nstatus: active\nsource: {src}\nnote: "The belief the offer is built on."\n---\n\n',
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")
    return slug or "buyer"


def collect_documents(intake: dict) -> list:
    """Doc sources = intake['documents'] + any *_upload / *_url URL values (GHL uploads)."""
    docs = list(intake.get("documents") or [])
    for key, val in intake.items():
        if (isinstance(val, str) and val.startswith(("http://", "https://"))
                and (key.endswith("_upload") or key.endswith("_url"))):
            docs.append(val)
    return list(dict.fromkeys(docs))  # dedupe, keep order


def _fetch_bytes(src: str):
    """Return (data, content_type, name) for a URL or local path."""
    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(src, headers={"User-Agent": "dfy-seeder"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read(), (resp.headers.get_content_type() or ""), src
    path = Path(src)
    return path.read_bytes(), (mimetypes.guess_type(path.name)[0] or ""), path.name


def load_document_block(src: str):
    """Fetch a doc and return a Claude content block (or None if unsupported)."""
    try:
        data, ctype, name = _fetch_bytes(src)
    except Exception as e:  # noqa: BLE001 — one bad upload shouldn't kill the run
        print(f"[warn] could not fetch {src}: {e}", file=sys.stderr)
        return None
    if len(data) > MAX_DOC_BYTES:
        print(f"[warn] skipping {name}: {len(data)} bytes exceeds cap", file=sys.stderr)
        return None

    ext = Path(urllib.parse.urlparse(src).path or name).suffix.lower()
    b64 = lambda: base64.standard_b64encode(data).decode()

    if ext == ".pdf" or "pdf" in ctype:
        return {"type": "document",
                "source": {"type": "base64", "media_type": "application/pdf", "data": b64()}}
    if ext in IMAGE_TYPES or ctype.startswith("image/"):
        return {"type": "image",
                "source": {"type": "base64", "media_type": IMAGE_TYPES.get(ext, ctype), "data": b64()}}
    if ext in (".txt", ".md", ".csv", ".html", ".htm") or ctype.startswith("text/"):
        text = data.decode("utf-8", "ignore")
        if ext in (".html", ".htm") or "html" in ctype:
            text = re.sub(r"<[^>]+>", " ", text)          # crude tag strip
            text = re.sub(r"[ \t]+", " ", text)
        return {"type": "text", "text": f"--- Uploaded: {name} ---\n{text.strip()[:MAX_TEXT_CHARS]}"}
    if ext == ".docx":
        try:
            import io
            import docx
            doc = docx.Document(io.BytesIO(data))
            text = "\n".join(p.text for p in doc.paragraphs)
            return {"type": "text", "text": f"--- Uploaded: {name} ---\n{text.strip()[:MAX_TEXT_CHARS]}"}
        except Exception as e:  # noqa: BLE001
            print(f"[warn] skipping {name}: install python-docx to read .docx ({e})", file=sys.stderr)
            return None
    print(f"[warn] skipping {name}: unsupported type ({ext or ctype})", file=sys.stderr)
    return None


def seed_vault(intake: dict, vault_dir: Path, model: str = core.DEFAULT_MODEL,
               documents=None) -> Path:
    """Extract the four context files (from answers + docs) into vault_dir/core/."""
    documents = documents if documents is not None else collect_documents(intake)

    # Docs first (better model attention on PDFs), then the answers text last.
    content = []
    for src in documents:
        block = load_document_block(src)
        if block:
            content.append(block)
    answers = ("Build the four context files from this buyer's intake. Uploaded "
               "documents (above) are their real materials — mine them for verbatim "
               "language and proof.\n\n" + core.format_answers(intake))
    content.append({"type": "text", "text": answers})

    raw = core.complete(EXTRACTION_SYSTEM, content, model=model)
    sections = core.split_sections(raw)
    missing = [f for f in CORE_FILES if f not in sections]
    if missing:
        raise RuntimeError(f"Extractor omitted context files: {missing}\n\n{raw[:500]}")

    core_dir = vault_dir / "core"
    core_dir.mkdir(parents=True, exist_ok=True)
    (vault_dir / "campaigns").mkdir(exist_ok=True)
    src_label = f"DFY intake — {vault_dir.name}"
    for name in CORE_FILES:
        body = sections[name].strip()
        (core_dir / f"{name}.md").write_text(
            FRONTMATTER[name].format(src=src_label) + body + "\n", encoding="utf-8")
    return core_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed a per-buyer Codify vault from a DFY intake.")
    parser.add_argument("--in", dest="infile", required=True, help="Intake JSON file")
    parser.add_argument("--doc", dest="docs", action="append", default=[],
                        help="Supporting doc URL or path (repeatable)")
    parser.add_argument("--slug", help="Vault name (default: derived from the intake)")
    parser.add_argument("--model", default=core.DEFAULT_MODEL)
    args = parser.parse_args()

    intake = json.loads(Path(args.infile).read_text(encoding="utf-8"))
    documents = list(dict.fromkeys(args.docs + collect_documents(intake)))
    slug = args.slug or slugify(intake.get("best_client") or intake.get("email") or "buyer")[:40]
    vault_dir = VAULTS_DIR / slug

    core_dir = seed_vault(intake, vault_dir, model=args.model, documents=documents)
    print(f"Seeded vault: {vault_dir}  ({len(documents)} doc(s) ingested)", file=sys.stderr)
    for f in sorted(core_dir.glob("*.md")):
        print(f"  {f.relative_to(core.REPO_ROOT)}", file=sys.stderr)
    print(f"\nNext: python3 dfy_build_campaign.py --vault {vault_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
