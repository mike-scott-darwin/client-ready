---
type: output
status: buildable-spec
date: 2026-07-04
account: act_463860554507371 (Michael Scott)
decision: decisions/2026-07-04-geo-cpm-restructure.md
---

# Campaign Spec — Geo/CPM Restructure (buildable)

Ready-to-build structure for the geo/CPM test. Build **paused**, review, then flip live.

## Campaign
- **Name:** `CRO - Sales - Geo/CPM Test - Jul26`
- **Objective:** Sales (Purchase) — OR **Leads/Engagement optimizing Initiate Checkout** if <50 purchases/week (seed phase)
- **Budget type:** CBO (Advantage+ campaign budget)
- **Daily budget:** $50–100/day (recommend $75 to start)
- **Bid strategy:** Highest volume (no cap) during learning

## Ad Set A — Broad Tier-1
- **Name:** `Broad - Tier1 - US/CA/UK/AU/NZ`
- **Geo:** United States, Canada, United Kingdom, Australia, New Zealand
- **Audience:** Advantage+ (broad) — no interest stacking
- **Age/gender:** 25–55, all (widen after data)
- **Placements:** Advantage+ (all)
- **Optimization event:** Purchase (or Initiate Checkout in seed phase)

## Ad Set B — Tier-2 English Expansion
- **Name:** `Broad - Tier2 - IE/SG/ZA/Nordics`
- **Geo:** Ireland, Singapore, South Africa, Sweden, Denmark, Norway, Finland
- **Audience:** Advantage+ (broad)
- **Everything else:** same as Ad Set A

## Creative (both ad sets)
- **Winner:** Ad10 video — "Discover Your Unfair Advantage" (video_id `4212384302347414`), the "red ocean / drowning in sameness" hook
- **Primary text:** the proven Jan26 copy (see reference/... or the winning-ad extract)
- **Headline:** "Discover Your Unfair Advantage"
- **CTA:** LEARN MORE → clientreadyoffer.com
- **Note:** update any "$17" price reference in the creative to "$27" before running

## Targets & kill rules
| Metric | Target | Kill |
|--------|--------|------|
| CPM | ~$50 | — |
| CPC | ~$1.75 | — |
| CPA | ≤ $88 | > $100 after ~$150 spend (per geo) |
| Blended 90-day value/buyer | ~$240 | — |

## Prerequisites (before spend)
1. **CAPI / pixel:** confirm Purchase + order-bump events fire cleanly. (Oct25 had none.)
2. **Creative price:** ensure the video/copy says $27, not $17.
3. **Bump test:** Variant C bump copy live (see outputs/order-bumps/ghl-bump-copy.md).

## Open decisions for Michael (needed before building live objects)
- [ ] Daily budget: $50 / $75 / $100?
- [ ] Seed phase (Initiate Checkout) or straight to Purchase?
- [ ] Confirm the pixel ID + that CAPI is firing.
- [ ] Reuse the existing Ad10 creative, or fresh upload?
