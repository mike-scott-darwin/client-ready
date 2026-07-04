---
type: reference
status: active
date: 2026-03-07
updated_from: 2026-02-01
linked_decisions:
  - decisions/2026-03-07-dfy-upsell-community-first.md
---

# Funnel Stages

## The Client Ready Funnel

```
AWARENESS (Content / Ads)
    |
MICRO-COMMITMENT ($47 Front-End)
    |
ORDER BUMPS ($37 + $67 + $97)
    |
OTO 1: DFY Offer Build ($197) + 30-day community trial
    |  NO --> Downsell: DFY Lite ($97) + 30-day community trial
    |
OTO 2: "What's Working Now" Newsletter ($37/mo)
    |
THANK YOU + ONBOARDING FORM (triggers DFY build)
    |
GHL TRAINING PORTAL (cross-sell locked products)
    |
EMAIL ASCENSION (10-day welcome + daily emails)
    |
COMMUNITY ($47/mo after trial) <-- THE ENGINE
    |
BACKEND: Accelerator ($5K) -- sold from community
    |
RETENTION (Results --> Referrals --> Case Studies)
```

---

## Stage 1: Awareness

**Goal:** They discover Michael exists

**Channels:**
- Paid ads (Facebook/Instagram) — primary
- Organic social content (LinkedIn, X)
- Word of mouth from clients
- Podcast appearances / collaborations

**Key message:** "The Coach Who Won't Tell You to Quit Your 9-to-5"

---

## Stage 2: Micro-Commitment — $47 Front-End

**Goal:** They make first purchase

**Product:** Client Ready Offer System ($47)

**Trigger:**
- Paid ads to cold traffic
- Mentioned in community
- Direct offer to engaged followers
- Content about offer creation

**What happens:**
- Buy $47 Client Ready Offer System
- See 3 order bump offers
- Enter OTO sequence
- Experience the methodology

**Metrics to track:**
- Conversion rate from ads to $47
- Front-end purchase volume

---

## Stage 3: Order Bumps — $37 + $67 + $97

**Goal:** Increase average order value

**Products:**
- **Bump 1: $37** — Quick Win DM Scripts (10 scripts + conversation system + objection handlers)
- **Bump 2: $67** — Plug & Play Templates (8 template packs, 50+ headlines, promo campaigns)
- **Bump 3: $97** — The First $5K Client Playbook (closing frameworks, Warm 50 plan, objection playbook)

**What happens:**
- Customer sees checkbox offers on order form
- One-click add to order
- Immediate delivery with main product

**Metrics to track:**
- Individual bump take rates (target: 25-35% each)
- Combined bump rate
- Average order value (target: $90-110)

---

## Stage 4: OTO 1 — DFY Offer Build ($197)

**Goal:** Upsell to done-for-you offer creation + community trial

**Product:** AI-built deliverables (ICP + offer document + ready-to-send sales doc + 5 ad hooks) + 30-day free community trial

**What happens:**
- Customer lands on OTO page after checkout
- Video explains: "We'll build your offer for you"
- Pitch: same methodology from $47 product, but we run it FOR you using AI + Michael's review
- One-click purchase (card already on file)
- Buyer redirected to 11-question onboarding form on thank you page
- Form submission triggers Claude API — deliverables generated in ~30 seconds
- Michael reviews (~10 min) and delivers within 24-48 hours
- 30-day community trial activates automatically

**If they say NO — Downsell: DFY Lite ($97):**
- Stripped version: ICP + offer document only (no sales doc, no ad hooks)
- Same 30-day community trial included
- Same onboarding form, shorter output

**Metrics to track:**
- OTO 1 take rate (target: 15%)
- Downsell take rate (target: 10% of remaining)
- Community trial activation rate
- Community trial-to-paid conversion (target: 70%)

**Cost per DFY generation:** ~$0.15-0.30 (Claude API)
**Michael's time per deliverable:** ~10 min review

See: `outputs/dfy-upsell/system-prompt.md` for Claude API spec

---

## Stage 5: OTO 2 — Newsletter ($37/mo)

**Goal:** Low-friction recurring revenue + ongoing touchpoint

**Product:** "What's Working Now" — monthly breakdown of tested offers, templates, and results

**What happens:**
- Shown to ALL buyers (not conditional)
- Immediate charge, no trial
- Monthly deliverable: one tested offer breakdown + templates + what the numbers showed
- Upsells to community: "Want the calls and DM access too? Join the community."

**Metrics to track:**
- Newsletter take rate (target: 8%)
- Newsletter retention (target: 60% at 3 months)

