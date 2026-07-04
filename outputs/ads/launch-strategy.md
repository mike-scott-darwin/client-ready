---
type: output
date: 2026-03-07
status: ready
updated_from: 2026-02-22
linked_research:
  - research/2026-03-03-miles-stutz-hotseat-march.md
  - research/2026-02-22-miles-stutz-ad-library-mining.md
  - research/2026-02-12-cat-howell-hotseat-feb9.md
linked_decisions:
  - decisions/2026-02-22-miles-stutz-mining-response.md
  - decisions/2026-02-17-ad-strategy-framework-update.md
---

# Low-Ticket Ad Strategy — Lean Launch to Scale

Two phases. Phase 1 validates the offer with minimum viable funnel and minimum viable budget. Phase 2 scales what works. Do not skip Phase 1. Do not add Phase 2 complexity until Phase 1 is complete.

---

# PHASE 1: VALIDATE

**Goal:** Confirm the offer sells to cold traffic before investing in OTOs, automation, or scaling.

**Funnel:** Short-form sales page + 3 order bumps + thank you page. No OTOs. No upsell pages. No downsells.

**Budget:** $30/day

**Timeline:** 1-3 weeks depending on data

**Exit criteria:** 10+ sales at CPA under $100, bumps converting at 30%+ each

---

## 1.1 The Validation Funnel

Build only these pages. Nothing else.

| Page | What It Does |
|------|-------------|
| **Sales page** | Pre-headline, headline, sub-headline, product mockup, buy button. That's it. No long-form copy, no video, no testimonials yet. |
| **Checkout** | $47 product + 3 order bumps ($37, $67, $97). Bumps unchecked. |
| **Thank you page** | Delivery access link + quick win CTA ("Open Prompt 1 now") |

**Why no OTOs:** OTOs add 3-4 pages to build, payment logic to wire, and variables to debug. If the front-end doesn't convert, none of that matters. Validate the core offer first.

**Why short-form sales page:** Miles' no-phone offer spends $900/day on a page with: pre-headline, headline, sub-headline, mockup, and a buy button. That's the format that validates. Long-form copy and video come later as CRO tests.

**Why unchecked bumps:** Pre-checked bumps inflate bump revenue but may reduce front-end conversion. Miles: "It only hurts the conversion if you pre-check them." Launch unchecked. Test pre-checked later in Phase 2 as an A/B test.

---

## 1.2 Pre-Launch Checklist

Complete all items before spending a dollar on ads.

### Technical

- [ ] CAPI (server-side tracking) set up — Stape.io ($10/mo) or GTM server-side
- [ ] Sales page live in GHL — short-form only (no split test yet)
- [ ] Checkout page with Stripe connected — $47 product + 3 bumps wired
- [ ] Thank you page live with portal access link
- [ ] Product uploaded to GHL training portal — front-end + bump tiles unlock on purchase
- [ ] Welcome email sequence loaded (BW01-BW10) — triggers on purchase
- [ ] Test purchase completed end-to-end: ad click → sales page → checkout → payment → portal access → welcome email received

### Ads

- [ ] Meta Business Manager configured
- [ ] Pixel installed + CAPI connected
- [ ] Ad account payment method set
- [ ] 3 image creatives produced (see 1.3)
- [ ] Ad copy written — 1 short-form + 1 long-form version
- [ ] 1 ABO campaign created with 2 ad sets (see 1.4)

---

## 1.3 Creative Production (~60 min)

### The Rule: Ad = Sales Page During Validation

Your ad images and copy must say the same thing as your sales page headline. 100% congruence. No creativity yet.

> "The first images we're creating basically say what the headline is saying on the sales page. That way we have 100% congruence between ad and sales page. Once you have a validated digital snack, do whatever." — Miles Stutz

### What to Produce

**3 static images, same message, different format:**

| # | Format | Description |
|---|--------|-------------|
| 1 | **Ugly static** | Your headline as text on a plain background. Notes app screenshot or bold text on solid color. This format drives 60-70% of conversions across accounts. |
| 2 | **Product mockup** | Screenshot of the actual product (PDF, prompts, offer document) on a device mockup. Proves the product is real. |
| 3 | **B-roll lifestyle** | Photo or short video of you in a normal setting (desk, car, walking) with aggressive text overlay of the headline + "Link below." Miles' highest performer. |

