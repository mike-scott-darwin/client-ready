---
type: decision
date: 2026-06-28
status: active
topics: [offer, front-end, order-bumps, otos, speed-to-result, congruence]
linked_research:
  - research/2026-05-19-miles-coaching-call-synthesis.md
  - research/2026-06-02-miles-coaching-call-synthesis.md
supersedes_partial:
  - decisions/2026-02-14-info-products-congruence-audit.md
---

# Offer Revamp — Speed to Result

**Context:** Reviving Client Ready as a cash-flow business. Audited the front end + bumps + OTOs against (a) speed-to-tangible-result and (b) the Miles Stutz May/June 2026 bump/OTO rules. Verdict: no teardown — fix one structural gap and sharpen framing.

---

## The core problem

The front end **promises "validate"** but **delivers "clarity."** The $47 buyer walks away from the afternoon with an *offer document* — not a validated offer. Validation (the product's own Component 4) is homework that happens later, depends on the buyer having a warm audience, and isn't guaranteed. This thins and slows the result vs. the promise. It is the #1 lever for making the offer both more valuable and faster.

Secondary issues:
- **Congruence gap:** front end says "don't build the funnel yet — validate first," then Bump 2 sells funnel templates and OTO1 sells a done-for-you offer. Violates the Miles rule that a bump/OTO must never make the front end feel incomplete or contradict it.
- **Framing:** OTO1 FAQ says "same destination, different path" → tells the $47 buyer they bought the worse version.
- **The fastest-result asset (DM outreach) is buried in a bump**, so most buyers don't get a quick result.

---

## Decisions

### 1. Front end delivers a same-day RESULT, not just a document
Add a final component — **"The 48-Hour Validation Sprint"**: the one outreach message to send + a 5-person tracker + a "first reply" target. The afternoon now ends with *"your offer is in front of 5 real prospects today,"* which delivers the promise word. Doubles as the case-study/testimonial collection engine (addresses the #1 proof gap).

### 2. Add a 10-minute "first win" at the top of the front end
Prompt 1 produces a one-sentence positioning statement. Frame it as "your clearest one-liner in 10 minutes." Fast perceived win → higher consumption → higher ascension.

### 3. Pull a light version of outreach into the core
One outreach script + the validation challenge go in the $47. The **$37 DM Scripts bump remains the full system** (10 scripts, objection handlers, 6-step flow, tracker) = the "more/convenience" upgrade. Every buyer now gets a faster result; the bump is still clearly worth it (convenience, not required).

### 4. Fix Bump 2 congruence
Reframe **$67 Templates** to lead with same-day-usable assets (filled offer-doc example, 50+ headlines, messaging map) and position the funnel/landing assets as "ready for the moment you've validated" — not "build now."

### 5. Reframe OTO1 DFY as "more + done," not "same destination"
Kill "same destination, different path." Position on what the $47 does NOT include: **ICP, ready-to-send Google sales doc, 5 ad hooks, personal review, 48h done-for-you.** Convenience + extra, never a replacement for the $47.

### 6. Direct-response + guarantee headlines (Miles rule)
- **$37 DM Scripts:** "Start your first sales conversation in the next 5 minutes — or your money back."
- **$67 Templates:** "Plug your offer in and have your page + emails ready today — or your money back." (lead with usable-today assets)
- **$97 Playbook:** "Close your first $5K client without a sales call — or your money back."

### 7. Consider a ready-to-send sales doc lower in the ladder (flagged, not yet decided)
The single fastest path to the *buyer's* first yes is a ready-to-send sales doc — currently locked in the $197 DFY. Evaluate adding a lightweight version to the $47 or $67 so more buyers get a yes in days. **Open question** — decide after the front-end revamp ships, to avoid over-cannibalizing DFY.

---

## What does NOT change
- Price points ($47 / $37 / $67 / $97 / $197 / $97 / $37mo) — all validated.
- The value-ladder structure and self-liquidating math.
- The 5 AI prompts (they're the core mechanism and they work).

## Success signals
- Higher front-end → bump take rate (Miles target 33%+).
- Higher product consumption (Day-3 "opened product" rate, offer.md).
- First inbound replies/sales reported by buyers within 48h (also feeds testimonials).

## Implementation
- [x] Rewrite `outputs/products/front-end-client-ready-offer-system.md` (10-min win + Validation Sprint + light outreach)
- [x] Update `outputs/products/oto1-dfy-offer-build.md` framing (more+done; killed "same destination")
- [x] Update bump page headlines in `outputs/pages/` (bump-1/2/3 — direct-response + guarantee)
- [ ] Reflect promise/result framing on the front-end *sales page* copy when pages are rebuilt (product is done; lander still says "validate")
- [ ] Reframe Bump 2 body to lead with same-day-usable assets (headline done; body still leads with funnel templates)
- [ ] Decide #7 (sales doc placement) after front-end ships
