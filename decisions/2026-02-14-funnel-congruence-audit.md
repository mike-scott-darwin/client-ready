---
type: decision
date: 2026-02-14
status: accepted
urgency: high
---

# Funnel Congruence Audit — Strip Guru Language, Fix Arc, Align Voice

## Situation

Full funnel copy is written and ready for launch: front-end sales page, 3 order bumps, 3 OTOs, test variants, and email sequences. Before going live with ads, we audited every page against soul.md, voice.md, audience.md, and the Confused → Clear → Converting transformation arc.

The front-end is strong. The post-purchase experience breaks congruence in three ways: guru-style language contradicts anti-guru positioning, the transformation arc assumes the buyer has completed the product when they just purchased it, and there are factual inconsistencies across page versions.

## Research

### funnel-congruence-audit
**Date:** 2026-02-14
**Source:** Claude Code full-funnel review
**Method:** Cross-referenced all page copy files against core reference files (soul.md, voice.md, audience.md, offer.md)

**Key finding:** The front-end builds trust with a skeptical year-2-3 audience. The bumps and OTOs spend that trust with copywriting tactics the audience has been burned by before — emojis, fake urgency, fabricated anchors, guru framing. The tone shift is severe enough that the most skeptical buyers (our exact target) will notice.

---

## Decision: Three-Phase Fix

### Phase 1: Fix Factual Errors (Before Launch — Blocking)

These are data integrity issues that could damage credibility or create compliance risk.

| # | File | Issue | Fix |
|---|------|-------|-----|
| 1 | `front-end-sales-page.md` line 302 | "100+ sales a day" — unsubstantiated outcome claim, most dangerous line in funnel | Delete or replace with "start generating sales consistently" |
| 2 | `front-end-test-variants.md` line 71 | "Ryan makes $1k/mo" vs main page line 219 "$14k/mo" — $13K discrepancy | Verify correct figure, update the wrong one |
| 3 | `front-end-test-variants.md` line 73 | "Alesia" vs main page line 225 "Alexia" — name spelling mismatch | Verify correct spelling, update |
| 4 | `front-end-test-variants.md` line 43 | "100+ verified students" vs main page line 67 "150+ verified students" | Pick the real number, align both |
| 5 | `oto1-sprint-full-page-copy.md` lines 181-186 | Placeholder testimonials with fabricated quotes still in doc | Remove entirely or add unmissable WARNING block |
| 6 | `oto2-dfy-full-page-copy.md` line 160 | "not AI-generated fluff" — contradicts front-end which IS 5 AI prompts | Rewrite: "not generic templates — this is custom to your business" |

### Phase 2: Strip Guru Language (Before Launch — Important)

The post-purchase tone must match the anti-guru front-end. These are find-and-replace level fixes.

