---
type: decision
status: active
date: 2026-07-04
trigger: Jan26/Oct25 ad data — $150 CPM on narrow Tier-1 was the real cost driver, not the page
linked_data:
  - Meta act_463860554507371 — Oct25 geo split + Jan26 CBO/ABO
  - Meta act_463860554507371 — winning creative Ad10 (video "red ocean / unfair advantage")
linked_spec: outputs/ads/campaign-spec-geo-cpm.md
related:
  - decisions/2026-07-04-front-end-27-digital-snack.md
  - decisions/2026-07-04-bump-revamp-value-added.md
---

# Decision: Geo/CPM Restructure — Broad Tier-1+2 English, Seed the Pixel

> The biggest cost lever in the funnel is **CPM**, not the sales page. Restructure paid to broad Tier-1 + high-intent Tier-2 English geos, drop narrow interest stacks, and seed the pixel — target CPA ~$88 to hit the self-liquidation line.

## The evidence (from live data)

Oct25 A/B'd geo; Jan26 ran Tier-1-only. CPA / AOV per segment:

| Segment | CPM | CPC | AOV/buyer | CPA |
|---|-----|-----|-----------|-----|
| Cold — Worldwide | $8 | $0.33 | ~$11 | $93 |
| Cold — AU/CA/US (narrow) | $159 | $2.51 | ~$11 | $272 |
| Cold — Interest (narrow) | $140 | $2.74 | ~$11 | $266 |
| Jan26 — Tier-1 CBO | $150 | $3.64 | ~$41 | $163 |
| Jan26 — Tier-1 ABO | $149 | $3.78 | ~$36 | $91 |

**Read:** Worldwide = cheap CPA but ~$11 buyers who never ascend (worthless for the $47/mo backend). Tier-1 = ~$41 buyers (4× value) but $150 CPM. The $150 CPM was caused by **narrow targeting** (1,700–1,900 impression audiences) and an **under-fed purchase pixel**, NOT by the geo being inherently unaffordable.

## The decision

1. **Geo — 3 tiers, exclude worldwide:**
   - Tier 1 (core): US · CA · UK · AU · NZ
   - Tier 2 (expansion, ~30–50% cheaper CPM): Ireland · Singapore · South Africa · Nordics (SE/DK/NO/FI)
   - Exclude pure worldwide / low-income geos (the ~$11-buyer trap)
2. **Targeting — broad, not narrow.** Advantage+ audience in Tier-1+2. This is the biggest CPM cut ($150 → ~$50 expected).
3. **Placements — Advantage+** (no feed-only hand-picking) to pull avg CPM down via Reels/Audience Network.
4. **Creative — the video winner (Ad10, "red ocean / unfair advantage").** Video CPM < static; its 4%+ CTR lowers effective CPC.
5. **Seed the pixel.** Until ~50 purchases/week, optimize for **Initiate Checkout**; switch to Purchase once volume supports it.

## Why (the math closes the loop)

| Metric | Jan26 now | After fix |
|--------|-----------|-----------|
| CPM | $150 | ~$50 |
| CPC | $3.65 | ~$1.75 |
| CVR | 2% | 2% |
| **CPA** | **$182** | **~$88** |

~$88 CPA is exactly the self-liquidation line for the revamped bumps (~$88 AOV at 50/35/20). **Bump revamp fixes AOV; geo/CPM fixes CPA; together the front-end + bumps self-liquidate — without touching the 2% page.**

## Guardrails / prerequisites

- **Non-negotiable:** confirm Purchase + bump events fire via **CAPI** before spending. Oct25 ran with zero tracking — unmeasurable.
- **Kill rule:** any geo with CPA > $100 after ~$150 spend.
- **Don't chase worldwide** for the cheap CPM — it imports non-ascending buyers. Judge on blended 90-day value, not CPA alone.
- This is a test grounded in prior data, not a guarantee. Validate CPM/CPC assumptions in the first $500 of spend.

## Not changed

Front-end ($27), bump prices, offer structure, sales page. This decision is about **traffic economics only**.