**Copy: 1 block, 2 lengths:**

| Version | Length | Use |
|---------|--------|-----|
| Short-form | Under 60 words | Primary text — earns spend fast at low budget |
| Long-form | 150-250 words | Primary text — tests depth vs. brevity |

Same headline across all ads. Same link description. Only the image format and copy length change. One variable at a time.

**Recommended first angle:** [Before the Funnel](./before-the-funnel.md) — "Everyone's selling you funnels. Nobody's asking: do you have an offer worth building one for?"

### Ad Setup Rules

Every ad, every stage:

- **CTA button:** "Learn More"
- **Advantage+ Creative:** OFF
- **Creative enhancements:** OFF
- **Site links:** OFF
- **Conversion event:** Purchase
- **Placements:** Advantage+ Placements (not manual)
- **Ad naming:** `[Awareness] - [Format] - [Angle]`
- **Link description:** "Build a clear, testable $5K offer in one afternoon. Self-guided system. $47."

---

## 1.4 Campaign Structure

**1 ABO campaign. 2 ad sets. $15/day each.**

| Ad Set | Targeting | Budget |
|--------|-----------|--------|
| 1 | Worldwide — broad, no interests | $15/day |
| 2 | Country-based — US, UK, Canada, Australia | $15/day |

Each ad set contains the same ads: 3 images x 2 copy lengths = 6 ads per ad set.

**Why 2 ad sets, not 1:** Worldwide often has cheaper CPMs but lower intent. Country-based has higher CPMs but better buyer quality. Running both tells you which audience converts profitably for your offer.

**Why not 3 ad sets:** Miles recommends a third lookalike ad set, but you need a customer list to build one. Add the lookalike ad set in Phase 2 after you have 50+ buyers.

### Management Rules

**Manage at the ad set level, not the ad level.**

Do not turn individual ads on or off inside an ABO ad set. This destabilizes the ad set. If an ad set is underperforming, replace the entire ad set with a new one.

> "Whenever I do that, I mess up an ad set. Just look at the performance of an ad set, and if the ad set is not performing, you replace the ad set with a new ad set." — Miles Stutz

**Exception:** CBO campaigns (Phase 2) — you can add/remove ads within a single CBO ad set because budget is managed at the campaign level.

### The First 72 Hours

- [ ] Launch both ad sets
- [ ] Do NOT touch anything for 72 hours — no budget changes, no turning ads off, no panicking
- [ ] After 72 hours: review data using kill criteria below

---

## 1.5 Kill Criteria

| Signal | Action |
|--------|--------|
| Ad set: $20 spend, zero clicks | Kill that ad set, launch a new one |
| Ad set: clicks but zero add-to-cart after $40 | Ad-to-page mismatch — check congruence |
| Ad set: CPA > $150 after $100 spend | Kill the ad set |
| Ad set: CPA $80-120 | Let it run, monitor |
| Ad set: CPA < $80 | Winner — increase budget (see 1.6) |
| Frequency 2.0 | Warning — monitor closely |
| Frequency 3.0+ | Fatigued — replace ad set with fresh creative |

**The $20 rule (low-ticket shortcut):** For a $47 product, signal reveals itself after ~$20 of spend per ad set. If an ad set hasn't shown interest by $20, it's probably not going to.

**The $300 rule:** If you spend $300 total without a single sale, change the offer. Don't optimize — change what you're selling.

---

## 1.6 Scaling Winners During Validation

When an ad set is profitable (CPA < $80):

- Increase budget by 20% every 48 hours (conservative)
- If you're willing to risk destabilizing: 50% daily is viable with strong winners

> "I went ahead and literally increased the budget on winning ad sets by 50% every day. Ad sets that spend more will be more stable, period." — Miles Stutz

Monitor cost closely after each increase. If CPA spikes, hold budget for 48 hours before increasing again.

---

## 1.7 Validation Milestones

| Sales | Status | Action |
|-------|--------|--------|
| 0 after $150 | Offer may not work | Check ad-to-page congruence, check headline clarity |
| 2-3 from $150 | Promising signal | Keep running, don't change anything yet |
| 5 | "Onto something" | Collect first testimonials. Check per-bump conversion rates. |
| 10 at CPA < $100 | **Validated** | Check bump rates. If 30%+ each: move to Phase 2. If not: fix bumps first. |

