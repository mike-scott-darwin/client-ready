---
type: research
date: 2026-02-01
source: mining
topics: [ads, cpa, aov, optimization, benchmarks]
status: complete
---

# Ad Analysis Framework: CPA vs AOV

**Source:** Skool post - "How to analyze results after offer validation & OTO launch?" (Sergio Sasso response)

---

## The Framework (from Sergio Sasso)

### Step 1: Calculate Funnel AOV
Know your average order value across all products (front-end + bumps + OTOs).

### Step 2: Compare CPA to AOV on Each Ad Set

| Scenario | Action |
|----------|--------|
| CPA > 1.5-2x AOV (spent that much, no results) | **Kill it** |
| CPA ≈ AOV (near or same) | **Leave it running** |
| CPA < AOV | **Scale it** — increase budget 20% every 48 hours |

---

## How to Launch New Ads

1. **Duplicate existing ad sets** inside the same campaign
2. **Change the ads** (new creatives/copy)
3. **Duplicate 4 times** for different audiences:
   - Interests
   - Lookalikes
   - Open targeting
   - Warm audience

---

## Real Benchmark Data (Raeed's Funnel)

### His Numbers
- **AOV:** $13
- **Goal:** 2x ROI (make money on front-end)
- **KPI:** CPA < AOV
- **Total UOC (unique outbound clicks):** 1,693
- **Total sales:** 46 sales + 19 order bumps

### Conversion Rates by Audience Type

| Audience | Sales | UOC | Conversion Rate | CPA |
|----------|-------|-----|-----------------|-----|
| **Warm** | 6 | 124 | 4.8% | $17.08 |
| **Interest** | 9 | 153 | 5.8% | $20.19 |
| **Lookalike** | 8+ | — | — | — |

### Key Insight
- Interest targeting outperformed warm audience on conversion rate
- But both CPAs ($17-20) are above his $13 AOV
- Needs to either improve AOV (more bumps) or improve conversion

---

## Validation Timeline (from original post)

1. **Validation:** 3 days cold traffic → 21 sales → **validated**
2. **OTO1 launch:** 1 full week → got sales
3. **Analysis phase:** Evaluate CPA, ROAS, CTR to decide scale/kill/improve

---

## Application to Client Ready

### Your Target Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| **Front-end price** | $27 | — |
| **Max cart** | $825 | All bumps + OTOs |
| **Target AOV** | $100-120 | With ~40% bump take rate |
| **Target CPA** | < $100 | To break even on front-end |
| **Scale threshold** | CPA < $80 | Room to increase budget |

### Decision Framework for Your Ads

| Your CPA | Action |
|----------|--------|
| > $150-200 (1.5-2x AOV) | Kill the ad set |
| $80-120 (≈ AOV) | Let it run, monitor |
| < $80 | Scale 20% every 48 hours |

### Audience Testing Order
1. **US, UK, Canada, Germany** (Miles' winning combo)
2. **US, UK, Canada** only
3. **Retargeting** (half budget, usually wins)
4. **Worldwide lookalike** (usually loses, but test anyway)
