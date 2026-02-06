# Module 3: Traffic Generation Playbook (Updated 2026)

**Aligned with Cat Howell's current methodology from Profit Lab.**

---

## The New Reality: Algorithm-First Advertising

> "The algorithm nowadays is really good at finding your ideal targeting. We don't really use lookalikes anymore or interest-based targeting."

Everything you learned about Facebook ads before 2024 is outdated. The platform has fundamentally changed. Here's what works now.

---

## Campaign Structure (2026)

### OLD Way (Don't Do This)
- Separate ad sets for TOF/MOF/BOF
- Interest-based targeting
- Lookalike audiences
- Ad set budgets (ABO for scaling)
- Retargeting campaigns
- Audience exclusions

### NEW Way
- **One ad set** with Advantage Plus targeting
- **Campaign Budget Optimization (CBO)** only
- **All creative in one ad set**
- **Target only by country/region** — no interests, no lookalikes, no exclusions
- Let the algorithm find your audience through your creative

**Why this works:** Facebook's algorithm is now sophisticated enough to find your buyers without your help. Your job is to provide it with creative, not audience restrictions.

---

## Campaign Setup (Step by Step)

### Step 1: Create Campaign
1. Click Create → **Sales objective**
2. Enable **Campaign Budget Optimization**
3. Set daily budget (see Budget table below)

### Step 2: Ad Set Level
1. Conversions location: **Website only** (NOT "Website and Calls")
2. Select your pixel
3. Conversion event: **Purchase**
4. Turn ON **Advantage Plus targeting**
5. Locations: Add countries only (US, UK, CA, AU, NZ — or your markets)
6. **No interests. No lookalikes. No exclusions.**

### Step 3: Ad Level
1. Turn **OFF** Advantage+ Creative (you control your creative)
2. Turn **OFF** all creative enhancements (except maybe music)
3. Turn **OFF** site links
4. CTA: **"Learn More"** for low-ticket offers
5. Create **single ads** — not multi-variant carousels

### Why Single Ads?
Multi-variant (dynamic creative): Can't know which creative got the sale.
Single ads: Know exactly what works, can duplicate and tweak winners.

> "When I find a winner, the first thing I'll do is duplicate this and change the headline. Or test a different image."

---

## Budget & Creative Ratio

**Critical insight:** Your budget determines how many ads you can test. Not enough budget per ad = not enough data to learn.

| Daily Budget | Number of Ads | Why |
|--------------|---------------|-----|
| $25-30/day | 3-4 ads | Need enough spend per ad to collect data |
| $100/day | 8-10 ads | Can test more variations |
| $500+/day | 15-20+ ads | Scale by adding more creative |

**The math:** At 2% conversion and $2 CPC, you need 50 clicks = $100 to expect one sale.

**Scaling rule:** Every time you raise the budget, add more ads to your ad set.

---

## The Awareness Framework

Based on Eugene Schwartz's "Breakthrough Advertising" — the key to scaling.

| Level | Definition | Creative Approach |
|-------|------------|-------------------|
| **Aware** | Knows you, knows your product | Direct response: "$27 — Start Now" |
| **Solution Aware** | Knows solutions exist, shopping options | "Why this beats [alternative]" |
| **Problem Aware** | Knows they have a problem, not solutions | Pain points, symptoms, "Are you..." |
| **Unaware** | Doesn't know they have a problem | Education, story, belief shifts |

### Why Your Ads Die After Week 1

Facebook shows your ads to warm audience first (aware/solution aware). Once that's exhausted, it shifts to cold (problem aware/unaware).

**If you only have "aware" creative, your ads tank when Facebook hits cold audience.**

This is why CPA rises at scale — not because "Facebook is broken."

### When You Hit Each Level

- **$100-500/day:** Mostly aware audience, good CPAs, "flow" state
- **$500-1000/day:** CPAs start rising, hitting problem aware
- **$1000+/day:** Definitely hitting unaware, need strategy changes

### Unaware Strategy (For Scaling)

1. **Create separate landing page** — doesn't look like a sales page
2. **Educate first** — shift their beliefs, show them they have a problem
3. **Long-form content** — video ads, engagement posts, VSLs
4. **Engagement campaigns** — cheap ($3-25/day), builds omnipresence

> "The businesses that scale really big are the ones who know how to speak to this unaware market."

---

## Creative Strategy

### Name Your Ads by Awareness Level

```
Aware - Image - Order Page
Solution Aware - Video - Sales Page
Problem Aware - Carousel - Sales Page
Unaware - Text - Sales Page
```

This naming convention tells you exactly what audience and format each ad targets.

### The Social Media → Ads Pipeline

Post on social media first, then use winning content as ads:
1. Tests messaging before spending money
2. Builds your messaging muscle
3. Creates ad creative automatically

### Text-Based Ads Work

> "I would literally just create a text-based image and I would open my notepad... screenshot a square version and a vertical version."

Format: Black background, white text, your hook. That's it.

### Message Types Framework (Critical for Scale)

Per Cat Howell's Andromeda insight — messaging diversity matters MORE than creative diversity.

| Message Type | Entry Point | Example |
|--------------|-------------|---------|
| Problem Agitation | Their pain | "You feel like an imposter..." |
| Transformation | The result | "From stuck to $5K in 30 days..." |
| Contrarian | Pattern interrupt | "Imposter syndrome isn't a confidence problem" |
| Social Proof | Authority | "114 coaches stopped feeling like frauds" |
| Identity Callout | Who they are | "For the coach wearing someone else's positioning" |

**Implementation:**
1. Choose 3-5 core angles for your offer
2. Write 5 message types per angle (15-25 total ads)
3. Pair messages with matching creative types
4. Launch all in the same ad set
5. Let the algorithm distribute to different audience segments

