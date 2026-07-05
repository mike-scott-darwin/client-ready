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

> **FORMAT PRIORITY — STATIC IMAGE PRIMARY, video secondary** (per Miles benchmark + our funnel data). For a $27 front-end, static image + long-form copy is the proven workhorse — Miles runs **95% static** on his primary low-ticket product. Lead both ad sets with the **Tier-1 static package** (`outputs/ads/2026-07-04-static-ads-tier1-miles-benchmark/`): 5 concepts, same copy across image variants, test the visual. Use the video below for **retargeting/warm only.**
- **Video (secondary / retargeting):** "AD1 – Short form Demo" — screen-demo of running the Zone-of-Genius prompt (ChatGPT) + face cam + **burned-in speech captions**. Hook header: "What If You Could Identify The ONE Problem You're Uniquely Positioned to Solve." CTA: "$27 — link below." Format: 1080×1080, **150s**, says $27 ✅.
- **Primary text (post copy):** the proven Jan26 "red ocean / drowning in sameness / YOU are the differentiator" copy
- **CTA button:** LEARN MORE → clientreadyoffer.com
- **Upload:** upload this $27 file fresh via upload_ad_video_file (do NOT reuse account `video_id 4212384302347414` — that was the old $17 cut).
- **Cold vs warm cuts:**
  - **Cold prospecting (Ad Sets A/B):** cut a **30–45s version** — hook → one prompt → the AI "wow" output (zoomed for mobile) → CTA. 150s is too long for cold.
  - **Warm / retargeting:** use the full 150s demo.
- **Fix before scaling:** zoom into the ChatGPT output moment (mobile readability — the proof shot is currently unreadable on phones).

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
