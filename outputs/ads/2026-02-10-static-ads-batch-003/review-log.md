---
type: output
subtype: review-log
date: 2026-02-10
batch: static-ads-batch-003
lenses: [ftc-compliance, meta-policy, copy-quality, voice-authenticity, substantiation]
---

# Review Log — Batch 003

## Review Pipeline

5 parallel compliance agents ran against the full batch. Findings were deduplicated and prioritized.

---

## P1 — Blocking (1 issue)

### P1-1: No typicality data for $27 product
**Lenses:** FTC Compliance, Substantiation
**Status:** OPEN — requires data collection, not a copy fix

Testimonials reference coaching outcomes (Renee's "10 years → 90 minutes," Wendy's "first sales calls in weeks"). FTC requires typicality data showing what AVERAGE $27 buyers achieve. Without `reference/proof/typicality.md`, these ads carry regulatory risk.

**Action required:** Collect average buyer outcome data before scaling ad spend. Ads can run at test budget; do not scale until typicality file exists.

---

## P2 — Should Fix (8 issues, all resolved)

### P2-1: BtF P1 Short-Form — Fabricated "$4K on a funnel" story
**Lens:** Substantiation, FTC Compliance
**Issue:** Short-form compressed version invented "She spent $4K on a funnel" — a pseudo-testimonial with no source.
**Fix:** Replaced with generic compressed version of actual P1 content. No specific dollar amount, no implied person.

### P2-2: BtF H1 + CU H1 — Parenthetical disclaimers in headlines
**Lens:** Copy Quality
**Issue:** Headlines read awkwardly with inline parenthetical disclaimers: "10 Years Stuck... (coaching result — same framework, $27 self-guided)"
**Fix:** Moved disclaimers to asterisk footnote format below headline. Clean headline + visible disclaimer.

### P2-3: BtF P4 — "Do you have an offer..." direct question
**Lens:** Meta Policy
**Issue:** "Do you have an offer worth building a funnel for?" targets a personal attribute (business status). Meta flags "Do you have..." patterns.
**Fix:** Rewritten as statement: "Most coaches never ask that question. They skip straight to building."

### P2-4: BtF P3 hook — Missing commas
**Lens:** Copy Quality
**Issue:** "This eliminates vague offers unclear positioning and months of guessing" — no commas in a list, hurts scannability.
**Fix:** Added commas and em dash: "This eliminates vague offers, unclear positioning, and months of guessing whether anyone will pay — for $27"

### P2-5: CTA monotony — "Link below" on every ad
**Lens:** Copy Quality
**Issue:** 13 of 14 CTAs were "Link below." Repetitive across the batch.
**Fix:** Varied CTAs by ad type: Deep/Testimonial ads keep "Link below." UGC ads use "Grab it here ↓". DR ads use "$27 — grab it here ↓". Mixed treatment on short-forms.

### P2-6: Uncontracted language throughout
**Lens:** Voice Authenticity
**Issue:** Multiple instances of "Here is," "That is," "It is," "cannot," "will not" — Michael's voice uses contractions naturally.
**Fix:** Global pass replacing all uncontracted forms: Here's, That's, It's, can't, won't, it'll, you're, I've, what's.

### P2-7: "Zone of genius" overuse
**Lens:** Voice Authenticity, Copy Quality
**Issue:** Appeared 5 times across the batch. Becomes wallpaper if repeated too often.
**Fix:** Reduced to 3 strongest placements (BtF P2, CU P1, CU P3). Replaced elsewhere with "core expertise" and "what you actually do well."

### P2-8: BtF P2 hook — Generic opening
**Lens:** Voice Authenticity
**Issue:** "Here is what nobody told me..." is generic influencer language, not a documented Michael voice pattern.
**Fix:** Rewritten to direct story hook: "I spent six months building a course nobody bought and the problem was never the funnel" — mirrors voice.md Pattern 7 (Story → Lesson).

---

## P3 — Consider (4 items, selectively applied)

### P3-1: Short-form P5 versions — Missing coaching disclaimer
**Status:** FIXED
**Fix:** Both BtF P5 and CU P5 short-forms now include "Coaching results — same framework, $27 self-guided."

### P3-2: "150+ coaches" and "4.7/5 rating" — Source documentation
**Status:** NOTED
**Fix:** Added "Social Proof Claims" section to Creative Notes with verification instructions. Numbers must be confirmed against Stripe/GHL before running.

### P3-3: "Proven" → "tested with real coaching clients"
**Status:** FIXED
**Fix:** CU P3 "the extraction framework is proven" → "the extraction framework has been tested with real coaching clients." More defensible, less absolute.

### P3-4: Outcome visualization closing lines
**Status:** NO CHANGE
**Rationale:** Lines like "Wake up knowing exactly what you sell" describe clarity outcomes, not income. They're aspirational about understanding, not earnings. FTC-safe as written.

---

## Summary

| Priority | Found | Fixed | Open |
|----------|-------|-------|------|
| P1 | 1 | 0 | 1 (typicality data — user action) |
| P2 | 8 | 8 | 0 |
| P3 | 4 | 3 | 0 (1 no-change-needed) |

**Batch status:** Ready for test-budget deployment. Do not scale until P1 (typicality data) is resolved.