| # | Current | Replacement | Where |
|---|---------|-------------|-------|
| 7 | "SPECIAL ONE-TIME INVITATION" | "ONE STEP FURTHER" or remove pre-headline | OTO 1, line 27 |
| 8 | "As a Coach — your Coach..." | "Here's my honest interest in this:" | OTO 1, line 63 |
| 9 | "profitably scale from $0/day... 30+ new paid customers" | Remove outcome claim; replace with mechanism description | OTO 1, lines 87-89 |
| 10 | "FAST-ACTION BONUS ONLY" | "BONUS:" | OTO 1, line 135 |
| 11 | All emojis (stars, targets, gifts, fire, bells) | Remove — match front-end's clean formatting | OTO 1 throughout |
| 12 | "DO NOT CLOSE THIS WINDOW OR CLICK THE 'BACK BUTTON'" | "Your order is processing. Watch the message below while we set up your access." | OTO 1, OTO 2, OTO 3 top bars |
| 13 | "GRAB THIS NO-BRAINER ADD-ON" | "ADD THIS TO YOUR ORDER" | Bump 1, line 26 |
| 14 | "started hundreds of real sales conversations" | Remove unsubstantiated claim or add qualifier: "designed to start real sales conversations" | Bump 1, line 26 |
| 15 | "WHAT IF your entire funnel strategy was done" | Direct rewrite: "YOUR COMPLETE FUNNEL STRATEGY — BUILT BY MICHAEL, READY TO IMPLEMENT." | OTO 2, line 44 |
| 16 | ~~$997~~ anchor on OTO 2 | Honest framing: "Launch price: $397 one-time" (match front-end's honesty) | OTO 2, line 186 |
| 17 | ~~$147~~ anchor on front-end | Verify: was it ever $147? If not, use honest framing or remove | Front-end, line 57 |
| 18 | "convert cold traffic into buyers instantly" | Replace "instantly" with "fast" or remove qualifier | Front-end, line 360 |
| 19 | "ensure your success" (lifetime support) | "support you as you build" | Front-end, line 388 |
| 20 | Run-on fear sentence about "going back to your corporate job" | Rewrite: "The Client Ready Offer replaces guesswork with a system. You stop hoping. You start knowing." | Front-end, line 287 |

### Phase 3: Fix the Transformation Arc (Before Launch — Important)

Every bump and OTO assumes the buyer already completed the front-end product. They haven't — they purchased it seconds ago. The arc needs to meet the buyer where they actually are.

**The principle:** Reframe from "you just did X" to "once you do X, you'll need this."

| # | File | Current Framing | Fixed Framing |
|---|------|-----------------|---------------|
| 21 | All bump full pages | "You just built your Client Ready Offer" | "Once you build your Client Ready Offer..." or "As you work through the system..." |
| 22 | Bump 1 (DM Scripts) | Assumes buyer is ready to sell today | Frame as: "While you build your offer, these scripts let you start conversations with your warm network — so you're not starting from zero when you're ready" |
| 23 | Bump 2 (Templates) | "You validated your offer. Now speed matters." | "When you're ready to implement, you won't start from scratch. These templates are waiting." |
| 24 | Bump 3 ($5K Playbook) | "you'll understand why $5K is actually easier to sell than $500" | Soften: "When your offer is clear, this playbook shows you how to price and close at the level your expertise deserves" |
| 25 | OTO 1 opening | "You now have everything you need" then immediately undermines it | Reframe: "The system gives you the extraction and validation. The Sprint gives you the launch — accountability, live support, and a 30-day timeline to go from validated offer to paying clients." |
| 26 | OTO 2 audience assumption | Assumes buyer can articulate expertise for onboarding form | Add: "After you work through the Offer System, you'll have the clarity to fill this out in 15 minutes" |

---

## What Changes

### Files to edit (outputs/pages/):
- `front-end-sales-page.md` — Fixes #1, #17, #18, #19, #20
- `front-end-test-variants.md` — Fixes #2, #3, #4
- `bump-1-quick-win-dm-scripts.md` — Fixes #13, #14, #21, #22
- `bump-2-plug-and-play-templates.md` — Fixes #21, #23
- `bump-3-first-5k-client-playbook.md` — Fixes #21, #24
- `oto1-sprint-full-page-copy.md` — Fixes #5, #7, #8, #9, #10, #11, #12, #25
- `oto2-dfy-full-page-copy.md` — Fixes #6, #12, #15, #16, #26
- `oto3-community-full-page-copy.md` — Fix #12

### No reference file changes needed
The reference files (soul.md, voice.md, audience.md, offer.md) are solid. The congruence issue is that the page copy drifted from them — not the other way around.

### Note on offer.md
Line 188 still says "Client Ready Accelerator (No-Phone Offer)" — the "No-Phone Offer" label was stripped from pages but remains in reference. Minor, but clean it up when editing offer.md for other reasons.

---

## Sequencing

1. **Phase 1 first** — factual errors are launch-blocking
2. **Phase 2 second** — guru language is trust-breaking for our specific audience
3. **Phase 3 third** — arc reframing is the most nuanced work

All three phases should be done before running paid traffic. The skeptical year-2-3 buyer who clicks an anti-guru ad and lands on an anti-guru front-end will feel the shift the moment they hit a "SPECIAL ONE-TIME INVITATION" with star emojis.

---

## The Test

After fixes, every page should pass this check from voice.md:
- [ ] Does this sound like me talking to a smart friend?
- [ ] Did I lead with value, not pitch?
- [ ] Is there a clear next step (or intentionally none)?
- [ ] Would I say this out loud naturally?
- [ ] Does it reject guru fluff?
- [ ] Is it specific, not vague?
