---
type: decision
status: accepted
date: 2026-03-09
trigger: Explored discounting missed bumps for DFY buyers — rejected in favor of sequencing
linked_decisions:
  - decisions/2026-03-07-dfy-upsell-community-first.md
  - decisions/2026-03-09-front-end-pricing-hold-47.md
---

# Decision: No Discounts for DFY Buyers — Bundle and Sequence Instead

## Context

Question: should DFY Offer Build ($197) buyers get a discount on bumps they skipped at checkout?

## Decision

**No discounts. Use sequencing and framing instead.**

DFY buyers are your highest-intent, highest-trust customers. They don't need a lower price — they need the right offer at the right moment. Discounting trains future buyers to skip bumps on purpose and undercuts the existing bump recovery emails.

## Why Discounts Hurt

1. **Trains buyers to wait.** If DFY buyers get deals on skipped bumps, future buyers skip bumps at checkout expecting a discount later. Punishes best customers (who bought everything upfront), rewards holdouts.

2. **Undercuts bump recovery sequence.** Recovery emails (Days 2/4/6) pitch missed bumps at full price. A DFY discount creates a competing offer at a lower price. Confusion kills conversion.

3. **Unnecessary margin loss.** DFY costs ~$0.15-0.30 to generate. 99% margin. No cost pressure requiring revenue recovery from discounted bumps. At 25% off, you lose $9-24 per bump — $500-1,500 per 100 DFY buyers for an unproven conversion lift.

4. **DFY buyers already trust you.** They just paid $197 and received quality deliverables in 24-48 hours. Trust is at peak. Full-price offers convert well at trust peaks.

## What to Do Instead

### 1. "Complete Your Toolkit" Email (Day 3-5, DFY buyers only)

Triggered after DFY delivery. One email, full price:

> "Your DFY Offer Build is delivered. You've got the ICP, the offer doc, the sales copy, and the ad hooks. Now here's what makes it actually work faster: [list missed bumps with one-line benefit each]. Grab what you need — everything's in your portal, one click to unlock."

**Why it works:** DFY delivery is the trust moment. They just saw the quality. Highest-conversion window for additional purchases.

### 2. Portal Locked Tiles (Already Built)

Every DFY buyer logs into the portal to access deliverables. Missed bumps show as locked tiles with titles, descriptions, and preview images. One-click purchase with card on file. Passive cross-sell on every login.

### 3. Community Prep Framing for Bump 3

DFY buyers have a 30-day community trial. Position Bump 3 ($97 — First $5K Client Playbook) as preparation:

> "You're in the 30-day community trial. Members who complete the $5K Playbook before their first hot seat call get 10x more out of it. Grab it now so you're ready."

**Why it works:** Uses community trial deadline as natural urgency. Positions buying as self-investment, not upsell. Pushes highest-margin bump without discounting.

## Implementation

| Tactic | Timing | Price | Status |
|--------|--------|-------|--------|
| "Complete Your Toolkit" email | Day 3-5 post-DFY delivery | Full price | Build in GHL |
| Portal locked tiles | Every login | Full price | Already in architecture |
| Community prep framing (Bump 3) | DFY delivery email or Day 1 of community trial | Full price ($97) | Add to DFY delivery sequence |
| Bump recovery emails | Days 2/4/6 | Full price | Already built |

## What Changes

- **Add** a "Complete Your Toolkit" email to the DFY buyer workflow in GHL (fires after delivery confirmation, Day 3-5)
- **Add** community prep framing for Bump 3 to DFY delivery email or community welcome
- **No changes** to bump pricing, recovery sequences, or portal architecture

## Review Trigger

After 50 DFY sales, measure:
- "Complete Your Toolkit" email conversion rate
- Portal cross-sell rate for DFY buyers vs non-DFY buyers
- Bump 3 take rate for DFY buyers who got community prep framing
