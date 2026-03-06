---
type: reference
status: active
date: 2026-03-06
---

# Weekly Positioning Check — Bot Instructions

Runs every Sunday at 6:00 AM. Catches drift before it compounds.

## Part 1 — Ghost Test

Answer these 3 questions "as Mike" using ONLY the reference files.
Do NOT use web search or outside knowledge.

Read these files first:
- /Users/michaelscott/Documents/GitHub/client-ready/reference/core/soul.md
- /Users/michaelscott/Documents/GitHub/client-ready/reference/core/offer.md
- /Users/michaelscott/Documents/GitHub/client-ready/reference/core/audience.md
- /Users/michaelscott/Documents/GitHub/client-ready/reference/core/voice.md

Then answer:

1. "What do you do and who do you help?"
2. "Why should someone buy from you instead of the 50 other coaches?"
3. "What happens if someone does nothing — what's the cost of staying stuck?"

After answering, evaluate your own answers:
- Do they sound SPECIFIC to Client Ready, or could any coach have said them?
- Are there concrete details (numbers, mechanisms, specific pain points)?
- Does the voice match voice.md (direct, no-BS, anti-guru)?

If any answer sounds generic, flag which reference file needs enrichment
and what's missing.

## Part 2 — Cadence Drift Check

Read /Users/michaelscott/Documents/GitHub/client-ready/reference/domain/content-strategy.md
to get the STATED publishing cadence.

Then check actual publishing activity:
- Run: git -C /Users/michaelscott/Documents/GitHub/client-ready log --since="30 days ago" --oneline --name-only
- Count content files created in outputs/, content/published/, content/drafts/
- Compare stated cadence vs actual output over the last 30 days

Flag any gaps:
- Stated "3-5 tweets daily" but only published 2 tweets last week
- Stated "weekly newsletter" but no newsletter in 3 weeks
- Any pillar with zero content in the last 30 days

## Part 3 — Send Report

Send a single Telegram message:

WEEKLY POSITIONING CHECK

GHOST TEST RESULTS:
- Q1 (What do you do): [PASS/NEEDS WORK] — [brief note]
- Q2 (Why you): [PASS/NEEDS WORK] — [brief note]
- Q3 (Cost of inaction): [PASS/NEEDS WORK] — [brief note]

REFERENCE GAPS (if any):
- [which file]: [what's missing or too generic]

CADENCE CHECK:
- Stated: [what content-strategy.md says]
- Actual (last 30 days): [what actually happened]
- Gaps: [what's behind schedule]

RECOMMENDATION:
[One sentence on what to prioritize this week]

## Rules

1. Be honest — if reference files are weak, say so
2. Compare against REAL output, not intentions
3. Keep the report under 500 words
4. This is a diagnostic, not a task list — surface problems, don't fix them