---

## Stage 6: Thank You + Onboarding

**Goal:** Activate buyers, trigger DFY build, get them into portal

**What happens:**
- **DFY buyers:** Thank you page shows onboarding form (11 questions). Completion triggers Claude API pipeline.
- **Non-DFY buyers:** Thank you page shows portal access + welcome video + "here's your first step."
- All buyers get portal login with purchased products unlocked, other products visible as locked tiles.

---

## Stage 7: Email Ascension

**Goal:** Build relationship, recover missed offers, drive community sign-ups

**What happens:**
- 10-day welcome sequence (automated)
- Daily email rhythm (manual broadcast after Day 10)
- Story → Offer → CTA framework

**Key changes from previous version:**
- Recovery emails now pitch DFY ($197) and DFY Lite ($97) instead of Sprint/Blueprint
- Day 6 email pitches community membership (not Sprint)
- Day 8 email pitches DFY offer build (not Blueprint)
- Day 10 invites to community trial (if not already in one)

**Ascension triggers:**
- High engagement → Community pitch
- DFY delivered + engaged → "Now deploy it — join the community"
- Community member + 30-90 days → Accelerator announcement

See: `reference/domain/funnel/email-rhythm.md`

---

## Stage 8: Community — THE ENGINE ($47/mo)

**Goal:** Retain, nurture, and convert to high-ticket

**How they enter:**
- 30-day free trial bundled with DFY Offer Build ($197) or DFY Lite ($97)
- Direct sign-up via email pitch or portal ($47/mo, no trial)
- Accelerator graduates stay as alumni

**What members get:**
- Weekly hot seat calls with Michael (live coaching)
- Sprint curriculum as self-paced learning path (Extract → Validate → Build → Launch)
- DFY templates of the month (tested assets Michael is running)
- "What's Working Now" breakdowns
- DM access to Michael
- Peer accountability + wins

**What this replaces:**
- Sprint ($297) weekly calls → now community calls
- Sprint 4-week curriculum → now community learning path
- Blueprint community access → now everyone in community
- OTO 3 (was a conditional downsell) → now the $47/mo central engine (beta entry)

**Pricing:** $47/mo, month-to-month, cancel anytime. No annual. No lock-in.

**Community → Accelerator pipeline:**
- Members watch Michael coach live for 30-90 days
- They ask "how do I work with you 1:1?"
- Michael announces limited spots → community members take them
- No sales page needed. No email pitch needed. Invoice sent. Paid. Done.

**Metrics to track:**
- Trial → paid conversion rate (target: 70%)
- Monthly retention rate (target: 85%)
- Accelerator inquiries from community
- Community MRR

---

## Stage 9: Backend — Accelerator ($5K)

**Goal:** Enroll in high-ticket done-with-you intensive

**Product:** Client Ready Accelerator — 8 weeks, 3 calls, unlimited async

**How they buy (community-first):**
- Michael announces limited spots in community (e.g., "5 spots open this month")
- Community members who've watched him coach for 30-90 days already know the quality
- They respond to the announcement
- Invoice sent directly — no sales page, no call needed
- Onboarding within 48 hours

**Fallback channel:** No-phone offer page still exists for email-driven buyers not in community.

**Metrics to track:**
- Accelerator conversion rate from community (target: 2% of members)
- Source tracking (community vs. email vs. direct)
- Results achieved

See: `reference/domain/delivery/accelerator.md`

---

## Stage 10: Retention — Results + Referrals

**Goal:** Deliver results, generate referrals and case studies

**What happens:**
- Complete engagement (community or Accelerator)
- Achieve promised transformation
- Collect testimonial
- Document case study
- Ask for referrals
- Community members become ongoing proof generators

**Metrics to track:**
- Client results achieved
- Testimonials collected
- Referrals generated
- Case studies created

---

## Funnel Economics (Targets)

| Metric | Target |
|--------|--------|
| Front-end price | $47 |
| Bump 1 rate | 25-35% |
| Bump 2 rate | 25-35% |
| Bump 3 rate | 20-30% |
| OTO 1 (DFY) rate | 15% |
| Downsell (DFY Lite) rate | 10% of remaining |
| OTO 2 (Newsletter) rate | 8% |
| Checkout AOV (front-end + bumps) | $90-110 |
| Full funnel AOV (incl. OTOs) | ~$135 |
| 90-day value per buyer | ~$260 |
| Community trial → paid | 70% |
| Community monthly retention | 85% |
| Accelerator from community | 2% of members |
| Customer acquisition cost | < checkout AOV |
