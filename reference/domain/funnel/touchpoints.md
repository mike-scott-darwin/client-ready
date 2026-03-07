---
type: reference
status: active
date: 2026-03-07
updated_from: 2026-02-01
linked_decisions:
  - decisions/2026-03-07-dfy-upsell-community-first.md
---

# Funnel Touchpoints

## Key Conversion Points

### 1. $47 Offer Sales Page

**URL:** https://clientreadyoffer.com/implement
**Purpose:** Convert cold traffic → paying customer
**Price:** $47
**CTA:** Buy Now

**Key elements:**
- Promise: Build an offer so clear it sells without a sales call — in one afternoon
- AI-assisted methodology
- Instant delivery
- Order bumps: $37 + $67 + $97

---

### 2. Order Bump Checkboxes

**Location:** Checkout page
**Purpose:** Increase AOV

| Bump | Price | Promise |
|------|-------|---------|
| Bump 1: Quick Win DM Scripts | $37 | First conversation in 5 minutes |
| Bump 2: Plug & Play Templates | $67 | Don't start from scratch |
| Bump 3: The First $5K Client Playbook | $97 | The playbook for landing your first high-ticket client |

---

### 3. OTO 1 Page (DFY Offer Build)

**URL:** Post-checkout redirect
**Purpose:** Upsell to done-for-you offer creation + community trial
**Price:** $197
**CTA:** Add to Order (one-click)

**Key elements:**
- "We'll build your offer for you" — same methodology, we run it for you
- AI-built: ICP + offer document + landing page copy + 5 ad hooks
- Michael reviews every deliverable before you receive it
- Includes 30-day free trial to Client Ready Community
- Delivered within 24-48 hours

**If NO → Downsell: DFY Lite**
- Price: $97
- ICP + offer document only (no landing page copy, no ad hooks)
- Same 30-day community trial included

---

### 4. OTO 2 Page (Newsletter)

**URL:** Post-OTO1 redirect
**Purpose:** Low-friction recurring revenue
**Price:** $37/mo (immediate charge, no trial)
**CTA:** Subscribe Now

**Key elements:**
- "What's Working Now" — monthly tested offer breakdown + templates
- Shown to ALL buyers (not conditional)
- Bridges to community: "Want the calls too? Join the community."

---

### 5. Thank You Page

**URL:** Post-OTO redirect
**Purpose:** Activate buyer, trigger DFY build if applicable

**DFY buyers see:**
- 8-question onboarding form
- "Complete this now — we start building your offer as soon as you submit"
- Portal access link

**Non-DFY buyers see:**
- Welcome video (60-90 seconds)
- Portal access link
- "Here's your first step"

---

### 6. Community Page

**URL:** Skool — https://www.skool.com/high-ticket-playbook-9467
**Purpose:** Retain members, nurture to high-ticket
**Price:** $97/mo (30-day trial for DFY buyers, direct sign-up for others)

**Key elements:**
- Weekly hot seat calls with Michael
- Sprint curriculum (self-paced learning path)
- DFY templates of the month
- DM access to Michael
- Month-to-month, cancel anytime

---

### 7. Accelerator Sales Page

**URL:** TBD (linked from community announcements, emails, direct)
**Purpose:** Sell $5K backend
**Price:** $5,000
**CTA:** Enroll Now

**Key elements:**
- Clear outcome + timeframe (8 weeks)
- Clear process (week-by-week)
- Clear delivery (3 calls, WhatsApp, Loom)
- Easy to start (pay → form → kickoff in 48h)

**Primary sales channel:** Community announcements (limited spots)
**Fallback:** No-phone offer page via email for non-community buyers

---

## Email Touchpoints

### Post-Purchase: 10-Day Welcome Sequence

| Day | Focus | Offer |
|-----|-------|-------|
| 1 | Welcome + quick win | -- |
| 2 | Your story (why you do this) | -- |
| 3 | First case study | Bump they missed |
| 4 | Common mistake to avoid | Templates ($67) |
| 5 | Quick tip + value | -- |
| 6 | Client transformation | Community ($97/mo) |
| 7 | Behind-the-scenes | -- |
| 8 | FAQ / objection handling | DFY Offer Build ($197) |
| 9 | "What happens next" roadmap | -- |
| 10 | Personal invite to community | Community trial |

### Parallel Recovery Sequences (Days 2-8, sent at 2PM)

- **Bump Recovery** (3 emails, Days 2/4/6) — pitches only the bumps they missed
- **DFY Recovery** (2 emails, Days 3/5) — DFY Offer Build for buyers who declined at checkout
- **Community Recovery** (1 email, Day 8) — direct community sign-up for buyers not on trial

### Post-Day 10: Daily Email Rhythm

- Story → Offer → CTA framework
- Rotate offers across the week
- Revenue on demand from buyer list

See: `reference/domain/funnel/email-rhythm.md`

---

## Community Touchpoints

### Client Ready Community (Skool)

**URL:** https://www.skool.com/high-ticket-playbook-9467
**Who has access:** DFY buyers (trial), direct sign-ups ($97/mo), Accelerator clients

**Engagement points:**
- Welcome thread (intro post)
- Weekly hot seat calls (live coaching)
- Sprint curriculum (self-paced learning path)
- DFY templates of the month
- Win celebrations
- Accelerator spot announcements

---

## Content Touchpoints

### Organic Content Strategy

**Platforms:** TBD (LinkedIn, X, YouTube?)

**Content pillars:**
1. Offer creation tips
2. Funnel strategy
3. Anti-guru positioning ("You can't grow into pain")
4. Behind the scenes / transparency

**Posting frequency:** TBD

---

## Touchpoint Gaps

_To build:_

- [ ] DFY OTO page ($197) in GHL
- [ ] DFY Lite downsell page ($97) in GHL
- [ ] DFY onboarding form (8 questions) in GHL
- [ ] Claude API integration (GHL webhook → Make.com/n8n → Claude → delivery)
- [ ] Newsletter OTO page ($37/mo) in GHL
- [ ] Community pricing set to $97/mo with 30-day trial logic in GHL
- [ ] Accelerator spot announcement template for community
- [ ] Updated email recovery sequences (DFY instead of Sprint/Blueprint)
- [ ] Content calendar defined
- [ ] Tracking/analytics fully set up
- [ ] Testimonial collection system

_Completed:_

- [x] 10-day welcome sequence (needs OTO references updated)
- [x] Daily email rhythm system
- [x] Bump copy and pages
- [x] DFY system prompt and API spec (`outputs/dfy-upsell/system-prompt.md`)
- [x] Funnel restructure analysis (`outputs/dfy-upsell/funnel-restructure.md`)
- [x] Accelerator delivery framework
