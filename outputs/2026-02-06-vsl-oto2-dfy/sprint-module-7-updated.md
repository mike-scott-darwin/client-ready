# Module 7: One-Click Campaign Templates (Updated 2026)

**Aligned with Cat Howell's current methodology from Profit Lab.**

---

## Campaign Philosophy

The old templates used interest stacking, lookalikes, and TOF/MOF/BOF separation. That's obsolete.

**New approach:**
- One ad set, Advantage Plus targeting
- CBO only (no ABO scaling)
- Country targeting only — no interests, no exclusions
- Creative diversity = your targeting
- Scale by adding creative, not new ad sets

---

## Template 1: Main Conversion Campaign

**Use for:** Your primary sales campaign at any budget level.

### Campaign Settings

| Setting | Value |
|---------|-------|
| Objective | Sales |
| Campaign Budget Optimization | ON |
| Daily budget | See Budget Table below |
| Campaign name | `LTO - [Offer Name] - CBO` |

### Ad Set Settings

| Setting | Value |
|---------|-------|
| Conversion location | Website only |
| Pixel | Your pixel |
| Conversion event | Purchase |
| Advantage Plus targeting | ON |
| Locations | US, UK, CA, AU, NZ (or your markets) |
| Interests | NONE |
| Lookalikes | NONE |
| Exclusions | NONE |
| Placements | Advantage+ Placements |
| Ad set name | `Advantage+ - [Countries]` |

### Ad Settings

| Setting | Value |
|---------|-------|
| Advantage+ Creative | OFF |
| Creative enhancements | OFF (except maybe music) |
| Site links | OFF |
| CTA | Learn More (for low-ticket) |
| Ad naming | `[Awareness Level] - [Format] - [Hook]` |

### Budget Table

| Your Budget | Number of Ads | Notes |
|-------------|---------------|-------|
| $25-30/day | 3-4 ads | Minimum viable |
| $50/day | 5-6 ads | Room to test |
| $100/day | 8-10 ads | Sweet spot for testing |
| $250/day | 12-15 ads | Pre-scale |
| $500+/day | 15-20+ ads | Scale mode |

---

## Template 2: Engagement Campaign

**Use for:** Building omnipresence, social proof, and warming cold audiences.

### Campaign Settings

| Setting | Value |
|---------|-------|
| Objective | Engagement |
| Daily budget | $3-25/day per platform |
| Campaign name | `Engagement - [Platform] - [Month]` |

### Ad Set Settings

| Setting | Value |
|---------|-------|
| Engagement type | Post engagement |
| Placements | MANUAL — Facebook Feed only OR Instagram Feed only (separate campaigns) |
| Audience | Broad + Custom audience (engaged last 30 days) |
| Ad set name | `[Platform] - Broad + Engaged 30d` |

### Ad Settings

| Setting | Value |
|---------|-------|
| Format | Existing post (select from your page) |
| Posts per ad set | 2 posts |
| Rotation | Weekly — swap in posts with organic engagement |

### Engagement Campaign Rules

1. Run separate campaigns for Facebook and Instagram
2. Rotate content weekly based on organic performance
3. Use video content for cheapest views
4. Monitor frequency — pause if over 3

---

## Template 3: Retargeting Campaign

**Use for:** Website visitors who didn't purchase.

### Campaign Settings

| Setting | Value |
|---------|-------|
| Objective | Sales |
| Campaign Budget Optimization | ON |
| Daily budget | $20-30/day |
| Campaign name | `Retargeting - [Offer Name]` |

### Ad Set Settings

| Setting | Value |
|---------|-------|
| Conversion location | Website only |
| Pixel | Your pixel |
| Conversion event | Purchase |
| Audience | Custom: Website visitors 180 days, exclude purchasers |
| Placements | Advantage+ Placements |
| Ad set name | `WV 180d - Exclude Purchasers` |

### Ad Settings

