---
type: research
status: complete
date: 2026-02-03
source: transcript
topics: [ads, facebook, campaign-structure, creative, awareness-levels, positioning, pixel, optimization]
linked_decisions:
  - decisions/2026-02-03-funnel-optimization-post-cat-howell.md
---

# Cat Howell — Low Ticket Ads Course

Source: Cat Howell Low Ticket Ads Training (2025)

---

## Core Philosophy: Facebook Mirrors Your Internal State

> "Facebook was reflecting this. So my ad accounts would get shut down, campaigns would stop working... I didn't realize that was actually just a mirror of me."

**Practical application:** Don't launch campaigns when you're in a bad headspace. If you're exhausted, angry, hangry — go touch grass first. The energy you bring affects results.

> "If you're really not in a good head space, it does pay to just go touch some grass... do something that shifts your energy, even just a little, and then come back to those campaigns."

---

## The Foundation: Positioning Over Everything

> "The success of your ads is gonna be dependent on the creatives that you give Facebook, the message. But that is going to hinge completely on your positioning."

**Positioning = Your Unique Selling Proposition**

Examples of positioning angles:
- **Guarantee:** "Performance-based" (how Cat made $20M)
- **Price:** "$50/week vs competitors at $2000/month"
- **Niche:** "For mobile car detailers only"
- **Method:** "Done in 24 hours"
- **Result:** "Without sales calls"

> "Positioning can be a niche. It can be the type of customer. It can be price. It can be guarantees. It can be something in how you work with clients."

**The positioning test:** If you're just screenshotting other people's ads and mimicking them, you'll sound like everyone else. You need something unique.

---

## Campaign Structure (2025 Update)

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

---

## Budget & Creative Ratio

| Daily Budget | Number of Ads | Why |
|--------------|---------------|-----|
| $25-30/day | 3-4 ads | Need enough spend per ad to collect data |
| $100/day | 8-10 ads | Can test more variations |
| $500+/day | 15-20+ ads | Scale by adding more creative |

> "If you have 19 or 20 ads in your ad set, you might be waiting a week and a half for a sale to come through just for it to get enough data."

**The math:** At 2% conversion and $2 CPC, you need 50 clicks = $100 to expect one sale. With $25/day budget split across 4 ads, each ad gets ~$6/day. Takes 4+ days per ad to reach statistical significance.

---

## The Awareness Framework

Based on Eugene Schwartz's "Breakthrough Advertising"

| Level | Definition | Creative Approach |
|-------|------------|-------------------|
| **Aware** | Knows you, knows your product | Direct response: "$27 — Start Now" |
| **Solution Aware** | Knows solutions exist, shopping options | "Why this beats [alternative]" |
| **Problem Aware** | Knows they have a problem, not solutions | Pain points, symptoms, "Are you..." |
| **Unaware** | Doesn't know they have a problem | Education, story, belief shifts |

> "The biggest mistake I'm seeing is people think diversity of creative means different formats... It's not about that. What Facebook wants is messaging across different levels of customer awareness."

### Why Ads Die After Week 1

Facebook shows your ads to warm audience first (aware/solution aware). Once that's exhausted, it shifts to cold (problem aware/unaware).

If you only have "aware" creative, your ads will tank when Facebook hits the cold audience.

> "A lot of people see they get results up front from their ads like the first week and then things tail off because they're not creating messaging for the unaware audience or the problem aware."

### Scaling = Talking to Unaware

> "The businesses that scale really big are the ones who know how to speak to this unaware market. It's very easy to speak to the aware market — it's like, here's my product, buy now. It takes a whole different type of marketer to speak to people who are unaware."

---

## Creative Strategy

### The Social Media → Ads Pipeline

Cat's method: Post on social media first, then use winning content as ads.

**Benefits:**
1. Tests messaging before spending money
2. Builds your messaging muscle
3. Creates ad creative automatically
4. Two birds, one stone

> "It took me less than an hour to launch all of these ad creatives... I had already posted about it on my IG or my Facebook page, or there was an email sent out."

### Text-Based Ads Work

> "I would literally just create a text-based image and I would open my notepad... screenshot a square version and a vertical version. You'd be surprised."

Format: Black background, white text, your hook. That's it.

### Naming Convention

Cat names ads by awareness level + format + destination:

```
Aware - Image - Order Page
Solution Aware - Video - Sales Page
Problem Aware - Carousel - Sales Page
Unaware - Text - Sales Page
```

---

## Pixel & Conversion API (CAPI)

### Basic Setup (Beginner)

1. **Base pixel** → Goes in head code of entire funnel
2. **Standard purchase event** → Goes on page AFTER order form (upsell page, not confirmation)

Ask ChatGPT: "Give me the Facebook base pixel code" and "Give me the code for Facebook standard purchase event"

### Why CAPI Matters

