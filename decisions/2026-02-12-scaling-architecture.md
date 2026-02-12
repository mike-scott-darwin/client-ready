---
type: decision
date: 2026-02-12
status: accepted
urgency: normal
---

# Scaling Architecture — Multiple Entry Points + Backend Revenue

## Situation

Cat Howell's Feb 9 hot seat revealed that her #1 scaling strategy is multiple entry points — flipping existing bumps/upsells into standalone front-end offers, all in one CBO campaign. She added 2 entry points and her CPA dropped back from $100 to profitable. Separately, her revenue split (50% ads / 50% backend) exposes a major gap in Client Ready's architecture: no backend email system exists yet.

## Research

### cat-howell-hotseat-feb9
**Date:** 2026-02-12
**Source:** Live Profit Lab hot seat call
See: `research/2026-02-12-cat-howell-hotseat-feb9.md`

---

## Decision 1: Multiple Entry Points

### The Opportunity

Client Ready already has products that could become standalone front-end offers:

| Product | Current Position | As Front-End | Different Buying Reason |
|---------|-----------------|--------------|------------------------|
| $27 Offer System | Front-end | Already there | "I need to figure out my offer" |
| $17 DM Scripts | Bump 1 | Standalone at $27-37 | "I need to start selling NOW" |
| $67 First $5K Client Playbook | Bump 3 | Standalone at $47-67 | "I need to close high-ticket" |
| $37 Templates | Bump 2 | Maybe — less standalone value | "I need plug-and-play assets" |

Each becomes its own order form → with the OTHER products as ITS bumps. Same catalog, different entry doors. All in one CBO, one ad set.

### Status: NOT YET

Don't build this before the core $27 funnel is validated. Cat's sequence:
1. Validate one offer first (get 30+ sales, know your CPA and AOV)
2. Build AOV with bumps/upsells
3. THEN add entry points for scale

**This is a scaling strategy, not a launch strategy.** Park it until post-validation.

### What Needs to Happen First
- [ ] Launch $27 funnel with ads
- [ ] Hit 30+ sales (validation threshold)
- [ ] Confirm AOV is $100+ consistently
- [ ] THEN consider flipping DM Scripts and/or $5K Playbook to standalone front-ends

---

## Decision 2: Backend Revenue System

### The Gap

Cat makes 50% of her revenue from backend (email sequences, product library, affiliate promotions). Client Ready has:
- An email ascension system DESIGNED in offer.md (10-day sequence + daily rhythm)
- ZERO of it built
- No affiliate relationships
- No product library beyond the funnel products

### The Priority

Backend revenue is not day-one. But it IS the real business. The sequence:

1. **Launch ads** (immediate)
2. **Build 10-day email sequence** (within first 30 days of launch)
3. **Start daily email rhythm** (once 100+ buyers in list)
4. **Add affiliate promotions** (once email system is running)

### What Changes

No reference file changes needed — the email system is already designed in `offer.md`. This decision documents the PRIORITY: backend email is the second-highest priority after launching ads. Not the third, not the fifth. Second.

### Affiliate Opportunity

Cat made $30K/month from ClickFunnels affiliates alone. Client Ready could affiliate with:
- GHL (funnel builder — already recommending it)
- Skool (community platform)
- AI tools (Claude, ChatGPT Plus)
- Email platforms (Beehiiv, ConvertKit)

Each affiliate recommendation fits naturally into the daily email rhythm and the product's use case. No awkward promotion — "here's what I use to build my funnel" is authentic.

---

## What Changes

Reference files affected:
- `reference/domain/ads-methodology.md` — scaling strategies framework already codified (Parts 2, 5, 8)
- No offer.md changes needed — email system already designed, entry point flip is future work
- This decision documents sequencing and priority, not structural changes
