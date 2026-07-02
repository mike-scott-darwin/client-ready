---
type: output
format: revenue-model
date: 2026-07-02
status: living-model
source_benchmarks:
  - reference/core/offer.md (Ad Strategy Framework — Cat Howell / Miles Stutz benchmarks)
  - research/2026-05-19-miles-coaching-call-synthesis.md
  - research/2026-06-02-miles-coaching-call-synthesis.md
caveat: PROJECTION from reference-class benchmarks, not booked revenue (~16 real buyers to date). Update the "Actuals" column as data comes in.
---

# Client Ready — Revenue Model & Self-Liquidation

**One-line thesis:** the front end + bumps are priced so **checkout AOV ≈ cost to acquire a buyer**, so ads break even at the point of sale. The DFY OTO, downsell, Monthly Playbook, community, GHL affiliate, and $5K Accelerator are all funded by traffic you already recovered — self-liquidating acquisition feeding a compounding recurring + backend engine.

> All figures below are **modeled**. They're the target math from documented benchmarks, not results. The point is to know which levers matter and to have a yardstick as real numbers replace them.

---

## The self-liquidation equation

```
Checkout AOV (front-end $47 + bumps $37/$67/$97)   ≈   CPA (ad spend ÷ buyers)
        ~$90–110 target                                  <$100 target
```

- If **Checkout AOV ≥ CPA** → the checkout *alone* pays back the ad. Everything after is profit. ✅ self-liquidating.
- If **Checkout AOV < CPA** → you're underwater at day 0 and rely on OTOs + recurring to break even over time. ⚠️ the danger zone.

**Miles's rule (do not skip):** don't scale ad spend until checkout AOV is consistently **$90+** and order-bump take-rate is **33%+**.

---

## Assumptions (the dials)

| Variable | Source | Conservative | Target | Strong | **Actuals** |
|---|---|---|---|---|---|
| CPA (cost per buyer) | offer.md target <$100 | $120 | $90 | $70 | _TBD_ |
| Checkout AOV (FE + bumps) | offer.md $90–110 | $80 | $100 | $115 | _TBD_ |
| Combined bump take-rate | offer.md 50%+ (33%+ min) | — | — | — | _TBD_ |
| Checkout CVR | offer.md 30% | — | — | — | _TBD_ |
| DFY OTO ($197) take | offer.md 15% | 10% | 15% | 20% | _TBD_ |
| DFY Lite ($97) take (of decliners) | offer.md 10% | 8% | 10% | 12% | _TBD_ |
| Monthly Playbook ($37/mo) take | offer.md 8% | 5% | 8% | 10% | _TBD_ |
| Community ($97/mo) paying, % of buyers | estimate | 7% | 12% | 18% | _TBD_ |
| Community trial→paid conversion | estimate | — | — | — | _TBD_ |
| Monthly churn (community + Playbook) | not modeled | — | — | — | _TBD_ |
| Accelerator ($5K) sales per 100 buyers | estimate | 0.5 | 1.5 | 3 | _TBD_ |

> **Fill the Actuals column once ≥30 checkout sales exist.** Retire the guessed inputs first (community %, Accelerator rate, churn). Track in Stripe/GHL, not Meta.

Community % and Accelerator rate aren't in offer.md as hard numbers — they're back-solved to land near the documented **~$260 90-day value/buyer** at Target. Flagged as the softest inputs.

---

## Per 100 buyers

### One-time revenue
| | Conservative | Target | Strong |
|---|---|---|---|
| Checkout (FE + bumps) | $8,000 | $10,000 | $11,500 |
| DFY OTO $197 | $1,970 | $2,955 | $3,940 |
| DFY Lite $97 | $700 | $825 | $930 |
| Monthly Playbook (1st mo) | $185 | $296 | $370 |
| **One-time total** | **~$10,900** | **~$14,100** | **~$16,700** |
| **One-time AOV / buyer** | **~$109** | **~$141** | **~$167** |

