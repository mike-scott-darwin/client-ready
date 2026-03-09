---
type: decision
status: accepted
date: 2026-03-09
trigger: Modeling low-ticket ecosystem + DFY community integration
linked_decisions:
  - decisions/2026-02-18-training-portal-ecosystem.md
  - decisions/2026-02-12-scaling-architecture.md
  - decisions/2026-03-07-dfy-upsell-community-first.md
  - decisions/2026-03-09-dfy-buyer-cross-sell-strategy.md
---

# Decision: Portal Ecosystem — Bumps as Standalone Tiles + DFY as Community Engine

## What Changed

Two additions to the portal ecosystem architecture:

1. **Checkout bumps double as standalone portal products.** Bumps stay on the checkout page as impulse purchases — nothing changes at point of sale. After purchase, declined bumps appear as locked tiles in the portal with one-click buy (card on file). Three conversion windows per product instead of one.

2. **DFY monthly rebuild included in community membership.** Community members ($97/mo) get one full DFY rebuild per month — new ICP, new offer doc, new sales doc, new ad hooks. Same Claude API integration, same 11-question form, same Michael review. Cost: ~$0.25/build. This becomes the retention engine that justifies the membership.

## Part 1: Bumps as Portal Tiles

### What Stays the Same

- Checkout bumps: $37/$67/$97, same copy, same checkbox, same position
- Bump pricing: unchanged
- Product contents: unchanged

### What Changes

Every bump also exists as a standalone portal tile. Purchase from checkout OR portal unlocks the same content — GHL treats them as the same product tier.

### Three Conversion Windows Per Product

| Window | Timing | Mechanism | Cost |
|--------|--------|-----------|------|
| Checkout bump | Day 0 | Impulse checkbox at checkout | $0 (already built) |
| Bump recovery email | Days 2/4/6 | Email pitches missed bumps | $0 (already designed) |
| Portal locked tile | Every login | One-click buy, card on file | $0 (passive) |

### Portal View (Example: Buyer Who Took Bump 1 Only)

```
✅ Client Ready Offer System ($47)     — unlocked
✅ Quick Win DM Scripts ($37)          — unlocked (bought as bump)
🔒 Plug & Play Templates ($67)        — locked, one-click buy
🔒 First $5K Client Playbook ($97)    — locked, one-click buy
🔒 The One-Page Funnel ($57)          — locked, standalone
🔒 Funnel Snapshot ($97)              — locked, standalone + GHL affiliate
```

### Standalone Entry Points (Phase 2 — After 30+ Sales)

Each bump can become its own ad campaign with its own checkout page and its own set of bumps:

| Standalone Entry | Price | Its Bumps | Target Buyer |
|------------------|-------|-----------|--------------|
| DM Scripts | $37 | Offer System $47 / Templates $67 / One-Page Funnel $57 | "I need to sell NOW" |
| $5K Playbook | $97 | Offer System $47 / DM Scripts $37 / Templates $67 | "I want high-ticket clients" |
| One-Page Funnel | $57 | Offer System $47 / Templates $67 / DM Scripts $37 | "I need a landing page" |
| Funnel Snapshot | $97 | Offer System $47 / One-Page Funnel $57 / Templates $67 | "I need a complete funnel" |

Same products. Different front door. Same portal. All in one CBO campaign.

**Not yet — Phase 2.** Validate the $47 funnel first (30+ sales, $100+ AOV).

---

## Part 2: DFY as Community Engine

### The Problem

Current community value prop: "Weekly calls + tested templates + DM access." That's good but not sticky enough — 15% monthly churn means members leave after ~7 months average.

### The Fix

Add monthly DFY rebuild to community membership. Members submit the same 11-question form (or update previous answers), get full deliverables in 24-48 hours. Michael reviews every build (~10 min).

### Why Coaches Need Monthly Rebuilds

- Pivoting niche after first month of testing
- Raising prices after initial validation
- Testing new ad hooks after first batch underperformed
- Adding a second offer tier
- Refining ICP after 10-20 client conversations
- Seasonal messaging updates

### Pricing Structure

| Tier | DFY Access | Price |
|------|-----------|-------|
| Non-member (portal only) | One-time DFY OTO | $197/build |
| Community member | 1 rebuild/month included | $97/mo |
| Extra rebuilds (members) | Additional builds | $97/build |
| Accelerator | Unlimited during engagement | Included in $5K |

### Economics

| Metric | Value |
|--------|-------|
| Cost per rebuild (Claude API) | $0.15-0.30 |
| Michael review time | ~10 min/build |
| Revenue per community member | $97/mo |
| Gross margin on rebuild | ~99.7% |
| At 100 members, all rebuilding monthly | Cost: $25/mo. Revenue: $9,700/mo. |

### Impact on Community Metrics

