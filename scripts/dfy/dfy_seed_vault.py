#!/usr/bin/env python3
"""
DFY vault seeder — the headless `co-extract` step.

Turns a buyer's 11-answer intake into a per-buyer Codify vault: four structured
context files (offer, audience, voice, soul) that every deliverable is then
generated from. This is what makes the six deliverables aligned by construction
instead of by a prompt rule.

Two of the four files ARE deliverables:
    core/audience.md -> Deliverable 1 (Dream Client Blueprint / ICP)
    core/offer.md    -> Deliverable 2 (Your Validated Offer)
The other two (voice, soul) are the substrate that keeps everything sounding
like the buyer.

Run dfy_build_campaign.py next to produce deliverables 3-6 from this vault.

Usage:
    python3 dfy_seed_vault.py --in intake.json                 # slug from best_client/email
    python3 dfy_seed_vault.py --in intake.json --slug acme     # explicit vault name

Requires:
    pip3 install anthropic     # ANTHROPIC_API_KEY or an `ant auth login` profile
"""

import argparse
import json
import re
import sys
from pathlib import Path

import dfy_generate as core

VAULTS_DIR = core.REPO_ROOT / "outputs" / "dfy-runs"

CORE_FILES = ("offer", "audience", "voice", "soul")

EXTRACTION_SYSTEM = """\
You are the Client Ready context extractor. Turn a coach or service provider's
raw intake answers into four structured Codify context files. You are NOT
writing marketing copy yet — you are building the SUBSTRATE that all their
deliverables will be generated from, so it must be specific, grounded, and
internally consistent.

Follow the Client Ready method: zone of genius first, one problem / one audience
/ one offer, clarity over hype. Name the mechanism (their process) with a clear,
non-hype name and 3-4 steps. Anchor the ICP on their best-client answer. Capture
their voice and their clients' VERBATIM language. Derive the core belief from
their story. Never invent testimonials, results, or income claims — use
[bracketed placeholders] where proof is missing. If an answer is vague, make the
strongest defensible interpretation and keep it tight.

Output EXACTLY four blocks, each markdown (headings, short sections), no
preamble, in this wrapper format and order:

<<<FILE:offer>>>
# Offer
(one-line pitch; The Problem; The Mechanism — named, 3-4 steps; The
Transformation before->after; What's Included; Pricing Recommendation with
reasoning; Guarantee; Objection Handling from their objections; The Bridge to a
higher-ticket offer)
<<<END>>>
<<<FILE:audience>>>
# Audience — Dream Client Blueprint
(one-line "you help WHO achieve WHAT by HOW"; The Anchor Client from their best
client; Demographics; Psychographics incl. their clients' verbatim words;
Awareness Level; Buying Triggers; Where They Hang Out; Disqualifiers)
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


def seed_vault(intake: dict, vault_dir: Path, model: str = core.DEFAULT_MODEL) -> Path:
    """Extract the four context files and write them into vault_dir/core/."""
    user_message = ("Build the four context files from this intake.\n\n"
                    + core.format_answers(intake))
    raw = core.complete(EXTRACTION_SYSTEM, user_message, model=model)
    sections = core.split_sections(raw)

    missing = [f for f in CORE_FILES if f not in sections]
    if missing:
        raise RuntimeError(f"Extractor omitted context files: {missing}\n\n{raw[:500]}")

    core_dir = vault_dir / "core"
    core_dir.mkdir(parents=True, exist_ok=True)
    (vault_dir / "campaigns").mkdir(exist_ok=True)  # where deliverables 3-6 land
    src = f"DFY intake — {vault_dir.name}"
    for name in CORE_FILES:
        body = sections[name].strip()
        (core_dir / f"{name}.md").write_text(FRONTMATTER[name].format(src=src) + body + "\n",
                                             encoding="utf-8")
    return core_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed a per-buyer Codify vault from a DFY intake.")
    parser.add_argument("--in", dest="infile", required=True, help="Intake JSON file")
    parser.add_argument("--slug", help="Vault name (default: derived from the intake)")
    parser.add_argument("--model", default=core.DEFAULT_MODEL)
    args = parser.parse_args()

    intake = json.loads(Path(args.infile).read_text(encoding="utf-8"))
    slug = args.slug or slugify(intake.get("best_client") or intake.get("email") or "buyer")[:40]
    vault_dir = VAULTS_DIR / slug

    core_dir = seed_vault(intake, vault_dir, model=args.model)
    print(f"Seeded vault: {vault_dir}", file=sys.stderr)
    for f in sorted(core_dir.glob("*.md")):
        print(f"  {f.relative_to(core.REPO_ROOT)}", file=sys.stderr)
    print(f"\nNext: python3 dfy_build_campaign.py --vault {vault_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
