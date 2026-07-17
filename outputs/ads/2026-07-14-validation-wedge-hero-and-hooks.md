---
type: output
subtype: hero-rewrite + static-ads
status: draft
review_status: "DRAFT — not yet run through /ad-review. No income claims by Michael; self-guided disclaimers present; no fabricated counts. Verify before deploy."
offer: client-ready
angle: validation-wedge
date: 2026-07-14
origin: decisions/2026-07-14-validation-wedge-positioning.md
source_files:
  - reference/core/offer.md
  - reference/core/voice.md
  - reference/core/audience.md
  - research/2026-07-14-skool-competitors-positioning-mining.md
  - outputs/pages/front-end-sales-page-v2-final.md (current live hero)
maps_to: outputs/pages/front-end-v2-ghl-swap-sheet.md
live_page: https://clientreadyoffer.com/digital_snacks22-3475-662204
---

# Validation-Wedge Hero + Ad Hooks

**Why this exists:** The Skool mining (2026-07-14) proved "sells itself" / "clarify your offer" are now category claims run by named competitors (Chun's World, Coach Builder, Bishop's Coaching Hub). Per `decisions/2026-07-14-validation-wedge-positioning.md`, cold-traffic hooks now lead with the one thing the field doesn't own: **validation — 5 real buyers, this afternoon, before you build.** "Sells itself" is demoted to body copy only. AI is framed as *speed*, never the pitch.

**Rules baked in (from the live page):** pain-first, plain language, no mechanism jargon, no income claims by Michael, no fake countdown, self-guided disclaimer, no fabricated `{{CUSTOMER_COUNT}}`.

---

## A. HERO REWRITE (replaces the HERO block in front-end-sales-page-v2-final.md)

**Current (to A/B against — the "sells-itself" hero):**
> Headline: *BUILD AN OFFER SO CLEAR IT SELLS ITSELF — IN ONE AFTERNOON.*

**New — Variant V (validation-led):**

**Pre-headline**
> YOU'VE GOT THE EXPERTISE. WHAT YOU DON'T HAVE IS A SINGLE YES.

**Headline**
> PUT YOUR $5K OFFER IN FRONT OF 5 REAL BUYERS THIS AFTERNOON — BEFORE YOU BUILD ANYTHING.

**Sub-headline**
> Most coaches don't have a marketing problem — they have an offer no real buyer has ever said yes to. And a clear offer nobody's validated is still a guess. 5 AI prompts pull your offer out of your head in an afternoon; a same-day step puts it in front of real people today. You build what already got a yes.

**CTA Button**
> GET INSTANT ACCESS — $27
> 30-Day Money-Back Guarantee

*[Product mockup image — show $27. Self-guided; results depend on your effort and your market.]*

**What changed & why:**
- Lead moved from *clarity → sells-itself* (contested) to *validation → 5 real buyers today* (uncontested wedge).
- The category line — **"a clear offer nobody's validated is still a guess"** — names the clarify-then-stall trap the whole field creates.
- AI kept, but reframed as **speed** ("5 AI prompts... in an afternoon"), not the differentiator.
- "Sells itself" removed from the hero. It can still live below the fold as an *outcome of* validation, never the promise.

> **Deploy note:** update the HERO block in `front-end-v2-ghl-swap-sheet.md` and A/B Variant V against the current "sells-itself" hero (same offer, same checkout, 50/50). Judge on checkout CVR per `offer.md` targets, not clicks.

---

## B. AD HOOKS (3 primaries — cold, problem/solution aware)

### Hook 1 — "The guess" reframe `SOLUTION AWARE`

**Hook (≤128 chars):** Your offer isn't unclear. It's unvalidated. No real buyer has told you yes — so you're polishing a guess.

```text
You keep rewriting your offer. New words, new headline, new niche. Still no clients.

Here's the truth: the problem isn't the wording. It's that no real buyer has ever told you yes. You've been polishing a guess.

Clarity you write at your desk collapses the second a real person reads it. Clarity that comes from watching 5 real prospects react — that holds.

So flip the order. Don't build the funnel, the content, the course. Extract the offer that's actually yours, then put it in front of 5 real people this afternoon and watch what they do.

The Client Ready Offer System is where that starts. 5 AI prompts pull the offer out of your head in one afternoon. A same-day step gets it in front of real buyers today. $27. Self-guided — results depend on your effort and your market.

Test, validate, build. In that order.
```

### Hook 2 — "You built backwards" `PROBLEM AWARE`

**Hook (≤128 chars):** Build the funnel first, then find buyers. Wrong. You just spent three months validating nothing.

```text
Most coaches build backwards. Funnel, content, course — months of work for an offer nobody confirmed they'd buy.

Then the launch is silent, and they decide they're just bad at this.

Wrong. You're not bad at this. You built before you validated.

Here's the fix, and it takes one afternoon: extract your offer with 5 AI prompts, then put it in front of 5 real prospects today. If they lean in, build. If they don't, you just saved yourself three months.

A clear offer nobody's said yes to is still a guess. Stop guessing.

The Client Ready Offer System — $27, one afternoon. Self-guided; results depend on your effort and your market.
```

### Hook 3 — "Everyone stops at clarity" `SOLUTION AWARE` (positions against the field)

**Hook (≤128 chars):** Everyone's telling you to "clarify your offer." Then they leave you at the hardest part.

```text
There's a whole industry teaching coaches to clarify their offer. Nail the niche. Write the one sentence. Make it irresistible.

Then they hand you off to "now go run ads."

But a clear offer is still a guess until a real buyer says yes to it. Clarity is the easy half. Validation is the half nobody walks you through.

Client Ready is that half. Extract the offer that's actually yours — 5 AI prompts, one afternoon — then get it in front of 5 real prospects today and read the room. You build what already got a yes.

$27. Self-guided; results depend on your effort and your market. Test, validate, build.
```

---

## Next

- [ ] Run these through `/ad-review` (compliance + 4-lens) before deploy — matches the review gate used on the clarity angles.
- [ ] Build Variant V hero into the GHL swap sheet; launch the A/B vs the current "sells-itself" hero.
- [ ] If Hook 3 ("everyone stops at clarity") wins, it becomes the spearhead angle — it directly converts the field's crowded "clarify" positioning into CR's category.