| Metric | Without DFY Engine | With DFY Engine |
|--------|-------------------|-----------------|
| Trial-to-paid conversion | 35% | 50% |
| Monthly churn | 15% | 10% |
| Community members (month 12, 150 buyers/mo) | 62 | 112 |
| Community MRR (month 12) | $6,014 | $10,864 |
| Average member lifespan | ~7 months | ~10 months |
| LTV per community member | $679 | $970 |

### Community Positioning Update

**Before:**
> "Month-to-month. Cancel anytime. Weekly calls + tested templates + direct access."

**After:**
> "Month-to-month. Cancel anytime. Every month you get a full DFY offer rebuild — new ICP, new copy, new ad hooks — delivered in 48 hours. Plus weekly calls, tested templates, and direct access to Michael. You stay because the builds alone are worth more than the membership."

### Community Onboarding Flow (DFY Buyers)

```
Day 0:  Buy $197 DFY → 30-day community trial starts
Day 1:  DFY deliverables arrive (ICP + offer doc + sales doc + ad hooks)
Day 3:  "Complete Your Toolkit" email (missed bumps at full price)
Day 7:  First hot seat call → review deliverables live with Michael
Day 14: Submit for first rebuild (refine based on what you learned)
Day 21: Rebuilt deliverables arrive → start testing
Day 28: "Your trial ends in 3 days. Stay for monthly rebuilds."
Day 30: Trial ends → $97/mo charge begins
```

---

## Combined Implementation Checklist

### Portal Infrastructure (Before First Ad Dollar)

- [ ] Fix sales page (29 items from GHL implementation checklist — 2-3 hrs)
- [ ] Create GHL membership area ("Client Ready Training Portal")
- [ ] Create 6 membership tiers — one per product:
  - [ ] Tier: Offer System ($47)
  - [ ] Tier: DM Scripts ($37)
  - [ ] Tier: Templates ($67)
  - [ ] Tier: $5K Playbook ($97)
  - [ ] Tier: One-Page Funnel ($57)
  - [ ] Tier: Funnel Snapshot ($97)
- [ ] Upload 4 existing products as training tiles with content
- [ ] Record 3-5 min video walkthrough per product (4 products)
- [ ] Configure locked tile display: title + description + preview image + price + buy button
- [ ] Configure one-click in-app purchase (card on file) for locked tiles
- [ ] Rewire checkout delivery: purchase → portal login (not Google Doc link)
- [ ] Set up GHL workflows: bump purchase at checkout → unlock matching tier
- [ ] Test full flow: buy $47 → portal shows 1 unlocked + 5 locked → buy locked tile → confirm unlock

### Email Automation

- [ ] Update welcome email: "here's your portal login" (not Google Doc link)
- [ ] Update bump recovery emails (Days 2/4/6): point to portal tiles
- [ ] Add "Complete Your Toolkit" email for DFY buyers (Day 3-5 post-delivery)
- [ ] Set up consumption tracking: GHL tracks who logs in and what they access
- [ ] Wire Day 3 email branch: opened product → advanced tips / hasn't opened → quick start

### DFY Integration

- [ ] Build "Request Rebuild" form in GHL (same 11 questions, pre-filled from last submission)
- [ ] Set up GHL workflow: community member submits form → Claude API → Michael review queue
- [ ] Add rebuild tracking: GHL custom field for builds used this month
- [ ] Cap at 1 rebuild/month for $97/mo members (extra at $97/build)
- [ ] Update community sales copy: OTO page, portal tile, recovery emails, trial-end email

### New Trainings (Month 1-2)

- [ ] Create One-Page Funnel training content ($57)
- [ ] Record video walkthrough + GHL template
- [ ] Create Funnel Snapshot training ($97)
- [ ] Build GHL snapshot export of complete funnel
- [ ] Record snapshot import + customization video
- [ ] Embed GHL affiliate link in Snapshot training
- [ ] Add both as portal tiles
- [ ] Build standalone checkout pages for each

### Multiple Entry Points (After 30+ Sales)

- [ ] Create standalone checkout for DM Scripts ($37) with cross-bumps
- [ ] Create standalone checkout for $5K Playbook ($97) with cross-bumps
- [ ] Create standalone checkout for One-Page Funnel ($57) with cross-bumps
- [ ] Create standalone checkout for Funnel Snapshot ($97) with cross-bumps
- [ ] Add all to one CBO campaign
- [ ] Track which entry point produces highest CLV

---

## What This Does NOT Change

- Checkout bumps stay as impulse purchases at $37/$67/$97
- DFY OTO stays at $197 one-time (first build + community trial)
- DFY Lite downsell stays at $97 one-time
- Community stays at $97/mo month-to-month
- Accelerator stays at $5K
- Skool stays for community — portal is for training content only
- All product contents stay the same
