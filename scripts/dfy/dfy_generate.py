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

# Minimal 5-question intake (merged from the original 11) + a price line + a
# catch-all links field. Uploaded docs are handled separately in
# dfy_seed_vault.py. Canonical spec:
# reference/domain/delivery/dfy-intake-questionnaire.md
FIELDS = [
    ("what_you_do", "What you do and who for"),
    ("pricing", "Current price and what you want to charge"),
    ("best_client", "Your best client — before and after (their words)"),
    ("process", "How you actually get them that result"),
    ("story", "Your story and what makes you different"),
    ("objections", "What makes people hesitate, and what they've tried that failed"),
    ("content_links", "Anything else that sounds like you (links, optional)"),
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


def format_answers(intake: dict) -> str:
    """Render the 11 intake answers as a labelled block (no instruction header)."""
    lines = ["## Their Answers", ""]
    for key, label in FIELDS:
        value = (intake.get(key) or "").strip() or "(not provided)"
        lines.append(f"**{label}:**")
        lines.append(value)
        lines.append("")
    return "\n".join(lines).rstrip()


def build_user_message(intake: dict, lite: bool = False) -> str:
    """Assemble the user message for the monolithic (legacy) generator."""
    message = ("Build the six deliverables for this person based on their "
               "questionnaire answers.\n\n" + format_answers(intake))
    if lite:
        message += LITE_INSTRUCTION
    return message


def split_sections(text: str) -> dict:
    """Parse `<<<FILE:name>>> ... <<<END>>>` blocks into {name: body}."""
    out = {}
    for match in re.finditer(r"<<<FILE:(\w+)>>>\s*\n(.*?)\n<<<END>>>", text, re.DOTALL):
        out[match.group(1).strip()] = match.group(2).strip()
    return out


def complete(system: str, user_message: str, model: str = DEFAULT_MODEL,
             max_tokens: int = MAX_TOKENS) -> str:
    """One grounded Claude call. Shared by the monolith, seeder, and campaign.

    Streamed (stays under the SDK's HTTP-timeout guard at large max_tokens);
    no temperature/top_p (Sonnet 5 / Opus 4.8 reject non-default sampling);
    thinking disabled for predictable per-order cost.
    """
    import anthropic

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY or an ant profile
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        thinking={"type": "disabled"},
        system=system,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        message = stream.get_final_message()

    if message.stop_reason == "refusal":
        raise RuntimeError("Refused by safety classifier; review the input.")

    return "".join(b.text for b in message.content if b.type == "text").strip()


def generate(intake: dict, lite: bool = False, model: str = DEFAULT_MODEL) -> str:
    """Legacy monolith: intake -> six deliverables in one call.

    Superseded by the Codify-native pipeline (dfy_seed_vault.py +
    dfy_build_campaign.py), which grounds every deliverable in shared context
    files. Kept as a fallback.
    """
    return complete(load_system_prompt(), build_user_message(intake, lite=lite), model=model)


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
