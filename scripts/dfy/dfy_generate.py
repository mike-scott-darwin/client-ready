#!/usr/bin/env python3
"""
DFY Offer Build — generation core (Step 3 of the DFY pipeline).

Takes a buyer's 11-question intake, calls Claude with the canonical system
prompt, and returns the six deliverables as markdown. This is the engine the
OTO1 ($197) DFY Offer Build and DFY Lite ($97) run on.

The system prompt is read live from the repo so the code and the doc never
drift:
    outputs/dfy-upsell/system-prompt.md   (the ``` fenced block)

Usage:
    # From a JSON intake file (see sample-intake.json for the shape):
    python3 dfy_generate.py --in intake.json --out build.md

    # DFY Lite (deliverables 1-2 only):
    python3 dfy_generate.py --in intake.json --out build.md --lite

    # Read JSON from stdin, write markdown to stdout:
    cat intake.json | python3 dfy_generate.py

Requires:
    pip3 install anthropic

Environment variables:
    ANTHROPIC_API_KEY  - or an `ant auth login` profile
    DFY_MODEL          - override the model (default: claude-sonnet-5)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Repo root = two levels up from scripts/dfy/
REPO_ROOT = Path(__file__).resolve().parents[2]
SYSTEM_PROMPT_DOC = REPO_ROOT / "outputs" / "dfy-upsell" / "system-prompt.md"

# Sonnet 5 = best quality/cost balance for this use case (per the DFY docs).
# Opus 4.8 (claude-opus-4-8) for max quality at ~3x cost.
DEFAULT_MODEL = os.environ.get("DFY_MODEL", "claude-sonnet-5")
MAX_TOKENS = 16000

# The 11 intake fields + optional content links, in prompt order.
FIELDS = [
    ("what_you_do", "What they do"),
    ("best_client", "Their best client"),
    ("result", "The result they deliver"),
    ("process", "Their process"),
    ("differentiator", "What makes them different"),
    ("story", "Their story"),
    ("pricing", "Current and desired pricing"),
    ("stuck_point", "What's stopping them"),
    ("client_language", "How their clients describe the problem (in their own words)"),
    ("failed_solutions", "What their clients tried before that didn't work"),
    ("objections", "Objections people have before buying"),
    ("content_links", "Links to best-performing content (optional)"),
]

LITE_INSTRUCTION = (
    "\n\nThis is a DFY Lite order. Generate only Deliverable 1 (ICP) and "
    "Deliverable 2 (Offer Document). Skip deliverables 3-6 (Google Offer Doc, "
    "Sales Page, Email Sequence, Ad Hooks)."
)


def load_system_prompt(doc_path: Path = SYSTEM_PROMPT_DOC) -> str:
    """Extract the system prompt from the first ``` fenced block in the doc."""
    text = doc_path.read_text(encoding="utf-8")
    match = re.search(r"```\s*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        raise ValueError(f"No fenced system-prompt block found in {doc_path}")
    return match.group(1).strip()


def build_user_message(intake: dict, lite: bool = False) -> str:
    """Assemble the user message from the intake answers."""
    lines = ["Build the six deliverables for this person based on their "
             "questionnaire answers.", "", "## Their Answers", ""]
    for key, label in FIELDS:
        value = (intake.get(key) or "").strip() or "(not provided)"
        lines.append(f"**{label}:**")
        lines.append(value)
        lines.append("")
    message = "\n".join(lines).rstrip()
    if lite:
        message += LITE_INSTRUCTION
    return message


def generate(intake: dict, lite: bool = False, model: str = DEFAULT_MODEL) -> str:
    """Run the Claude generation and return the deliverables markdown."""
    import anthropic

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY or an ant profile
    system_prompt = load_system_prompt()
    user_message = build_user_message(intake, lite=lite)

    # Stream to stay under the SDK's non-streaming HTTP-timeout guard at 16k.
    # No temperature/top_p — Sonnet 5 / Opus 4.8 reject non-default sampling.
    # Thinking disabled for predictable per-order cost; flip to
    # {"type": "adaptive"} for higher-quality copy at higher token cost.
    with client.messages.stream(
        model=model,
        max_tokens=MAX_TOKENS,
        thinking={"type": "disabled"},
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        message = stream.get_final_message()

    if message.stop_reason == "refusal":
        raise RuntimeError("Generation refused by safety classifier; review the intake.")

    return "".join(b.text for b in message.content if b.type == "text").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a DFY offer build from an intake.")
    parser.add_argument("--in", dest="infile", help="Intake JSON file (default: stdin)")
    parser.add_argument("--out", dest="outfile", help="Output markdown file (default: stdout)")
    parser.add_argument("--lite", action="store_true", help="DFY Lite — deliverables 1-2 only")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    raw = Path(args.infile).read_text(encoding="utf-8") if args.infile else sys.stdin.read()
    try:
        intake = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid intake JSON: {e}", file=sys.stderr)
        return 1

    result = generate(intake, lite=args.lite, model=args.model)

    if args.outfile:
        Path(args.outfile).write_text(result, encoding="utf-8")
        print(f"Wrote {len(result)} chars to {args.outfile}", file=sys.stderr)
    else:
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
