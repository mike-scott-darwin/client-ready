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
| Front-end only | $27 | No bumps taken |
| 1 bump average | $94 | $27 + avg bump ($67) |
| Target AOV | $70-90 | Multiple bumps (per Cat Howell benchmarks) |
| Max cart | $228 | $27 + $37 + $67 + $97 (all 3 bumps) |

> **Front-end is $27 as of 2026-07-04** (reverted from $47 — see [decisions/2026-07-04-front-end-27-digital-snack.md](../../../decisions/2026-07-04-front-end-27-digital-snack.md)). At $27 the front-end is a **buyer-acquisition price, not self-liquidating** — recover spend on bumps + OTOs + continuity. A lower price should also lift sales-page conversion and pull CPA below the $100 baseline used here; re-derive CPA from live data once the $27 page is running.

**Breakeven:** CPA = AOV. Every dollar of AOV above CPA is front-end profit. OTOs and email backend are pure profit on top.

**Note:** Don't count OTO or backend revenue until it's built and proven. Front-end must self-liquidate on its own.

### AOV by Bump Rate

| Scenario | Bump 1 (37) | Bump 2 (67) | Bump 3 (97) | AOV | vs CPA |
|----------|-------------|-------------|-------------|-----|--------|
| Conservative | 25% | 15% | 10% | ~56 | Losing ~44/sale |
| Moderate | 35% | 25% | 15% | ~71 | Losing ~29/sale |
| Aggressive | 40% | 30% | 20% | ~81 | Losing ~19/sale |
| Cat benchmark | 50%+ combined | — | — | ~80-100 | Near/at breakeven |

**Read this as:** At a $27 front-end and a $100 CPA, the checkout does **not** self-liquidate at any realistic bump rate — that's expected and by design (see note above). The $27 play wins by (a) lower CPA from a cheaper, higher-converting entry, and (b) backend recovery via OTOs + $47/mo community + $37/mo newsletter. Judge it on **blended 90-day value per buyer (~$240)**, not front-end AOV.

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

**Net cash needed:** At a $100 CPA and ~$70 AOV, you lose ~$30/sale on the checkout during validation — but the $27 entry should convert better than the old $47 page, pulling CPA down and offsetting the lower AOV. Budget conservatively: assume ~$30/sale checkout loss over 30 sales (~$900) + timing gaps. Realistic cash outlay: $3,000 upfront, most returned as revenue + backend over 30-90 days. Treat validation cost as buyer-acquisition spend recovered by OTOs/continuity, not a checkout loss to eliminate.

**Why $27 (revised 2026-07-04):** Client Ready ran $27 → $47 → and reverted to **$27**. The earlier case for $47 was that it cut checkout losses during validation. The Jan26 paid data undercut that: the front-end **failed to self-liquidate at $47 on cold traffic** (~0.29 ROAS at the checkout), so the higher price bought a higher barrier without the self-liquidation payoff. The $27 revival is a deliberate **digital-snack / cash-flow** move — maximize buyer volume at a low, frictionless entry and recover spend on bumps + OTOs + continuity. Full rationale: [decisions/2026-07-04-front-end-27-digital-snack.md](../../../decisions/2026-07-04-front-end-27-digital-snack.md). **Watch item:** cheaper buyers historically take fewer bumps (Cat Howell data) — if bump attach craters, revisit.

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