### Bump Conversion Gate

Before moving to Phase 2, each bump must convert at 30% or higher. If a bump is under 30%:

1. Change the bump offer (not just the copy)
2. Consider testing a different product as the bump
3. You can sell bumps before building the product — list it, see if it converts, then build

> "Your bumps should convert at 30, 40, at like a minimum of 30%." — Miles Stutz

**Do not scale ad spend with broken bumps.** Bumps are what make the funnel self-liquidating. Without 30%+ bump rates, you need unrealistic CPA to break even.

---

## 1.8 Troubleshooting (Validation Phase)

If the front-end isn't converting, check in this order:

1. **Ad-to-page congruence?** Does the ad promise the same thing as the headline? If not, align them.
2. **Headline clear enough?** Can someone read it in 5 seconds and know what they get, who it's for, and what it costs?
3. **Enough spend?** At 2% CVR, $2 CPC → need ~$100 per expected sale. Don't judge with $20 of data.
4. **CPC acceptable?** Target under $7. Higher = hook isn't stopping the scroll.
5. **CTR over 1%?** Below 1% = the creative isn't earning attention. Change the image first.
6. **Landing page views match outbound clicks?** If Meta reports 50 clicks but GHL shows 20 views, you have a page load or tracking problem.
7. **Price right?** $47 is confirmed sweet spot. Don't go lower — cheap buyers don't buy bumps.

**If nothing works after $300:** Change the offer. Not the ads, not the copy, not the colors. The offer.

> "If you spend $300 without a sale, change the snack. Don't optimize — change the offer." — Miles Stutz

---

# PHASE 2: SCALE

**Entry requirement:** 10+ sales, CPA < $100, each bump converting at 30%+.

Phase 2 has four stages. Each stage is funded by revenue from the previous stage. Do not jump stages.

---

## 2.1 Post-Validation Setup (Before Scaling Ads)

Once the offer is validated, build the rest of the funnel before increasing ad spend:

### Add OTO Pages

| Page | Priority |
|------|----------|
| OTO 1: DFY Offer Build ($197) | Build first — highest revenue impact |
| OTO 1 Downsell: DFY Lite ($97) | Build second |
| OTO 2: Newsletter ($37/mo) | Build third |
| Community page ($47/mo) | Build fourth — or place on thank you page |

### Add CRO Elements to Sales Page

A/B test ONE element at a time. Run each test for at least 30 sales per variant before choosing a winner.

**First A/B test — add proof:**
- 2 text testimonials below the product mockup (collect during validation phase from first 5 buyers)
- A guarantee statement

**Second A/B test — add "works for you" section:**
- "This method works for [X] types of coaches" — list 4-6 market segments
- This answers the buyer's second question: "OK, it works — but will it work for ME?"

> "The next question they ask is, is it working? By adding proof, you can answer that question. The next question is, is this going to work for me? By adding industries, you can answer that question." — Miles Stutz

**Third A/B test — page format:**
- Variant A: Current short-form (headline + mockup + button)
- Variant B: Hybrid VSL (headline + video + long-form text + visual evidence)
- Same copy, same offer, same checkout. Judge after 30 sales per variant.

### Wire DFY API Pipeline

- GHL form (11 questions) → webhook → Make.com → Claude API → output
- Test with 3-5 fake submissions before going live
- System prompt: `outputs/dfy-upsell/system-prompt.md`

### Add Recovery Email Sequences

- Bump recovery (BR01-BR03): pitch missed bumps — Days 2/4/6
- OTO recovery (OR01-OR03): DFY pitch for buyers who declined — Days 3/5/7
- Community recovery (CR01): direct sign-up pitch — Day 8

---

## 2.2 Stage 1: Expand — $60/day

**Trigger:** OTOs live, first CRO test running, 10+ sales

| Ad Set | Budget | Status |
|--------|--------|--------|
| Winning ad set from validation | $30/day | Keep running |
| New angle: [Content Merry-Go-Round](./content-merry-go-round.md) | $30/day | Testing |

### What to Produce (~45 min)