Standard pixel = browser-based (affected by cookie blocking)
CAPI = server-side (accurate, tracks AOV)

> "If you're tracking average order value, Facebook will start to optimize for purchase conversion value. It'll start to optimize to go after more of the higher paying customers."

**Without CAPI:** No AOV tracking, no results value, Facebook optimizes for volume only

**With CAPI:** Tracks every bump/upsell, Facebook optimizes for value

### CAPI Setup

- Use Stape.io ($10/month) for non-techie setup
- Or hire a developer for custom setup
- Once CAPI works, remove standard purchase event (prevents double reporting)

> "CAPI tracking will give you solid reporting. That's all you need. You don't need Hyros or third-party tools."

---

## Troubleshooting Checklist (8 Points)

From Cat's troubleshooting framework:

### 1. Has there been enough spend at the ad level?

Calculate: (1 ÷ expected conversion rate) × CPC = cost per sale

At 2% conversion, $2 CPC → need $100 spend to expect 1 sale

### 2. Has there been enough landing page views/link clicks?

At 2% conversion → need 50 landing page views to expect 1 sale

### 3. Is CPC acceptable?

**Target:** Under $7 (varies by audience)

Niche B2B might be $9+ but with higher conversion rates

### 4. Is CTR acceptable?

**Target:** Over 1%

Low CTR = hook isn't stopping the scroll

### 5. Does the ad "keep the scent"?

Does the landing page match what the ad promised?

> "You're saying one thing in your ad, and then they're hitting this landing page and they're like, where am I? This happens so much."

### 6. Messaging & positioning (biggest culprit)

> "If you're getting clicks, decent cost per clicks and it's not converting, that means your sales page is losing the job. It's usually your messaging. It's usually how you've positioned your offer."

### 7. Pricing

**Cold audience sweet spot:** $17-$67

**Can go to $197 if:**
- Solid testimonials
- Super defined USP (micro outcome)
- Authority in the space

> "If you're trying to sell something that's $300 upfront to a cold audience and they've never heard of you before... that's part of your messaging. It's not gonna work that well."

**Membership note:** Don't sell memberships cold. Use low-ticket front-end first.

### 8. Do you actually care about what you're selling?

> "If you're just doing it for the money and you don't actually care, it's not a song of your soul. It's not gonna work."

---

## Optimization Process

### Facebook's Recommendation (New Algorithm)

> "Don't optimize at the ad level anymore. Optimize at the ad set level."

If an ad is still getting spend, Facebook is using it in the awareness journey — even if it's not getting direct sales.

### Cat's Approach

Still turns off underperforming ads, but with context:
- Check if ad has spent enough first
- Check ad set level performance
- When ad cap is hit, duplicate ad set and add new creative

### Scaling Method

1. Add more creative (scale by feeding the algorithm)
2. Duplicate ad set with new creative when hitting ad limits
3. Raise budget as you add creative

> "Every time you raise the budget, you should be adding more ads into your ad set."

---

## Key Benchmarks

| Metric | Target | Notes |
|--------|--------|-------|
| Landing page conversion | 2-5% cold, 10-15% warm | Below 2% = messaging problem |
| CPC | Under $7 | Higher OK for niche B2B |
| CTR | Over 1% | Below = hook problem |
| Cost per sale | $50-100 | At 2% CVR, $2 CPC |
| AOV | $100+ | Need bumps/upsells |

### Conversion Rate Math

```
Conversion rate × CPC = Cost per sale

2% × $2 CPC = $100 per sale
3% × $2 CPC = $66 per sale
4% × $2 CPC = $50 per sale
5% × $2 CPC = $40 per sale
```

> "If you raise the conversion rate by even 1%, look what happens... you have almost half the cost per acquisition."

---

## Multiple Funnels Strategy

Cat runs 3+ funnels to different low-ticket offers:
- Low Ticket Codex
- Low Ticket Ads
- Spell Crafter (different ecosystem)

> "The marketers that are able to scale... my goal is to spend $1000-3000 a day. As you scale, you're gonna want to have a couple entry points."

**Important:** All offers should connect to ONE ecosystem/big idea. Cat's mistake was mixing woo (Spell Crafter) with business (Low Ticket Codex).

---

## Quotes Worth Saving

On positioning:
> "The most important thing to your success in business, fuck ads, is your positioning. This is what Ogilvy says."

On testing:
> "I'm gonna give you a framework. Test this and make it your own. This is not God's word."

On creative:
> "Your job and your only job is to provide Facebook with creative along this awareness scale."

On passive income:
> "If you're thinking you're gonna run some ads so that you have a completely passive business, I've got a hard truth for you. That doesn't exist."

On social posting:
> "You will improve your ad results if you are making a habit of talking about your offer on social media. It does help."

On pricing:
> "I find pricing between $17-$67 works best for cold audience. You can go to $197 if you have SOLID testimonials and a super defined USP."
