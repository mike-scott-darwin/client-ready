---
type: decision
date: 2026-02-14
status: codified
---

# Info Products Congruence Audit

## Situation

Before emailing info products to buyers, audited all 7 product files in `outputs/products/` against core reference files (offer.md, voice.md, soul.md, audience.md) for congruency.

## Issues Found & Fixed

### Critical (3)

1. **Wrong product name in 3 files** — "$67 Offer Validation Kit" appeared in front-end, bump-1, and bump-2 cross-sell sections. The actual $67 product is "The First $5K Client Playbook" (pricing psychology, conversation frameworks, Warm 50). Fixed name and description in all 3 files.

2. **Internal production workflow exposed in Blueprint** — `oto2-done-for-you-funnel.md` contained 370+ lines of internal AI generation workflow including the master prompt and "$80-100/hour effective rate" analysis. Removed from client-facing file. Preserved in `outputs/products/internal/blueprint-generation-workflow.md`.

3. **"$397 DFY" terminology contradicted positioning** — Used in both Blueprint and Accelerator files. offer.md explicitly says "strategy + copy + GHL snapshot, not a fully built live funnel." Fixed to "$397 Blueprint" in both files, updated comparison table in Accelerator FAQ.

### Important (4)

4. **Income claim in DM Scripts (FTC risk)** — "potentially $2K-$10K from 15 minutes per day of DMs" from a $17 product with no typicality data. Changed to "1-2 sales from 15 minutes per day of warm outreach."

5. **Unsubstantiated "80-90% bump rates" claim** — Accelerator stated this as a result of Andromeda approach with no data. Changed to "stronger bump take rates."

6. **WhatsApp vs. Slack inconsistency** — Accelerator weekly pattern said "SLACK" but rest of file and offer.md say WhatsApp. Fixed to WhatsApp.

7. **"Retargeting campaign live" in Sprint Week 3** — Sprint buyers don't have existing traffic to retarget. Changed to "First campaign live."

### Minor (noted, not all changed)

8. **"install offer recovery" → "bump recovery"** in Blueprint copy pack list. Fixed.

9. **Blueprint FAQ tech mention** — Referenced ClickFunnels/Kajabi/WordPress when system is GHL-based. Fixed to reference GHL.

10. **Bump 2 delivers more than offer.md lists** — Includes Awareness Level Messaging Map and Promo templates not in offer.md. Over-delivery, not a problem. offer.md should be updated to reflect actual contents (deferred).

11. **Blueprint filename** — `oto2-done-for-you-funnel.md` is legacy name. Not renamed to avoid breaking references.

## What Changed

Files modified:
- `outputs/products/front-end-client-ready-offer-system.md` — Fixed $67 product name
- `outputs/products/bump-1-quick-win-dm-scripts.md` — Fixed $67 product name + removed income claim
- `outputs/products/bump-2-plug-and-play-templates.md` — Fixed $67 product name
- `outputs/products/oto1-client-ready-sprint-4-week.md` — Fixed retargeting → first campaign
- `outputs/products/oto2-done-for-you-funnel.md` — Fixed bump recovery terminology, FAQ tech mention, removed internal section
- `outputs/products/backend-client-ready-accelerator.md` — Fixed DFY → Blueprint, removed 80-90% claim, fixed Slack → WhatsApp

Files created:
- `outputs/products/internal/blueprint-generation-workflow.md` — Internal workflow preserved

## Voice & Soul Congruency

All 7 products passed voice and soul checks:
- Direct, practical, no-BS tone throughout
- No guru language (revolutionary, incredible, game-changer, etc.)
- Anti-guru positioning maintained consistently
- "You can't grow into pain" philosophy properly woven into front-end
- Transformation arc (Confused → Clear → Converting) consistent
- Guide-not-guru framing respected across all tiers

## Remaining (Deferred)

- Update offer.md Bump 2 description to match actual product contents
- Rename `oto2-done-for-you-funnel.md` → `oto2-client-ready-blueprint.md` (coordinate with any references)