| Setting | Value |
|---------|-------|
| Format | Image or short video |
| Copy style | Reminder + urgency + CTA |
| Variations | 3 minimum |

### Retargeting Creative Angles

1. **Reminder:** "Still thinking about it?"
2. **Social proof:** "[X] coaches already inside"
3. **Objection handler:** Address top objection
4. **Urgency:** Time/price-based if applicable

---

## Pixel & CAPI Setup Checklist

### Step 1: Base Pixel Installation

- [ ] Go to Events Manager → Data Sources
- [ ] Select your pixel → Settings
- [ ] Copy your pixel base code
- [ ] Install in `<head>` of ALL funnel pages:
  - Landing page
  - Checkout page
  - Upsell pages
  - Confirmation page

### Step 2: Standard Purchase Event

- [ ] Add purchase event to the page AFTER the order form
- [ ] This is usually your first upsell page (NOT confirmation)
- [ ] Code placement: In `<body>`, fires on page load

```html
<script>
  fbq('track', 'Purchase', {
    value: PURCHASE_VALUE,
    currency: 'USD'
  });
</script>
```

### Step 3: CAPI Setup (via Stape.io)

- [ ] Create account at stape.io (~$10/month)
- [ ] Follow their Facebook CAPI setup guide
- [ ] Connect to your pixel
- [ ] Test events in Events Manager → Test Events
- [ ] Once CAPI working: Remove standard purchase event (prevents double reporting)

### Step 4: Verify in Events Manager

- [ ] Go to Events Manager → Your Pixel → Test Events
- [ ] Open your funnel in a new tab
- [ ] Complete a test purchase
- [ ] Confirm Purchase event fires with correct value
- [ ] Check Event Match Quality score (aim for 8+)

---

## Ads Manager Column Setup

### How to Set Up

1. Go to Ads Manager
2. Click Columns dropdown → Customize Columns
3. Add these columns IN THIS ORDER:
4. Save as preset: "Cat Howell Setup"

### The Columns

| Order | Column | Why |
|-------|--------|-----|
| 1 | **Frequency** | Most important — shows ad fatigue |
| 2 | Results | Your conversions |
| 3 | Cost per result | Your CPA |
| 4 | Purchase ROAS | Return on ad spend |
| 5 | Purchase conversion value (AOV) | Average order value |
| 6 | Website purchases conversion value | Total revenue |
| 7 | Amount spent | Your spend |
| 8 | CTR (link click-through rate) | Hook effectiveness |
| 9 | CPC (cost per link click) | Click efficiency |
| 10 | Landing page views | Actual page loads |

---

## Frequency Monitoring Protocol

| Frequency | Status | Action |
|-----------|--------|--------|
| < 2 | ✅ Healthy | Can scale |
| 2.0 | ⚠️ Warning | Monitor closely |
| 3+ | 🛑 Fatigued | Do NOT scale — add new creatives |

**Critical:** Never scale a campaign with frequency 3+. You'll waste money showing the same ad to the same people.

**Fix for high frequency:** Add new creative to the ad set. Don't raise budget until frequency drops below 2.

---

## Creative Launch Checklist

Before launching any campaign, ensure you have:

### Minimum Viable (3-4 ads)

- [ ] 1 Aware-level ad (direct response, "$27 — Start Now")
- [ ] 1 Problem Aware ad (pain point focus, "Are you struggling with...")
- [ ] 1 Social proof ad (testimonial screenshot or results)
- [ ] 1 Pattern interrupt ad (contrarian or unexpected angle)

### Recommended (8-10 ads)

All of the above, plus:

- [ ] 2 additional message variations of your best hook
- [ ] 1 Video ad (talking head or text-on-screen)
- [ ] 1 Text-only image ad (black background, white text)
- [ ] 1 Carousel (for education or story arc)
- [ ] 1 Unaware-level ad (education/belief shift)

### Scale Mode (15-20 ads)

All of the above, plus:

