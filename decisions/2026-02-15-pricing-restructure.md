---
type: decision
date: 2026-02-15
status: codified
urgency: high
linked_research:
  - research/2026-02-15-miles-stutz-hot-seat-transcript.md
  - research/2026-02-15-miles-stutz-low-ticket-funnel-data-mining.md
linked_decisions:
  - decisions/2026-02-15-ad-strategy-update-miles-stutz.md
---

# Front-End Pricing Restructure for Self-Liquidating Checkout

## Situation

Ad strategy decision requires front-end to self-liquidate WITHOUT OTOs. At current pricing (27 front-end + 17/37/67 bumps), realistic AOV is 52-58. With likely CPA of 80-120, the funnel loses 40-60 per sale on the front end. That's not self-liquidating.

## Research

Cat Howell data: 47 is her sweet spot. 17 front-end killed AOV. Higher-priced bumps converted BETTER (33/44/55 at 4.0% vs 17/33/55 at 2.3%).

Miles Stutz data: 95 CPA on 17 product. 45 CPA on 9 product. Higher price = higher CPA but not proportionally.

Giovanni data: 47 product converting at 3.8% organic with 57.86 AOV (weak bumps though — only 2 bump sales out of 59).

## Decision

Raise all front-end prices:

**Before:**
- Front-end: 27
- Bump 1 (DM Scripts): 17
- Bump 2 (Templates): 37
- Bump 3 (5K Playbook): 67
- Max checkout: 148
- Realistic AOV: 52-58

**After:**
- Front-end: 47
- Bump 1 (DM Scripts): 37
- Bump 2 (Templates): 67
- Bump 3 (5K Playbook): 97
- Max checkout: 248
- Projected AOV moderate: 91
- Projected AOV aggressive: 101

**Strikethrough pricing updates:**
- Bump 1: was showing 97 struck through to 17. Now: 197 struck through to 37
- Bump 2: was showing 197 struck through to 37. Now: 297 struck through to 67
- Bump 3: was showing 297 struck through to 67. Now: 497 struck through to 97

**Why this works:**
- 47 AOV floor (even with zero bumps) is already halfway to CPA
- Cat's data shows higher bumps convert better, not worse
- Value perception improves — "297 struck to 67" is more believable than "197 struck to 37"
- At moderate bump rates (35%/25%/15%), AOV of 91 is in self-liquidating range vs 100-110 CPA
- OTOs and email ascension become pure profit, not survival

**What doesn't change:**
- OTO prices stay the same (Sprint 297, Blueprint 397, Community 47/mo, Accelerator 5K)
- Product contents stay the same
- Promise and positioning stay the same
- Only the price tags on the checkout page change

## What Changes

**offer.md:**
- Front-end price: 27 to 47
- Bump 1 price: 17 to 37 (strikethrough 197)
- Bump 2 price: 37 to 67 (strikethrough 297)
- Bump 3 price: 67 to 97 (strikethrough 497)
- Max checkout value: 148 to 248
- Target AOV: update to 90-110
- Headline promise: update "in one afternoon" language if needed for 47 price point
- Funnel metrics table: update all prices
- Bump tracking rows: update prices
- CPA thresholds: may need adjustment for higher AOV
