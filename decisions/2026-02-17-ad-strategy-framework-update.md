---
type: decision
date: 2026-02-17
status: accepted
urgency: high
linked_research:
  - research/2026-02-17-abo-vs-cbo-campaign-structure.md
  - research/2026-02-17-andromeda-tiktok-mining.md
  - research/2026-02-17-meta-ads-strategies-2026-gemini.md
---

# Ad Strategy Framework Update — Post-Andromeda 2026

## Situation

Current Ad Strategy Framework in offer.md was built from Miles Stutz + Cat Howell research (Feb 2026) but predates three deep research sessions on:
1. ABO vs CBO campaign structure (Gemini, 33 sources)
2. Andromeda update implications (TikTok practitioner mining, 20 videos)
3. Latest 2026 Meta ads strategies (Gemini, 27 sources)

The framework is solid but has gaps and outdated assumptions. This decision codifies all three research files into specific offer.md updates.

## Decisions

### 1. Three-Stage Campaign Pipeline (replaces current two-stage)

**Current:** ABO testing → CBO/ASC scaling (treated as interchangeable)
**New:**
- **Stage 1: ABO Testing** — Permanent sandbox, one concept per ad set, $50/day per ad set
- **Stage 2: CBO Winners** — Proven creatives only, graduate via Post ID extraction
- **Stage 3: ASC Scaling** — Only with matured pixel + proven creatives (not interchangeable with CBO)

**Why:** ASC is a black box that can't exclude past purchasers and over-indexes on retargeting at low volume. CBO is the middle step.

### 2. One Concept Per Ad Set (replaces 8-10 ads per ad set)

**Current:** "8-10 ads per ad set" in ABO testing
**New:** One CONCEPT per ad set, variants within. Each ad set tests a single angle (Pain, Mechanism, Social Proof).

**Why:** 8-10 ads in one ad set means Meta picks a winner fast and starves the rest. One concept per ad set forces equal spend across concepts, giving you real data on each angle.

### 3. Post ID Extraction Step

**Add:** When graduating winners from ABO → CBO, extract the Post ID so the winning ad keeps its social proof (likes, comments, shares). Don't create a new ad — reference the existing one.

### 4. 70/20/10 Budget Split

**Current:** No explicit budget split defined for scaling vs testing
**New:**
- 70% Scaling (Broad CBO, best creatives)
- 20% Testing (ABO sandbox, new concepts)
- 10% Retargeting (optional, or fold into scaling)

**Launch phase flip:** At launch, reverse to 70% testing / 30% scaling (no winners yet). Shift ratio as winners emerge.

### 5. Creative IS Targeting (Post-Andromeda Principle)

**Add as top-level principle:** Post-Andromeda, Meta's algorithm operates at the account level. Creative (copy + visual) is the primary targeting signal. Broad targeting is default. Interest stacking, lookalikes, and micro-segmentation restrict the AI and raise CPMs.

### 6. New Creative Formats

**Add to creative mix:**
- **"Ugly" Static Ads** — Notes app screenshots, tweet formats, text-on-plain-background. Driving 60-70% of conversions for many accounts. They read as content, not ads.
- **Silent Review** — Screen recording of the product (PDF, prompts, templates) without speaking. Facial reactions + text overlay only. Feels native, breaks the pattern of "shouting" marketers.
- **"Don't Buy This" Hook** — Reverse psychology: "Don't buy this system... if you hate having an offer that sells itself." Filters for high-intent buyers.

**Creative format ranking (2026):**
1. "Ugly" static text-on-background
2. Silent Review
3. B-roll with text overlay (already in framework)
4. Founder face-to-camera (essential for brand, not best for cold traffic)
5. AI UGC (good for volume testing, but buyers spot deepfakes)
6. Human UGC (highest trust for hero assets)

### 7. Radical Creative Variance

**Add as principle:** Testing minor variations (button colors, slight copy tweaks) is dead. "Radical Variance" = testing entirely different concepts (Silent Review vs Founder Story vs Problem/Solution) to reach different pockets of the broad audience.

### 8. Cost Caps for Scaling

**Add:** When scaling CBO/ASC campaigns at higher spend ($5K+/day eventually), use Cost Caps (target CPA bidding) instead of Lowest Cost. Set cap slightly above target CPA. Meta only spends when it finds conversions at that price. Protects profitability on volatile days.

### 9. CAPI as Pre-Launch Requirement

**Add:** Server-side Conversions API (CAPI) setup is critical. Bypasses browser cookie blocking (iOS 14+). Improves "Event Match Quality" score, lowers CPMs. Should be set up before first dollar of ad spend.

### 10. $20 Rule for Low-Ticket Testing

**Add alongside $300 rule:** For low-ticket items ($47), winners reveal themselves after ~$20 of spend per concept. Faster signal than the $300 rule (which applies to higher-ticket offers).

### 11. Hybrid VSL Landing Page

**Add:** Naked VSLs (video-only pages) are dying — high bounce rates from cold traffic. The winning format is the "Hybrid VSL":
1. Headline (big promise)
2. VSL video (5-15 min, founder + B-roll of product)
3. Long-form text (entire script adapted to readable copy BELOW the video)
4. Visual evidence (GIFs/screenshots of the product being used)
5. Mobile-first (80%+ traffic is mobile)

### 12. What's NOT Working in 2026

**Add as anti-patterns:**
- Interest stacking — restricts AI, raises CPMs
- Micro-budget ad sets ($5/day) — never exit learning phase
- Naked VSL pages — video-only pages bouncing hard
- Manual placements ("Feed Only") — Advantage+ Placements finds cheaper inventory
- Lookalikes as primary targeting — algorithm does it better automatically

## What Changes

**File:** `reference/core/offer.md` — Ad Strategy Framework section (lines 374-480)

Updates:
1. Add "Post-Andromeda Principles" subsection (creative IS targeting, broad default, radical variance)
2. Replace "8-10 ads per ad set" with "one concept per ad set, variants within"
3. Add three-stage pipeline: ABO → CBO (via Post ID) → ASC
4. Add 70/20/10 budget split (with launch-phase flip)
5. Add creative format rankings with Silent Review + ugly static
6. Add Cost Caps for scaling
7. Add CAPI as pre-launch requirement
8. Add $20 rule for low-ticket alongside $300 rule
9. Add Hybrid VSL landing page structure
10. Add "What's NOT Working" anti-patterns list

**No other files affected.** This is a reference file update only.

## Risk

Low. These are research-backed refinements to an existing framework. All changes are additive or corrective — nothing structural changes about the funnel or pricing.
