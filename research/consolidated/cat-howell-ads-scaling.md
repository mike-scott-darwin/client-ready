---
type: research
status: active
date: 2026-02-03
sources:
  - 2026-02-03-cat-howell-hotseat-scaling.md
  - 2026-02-03-cat-howell-low-ticket-ads-course.md
  - 2026-02-01-cat-howell-scaling-split-tests.md
  - 2026-02-01-ad-analysis-cpa-aov-framework.md
topics: [ads, facebook, scaling, AOV, awareness-levels, campaign-structure, creative, pixel]
---

# Cat Howell: Low-Ticket Ads & Scaling Masterclass

Consolidated research from Cat Howell's Profit Lab training, hot seat calls, and Facebook posts.

---

## Core Philosophy

### Facebook Mirrors Your Internal State

> "Facebook was reflecting this. So my ad accounts would get shut down, campaigns would stop working... I didn't realize that was actually just a mirror of me."

Don't launch campaigns when you're in a bad headspace. The energy you bring affects results.

### Positioning Over Everything

> "The success of your ads is gonna be dependent on the creatives that you give Facebook, the message. But that is going to hinge completely on your positioning."

Positioning = Your Unique Selling Proposition. Examples:
- **Guarantee:** "Performance-based"
- **Price:** "$50/week vs competitors at $2000/month"
- **Niche:** "For mobile car detailers only"
- **Method:** "Done in 24 hours"
- **Result:** "Without sales calls"

---

## Campaign Structure (2026)

### Old Way (Don't Do This)
- Separate ad sets for TOF/MOF/BOF
- Interest-based and lookalike targeting
- Ad set budgets
- Retargeting campaigns

### New Way
- **One ad set** with Advantage Plus targeting
- **Campaign Budget Optimization (CBO)**
- **All creative in one ad set**
- **Target only by country/region** — no interests, no lookalikes, no exclusions
- Let the algorithm find your audience through your creative

> "The algorithm nowadays is really good at finding your ideal targeting. We don't really use lookalikes anymore or interest-based targeting."

### Campaign Setup Steps

1. Click Create → Sales objective
2. Enable Campaign Budget Optimization
3. Set daily budget
4. At ad set level:
   - Website only (NOT "Website and Calls")
   - Select your pixel
   - Purchase as conversion event
   - Advantage Plus targeting
   - Add countries only (US, UK, CA, AU, NZ)
5. At ad level:
   - Turn OFF Advantage+ Creative
   - Turn OFF all creative enhancements (except maybe music)
   - Turn OFF site links
   - Use "Learn More" CTA for low-ticket

### Campaign Naming Convention
- LTO = Low Ticket Offer
- CBO = Campaign Budget Optimization (scaling)
- ABO = Ad Set Budget Optimization (testing)

---

## Budget & Creative Ratio

| Daily Budget | Number of Ads | Why |
|--------------|---------------|-----|
| $25-30/day | 3-4 ads | Need enough spend per ad to collect data |
| $100/day | 8-10 ads | Can test more variations |
| $500+/day | 15-20+ ads | Scale by adding more creative |

**The math:** At 2% conversion and $2 CPC, you need 50 clicks = $100 to expect one sale.

---

## The Awareness Framework

Based on Eugene Schwartz's "Breakthrough Advertising"

| Level | Definition | Creative Approach |
|-------|------------|-------------------|
| **Aware** | Knows you, knows your product | Direct response: "$27 — Start Now" |
| **Solution Aware** | Knows solutions exist, shopping options | "Why this beats [alternative]" |
| **Problem Aware** | Knows they have a problem, not solutions | Pain points, symptoms, "Are you..." |
| **Unaware** | Doesn't know they have a problem | Education, story, belief shifts |

### Why Ads Die After Week 1

Facebook shows your ads to warm audience first (aware/solution aware). Once that's exhausted, it shifts to cold (problem aware/unaware).

If you only have "aware" creative, your ads will tank when Facebook hits the cold audience.

### When You Hit Each Level

- **$100-500/day:** Mostly aware audience, good CPAs, "flow" state
- **$500-1000/day:** CPAs start rising, hitting problem aware
- **$1000+/day:** Definitely hitting unaware, need strategy changes

### Unaware Strategy

1. **Create separate landing page** — doesn't look like a sales page
2. **Educate first** — shift their beliefs, show them they have a problem
3. **Long-form content** — video ads, engagement posts, VSLs
4. **Engagement campaigns** — cheap ($3-25/day), builds omnipresence

> "The businesses that scale really big are the ones who know how to speak to this unaware market."