- [ ] Multiple awareness levels for each angle
- [ ] Creative variations (same copy, different image)
- [ ] Copy variations (same image, different hook)
- [ ] Format variations (same message, different format)

---

## Testing Protocol

### Phase 1: Initial Launch ($25-30/day)

**Duration:** Until $100 spent OR 30+ sales (whichever comes first)

**What to monitor:**
- CTR (should be >1%)
- CPC (should be <$7)
- Any early conversions

**Do NOT do:**
- Kill ads before $100 spend
- Make any optimization decisions
- Panic if no sales in first 48 hours

### Phase 2: Early Optimization ($50-100/day)

**When:** After 30+ sales

**Actions:**
- Review which ads got the most purchases
- Duplicate winners with headline variations
- Pause ads with 0 purchases AND CTR <1%
- Add new creative in underrepresented awareness levels

### Phase 3: Scale ($100+/day)

**When:** After 100+ sales and stable ROAS

**Actions:**
- Increase budget incrementally (20-30% at a time)
- Add creative with every budget increase
- Monitor frequency obsessively
- Expand to new awareness levels if hitting unaware

---

## Campaign Naming Convention

### Campaigns

`[Type] - [Offer] - [Optimization]`

Examples:
- `LTO - Client Ready - CBO`
- `Retargeting - Client Ready`
- `Engagement - IG - Feb`

### Ad Sets

`[Targeting] - [Countries/Audience]`

Examples:
- `Advantage+ - US UK CA AU NZ`
- `WV 180d - Exclude Purchasers`
- `IG Feed - Broad + Engaged 30d`

### Ads

`[Awareness Level] - [Format] - [Hook/Angle]`

Examples:
- `Aware - Image - $27 Direct CTA`
- `Problem Aware - Video - Imposter Syndrome`
- `Solution Aware - Carousel - Why This Beats Courses`
- `Unaware - Text - The Hidden Reason`

---

## Quick Reference: Key Numbers

| Metric | Target | Red Flag |
|--------|--------|----------|
| CTR | >1% | <0.5% |
| CPC | <$7 | >$10 |
| Landing page CVR | 2-5% cold | <1% |
| CPA | <$100 (for $27-67 offer) | >$150 |
| Frequency | <2 | >3 |
| ROAS | >2.0 | <1.0 |

---

## Implementation Checklist

### Week 1: Setup

- [ ] Pixel installed on all pages
- [ ] CAPI configured via Stape.io
- [ ] Test event verified in Events Manager
- [ ] Ads Manager columns configured
- [ ] Campaign naming convention documented

### Week 2: Launch

- [ ] 3-4 ads created across awareness levels
- [ ] Main conversion campaign live at $25-30/day
- [ ] Engagement campaign live at $5/day
- [ ] Monitoring dashboard bookmarked

### Week 3: Optimize

- [ ] First 30 sales analyzed
- [ ] Winners identified
- [ ] Variations of winners created
- [ ] Underperformers paused

### Week 4: Scale

- [ ] Budget increased if ROAS stable
- [ ] New creative added with budget increase
- [ ] Frequency monitored
- [ ] Retargeting campaign launched

---

## Troubleshooting Quick Reference

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| No impressions | Audience too narrow | Confirm Advantage+ is ON, countries only |
| High CPC (>$7) | Hook not working | Test new headlines/images |
| Low CTR (<1%) | Creative not stopping scroll | New pattern interrupt hooks |
| Clicks but no sales | Page not converting | Check message match, page copy |
| High frequency (3+) | Ad fatigue | Add new creative before scaling |
| ROAS dropping at scale | Hitting unaware audience | Add Problem Aware/Unaware creative |

---

## Next Steps

1. Complete Pixel & CAPI Setup Checklist
2. Set up Ads Manager columns
3. Create your first 3-4 ads using the Creative Launch Checklist
4. Launch Main Conversion Campaign at $25-30/day
5. Wait for 30+ sales before optimizing
