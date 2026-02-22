---
type: decision
date: 2026-02-22
status: codified
urgency: medium
linked_research:
  - research/2026-02-22-miles-stutz-ad-library-mining.md
  - research/2026-02-11-miles-stutz-apify-scrape-synthesis.md
  - research/2026-02-10-miles-stutz-ad-library-mining.md
---

# Response to Miles Stutz Feb 22 Mining — 6 Decisions

## Situation

Miles Stutz nuked his entire ad account between Feb 11 and Feb 22. Relaunched 194 ads in 7 days. Killed digitalsnacks.co, replaced with Rapid Ascension ($17) at freeclientsystem.com. Shifted from 61% video to 70% static image. Anti-Organic (his #1 angle) collapsed from 35% to 3%, replaced by Low-Ticket Ascension at 37%.

Six decisions needed based on the mining findings.

---

## Decision 1: Static Image Volume Strategy

**Question:** Should we test 5-10 image creatives per copy block instead of 1-2?

**Decision: YES — adopt "same copy, multiple images" as default creative testing method.**

Miles' #1 play is 54 different images with the exact same body text. This is radical creative variance applied to visuals, not copy. Meta's algorithm finds which scroll-stopper works for which audience segment.

**Implementation:**
- For each copy block, create 5 image variants minimum (not 1-2)
- Image types to test per copy block: product mockup, lifestyle, text-on-background, bold color interrupt, device screen
- Same body copy across all 5 — only the image changes
- Kill individual images at $20 spend with no signal (per existing $20 rule)
- This replaces the previous assumption of "one image per ad, vary the copy"

**What this does NOT mean:**
- Don't create 54 variants like Miles (he has the spend to test at that scale)
- Don't stop testing copy variations — still need multiple copy blocks
- The combo is: 4-6 copy blocks × 5 images each = 20-30 ads at launch

**Risk:** Low. More creative variants is aligned with existing "Radical Creative Variance" principle from the Feb 17 ad strategy decision. This makes the principle concrete.

---

## Decision 2: AI-Forward Ad Copy

**Question:** Should "AI-powered" / "AI prompts" be featured in headlines and link descriptions, not just product details?

**Decision: YES — elevate AI from product feature to headline-level positioning.**

Miles' link description across 113 ads: "AI-powered system. 1,090+ students. Build your first Digital Snack in 60 minutes. $17 today." AI is first — before social proof, before the mechanism, before the price.

Client Ready already has "AI Does 90%" as angle #6 in main-angles.md. But it's listed as a secondary use ("$47 offer, lead magnet, content") and doesn't appear in the ad copy framework prominently.

**Implementation:**
- Add "AI-powered" or "5 AI prompts" to link descriptions in all ad variants
- Test AI-forward headlines: "5 AI prompts that build your $5K offer in one afternoon"
- Position AI as the speed mechanism: AI = why it takes one afternoon instead of one month
- Keep the human element: "AI does the heavy lifting, you make the decisions"

**What this does NOT mean:**
- Don't position as an "AI tool" — it's a coaching system that uses AI
- Don't overclaim ("AI writes your entire business") — be specific about what the AI does (extract zone of genius, map ideal client, surface pain points, construct story, assemble offer)

**Risk:** Low. AI positioning is trending. Client Ready's 5 AI prompts are a genuine differentiator. Elevating them in copy is honest and specific.

---

## Decision 3: Counterintuitive Hook Pattern

**Question:** Should we adopt Miles' "backwards reveal" hook structure as an ad copy pattern?

**Decision: YES — add counterintuitive hook as a copy pattern in the angle library.**

Miles' most-repeated hook (54x): "I don't chase high-ticket clients, haven't in over a year now and I still made $750,000 last year. What I do instead sounds a little backwards..."

The structure: [deny the expected action] → [proof it works anyway] → [curiosity trigger about the alternative]. This creates massive curiosity because it contradicts the reader's assumption.

**Client Ready adaptation (no income claims):**
- "I don't sell $5K coaching packages. I sell a $47 system — and the $5K clients come to me."
- "I stopped doing sales calls. My close rate went up." (adapt to Client Ready's voice — less "bro," more grounded)
- "I don't tell coaches to quit their 9-to-5. That's exactly why they trust me enough to buy."

**Implementation:**
- Add "Counterintuitive Reveal" as a hook pattern in main-angles.md under a new "Hook Patterns" section
- Template: `[I don't/stopped doing X] + [unexpected positive result] + [curiosity bridge to mechanism]`
- Apply to 2-3 existing angles to create new copy variants — it's a structure, not a standalone angle
- Combine with existing angles: "I stopped posting content daily. My revenue doubled." (Content Merry-Go-Round + Counterintuitive)

**Risk:** Low. This is a copy structure, not a positioning change. Adaptable to Client Ready's voice without income claims.

---

## Decision 4: Anti-Customization Angle

**Question:** Should "Stop Customizing. Start Scaling." be added to the angle library?

**Decision: YES — add as a secondary angle. It's directly applicable but not a priority launch angle.**

Miles has 2 ads on this angle (1% of library). It's new and lightly tested on his end. But the thesis maps perfectly to Client Ready: the $47 system gives you ONE offer document template, not a custom strategy. The templates in Bump 2 are plug-and-play. The entire philosophy is anti-customization.

**The angle:**
- **Enemy:** The belief that every client needs a custom offer
- **Reframe:** "Custom" = unfocused. Clear, repeatable = scalable.
- **Hook examples:**
  - "Stop customizing your offer for every prospect. Build one that works for all of them."
  - "I used to rewrite my offer for every single lead. Then I realized: if it needs rewriting, it's not clear enough."
  - "The coaches charging $5K+ don't have 10 different offers. They have one. It's just that clear."

**Implementation:**
- Create `reference/proof/angles/anti-customization.md` as a new angle file
- Add to main-angles.md under "Secondary Angles (To Test)"
- Don't prioritize for launch — test after Before the Funnel, Misalignment, Content Merry-Go-Round, and Clarity Unlock are running
- Pairs well with "One Afternoon" angle (one template + one afternoon = done)

**Risk:** Low. Additive to the angle library. Doesn't change positioning or compete with priority angles.

---

## Decision 5: Case Study as #1 Gap

**Question:** Should acquiring the first client case study be elevated to the top priority gap?

**Decision: YES — case study acquisition is now the #1 gap, ahead of all other reference file gaps.**

Miles runs 16 ads (8% of library) on a single case study: Diego, a chess teacher making $14K/month. The specificity ("20-page guide," "The Opening Trap Guide," "$30/day in ads") makes it credible. One concrete story unlocks an entire ad angle category.

Client Ready has zero external case studies. The only proof is Michael's own 114-sales-in-30-days story. This limits:
- Ad copy (can't run case study angles)
- Landing page (no third-party proof)
- Checkout (no testimonial snippets above bumps — a known conversion gap from Miles' research)
- Email sequences (no "here's what happened to [name]" stories)

**Implementation:**
- After first 5-10 sales: actively solicit one detailed case study
- Collect: name, niche, specific result, timeline, one quote
- Mine it into: ad angle, testimonial snippet, email story, landing page proof element
- Even a partial result ("used the system, got clarity on their offer in 2 hours") is better than nothing
- Update testimonials.md and create a case study angle file when available

**Interim workaround (pre-case-study):**
- Lean harder on Michael's own story (114 sales in 30 days) — it IS a case study, just the founder's
- Use the "Anti-Proof" angle from Miles' research: "You don't need testimonials if your offer is clear." This reframes the gap as a feature while the gap is real

**What changes immediately:**
- Update `reference/proof/testimonials.md` status note: "Case study acquisition is the #1 priority gap. Trigger: 5 sales."
- Add to `CLAUDE.md` current gaps: Case study = #1 priority (currently "None collected yet" — upgrade urgency)

**Risk:** None. This is a prioritization shift, not a strategy change. The gap was already identified; this makes it explicit.

---

## Decision 6: $47 Price Validation

**Question:** Should Miles' price migration ($7 → $17) be documented as external validation of Client Ready's $47 price point?

**Decision: YES — document as supporting evidence. Do not change pricing.**

The evidence chain:
1. **Cat Howell (Feb 2026):** $17 front-end killed AOV (dropped from $140 to $70-80). "$47 is her sweet spot — people paying $47 tend to buy everything."
2. **Miles Stutz (Feb 11):** Ran $7 front-end at digitalsnacks.co
3. **Miles Stutz (Feb 22):** Killed $7 entirely. Moved to $17. Still lower than Cat's recommendation.
4. **Client Ready:** $47 from launch, aligned with Cat's data

Miles moving UP from $7 to $17 validates the principle: cheap front-ends attract cheap buyers who don't ascend. Client Ready at $47 is positioned for higher AOV from day one — IF bumps convert at target rates (50%+ take rate, $90-110 AOV).

**Implementation:**
- Add to offer.md under "Checkout Optimization" or "Front-end pricing warning": "External validation: Miles Stutz moved from $7 to $17 in Feb 2026, killing the $7 front-end entirely. Supports $47 as right price point for buyer quality."
- No price changes. $47 stays.
- Monitor: if Miles later moves to $27 or $47, that's further signal

**Risk:** None. Documenting evidence, not changing strategy.

---

## Decision 7: Landing Page Split Test — Video vs Static Mockup

**Question:** Should the front-end landing page run a split test: Hybrid VSL (with video) vs static mockup (no video)?

**Decision: YES — run both variants from launch.**

**Variant A: Hybrid VSL (video)**
- Headline + embedded video + long-form text below + visual evidence
- Video provides founder trust, tone, energy
- Aligned with the Hybrid VSL format in offer.md (headline → video → long-form text → visual evidence → mobile-first)

**Variant B: Static mockup (no video)**
- Headline + product mockups/screenshots + long-form text + visual evidence
- No video production dependency
- Loads faster on mobile (80%+ of traffic)
- Aligned with Miles' finding: Rapid Ascension product runs 95% static — his landing page may not use video either

**Supporting evidence:**
- Miles' complete account reset to 95% static image ads suggests his funnel may be optimizing for static-first experiences
- Cat Howell's Hybrid VSL recommendation is strong, but her data is from higher-spend accounts with warm traffic mixed in
- Naked VSL (video only, no text below) is confirmed dead — both variants include long-form text
- The real question isn't video vs no-video — it's whether the VIDEO adds enough trust to justify the slower load time and production overhead

**Implementation:**
- Build both pages in GHL
- Same copy, same offer, same bumps, same checkout
- Only difference: video section vs product mockup/screenshot section
- Run 50/50 split at $50/day minimum per variant (need $100/day total for meaningful data)
- Decision window: 30 sales minimum per variant before judging (per Cat's "30 sales to trust data" rule)
- Track: conversion rate, AOV, time on page, scroll depth

**Kill criteria:**
- If one variant has 2x+ conversion rate after 30 sales each → kill the loser
- If within 20% of each other after 50 sales each → keep the video version (brand-building compounds over time)
- If video variant loads >3s slower on mobile → optimize before comparing

**What this does NOT decide:**
- Which version to scale with (that comes from data)
- Whether to add video later to the static version (yes, eventually — but test clean first)
- Ad creative format (separate from landing page format — ads can be static even if landing page has video)

**Risk:** Low. Split testing is the right approach. Both variants are viable. The only cost is building two pages instead of one.

---

## Summary

| # | Decision | Action | Priority | Risk |
|---|----------|--------|----------|------|
| 1 | Static image volume | 5 images per copy block (default) | High — affects launch creative brief | Low |
| 2 | AI-forward copy | Elevate AI to headline/link descriptions | High — affects all ad copy | Low |
| 3 | Counterintuitive hook | Add hook pattern to angle library | Medium — copy structure, not new angle | Low |
| 4 | Anti-Customization | New secondary angle file | Low — test after priority angles | Low |
| 5 | Case study #1 gap | Elevate to top priority, update gaps | High — unlocks proof-based ads | None |
| 6 | $47 validation | Document evidence in offer.md | Low — documentation only | None |
| 7 | Landing page split test | Video vs static mockup, 50/50 from launch | High — affects launch page build | Low |

## What Changes

**If all 6 accepted:**

1. **`reference/core/offer.md`** — Add Miles $7→$17 evidence to pricing section. Add "5 images per copy block" note to creative testing section.
2. **`reference/proof/angles/main-angles.md`** — Add "Counterintuitive Reveal" hook pattern section. Move "AI Does 90%" from secondary to primary positioning note. Add Anti-Customization to secondary angles.
3. **`reference/proof/angles/anti-customization.md`** — New file. Secondary angle with hooks, enemy, reframe.
4. **`reference/proof/testimonials.md`** — Add priority note: "Case study acquisition = #1 gap. Trigger: 5 sales."
5. **`CLAUDE.md`** — Update testimonials gap from "None collected yet" to "#1 priority — trigger at 5 sales"

## Risk

All 6 decisions are low-risk. No pricing changes. No positioning changes. No structural changes. All are either documentation (evidence capture), additive (new angle), or refinement (creative testing method). The mining validated existing strategy more than it challenged it.
