---
type: research
date: 2026-02-17
source: gemini-deep-research + web mining
topic: ABO vs CBO Facebook/Meta ad campaign structure
relevance: Ad strategy framework in offer.md
---

# ABO vs CBO Campaign Structure for Low-Ticket Funnels

## One-Sentence Summary

ABO is for testing (forces equal spend across creatives), CBO is for scaling (algorithm finds cheapest conversions), and the "ABO forever" crowd has a point for tight-margin funnels but requires elite manual management.

## Key Findings

### 1. Conventional Wisdom Still Holds — With Nuance

The "ABO for testing, CBO for scaling" framework remains accurate in 2025-2026. What's changed is the rise of Advantage+ (ASC) as a third option, and better understanding of WHY CBO starves ad sets.

### 2. Why CBO "Starves" Ad Sets

CBO distributes budget based on **predicted marginal cost**. If Ad Set A has a historical CPA of $20 and Ad Set B (new, untested) has a predicted CPA of $50, CBO will spend 90%+ on Ad Set A. The problem: Ad Set B might have achieved $15 CPA if given 5,000 impressions to optimize, but CBO never gave it the chance. This is prediction-based, not performance-based — and that's the core flaw for testing.

### 3. ABO Guarantees Data Collection

With ABO, if you allocate $50 to an ad set, Meta MUST spend $50 on it. This is critical when testing new angles because you need data on EVERY angle to make informed decisions. CBO optimizes for efficiency, not information.

### 4. The "ABO Forever" School

Some high-spend media buyers ($1K-$10K/day) run ABO exclusively because:
- CBO optimizes for CTR/engagement, not necessarily conversions
- Low-ticket margins are too tight for CBO's "waste" period
- Manual control lets you force the "72-hour rule" (let ads run 3 days before judging)
- **Trade-off:** Requires daily manual intervention. You become the algorithm.

### 5. The Hybrid Model (Consensus Best Practice)

Most practitioners recommend:
- **ABO Campaign (20% of budget):** Perpetual "sandbox" for testing new creatives
- **CBO Campaign (80% of budget):** "Winners circle" with only proven ads
- Graduate winners from ABO → CBO using **Post ID extraction** (retains social proof)

### 6. Advantage+ Shopping (ASC) — Scaling Tool Only

ASC can lower CPA by 17-30% but:
- No audience targeting control (black box)
- Struggles to exclude past purchasers (wastes spend on $47 product)
- Only useful with proven creatives and matured pixel
- Some practitioners saw ASC CPA double vs manual CBO (over-indexes on retargeting)

### 7. Your Specific Situation ($150/day, New Funnel)

**Recommended launch structure: ABO**

- Campaign: ABO, Sales objective
- 3 ad sets x $50/day each
- Each ad set = one creative angle (Pain, Mechanism, Social Proof)
- Targeting: Broad (let creative define the audience)
- Run 72 hours untouched
- Day 4: Kill any ad set with CPA > $80 (1.5x breakeven)
- Week 3+: Graduate winners to CBO via Post ID extraction
- Scale CBO 20% every 2-3 days as long as CPA holds

### 8. Common Mistakes

1. **Using Traffic objective for sales** — trains pixel to find clickers, not buyers
2. **Over-segmenting** — 10 ad sets at $10/day each means none exit learning phase
3. **Premature CBO scaling** — moving to CBO without statistical significance (need 10+ sales per creative)
4. **"Set and forget" ABO** — ABO forces spend even when performance dips, needs daily hygiene
5. **Ignoring creative fatigue** — ship new ads weekly ("creative velocity")

### 9. Key Metrics Benchmarks

- ABO delivers 94% avg ROAS for prospecting vs 81% for CBO (general benchmark)
- Checkout CVR target: 30% (from Miles Stutz)
- Budget per ad set for meaningful data: $50/day minimum
- Time to judge: 72 hours minimum, 7-14 days for real significance
- Scale trigger: 50+ purchases recorded, stable winning creative

### 10. How This Maps to Current offer.md Strategy

**Current offer.md says:**
- Testing: ABO at $50/ad set, 8-10 ads per ad set, 3 new ad sets per week
- Scaling: CBO/ASC with monthly winners, $100/day starting budget

**Research validates this** but adds:
- Keep ABO running permanently (20% of budget) as testing sandbox
- Don't put 8-10 ads in one ABO ad set — one CONCEPT per ad set, variants within
- Use Post ID extraction when moving winners to CBO
- ASC is the third stage, not interchangeable with CBO
- Cost caps in CBO/ASC stabilize volatile days

## Implications for Reference Files

- offer.md Ad Strategy section could add: permanent ABO testing sandbox, Post ID extraction step, ASC as third stage (not replacement for CBO)
- The 80/20 budget split (CBO winners / ABO testing) is a clean rule worth codifying

## Open Questions

- Miles Stutz runs ABO at $50/ad set — does he graduate to CBO or stay ABO-only?
- What's Cat Howell's actual campaign structure at scale?
- Should we set cost caps on CBO campaigns from day one?

## Sources

- Gemini Deep Research (33 sources synthesized)
- Sam Piliero (WisdomAI) — CBO default, 80/20 hybrid
- Motion App — 3-phase creative testing framework
- Multiple Reddit r/facebookads threads
- TwoOwls, Madgicx, AdAmigo, Rowads practitioner guides