---

## Validation Thresholds

**When is your funnel validated?**

| Sales | Status |
|-------|--------|
| 5-10 | "Onto something" but NOT validated |
| 30 | Minimum to trust split test data |
| 100 | Truly validated — numbers stabilize |

> "The first six sales that come in, I'm like, oh, this page is the winner for sure... But when I leave it 30, 40 sales, sometimes it's the total opposite."

**Implication:** Don't optimize or make big decisions until you have 30+ sales. Everything before that is noise.

---

## Tracking: Pixel & CAPI

### The Problem with Standard Pixel

Standard pixel = browser-based (affected by iOS privacy, cookie blocking).
You're not seeing all your conversions.

### CAPI (Conversion API) is Required

CAPI = server-side tracking (accurate, tracks AOV).

> "If you're tracking average order value, Facebook will start to optimize for purchase conversion value. It'll start to optimize to go after more of the higher paying customers."

### Basic Setup

1. **Base pixel** → Head code of entire funnel
2. **Standard purchase event** → Page AFTER order form (upsell page, not confirmation)

### CAPI Setup

- Use **Stape.io** ($10/month) for non-techie setup
- Once CAPI works, remove standard purchase event (prevents double reporting)

> "CAPI tracking will give you solid reporting. That's all you need. You don't need Hyros or third-party tools."

---

## Engagement Campaigns

Separate from your conversion campaigns. Purpose: Build omnipresence cheaply.

**Structure:**
- $3-25/day budget
- 2 posts per ad set
- Separate campaigns for IG and Facebook placements
- Rotate content weekly (check organic engagement first)
- Target: Cold audience + Warm (engaged last 30 days)

**Why it works:**
- Cheap (video views/engagement = cheapest objectives)
- Builds omnipresence ("you're everywhere on my feed")
- Social proofs your content
- Auction performance: engagement helps you compete

---

## Troubleshooting Checklist

When ads aren't working, check in this order:

### 1. Has there been enough spend at the ad level?
Calculate: (1 ÷ expected conversion rate) × CPC = cost per sale
At 2% conversion, $2 CPC → need $100 spend to expect 1 sale

### 2. Has there been enough landing page views?
At 2% conversion → need 50 landing page views to expect 1 sale

### 3. Is CPC acceptable?
**Target:** Under $7 (varies by audience)

### 4. Is CTR acceptable?
**Target:** Over 1% — Low CTR = hook isn't stopping the scroll

### 5. Does the ad "keep the scent"?
Does the landing page match what the ad promised? (One Pizza, Get Pizza rule)

### 6. Messaging & positioning (biggest culprit)
> "If you're getting clicks, decent cost per clicks and it's not converting, that means your sales page is losing the job."

### 7. Pricing
**Cold audience sweet spot:** $17-$67
**Can go to $197 if:** Solid testimonials, super defined USP, authority

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

### Real Campaign Performance (Cat Howell)

| Campaign | CPA | ROAS | AOV |
|----------|-----|------|-----|
| LTO - Money - Scaling | $61.53 | 2.12 | $130.57 |
| LTO - Visionaries - Scaling | $77.61 | 2.35 | $182.75 |
| Warm - Lab/Codex | $97.51 | — | — |

---

## Scaling Advice

### $100 CPA is Normal

> "A $100 CPA is quite normal. If your funnel converts at 2% and you are getting $2 link clicks then that's a $100 CPA."

The fix: Increase conversion rate OR decrease CPC. If you have a healthy AOV, $100 CPA is fine.

### Hyper-Segment Your Copy

> "The best way to reduce your CPA at scale is to hyper-segment your ad copy and sales page (ex: instead of selling a course on ads to low ticket offers, position it as 'ads to sell $17 ebooks')."

### Target More Unaware Audiences

> "Build out your existing sales page and creatives to they speak to more unaware segment of the audience - as CPA creep is usually because Facebook has depleted the aware segment."

### Higher CPA Can Mean Better Customers

> "Some of my greatest campaigns with return on ad spend and AOV were my most expensive cost per purchase."

Don't optimize for lowest CPA. Optimize for:
1. ROAS (are you profitable?)
2. AOV (are customers spending?)

---

## Facebook Ads Manager Setup

### Column Setup (In Order)

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

---

## Optimization Process (New Algorithm)

> "Don't optimize at the ad level anymore. Optimize at the ad set level."

If an ad is still getting spend, Facebook is using it in the awareness journey — even if it's not getting direct sales.

### Scaling Method

1. Add more creative (scale by feeding the algorithm)
2. Duplicate ad set with new creative when hitting ad limits
3. Raise budget as you add creative

---

## Campaign Naming Convention

- **LTO** = Low Ticket Offer
- **CBO** = Campaign Budget Optimization (scaling)
- **ABO** = Ad Set Budget Optimization (testing)

Example: `LTO - Client Ready - CBO Scaling`

---

## Summary: The Traffic Hierarchy

Master each level before moving to the next:

| Level | Source | Cost | Best For |
|-------|--------|------|----------|
| 1 | Warm outreach (DMs) | Free | First 1-5 clients |
| 2 | Retargeting ads | Low | People who know you |
| 3 | Email to buyers | Free | Existing customers |
| 4 | Lookalike audiences | Medium | Scaling proven offers |
| 5 | Cold interest targeting | High | At scale |
| 6 | Broad/algorithmic | High | Mature funnels only |

---

## Next Steps

1. Set up your pixel + CAPI (Module 7 has the checklist)
2. Create 3-4 ads across different awareness levels
3. Launch at $25-30/day
4. Wait for 30+ sales before optimizing
5. Add more creative as you scale