Target's ~$141 lines up with offer.md's documented ~$135 full-funnel AOV. ✓

### Recurring (per month, from that cohort)
| | Conservative | Target | Strong |
|---|---|---|---|
| Community $97/mo | $680 | $1,164 | $1,746 |
| Monthly Playbook $37/mo | $185 | $296 | $370 |
| **Recurring / month** | **~$865** | **~$1,460** | **~$2,120** |

Each cohort lays down a new monthly layer that **stacks** on the next — this is the compounding part. (Before churn; GHL affiliate ~$39/mo per Snapshot buyer is upside on top.)

### Backend (Accelerator $5K, sold from community)
| | Conservative | Target | Strong |
|---|---|---|---|
| Accelerator revenue | $2,500 | $7,500 | $15,000 |

Lumpy and delayed — sells over weeks from the community room, not at checkout. Highest variance, highest margin.

---

## Per $10,000 of ad spend

| | Conservative | Target | Strong |
|---|---|---|---|
| Buyers ($10k ÷ CPA) | 83 | 111 | 143 |
| **Day-0 one-time revenue** | **~$9,000** | **~$15,600** | **~$23,900** |
| Day-0 vs spend | **–$1,000 ⚠️** | **+$5,600 ✅** | **+$13,900 ✅** |
| Recurring added / month | ~$720 | ~$1,620 | ~$3,030 |
| Backend (over following weeks) | ~$2,100 | ~$8,300 | ~$21,500 |
| **~90-day total** (one-time + ~3 mo recurring + backend) | **~$13,200** | **~$28,800** | **~$54,500** |
| **~90-day return on $10k** | **~1.3×** | **~2.9×** | **~5.4×** |

**Read this carefully:** in the **Conservative** case you are *slightly negative at day 0* and only pull into profit over 90 days via recurring + backend. That's the whole reason CPA <$100 and checkout AOV $90+ are non-negotiable — they move you from "hope the backend saves it" to "profitable at checkout."

---

## Levers, ranked by impact
1. **Order-bump take-rate (→33%+).** Pushes checkout AOV over $90 → flips you into true self-liquidation. Cheapest lever (copy + guarantee headlines, already drafted).
2. **CPA (<$100).** Geo/creative/offer testing. Miles: "$300 rule" + "$20 signal" — kill losers fast.
3. **DFY OTO take (15%).** Biggest one-time profit block; the 6-deliverable value stack + "more, done" framing support it.
4. **Community trial→paid conversion.** The throttle on the whole recurring engine.
5. **Backend cadence.** 1 extra $5K sale per 100 buyers ≈ the entire one-time profit of that cohort. Compounds hardest.

---

## Instrument these (turn projection → actuals)
Track in Stripe/GHL (not Meta — it over-attributes):
- Checkout CVR (target 30%), **checkout AOV**, **combined bump rate**, per-bump rate
- CPA, per-concept spend-to-first-sale
- DFY take, DFY Lite take, Playbook take
- Community trial starts → paid conversion → churn
- Accelerator sales + time-from-purchase-to-Accelerator

Add an **"Actuals"** column here once ≥30 checkout sales exist; retire the guessed inputs first (community %, Accelerator rate).

---

## Caveats
- **Unvalidated.** Reference-class benchmarks, not your numbers. The relaunch's first job is proving checkout AOV + OTO rates on cold traffic.
- **Proof gap.** Testimonials (your #1 documented gap) materially move DFY/community/backend conversion — the model is soft until you have them.
- **Backend timing.** The $5K attribution is real but *delayed*; don't bank day-0 cash flow on it.
- **DFY fulfillment.** At 15%+ DFY uptake, Michael-review load scales — the weekly slot-cap decision gates how hard you can push it.
- **Recurring churn** not modeled; haircut the annualized recurring by your observed monthly churn once known.
