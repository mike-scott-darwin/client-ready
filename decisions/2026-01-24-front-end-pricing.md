---
type: decision
date: 2026-01-24
status: proposed
linked_research:
  - research/2026-01-23-cat-howell-low-ticket-ecosystem.md
supersedes: null
---

# Decision: Front-End Pricing ($17 vs $27)

## Context

Current front-end offer (Client Ready Offer Guide) is priced at $17. With the Andromeda update, Meta's algorithm favors $27-$97 for self-liquidating funnels. Need to decide whether to raise price before launching ads.

**Trigger:** Andromeda research revealed $27-$97 is optimal range for SLO funnels.

---

## Research Summary

From `research/2026-01-23-cat-howell-low-ticket-ecosystem.md`:

- Andromeda's 2026 SLO requirement: $27-$97 "no-brainer" front-end
- Cat Howell's range: $17-$97 (still valid but $27+ preferred)
- Target AOV: $100-$200 per funnel
- Your current stack: $17 + $37 bump + $27 bump = $81 max cart (before OTOs)
- At $27: $27 + $37 + $27 = $91 max cart (before OTOs)

---

## Considered Options

### Option A: Keep $17

Stay at current price point.

**Pros:**
- Lower barrier to entry
- "Impulse buy" territory
- Already positioned and messaged around $17
- Can always raise later with data

**Cons:**
- Below Andromeda's optimal range
- Lower AOV = harder to self-liquidate
- May signal "cheap" vs "valuable"
- $17 + bumps = $81 max (tight margins)

**Effort:** None

---

### Option B: Raise to $27

Increase front-end to $27.

**Pros:**
- In Andromeda's optimal range ($27-$97)
- Higher AOV = easier to self-liquidate
- $27 + bumps = $91 before OTOs
- Still "no-brainer" impulse territory
- Signals more value
- Matches Cat Howell's recommended structure ($27 masterclass)

**Cons:**
- Slightly higher barrier
- Need to update sales page messaging
- May reduce conversion rate (test required)

**Effort:** Low (price change + copy tweaks)

---

### Option C: Raise to $37

Jump to $37 front-end.

**Pros:**
- Stronger AOV
- More room for ad spend
- $37 + $37 + $27 = $101 before OTOs

**Cons:**
- May hurt conversion rate significantly
- Crosses from "impulse" to "consideration" territory
- Bigger messaging overhaul needed
- Riskier without validation data

**Effort:** Medium

---

## Decision

**[TBD — awaiting your input]**

### Recommendation: Option B ($27)

Reasoning:
1. Hits Andromeda's optimal range without leaving impulse territory
2. Cat Howell's proven structure uses $27 masterclass as front-end
3. Low effort to implement
4. Can always test $17 vs $27 once funnel is live
5. $10 increase × volume = significant AOV lift

---

## Consequences

### If We Choose $27

**What Becomes Easier:**
- Self-liquidating math (higher AOV per buyer)
- Andromeda optimization (algorithm favors this range)
- Perceived value positioning

**What Becomes Harder:**
- Nothing significant at $27 price point

**What We're Accepting:**
- Slight potential conversion rate drop (mitigated by value perception)
- Need to update sales page copy to justify $27

---

## Action Items

If decision is accepted:

- [ ] Update `reference/core/offer.md` — Change front-end price from $17 to $27
- [ ] Update `CLAUDE.md` — Update funnel table pricing
- [ ] Update sales page copy to reinforce $27 value
- [ ] Update `focus.md` — Remove pricing decision from "Decisions Needed"

---

## Review Date

Review after 100 front-end purchases to compare:
- Conversion rate at $27 vs industry benchmarks
- AOV achieved vs $80-150 target
- Self-liquidating ratio (ad spend : front-end revenue)
