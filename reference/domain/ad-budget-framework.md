---
type: reference
status: active
date: 2026-02-14
source: Cat Howell Profit Lab data + Miles Stutz research + funnel math
---

# Ad Budget Framework

## Funnel Economics

| Scenario | AOV | How |
|----------|-----|-----|
| Front-end only | $47 | No bumps taken |
| 1 bump average | $114 | $47 + avg bump ($67) |
| Target AOV | $90-110 | Multiple bumps (per Cat Howell benchmarks) |
| Max cart | $248 | $47 + $37 + $67 + $97 (all 3 bumps) |

**Breakeven:** CPA = AOV. Every dollar of AOV above CPA is front-end profit. OTOs and email backend are pure profit on top.

**Note:** Don't count OTO or backend revenue until it's built and proven. Front-end must self-liquidate on its own.

---

## CPA Math

At 2% sales page conversion and $2 CPC:
- 50 clicks = 1 sale
- 50 clicks × $2 = **$100 CPA**

| Daily Budget | Clicks/Day | Sales/Day | Days to 30 Sales |
|--------------|-----------|-----------|-------------------|
| $25/day | ~12 | ~0.25 | ~120 days |
| $50/day | ~25 | ~0.5 | ~60 days |
| $100/day | ~50 | ~1 | ~30 days |
| $200/day | ~100 | ~2 | ~15 days |

---

## Budget Phases

### Phase 1: Validation ($50-100/day — 30 days)

**Goal:** 30+ sales to validate funnel economics.

| Budget | Monthly Cost | Timeline to 30 Sales |
|--------|-------------|---------------------|
| $50/day (minimum) | $1,500/mo | ~60 days |
| $100/day (recommended) | $3,000/mo | ~30 days |

**Budget $3,000 for first 30 days.** This is validation investment, not expected return.

**Rules during validation:**
- Expect $2,000 of spend before judging — learning phase is real
- Don't optimize before 30 sales — early data lies
- Don't panic at day 3
- The $300 rule: if $300 spent with zero sales, change the offer/headline — don't optimize

### Phase 2: Optimization (after 30+ sales)

Evaluate actual CPA vs actual AOV:

| CPA | AOV | Status | Action |
|-----|-----|--------|--------|
| > $150-200 | Any | Losing money | Kill the ad, test new creative |
| $100-150 | < $100 | Bleeding | Fix checkout — bump pricing, bump order, proof |
| $80-120 | $100-120 | Self-liquidating | Let it run, monitor |
| < $80 | $100+ | Profitable | Scale 20% every 48 hours |

**Don't scale until AOV is consistently $100+.**

### Phase 3: Scale (after proven economics)

- Add budget as you add creative — every budget increase needs new ads
- Scale 20% every 48 hours (not bigger jumps)
- Watch frequency — if > 2, ads are fatiguing, add new creative before scaling
- Add entry points (DM Scripts, $5K Playbook as standalone front-ends) per `decisions/2026-02-12-scaling-architecture.md`

---

## Budget by Ad Count

| Daily Budget | Ads to Run | Why |
|--------------|-----------|-----|
| $25-30/day | 3-4 ads | Need enough spend per ad to collect data |
| $50/day | 5-6 ads | Minimum for meaningful testing |
| $100/day | 8-10 ads | Recommended for real data |
| $500+/day | 15-20+ ads | Scale by feeding algorithm more creative |

---

## CPA Decision Thresholds

For Client Ready funnel (target AOV $100-120):

| CPA | Action |
|-----|--------|
| > $150-200 | Kill the ad |
| $80-120 | Let it run, monitor |
| < $80 | Scale 20% every 48 hours |

---

## Key Metrics to Track

**Track in Stripe/GHL, not Meta.** Meta over-attributes.

| Metric | Target | Calculation |
|--------|--------|-------------|
| CPA | < $100 | Ad spend / purchases |
| AOV | $100+ | Total revenue / orders |
| Combined bump rate | 50%+ | Orders with ANY bump / total orders |
| Opt-in rate | 3%+ | Opt-ins / outbound clicks |
| Sales page conversion | 10%+ | Purchases / opt-ins |
| Frequency | < 2 | In Meta Ads Manager — fatigue indicator |
| CTR | > 1% | Below = hook isn't stopping scroll |
| CPC | < $7 | Higher OK for niche B2B |

---

## The Self-Liquidating Test

The funnel is self-liquidating when:

```
Front-end AOV ≥ CPA
```

At that point, you're acquiring customers for free. Every OTO sale, email conversion, and backend sale ($5K Accelerator) is pure profit.

**Cat Howell's benchmark:** 50% of revenue from front-end, 50% from backend (email + product library + affiliates). But backend takes time to build — front-end must work alone first.

---

## Affiliate Revenue Potential (Future)

Once email system is running, natural affiliate recommendations:

| Tool | Fit | Revenue Model |
|------|-----|---------------|
| GHL | Already recommending for funnels | Monthly recurring |
| Skool | Community platform | Monthly recurring |
| AI tools (Claude, etc.) | Used in the product | Referral bonus |
| Email platforms | Part of the funnel | Monthly recurring |

Cat Howell made $30K/month from ClickFunnels affiliates alone. This is future revenue — don't build until email system is live and daily broadcasts are running.
