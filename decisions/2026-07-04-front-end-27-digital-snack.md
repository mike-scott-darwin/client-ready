---
type: decision
status: active
date: 2026-07-04
trigger: Jan26 paid-ads autopsy (front-end didn't self-liquidate at $47) + digital-snack cash-flow revival
supersedes:
  - decisions/2026-01-24-front-end-pricing.md
linked_data:
  - Meta account act_463860554507371 — campaigns "CRO - Sales - Jan26" / "(ABO)"
---

# Decision: Front-End Price $47 → $27 (Digital-Snack Cash-Flow Entry)

> Reverses the 2026-01-24 decision that moved the front-end $27 → $47. The front-end is now **$27**. Everything else in the funnel is unchanged: bumps $37 / $67 / $97, DFY OTO1 $197, DFY Lite $97, Newsletter (Monthly Playbook) $37/mo, Community $47/mo beta, Accelerator $5K+.

## What Changed

- **Front-end: $47 → $27.** One-time entry price for the Client Ready Offer System.
- Recomputed funnel math everywhere the front-end is a summand:
  - Max one-time cart: ~~$545~~ → **$462** ($27 + $37 + $67 + $97 + $197 + first $37 newsletter)
  - Checkout AOV target: ~~$90-110~~ → **$70-90**
  - Full funnel AOV: ~~$135~~ → **~$115**
  - 90-day value per buyer: ~~$260~~ → **~$240** (community at $47 beta)
- Reframed the front-end from "self-liquidating checkout" to **"buyer-acquisition price."** At $27 the checkout is not expected to self-liquidate; spend is recovered on bumps + OTOs + continuity.

## Why

**1. The higher price bought no self-liquidation.** The Jan26 paid push (act_463860554507371) is the evidence. At a ~$47/$17-era price the front-end still ran **underwater on cold Tier-1 traffic**:
- CRO - Sales - Jan26 (CBO): $1,307.89 spend → 8 purchases → $325.54 → **0.25 ROAS**
- CRO - Sales - Jan26 (ABO): $453.44 spend → 5 purchases → $177.83 → **0.39 ROAS**
- Blended: ~$1,761 spend → 13 sales → ~0.29 ROAS. Strong ad CTR (~4%), but ~2.2% click-to-buy at the checkout — roughly 3.5× too low to break even on the front-end alone.

The lesson: raising the price to $47 didn't make the checkout self-liquidate. It only raised the barrier. If the front-end can't self-liquidate at either price on cold traffic, take the price that maximizes **buyer volume** and recover on the backend.

**2. Digital-snack cash-flow strategy.** The Client Ready revival is a cash-flow play (Miles Stutz digital-snack playbook): a low, frictionless entry that maximizes the number of buyers entering the funnel, then monetizes via order bumps, the DFY OTOs, and $47/mo community + $37/mo newsletter continuity. Lower entry → higher sales-page conversion → lower CPA → more buyers into the ascension engine.

## The Known Risk (must monitor)

Cheaper front-ends historically attract lower-quality buyers who take fewer bumps/upsells:
- **Cat Howell:** a $17 front-end dropped her AOV from $140 to $70-80; she calls $27 the minimum and $47 her sweet spot ("people paying $47 tend to buy everything").
- **Miles Stutz:** killed his $7 front-end (digitalsnacks.co) and moved to $17 for the same reason.

Because of this, **at $27 the entire model depends on bump + OTO take-rate at checkout.** Protect that above all else.

**Kill criteria:** if, after ~30 sales at $27, the order-bump attach rate craters (i.e., front-end buyers don't take bumps at a rate that gets blended 90-day value to ~$240), revisit the price. The $27 vs $47 question is a live test, not a settled fact.

## What Did NOT Change

Bumps, DFY OTO1/downsell, Newsletter, Community ($47/mo beta), and Accelerator all hold at their current prices. This decision touches the **front-end only**.