- 3 new static images for Content Merry-Go-Round (ugly static + mockup + B-roll)
- 1 short-form + 1 long-form copy block
- Also: add a second copy block to the winning validation ad set (new long-form version + 3 fresh images)

### Creative Refresh Cadence

Launch new creative once a week minimum. The more often, the better.

> "The more often you do it, the better. That's the whole Meta philosophy at the moment. Launch more ads." — Miles Stutz

Options for generating fresh creative quickly:
- Keep winning copy, change images (new ugly static, new B-roll angle, AI comic variant)
- Keep winning image, change copy (new hook, new angle, new length)
- Feed winning ads into AI: "Recreate something similar but with a different hook"

### Advance to Stage 2

**30 total sales.** Revenue self-funding at this point.

---

## 2.3 Stage 2: Scale — $90/day

**Trigger:** 30 total sales, data stable

| Ad Set | Budget | Status |
|--------|--------|--------|
| Winning ad sets from Stage 1 | $60/day | Best performers |
| New angle: [Clarity Unlock](./clarity-unlock.md) | $30/day | Testing |

### What to Produce (~45 min)

- 3 new images for Clarity Unlock
- 1 short-form + 1 long-form copy
- Add third ad set: lookalike audience (now possible with 30+ buyers)

### Also at Stage 2

- **Mid-funnel branding campaigns:** Launch after 50+ sales. 5 head-talking videos at $5/day each ($25/day total). Engagement campaign optimized for through-play views. Retarget buyer/visitor audiences. Not selling — just showing your face. Builds frequency and familiarity for community/backend conversion.

### Advance to Stage 3

**AOV confirmed $100+ consistently.** If AOV is under $100, fix bumps and OTO conversion before increasing spend.

---

## 2.4 Stage 3: Full Scale — $200/day

**Trigger:** AOV $100+, 50+ sales, CRO tests showing improvement

This is the first time CBO enters. You now have enough proven winners and enough budget for the algorithm to optimize.

| Allocation | Budget | What |
|-----------|--------|------|
| ABO Testing | $60/day (30%) | New [Misalignment](./misalignment.md) angle + creative refresh |
| CBO Scaling | $140/day (70%) | Proven winners only |

### CBO Setup

1. Create one CBO campaign — Sales objective
2. One ad set inside it — broad targeting
3. Add 5-6 proven winners (10+ sales each) using **Post ID extraction** (keeps social proof — likes, comments, shares)
4. Starting budget: $100-140/day
5. Scale by adding more winning creative, not just more budget

### Cost Caps for Protection

At higher spend, use Cost Caps (target CPA bidding) instead of Lowest Cost. Set cap slightly above your target CPA. Meta only spends when it finds conversions at that price. Protects profitability on volatile days (especially during CPM spikes from external events).

### Advance Beyond Stage 3

**ASC (Advantage Shopping Campaigns):** Only after 100+ total sales and a matured pixel. Let Meta's algorithm handle everything. Not before the data is there.

---

# REFERENCE

---

## The 4 Angles

| # | Angle | Hook | Awareness | Stage |
|---|-------|------|-----------|-------|
| 1 | **[Before the Funnel](./before-the-funnel.md)** | "Everyone's selling you funnels. Nobody's asking: do you have an offer worth building one for?" | Problem Aware / Unaware | Validation |
| 2 | **[Content Merry-Go-Round](./content-merry-go-round.md)** | "You've been posting for 12 months. Getting likes. Nobody's buying." | Problem Aware | Stage 1 |
| 3 | **[Clarity Unlock](./clarity-unlock.md)** | "Most coaches can't explain their offer in one sentence. Fix that in one afternoon." | Solution Aware | Stage 2 |
| 4 | **[Misalignment](./misalignment.md)** | "I burned down a business that was working. Best decision I ever made." | Unaware (belief shift) | Stage 3 |

---

## Target Metrics

### Validation Phase

| Metric | Target | Note |
|--------|--------|------|
| CPA | < $100 | Break-even range |
| Bump take rate | 30%+ per bump | Below = fix bumps before scaling |
| CTR | Over 1% | Below = creative isn't earning attention |
| CPC | Under $7 | Higher OK for niche B2B |
| Landing page CVR | 2-5% cold | Below 2% = headline/messaging problem |

