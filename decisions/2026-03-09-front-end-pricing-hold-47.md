---
type: decision
status: accepted
date: 2026-03-09
trigger: Revisited $27 vs $47 front-end pricing during Gemini research review
linked_research:
  - research/consolidated/pricing-slo-strategy.md
  - research/2026-02-15-miles-stutz-low-ticket-funnel-data-mining.md
  - research/2026-03-08-offer-validation-gemini.md
linked_decisions:
  - decisions/2026-01-24-front-end-pricing.md
  - decisions/2026-02-15-pricing-restructure.md
  - decisions/2026-03-07-dfy-upsell-community-first.md
---

# Decision: Hold Front-End at $47 — Don't Drop to $27

## Context

Question raised: should we drop the front-end from $47 to $27 to increase volume and move more people into the $97/mo community? Bump 3 at $97 and DFY at $197 also reviewed.

## Decision

**Keep $47.** Keep all bump prices. Keep DFY at $197. No changes.

This is the third time this question has been evaluated. The data is consistent.

## Why $27 Doesn't Work

### The math doesn't self-liquidate
- Expected CPA: $80-120
- At $27 + moderate bump rates (35%/25%/15%): AOV ~$52-58
- Loss per sale: $30-60 on the front end
- At $47 + same bump rates: AOV ~$91-101 — self-liquidating range

### Cheap buyers don't ascend
- Research: "$7 buyer list is about as effective as a freebie list" for $300+ backend
- Miles Stutz killed his $7 front-end entirely, moved to $17 minimum
- Cat Howell: $17 front-end dropped AOV from $140 to $70-80
- The community path runs through the $197 DFY (bundled 30-day trial) — cheaper front-end buyers convert to DFY at lower rates

### Higher bumps convert better, not worse
- Cat Howell split test: $33/$44/$55 bumps at 4.0% vs $17/$33/$55 at 2.3%
- Bump 3 at $97 pre-qualifies for $5K Accelerator intent
- No evidence that current bump pricing is a conversion problem

## Why $47 Serves the Community Goal Better

The priority is recurring revenue through community ($97/mo). The primary community entry point is the DFY upsell ($197), which bundles a 30-day trial.

| Path to Community | $27 front-end | $47 front-end |
|-------------------|--------------|--------------|
| Buyer quality | Lower | Higher |
| DFY OTO take rate | Lower (cheaper buyers) | ~15% expected |
| Community trials started | Fewer | More |
| Trial-to-paid conversion | Lower | Higher |
| 90-day value per buyer | ~$180 | ~$260 |

More volume at $27 doesn't compensate for lower ascension rates. The community fills faster with $47 buyers who actually use the DFY and start the trial.

## Higher-Impact Levers for Community Growth

Instead of dropping the price, optimize these:

1. **Welcome sequence** — 82% open rates. Days 9-10 pitch community. Optimize copy.
2. **DFY OTO conversion** — every DFY buyer auto-starts community trial
3. **Community recovery email** — Day 8, direct pitch to non-DFY buyers
4. **In-portal locked tiles** — community visible as locked tile on every login
5. **$100 validation test** — get the funnel live and test with real traffic first

## What Stays

| Element | Price | Status |
|---------|-------|--------|
| Front-end | $47 | Hold |
| Bump 1 (DM Scripts) | $37 | Hold |
| Bump 2 (Templates) | $67 | Hold |
| Bump 3 (5K Playbook) | $97 | Hold |
| DFY Offer Build | $197 | Hold |
| DFY Lite | $97 | Hold |
| Newsletter | $37/mo | Hold |
| Community | $97/mo | Hold |
| Accelerator | $5K | Hold |

## Review Trigger

Revisit pricing only after:
- 50+ front-end sales with paid traffic data
- Actual CPA, AOV, and bump take rates measured
- If AOV is consistently >$120, consider testing $57 or $67 front-end (up, not down)