---

## Validation Thresholds

| Sales | Status |
|-------|--------|
| 5-10 | "Onto something" but NOT validated |
| 30 | Minimum to trust split test data |
| 100 | Truly validated — numbers stabilize |

> "The first six sales that come in, I'm like, oh, this page is the winner for sure... But when I leave it 30, 40 sales, sometimes it's the total opposite."

---

## AOV Levers

### 1. Order Bumps (Highest Impact)

More order bumps nearly **DOUBLED** conversion rates and earnings per page view in Cat's split test:

| Metric | Control (fewer bumps) | Variation (3 bumps) | Change |
|--------|----------------------|---------------------|--------|
| Opt-in rate | 5.17% | **10.02%** | **+94%** |
| Sales rate | 4.94% | **9.44%** | **+91%** |
| Earnings/page view | $3.39 | **$6.10** | **+80%** |

**Bump vs Upsell positioning matters:**
- Same offer, different placement = different conversion
- Test bump order (17/33 vs 33/17 can have "crazy results")

### 2. Front-End Price Point

> "When I did a $17 promo, my AOV went right down. I was getting more sales, more volume, more customers, higher conversion rate, but they were not buying as many of the order bumps and upsells than when I was selling at $47 or $67."

### 3. Membership Trial as Upsell

> "Maybe test out having a membership upsell where you're doing two months or something and you're charging a hundred bucks up front, which would immediately bring your average order value to like $60."

---

## Creative Strategy

### The Social Media → Ads Pipeline

Post on social media first, then use winning content as ads:
1. Tests messaging before spending money
2. Builds your messaging muscle
3. Creates ad creative automatically

### Text-Based Ads Work

> "I would literally just create a text-based image and I would open my notepad... screenshot a square version and a vertical version."

Format: Black background, white text, your hook. That's it.

### Naming Convention

Name ads by awareness level + format + destination:
```
Aware - Image - Order Page
Solution Aware - Video - Sales Page
Problem Aware - Carousel - Sales Page
Unaware - Text - Sales Page
```

---

## Engagement Campaigns

Cat runs separate campaigns for IG and Facebook placements.

**Structure:**
- $3-25/day budget
- 2 posts per ad set
- Rotate content weekly (check what got organic engagement first)
- Target: Cold audience + Warm (engaged last 30 days)

**Why it works:**
- Cheap (video views/engagement = cheapest objectives)
- Builds omnipresence ("you're everywhere on my feed")
- Social proofs your content
- Auction performance: engagement helps you compete

---

## Pixel & Conversion API (CAPI)

### Basic Setup

1. **Base pixel** → Goes in head code of entire funnel
2. **Standard purchase event** → Goes on page AFTER order form (upsell page, not confirmation)

### Why CAPI Matters

Standard pixel = browser-based (affected by cookie blocking)
CAPI = server-side (accurate, tracks AOV)

> "If you're tracking average order value, Facebook will start to optimize for purchase conversion value. It'll start to optimize to go after more of the higher paying customers."

### CAPI Setup

- Use Stape.io ($10/month) for non-techie setup
- Once CAPI works, remove standard purchase event (prevents double reporting)

> "CAPI tracking will give you solid reporting. That's all you need. You don't need Hyros or third-party tools."

---

## Troubleshooting Checklist

### 1. Has there been enough spend at the ad level?
Calculate: (1 ÷ expected conversion rate) × CPC = cost per sale
At 2% conversion, $2 CPC → need $100 spend to expect 1 sale

### 2. Has there been enough landing page views/link clicks?
At 2% conversion → need 50 landing page views to expect 1 sale

### 3. Is CPC acceptable?
**Target:** Under $7 (varies by audience)

### 4. Is CTR acceptable?
**Target:** Over 1% — Low CTR = hook isn't stopping the scroll

### 5. Does the ad "keep the scent"?
Does the landing page match what the ad promised?

### 6. Messaging & positioning (biggest culprit)
> "If you're getting clicks, decent cost per clicks and it's not converting, that means your sales page is losing the job."

### 7. Pricing
**Cold audience sweet spot:** $17-$67
**Can go to $197 if:** Solid testimonials, super defined USP, authority

### 8. Do you actually care about what you're selling?
> "If you're just doing it for the money and you don't actually care, it's not a song of your soul. It's not gonna work."

---

## Scaling Advice

### Hyper-Segment Your Copy

> "The best way to reduce your CPA at scale is to hyper-segment your ad copy and sales page (ex: instead of selling a course on ads to low ticket offers, position it as 'ads to sell $17 ebooks')."

