#!/usr/bin/env python3
"""
DFY campaign generator — the headless `co-campaign` step.

Reads a per-buyer vault's context files (seeded by dfy_seed_vault.py) and
generates deliverables 3-6 into the vault's campaigns/ folder. Because every
asset is generated from the SAME offer/audience/voice/soul, the mechanism name,
signature reframes, verbatim client language, and numbers stay consistent by
construction — the alignment win over the monolithic generator.

    Deliverable 3  One-Page Sales Weapon   (warm DM/email doc)
    Deliverable 4  Plug-and-Play Sales Page (cold landing)
    Deliverable 5  Buyer-to-Client Email Machine (5 emails)
    Deliverable 6  5 Scroll-Stopping Ad Hooks

(Deliverables 1 & 2 are already the vault's core/audience.md and core/offer.md.)

Usage:
    python3 dfy_build_campaign.py --vault ../../outputs/dfy-runs/<slug>
    python3 dfy_build_campaign.py --vault <dir> --lite   # skip 3-6 (Lite = 1-2 only)

Requires:
    pip3 install anthropic
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import dfy_generate as core

CORE_FILES = ("offer", "audience", "voice", "soul")

# name -> (delimiter key, output filename stem, deliverable label)
ASSETS = {
    "ad_hooks": ("2026-XX-ad-hooks", "6 — 5 Scroll-Stopping Ad Hooks"),
    "email_sequence": ("2026-XX-email-sequence", "5 — Buyer-to-Client Email Machine"),
    "sales_weapon": ("2026-XX-sales-weapon", "3 — One-Page Sales Weapon (warm)"),
    "landing_page": ("2026-XX-landing-page", "4 — Plug-and-Play Sales Page (cold)"),
}

GENERATION_SYSTEM = """\
You are the Client Ready campaign generator. You are handed four context files
for one coach — offer, audience, voice, soul — already extracted and validated.
Generate four ready-to-use deliverables, GROUNDED IN THOSE FILES. Every asset
must use the SAME offer name, the SAME named mechanism, the SAME transformation,
and mirror the clients' verbatim language from the voice file. Write in THEIR
voice with Michael Scott's directness underneath: short lines, no hype, anti-guru
(avoid: revolutionary, crush it, hustle, guru, game-changer, passive income).
Never invent testimonials or income claims — use [bracketed placeholders].

Output EXACTLY four blocks in this wrapper format and order:

<<<FILE:ad_hooks>>>
# 5 Ad Hooks
Five hooks across awareness levels — Aware, Solution-aware, Problem-aware,
Curiosity, Contrarian. Each: one punchy hook line + a suggested format
(face-to-camera / text-on-background / B-roll / silent). Use the mechanism name
and the clients' verbatim words.
<<<END>>>
<<<FILE:email_sequence>>>
# 5-Email Sequence
Welcome, Story, Common mistake, Social proof (with a testimonial placeholder),
Direct pitch. Each email: Subject + Preview + short body ending in a CTA.
<<<END>>>
<<<FILE:sales_weapon>>>
# One-Page Sales Weapon (warm)
A copy-paste DM/email for their warm audience. SHORT lines, not paragraphs.
Headline; who it's for (use best-client language); tease the 3 mechanism steps;
their backstory in fragments; contrast-with-proof (placeholder); benefits using
client language; what you get; push/who-it's-not-for; CTA = a keyword reply (not
a link); price reveal.
<<<END>>>
<<<FILE:landing_page>>>
# Plug-and-Play Sales Page (cold)
A full cold-traffic landing page, scannable with clear subheads: Hero
(headline+subhead+CTA); The Problem; Why the usual fixes fail; The Solution /
Mechanism; What's Included; Who it's for / not for; About; Proof (placeholder);
FAQ (from objections); Pricing + Guarantee; Final CTA.
<<<END>>>
"""


def load_context(vault_dir: Path) -> str:
    core_dir = vault_dir / "core"
    parts = []
    for name in CORE_FILES:
        path = core_dir / f"{name}.md"
        if not path.exists():
            raise FileNotFoundError(f"Missing context file: {path} — run dfy_seed_vault.py first.")
        parts.append(f"# === core/{name}.md ===\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def build_campaign(vault_dir: Path, model: str = core.DEFAULT_MODEL,
                   stamp: str | None = None) -> list[Path]:
    context = load_context(vault_dir)
    user_message = ("Generate the four deliverables from these context files.\n\n"
                    + context)
    raw = core.complete(GENERATION_SYSTEM, user_message, model=model)
    sections = core.split_sections(raw)

    missing = [k for k in ASSETS if k not in sections]
    if missing:
        raise RuntimeError(f"Generator omitted assets: {missing}\n\n{raw[:500]}")

    stamp = stamp or date.today().isoformat()
    campaigns = vault_dir / "campaigns"
    campaigns.mkdir(exist_ok=True)
    written = []
    for key, (_, label) in ASSETS.items():
        stem = key.replace("_", "-")
        path = campaigns / f"{stamp}-{stem}.md"
        header = (f"---\ntype: output\nformat: {stem}\ndate: {stamp}\n"
                  f'deliverable: "{label}"\n'
                  "source_files: [core/offer.md, core/audience.md, core/voice.md, core/soul.md]\n---\n\n")
        path.write_text(header + sections[key].strip() + "\n", encoding="utf-8")
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate DFY deliverables 3-6 from a seeded vault.")
    parser.add_argument("--vault", required=True, help="Per-buyer vault directory")
    parser.add_argument("--model", default=core.DEFAULT_MODEL)
    parser.add_argument("--date", dest="stamp", help="Date stamp for filenames (default: today)")
    parser.add_argument("--lite", action="store_true", help="DFY Lite — skip 3-6 (1-2 are the vault)")
    args = parser.parse_args()

    vault_dir = Path(args.vault).resolve()
    if args.lite:
        print("DFY Lite: deliverables 1-2 are core/audience.md + core/offer.md. Nothing to generate.",
              file=sys.stderr)
        return 0

    written = build_campaign(vault_dir, model=args.model, stamp=args.stamp)
    print(f"Generated {len(written)} deliverables in {vault_dir / 'campaigns'}:", file=sys.stderr)
    for p in written:
        print(f"  {p.relative_to(core.REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