### Scaling Phase

| Metric | Target | Note |
|--------|--------|------|
| Front-end AOV | $100+ | Must hit before scaling beyond $60/day |
| CPA (profitable) | < $80 | Scale winners aggressively |
| Checkout CVR | 30% | Checkout page views → completed purchases |
| ROAS | 2.0+ | Track in Stripe/GHL, not Meta |
| OTO 1 conversion | 15% | DFY Offer Build |
| OTO 1 downsell | 10% of remaining | DFY Lite |
| OTO 2 conversion | 8% | Newsletter |

---

## Creative Format Rankings (2026)

1. **"Ugly" static text-on-background** — Notes app screenshots, tweet formats, high-contrast text. 60-70% of conversions for many accounts. Reads as content, not ads.
2. **B-roll with aggressive text overlay** — Random lifestyle footage (eating, walking, driving) with headline overlay. Miles' current top performer. Engagement from comment arguments breaks down cost further.
3. **Silent Review** — Screen recording of product with facial reactions + text overlay. TikTok-native, high trust.
4. **Founder face-to-camera** — Essential for brand building, not the best for cold traffic.
5. **AI UGC** — Good for volume testing at lower cost. Buyers can spot deepfakes.
6. **Human UGC** — Highest trust for hero assets.

---

## Ad-to-Page Congruence Rules

**During validation (Phase 1):**
- Ad images must say the same thing as the sales page headline
- 100% congruence — no creativity, no experimentation
- This isolates whether the offer itself is in demand

**After validation (Phase 2+):**
- Experiment freely — change images, try different hooks, test comic variants
- Your opinion doesn't matter. Your branding doesn't matter. Cold traffic doesn't know you.
- Data determines what works. If blue converts, make your brand blue.

> "With cold traffic, your opinion doesn't matter. Your branding generally doesn't matter because people don't know who you are. The data matters." — Miles Stutz

---

## CPM Context

CPMs fluctuate based on external events (elections, wars, holidays). Miles reported CPMs >$100 during March 2026 geopolitical events.

If you see a sudden CPM spike:
- Don't kill your ads
- Don't change your strategy
- Wait 3-5 days for normalization
- Monitor CPA, not CPM — you can have high CPMs and still be profitable

---

## Email Strategy During Validation

During Phase 1, email is a sales channel, not a nurture channel.

> "When I started with this journey, I made an offer by email every single day. Below $3 million a year, probably the most important craft for you to learn is making offers that people buy." — Miles Stutz

- Welcome sequence (BW01-BW10) runs automatically
- After Day 10: daily emails, each with one offer from your ladder
- Don't overthink segmentation until you have significant volume
- Making any offer > making no offer

---

## Source Files

- **Ad copy:** [before-the-funnel.md](./before-the-funnel.md), [clarity-unlock.md](./clarity-unlock.md), [content-merry-go-round.md](./content-merry-go-round.md), [misalignment.md](./misalignment.md)
- **Creative briefs:** [launch-creatives-brief.md](./images/launch/launch-creatives-brief.md)
- **One-liners (ugly static source):** [one-liners.md](./one-liners.md)
- **Creative production guide:** [creative-guide.md](./creative-guide.md)
- **Angle details:** [angles/](../../reference/proof/angles/)
- **Miles Stutz March hot seat:** [2026-03-03-miles-stutz-hotseat-march.md](../../research/2026-03-03-miles-stutz-hotseat-march.md)
- **Miles Stutz ad library mining:** [2026-02-22-miles-stutz-ad-library-mining.md](../../research/2026-02-22-miles-stutz-ad-library-mining.md)
- **Cat Howell consolidated:** [cat-howell-ads-scaling.md](../../research/consolidated/cat-howell-ads-scaling.md)
- **Cat Howell AOV benchmarks:** [2026-02-06-cat-howell-aov-benchmarks.md](../../research/2026-02-06-cat-howell-aov-benchmarks.md)
- **Decisions:** [2026-02-22-miles-stutz-mining-response.md](../../decisions/2026-02-22-miles-stutz-mining-response.md), [2026-02-17-ad-strategy-framework-update.md](../../decisions/2026-02-17-ad-strategy-framework-update.md)