### Target More Unaware Audiences

> "Build out your existing sales page and creatives to they speak to more unaware segment of the audience - as CPA creep is usually because Facebook has depleted the aware segment."

### $100 CPA is Normal

> "A $100 CPA is quite normal. If your funnel converts at 2% and you are getting $2 link clicks then that's a $100 CPA."

The fix: Increase conversion rate OR decrease CPC. If you have a healthy AOV, $100 CPA is fine.

### Testing vs Scaling Performance

Great results in testing campaign (ROAS 3-7), terrible in scaling campaign (ROAS 0.4-0.6)?

> "No not doing anything wrong - not all ads will perform in the scaling campaign as they did in the testing one as these are separate campaigns with different learning optimisations."

**Rule of thumb:** Give it a minute - if it persists at $150 CPA after a couple sales then ax it (keep it running in your ABO testing campaign though).

---

## Key Benchmarks

| Metric | Target | Notes |
|--------|--------|-------|
| Landing page conversion | 2-5% cold, 10-15% warm | Below 2% = messaging problem |
| CPC | Under $7 | Higher OK for niche B2B |
| CTR | Over 1% | Below = hook problem |
| Cost per sale | $50-100 | At 2% CVR, $2 CPC |
| AOV | $100+ | Need bumps/upsells |
| ROAS | 2.0+ | Cat's range: 2.0-2.35 |

### Cat's Actual Campaign Performance

| Campaign | CPA | ROAS | AOV |
|----------|-----|------|-----|
| LTO - Money - Scaling | $61.53 | 2.12 | $130.57 |
| LTO - Visionaries - Scaling | $77.61 | 2.35 | $182.75 |
| Warm - Lab/Codex | $97.51 | — | — |

---

## Tracking & Optimization

### Facebook Ads Manager Columns

Set up in this order:
1. **Frequency** (FIRST — most important for fatigue)
2. Results
3. Cost per result
4. Purchase ROAS
5. AOV
6. Results value
7. Amount spent
8. CTR / CPC
9. Landing page views

### Frequency Rules

| Frequency | Status | Action |
|-----------|--------|--------|
| < 2 | Healthy | Can scale |
| 2 | Warning | Monitor closely |
| 3+ | Fatigued | Do NOT scale — roll out new creatives |

> "If you try to scale a campaign with fatigued ads, you're gonna blow that up."

### Why Single Ads Beat Multi-Variant

Multi-variant: Can't know which creative got the sale
Single ads: Know exactly what works, can duplicate and tweak

> "When I find a winner, the first thing I'll do is duplicate this and change the headline. Or test a different image."

### Higher CPA Can Mean Better Customers

> "Some of my greatest campaigns with return on ad spend and AOV were my most expensive cost per purchase."

Don't optimize for lowest CPA. Optimize for:
1. ROAS (are you profitable?)
2. AOV (are customers spending?)

---

## Split Test Findings

### More Order Bumps = Higher Everything
The order form with the most order bumps has a higher conversion rate + higher earnings per click.

### Video vs No Video
> "I ran a split test on my main sales page - one with video, one without. The one without the video has worked best."

Test everything. Assumptions are often wrong.

### Conversion Rate with Video
Cat's benchmark: 5-6% conversion rate on sales page (with video)
She removed video → conversion dropped. Added video back → returned to 5-6%.

---

## Optimization Process

### Facebook's Recommendation (New Algorithm)

> "Don't optimize at the ad level anymore. Optimize at the ad set level."

If an ad is still getting spend, Facebook is using it in the awareness journey — even if it's not getting direct sales.

### Scaling Method

1. Add more creative (scale by feeding the algorithm)
2. Duplicate ad set with new creative when hitting ad limits
3. Raise budget as you add creative

> "Every time you raise the budget, you should be adding more ads into your ad set."

---

## Quotes Worth Saving

On positioning:
> "The most important thing to your success in business, fuck ads, is your positioning."

On testing:
> "I'm gonna give you a framework. Test this and make it your own. This is not God's word."

On creative:
> "Your job and your only job is to provide Facebook with creative along this awareness scale."

On validation:
> "30 to 100 sales. Below that, it's not really validated."

On free stuff:
> "When you're first getting started out, fuck the free shit. Don't do that. You must sell your offer. Direct response straight up."

On alignment:
> "If it's not a song of your soul... you will give up."

On emotional regulation:
> "If you can see it over a 30 day window and you can see the profit you brought home and how it's actually upward overall, you're gonna have a higher tolerance."
