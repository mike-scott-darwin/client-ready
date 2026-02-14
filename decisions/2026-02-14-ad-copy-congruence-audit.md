---
type: decision
date: 2026-02-14
status: accepted
urgency: normal
---

# Ad Copy Congruence Audit — Mostly Clean, 5 Fixes

## Situation

Audited all ad copy (one-liners batch 001, static ads batches 002-004) against soul.md, voice.md, audience.md, and the Confused → Clear → Converting transformation arc. This audit ran alongside the funnel page congruence audit (see `decisions/2026-02-14-funnel-congruence-audit.md`).

## Research

### ad-copy-congruence-review
**Date:** 2026-02-14
**Source:** Claude Code cross-reference of all ad output files against core reference files
**Files reviewed:** `outputs/ads/2026-02-10-one-liners-cold-traffic-scale/one-liners-batch-001.md`, `outputs/ads/2026-02-10-static-ads-5x5-cold-traffic/static-ads-batch-002.md`, `outputs/ads/2026-02-10-static-ads-batch-003/static-ads-batch-003.md`, `outputs/ads/2026-02-10-static-ads-batch-004/static-ads-batch-004.md`

---

## Verdict: Ads Are Congruent

The ad copy is significantly more voice-consistent than the funnel pages. Tone is anti-guru throughout. Transformation arc is respected (Confused → Clear only, doesn't overpromise). Testimonial disclaimers are thorough on every reference. Belief-shift ads run without CTA. "Fair warning" backend disclosure is authentic.

**The ads are ready to run** — with 5 specific fixes below.

---

## Decision: 5 Fixes Before Launch

### Fix 1: Unverified Social Proof (Already Flagged — Blocking)

**Issue:** "150+ coaches" and "4.7/5 rating" appear in ads without verification.

**Where:**
- Batch 002: BtF P3, CU P3
- Batch 003: BtF P3, CU P3
- Batch 004: CMR P3
- One-liners: lines 4, 15, 24

**Fix:** Verify "150+" against Stripe/GHL purchase count. Verify "4.7/5" source (Skool reviews?). If unverifiable, replace with mechanism proof per Part 13 of ads methodology: "5 AI prompts. One afternoon. One clear offer document."

### Fix 2: "15 Minutes" vs "One Afternoon" Timeframe Conflict

**Issue:** `main-angles.md` lists a "15 Minutes" angle ("Create your complete offer document in 15 minutes"). Every ad batch uses "one afternoon." Running both creates competing timeframes.

**Fix:** "One afternoon" is canonical — it's used across all 4 ad batches and the front-end sales page. Update `main-angles.md` angle #2 to "one afternoon" or retire the 15-minute claim.

### Fix 3: "No DMs" vs DM Scripts Bump Tension

**Issue:** One-liner #14 says "No cold DMs required." Bump 1 is DM Scripts. A skeptical buyer may see the contradiction. (The scripts are for warm outreach, not cold — but the nuance may be lost.)

**Fix:** Change one-liner #14 from "No cold DMs required" to "No cold outreach required" — or add "warm" qualifier: "No cold DMs required — warm conversations only."

### Fix 4: Ryan Revenue Figure (Carries from Funnel Audit)

**Issue:** One-liners extracted specifics reference "Ryan" from the front-end sales page. The $1K/mo vs $14K/mo discrepancy (flagged in funnel audit) will carry into any ad using Ryan's results.

**Fix:** Resolve the correct figure in the front-end sales page first (see `decisions/2026-02-14-funnel-congruence-audit.md`, Fix #2). Then update one-liners extracted specifics if Ryan's data is used.

### Fix 5: "114 Sales in 30 Days" Framing Guard

**Issue:** One-liners extracted specifics include "114 sales in 30 days" as a proof point. Not currently in any ad copy (good). But if used, it must be framed as Michael's founder result, not the product's promise.

**Fix:** No action needed now. Guard rail: if this proof point enters ad copy, frame as "Michael's launch results" with clear context that this is the founder's experience running paid traffic, not a typical buyer outcome.

---

## What's Clean (No Changes Needed)

| Element | Status |
|---------|--------|
| Voice consistency | Clean — anti-guru throughout, no hype words |
| Transformation arc | Clean — Confused → Clear only, doesn't overpromise |
| Testimonial disclaimers | Clean — "coaching, not the $27 product" on every reference |
| Soul alignment | Clean — philosophy respected |
| Audience targeting | Clean — speaks to year 2-3 searcher |
| Belief-shift ads | Clean — mechanism only, no CTA |
| Backend disclosure | Clean — "I hate when people pretend there's no backend" |
| Compressed short-form | Clean — same angles, honest framing |

---

## What Changes

### Files to edit:
- `reference/proof/angles/main-angles.md` — Fix #2: update "15 minutes" to "one afternoon"
- `outputs/ads/2026-02-10-one-liners-cold-traffic-scale/one-liners-batch-001.md` — Fix #3: update line 14
- Social proof ads (Fix #1) — hold until Stripe/GHL verification, then update or replace

### No changes needed:
- Batches 002, 003, 004 ad copy (beyond social proof lines)
- Image prompts
- Ultra-short video scripts
- Headlines

---

## Relationship to Funnel Audit

The contrast between ad quality and funnel page quality reinforces the priority: **fix the post-purchase experience before launch.** The buyer journey right now is:

1. Honest, in-voice ad (clean)
2. Honest, in-voice sales page (mostly clean)
3. Guru-style OTOs with emojis and pressure tactics (broken)

Fixing the funnel pages (`decisions/2026-02-14-funnel-congruence-audit.md`) makes the whole experience congruent end to end.
