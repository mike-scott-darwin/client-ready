# Client Ready

Get your offer ready. Get clients.

---

> **Engine:** This repo uses [vip](https://github.com/mainbranch-ai/vip) as the engine.
> Add vip as an additional working directory to access skills and lenses.

---

## What This Business Does

Michael Scott helps coaches validate their offers before building — scale from $27 low-ticket to $5K+ high-ticket clients using an engineering-minded, AI-assisted approach.

**Tagline:** "The Coach Who Won't Tell You to Quit Your 9-to-5"

**Positioning:** Build an offer so clear it sells without a sales call — in one afternoon.

---

## The Funnel

| Step | Price | Product |
|------|-------|---------|
| Front-end | $27 | Client Ready Offer System |
| Bump 1 | $37 | Quick Win DM Scripts |
| Bump 2 | $67 | Plug & Play Templates |
| Bump 3 | $97 | The First $5K Client Playbook |
| Standalone | $57 | The One-Page Funnel (portal training) |
| Standalone | $97 | Plug & Play Funnel Snapshot (portal + GHL affiliate) |
| OTO 1 | $197 | DFY Offer Build (6 deliverables: dream client profile + validated offer + sales doc + sales page + 5-email sequence + 5 ad hooks + 30-day community trial) |
| Downsell | $97 | DFY Lite (ICP + offer doc + 30-day community trial) |
| OTO 2 | $37/mo | The Monthly Playbook (continuity; formerly "What's Working Now" Newsletter) |
| Community | $47/mo | Client Ready Community — **$47/mo beta entry** (30-day trial via DFY, then $47/mo month-to-month; $97/mo is the post-beta target) |
| Backend | $5K+ | Client Ready Accelerator (sold from community) |

**Checkout AOV target:** $70-90 | **Full funnel AOV:** ~$115 | **90-day value per buyer:** ~$190 (community at $47 beta; ~$240 at the $97 target)
> **Front-end is $27** (lowered from $47 on 2026-07-04 — see [decisions/2026-07-04-front-end-27-digital-snack.md](decisions/2026-07-04-front-end-27-digital-snack.md)). At $27 the front-end is a **buyer-acquisition price, not self-liquidating** — the model recovers spend on bumps + OTOs + continuity, not the front-end alone.
**Recurring:** Community ($47/mo) + The Monthly Playbook ($37/mo) + GHL affiliate (~$39/mo)
**Delivery:** All low-ticket products deliver through GHL training portal. DFY via Claude API + Michael review.
**Community = engine:** Sprint curriculum + weekly calls live in community. Accelerator spots announced there first.
**Decision:** [decisions/2026-03-07-dfy-upsell-community-first.md](decisions/2026-03-07-dfy-upsell-community-first.md)

---

## Folder Structure

```
client-ready/
├── CLAUDE.md              ← You are here
├── README.md
│
├── reference/
│   ├── core/
│   │   ├── offer.md       # Value ladder and positioning
│   │   ├── audience.md    # Who we serve
│   │   └── voice.md       # How we sound
│   │
│   ├── proof/
│   │   ├── testimonials.md    # Client wins (NEEDS CONTENT)
│   │   └── angles/
│   │       └── main-angles.md # Proven messaging hooks
│   │
│   └── domain/
│       ├── content-ideas.md   # PRIMARY source for all content
│       ├── classroom/
│       │   ├── modules.md     # Skool curriculum
│       │   └── resources.md   # Downloads and templates
│       ├── membership/
│       │   ├── pricing.md     # Pricing model
│       │   └── benefits.md    # What members get
│       └── funnel/
│           ├── stages.md      # Customer journey
│           └── touchpoints.md # Conversion points
│
├── research/              # Dated investigations
├── decisions/             # Dated choices with rationale
└── outputs/               # Generated content
```

---

## Quick Reference

### Audience
Coaches and service providers who want to sell high-ticket ($5K+) but are stuck at the early stages. May still have a 9-to-5. Need practical, no-fluff guidance.

### Voice
Direct. No-BS. Engineering mindset. Short sentences. "Wrong." "Test, validate, build." Alignment-first (not anti-guru — retired Mar 2026).

### Core Philosophy
- "You can't grow into pain" — Align offer with actual skills
- "Test, validate, build" — Engineering approach
- Reality over Perception — Substance before marketing
- "Nobody is coming to save you" — Action over perfection

### Signature Phrases
- "Wrong."
- "Let's go."
- "Period, full stop."
- "You can't grow into pain."
- "Test, validate, build."
- "The Coach Who Won't Tell You to Quit Your 9-to-5"

---

## Key URLs

- **Skool:** https://www.skool.com/high-ticket-playbook-9467
- **$27 Offer:** https://clientreadyoffer.com/implement

---

## Current Gaps

| Area | Status |
|------|--------|
| Testimonials | ⚠️ **#1 priority gap** — trigger case study collection at 5 sales |
| 1:1 pricing | ⚠️ "$5K+" — exact price TBD |
| Email sequences | ✅ 6 workflows defined in `reference/domain/funnel/email-rhythm.md` |
| DFY OTO page | ⚠️ Not yet built — need GHL page for $197 DFY Offer Build |
| DFY Lite downsell page | ⚠️ Not yet built |
| DFY API integration | ⚠️ Claude API + GHL webhook pipeline not yet wired |
| Community pricing | ⚠️ Need to set $47/mo in GHL with 30-day trial logic |
| Newsletter OTO page | ✅ Built — "The Monthly Playbook" $37/mo (live; fixes in oto2-monthly-playbook-ghl-swap-sheet.md) |
| Content strategy | ✅ Defined in `reference/domain/content-strategy.md` |

---

## Content Rule

**All content — posts, newsletters, threads, carousels — must pull from `reference/domain/content-ideas.md` as the primary source.** This file contains ideas validated against offer.md, audience.md, voice.md, main-angles.md, and content-strategy.md. No off-message content. If an idea isn't in the library, check it against all 5 reference files before drafting.

---

## Using This Repo

**Generate content:**
```
/ad-static    # Static ad copy
/ad-video-scripts    # Video scripts
/skool-vsl-scripts   # VSL scripts
```

**Add context:**
```
/enrich    # Fill gaps in reference files
/think     # Research and decide
```

**Review before shipping:**
```
/ad-review    # Compliance + quality check
```

**Local skills (this repo):**
```
/product-doc       # Generate product documentation
/landing-page      # Hybrid VSL landing page copy
/email-sequence    # GHL email sequence drafter
/mine              # Competitor intelligence mining
```
