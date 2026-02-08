---
type: decision
date: 2026-02-08
status: codified
urgency: high
---

# OTO 1: Single Sprint Option (Kill Self-Paced)

## Situation

OTO 1 previously offered two options at the same step:
- Option 1: Self-Paced ($97 → $70 after $27 credit)
- Option 2: 4-Week Sprint ($297 → $270 after $27 credit)

Reviewed whether this was optimal for V1.0 launch.

## Research

### Miles Stutz (OTO Architecture)
- His OTO flow is always OTO1 → Downsell → OTO2 → Downsell. One thing at one price at each step. Never two parallel options.
- No-Phone Offer principle: "The offer itself must be clear enough for an instant yes/no decision." Two options turns yes/no into comparison shopping.
- His live coaching only appears at premium backend ($1,997 D4Y), not mid-funnel. But our funnel is smaller and we need testimonials now.
- "Don't think OTOs until bumps are carrying."

### Cat Howell (Testing & Conversion)
- "Add upsells sequentially. Don't launch multiple at once."
- 30 sales minimum per option to evaluate. Two options splits the sample.
- OTOs above $60 convert at 10-20%.

### Self-Paced Implementation Problem
- Our own copy says "9/10 people spend weeks building funnels... Many never launch at all" — that's literally describing self-paced buyers.
- Self-paced buyers don't implement → no testimonials → hurts flywheel.
- V1.0 needs results and case studies. Sprint's accountability structure produces those.

## Options

### A: Keep two options (rejected)
**Pros:** Lower price point captures more buyers, higher total conversion rate.
**Cons:** Decision fatigue, can't test cleanly, self-paced buyers don't implement, dilutes Sprint positioning.

### B: Sprint only at $270 (selected)
**Pros:** Clean yes/no, everyone gets accountability, higher implementation rate, more testimonials, follows Miles/Cat OTO architecture.
**Cons:** Higher price may lower conversion rate. But Sprint buyers are more valuable.

### C: Sequential (self-paced as OTO1, Sprint as OTO2) (considered for future)
**Pros:** Follows Miles' exact architecture. Each step is clean yes/no.
**Cons:** More complex funnel to build. Can revisit after V1.0 validation.

## Decision

**Sprint only at $270.** Single option. Clean yes/no. Everyone who buys gets live support, implements, and produces results we can use as testimonials.

Self-paced content (5 modules) is still delivered — it's included in the Sprint. The modules don't go away; they just come with support now.

Can revisit sequential model (Option C) after V1.0 produces 30+ Sprint sales and we have data.

## What Changes

- `reference/core/offer.md` — Replace two-option Sprint with single $270 Sprint. Update funnel metrics table.
- `outputs/pages/oto1-sprint-full-page-copy.md` — Rewrite to single offer box. Remove Option 1/Option 2 structure. Add dedicated Live Support section. Update hero, opening copy, pricing.
- `outputs/pages/oto1-sprint-landing-page.md` — Will need update to match (not done yet).
- Self-paced product file remains (content is still delivered as part of Sprint).
