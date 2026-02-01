---
type: decision
date: 2026-02-01
status: codified
---

# Bump Restructure — Congruency + AOV Fix

## Situation

Funnel had congruency issues between front-end, Bump 1, and Bump 2. Estimated AOV was ~$88, below $100 target.

## Issues Identified

1. **Front-End and Bump 1 overlap** — Both promised "AI to extract zone of genius"
2. **Bump 1 and Bump 2 overlap** — Both claimed to give you a funnel
3. **Timeline contradiction** — Bump 1 said "24 hours," Sprint said "30 days"
4. **Price sequence inverted** — Bump 1 ($47) > Bump 2 ($37)
5. **Energy mismatch** — Bump 1 added work (challenge), Bump 2 reduced work (templates)

## Decision

Restructure bumps for logical flow:

```
$27: WHAT is your offer? (Extract)
  ↓
$37: HOW do I build it? (Templates — reduces energy)
  ↓
$67: HOW do I sell it? (Traffic — next logical step)
  ↓
$97-297: Help me launch (Community + accountability)
  ↓
$397: Do it for me
```

### Old Structure

| Bump | Price | Name |
|------|-------|------|
| Bump 1 | $47 | AI Offer Extract & 24-Hour Launch System |
| Bump 2 | $37 | Six Figure Funnel + 30-Day Email Templates |

### New Structure

| Bump | Price | Name |
|------|-------|------|
| Bump 1 | $37 | Plug & Play Templates |
| Bump 2 | $67 | Traffic & Launch Kit |

## AOV Impact

| Metric | Before | After |
|--------|--------|-------|
| Bump 1 price | $47 | $37 |
| Bump 2 price | $37 | $67 |
| Max cart (bumps) | $84 | $104 |
| Est. AOV | ~$88 | ~$107 |

## Rationale

- **Templates first** — Reduces energy (good bump behavior), higher conversion
- **Traffic second** — Logical next step after you have templates
- **No overlap** — Each product solves a distinct problem
- **No timeline contradiction** — Templates + traffic prep you; Sprint/DFY launches you

## Action Items

- [x] Create decision file
- [x] Update offer.md with new bump structure
- [x] Update Funnel Metrics table
- [x] Push to GitHub
