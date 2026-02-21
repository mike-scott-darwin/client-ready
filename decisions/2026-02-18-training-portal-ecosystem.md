---
type: decision
date: 2026-02-18
status: codified
urgency: normal
linked_research:
  - research/2026-02-18-training-portal-ecosystem-gemini.md
  - research/2026-02-14-low-ticket-to-high-ticket-ecosystem-gemini.md
linked_decisions:
  - decisions/2026-02-12-scaling-architecture.md
  - decisions/2026-02-14-ecosystem-architecture-iron-strike.md
---

# Training Portal Ecosystem — Option B (Convert + First New Training)

## Situation

Currently delivering all products as Google Docs. Buyers receive a link, download, and never see the rest of the product catalog. This is a dead-end delivery model — no passive cross-sell, no visual exposure to other products, no second-chance purchases.

The screenshot reference (Miles Stutz's training portal) shows the alternative: 9 standalone mini-trainings in a portal where every buyer sees all available trainings. Each training is a standalone ad entry point. The portal itself acts as a passive storefront.

## Decision: Option B — Convert Existing + One New Training

### What Changes

#### 1. Training Portal in GHL (New Delivery Mechanism)

Replace Google Doc delivery with a GHL membership portal. Every product becomes a training tile with video walkthroughs.

**Architecture:**
```
GHL Membership Portal (Content Library)
  ├── Client Ready Offer System ($47) — unlocked on purchase
  ├── Quick Win DM Scripts ($37) — locked/unlockable
  ├── Plug & Play Templates ($67) — locked/unlockable
  ├── The First $5K Client Playbook ($97) — locked/unlockable
  ├── The One-Page Funnel (NEW, $57) — locked/unlockable
  ├── The Plug & Play Funnel Snapshot (NEW, $97) — locked/unlockable [GHL affiliate trigger]
  └── [Future trainings] — locked/unlockable

Skool Community (Support & Engagement)
  ├── Discussion threads, weekly calls, accountability
  └── NOT where training content lives
```

**Key UX:** Buyers log in and see their purchased training(s) unlocked. All other trainings appear as locked tiles with titles, descriptions, and preview images. Clicking a locked tile triggers a one-click purchase using card on file (GHL in-app upsell).

#### 2. Existing Bumps: Stay on Checkout, Upgrade Delivery

Order bumps remain as checkout bumps at $37/$67/$97. **Nothing changes at the point of sale.** The only change is delivery:

| Product | Before | After |
|---------|--------|-------|
| DM Scripts ($37) | Google Doc link | Portal tile unlocked + video walkthrough |
| Templates ($67) | Google Doc link | Portal tile unlocked + video walkthrough |
| First $5K Playbook ($97) | Google Doc link | Portal tile unlocked + video walkthrough |

If buyer declines a bump at checkout → they see it locked in the portal → second-chance conversion without additional marketing.

#### 3. New Training: "The One-Page Funnel" ($57)

**Why this training:** It fills the biggest gap in the transformation arc — the "Build" phase. Current products cover Extract ($47 Offer System), Validate (DM Scripts, $5K Playbook), but nothing covers "I have my offer, now I need a page that sells it."

**What it covers:**
- The hybrid VSL landing page structure (headline + video + long-form text + visual evidence)
- AI-assisted copy generation from your offer document
- Mobile-first design principles
- The 5-Second Test (pre-launch gate)
- Template + walkthrough for building in GHL

**Ad angle:** "Build your landing page in one afternoon" — reaches a different buyer than "validate your offer." Same portal, new entry point.

**Price:** $57 (sits between the $47 front-end and $67 Templates bump)

**Portal position:** Standalone training tile. Also offered as a cross-sell in the welcome email sequence after Day 3 consumption check.

#### 4. New Training: "The Plug & Play Funnel Snapshot" ($97)

**Why this training:** It's the self-service version of the Blueprint ($397). Coaches who want a done-for-you funnel but don't need custom strategy or copy. Also the strongest GHL affiliate trigger — buyers can't use the snapshot without a GHL account.

**What it covers:**
- Pre-built GHL snapshot of the complete Client Ready funnel (landing page, checkout, bumps, OTO pages, email sequences)
- Video walkthrough: import snapshot → customize copy → connect Stripe → go live
- Same funnel architecture Michael uses — not a generic template

**How it differs from Blueprint ($397):**
- Snapshot = self-service with template. Blueprint = Michael builds custom.
- Snapshot includes generic copy you customize. Blueprint includes copy Michael writes for you.
- Snapshot has video walkthrough. Blueprint has 60-min integration call.

**GHL Affiliate Layer:**
- Requires a GHL account to use → affiliate link embedded in training
- GHL pays 40% recurring commission (~$39/mo per referral on $97/mo plan)
- Every Snapshot buyer who signs up for GHL = recurring affiliate revenue
- The One-Page Funnel ($57) also soft-links GHL as optional ("here's how to build this in GHL")

**Price:** $97 (matches Playbook bump price, positioned as premium portal training)

**Portal position:** Standalone training tile. Visible to all portal users. Strongest cross-sell for anyone who already has the Offer System + One-Page Funnel.

#### 5. Multiple Ad Entry Points (Post-Validation)

Once core funnel is validated (30+ sales, $100+ AOV per scaling-architecture decision), each portal training can become a standalone front-end ad campaign:

| Entry Point | Ad Angle | Portal Effect |
|-------------|----------|---------------|
| $47 Offer System | "Validate your $5K offer in one afternoon" | Sees 5 other trainings locked |
| $37 DM Scripts | "First client conversation in 5 minutes" | Sees 5 other trainings locked |
| $57 One-Page Funnel | "Build your landing page in one afternoon" | Sees 5 other trainings locked |
| $97 Funnel Snapshot | "Import a proven funnel — customize in one afternoon" | Sees 5 other trainings locked + GHL affiliate |

Every entry point funnels into the same portal → same backend → same $5K Accelerator path.

### What Stays the Same

- Checkout flow (front-end + bumps + OTOs) — unchanged
- Bump prices ($37/$67/$97) — unchanged
- OTO structure (Sprint $297, Blueprint $397, Community $47/mo) — unchanged
- Backend ($5K Accelerator) — unchanged
- Email ascension system — unchanged (portal adds a passive cross-sell layer on top)

### What This Unlocks

1. **Passive cross-sell:** Every portal login is a sales impression. No email needed.
2. **Second-chance bump recovery:** Declined bumps stay visible as locked tiles.
3. **Multiple ad entry points:** Each training = different ad angle = different buyer persona, all converging in the same portal.
4. **GHL affiliate revenue:** Funnel Snapshot training requires GHL → 40% recurring commission (~$39/mo per referral). Compounds as portal grows.
5. **Consumption tracking:** GHL tracks who logs in, what they watch, what they click on. Feeds into the consumption-triggered email branch (Day 3 split from iron-strike decision).
6. **Future product expansion:** Adding a new training = adding a new tile + a new ad campaign. No funnel rebuild required.

### Implementation Sequence

**Phase 1: Portal Infrastructure (Before first ad spend)**
- [ ] Set up GHL membership area with locked/unlocked tile structure
- [ ] Record 3-5 min video walkthroughs for each existing product
- [ ] Upload existing products as training tiles
- [ ] Configure one-click in-app upsell for locked tiles
- [ ] Rewire checkout delivery: after purchase → portal login (not Google Doc link)
- [ ] Test: buy the $47, confirm portal access shows correct unlocked/locked state

**Phase 2: New Trainings (Month 1-2)**
- [ ] Create "The One-Page Funnel" training content ($57)
- [ ] Record video walkthrough + GHL template
- [ ] Create "The Plug & Play Funnel Snapshot" training ($97)
- [ ] Build GHL snapshot of complete funnel (export as shareable snapshot)
- [ ] Record snapshot import + customization video walkthrough
- [ ] Embed GHL affiliate link in Snapshot training (sign-up step)
- [ ] Add both as portal tiles
- [ ] Build standalone checkout pages for each training
- [ ] Write ad creative for each entry point

**Phase 3: Multiple Entry Points (After 30+ sales)**
- [ ] Create standalone ad campaigns for DM Scripts, One-Page Funnel, and Funnel Snapshot
- [ ] Each campaign → its own checkout → portal access
- [ ] Track which entry point produces highest CLV
- [ ] Track GHL affiliate sign-ups from Snapshot training

### Metrics to Track

| Metric | Target | Why |
|--------|--------|-----|
| Portal login rate | 60%+ of buyers | If they don't log in, portal cross-sell doesn't work |
| In-portal cross-sell rate | 10-15% of logged-in users | "Browse and buy" conversion |
| Second-chance bump conversion | 5-10% | Buyers who declined bump at checkout, bought it later in portal |
| CLV (30-day) | $90-120 | First purchase + portal cross-sells + email ascension |
| Entry point diversity | 3+ ad campaigns | More doors into the same portal |
| GHL affiliate sign-ups | Track | Funnel Snapshot buyers who sign up for GHL |
| GHL affiliate MRR | Track | ~$39/mo per active referral |

### What This Does NOT Change

- This is NOT a replacement for the checkout bump model. Bumps stay.
- This is NOT a membership. One-time purchases unlock tiles permanently.
- This is NOT Skool classroom. Content lives in GHL. Skool stays for community.
- This does NOT require creating all trainings before launch. Start with the 4 existing products in the portal, add The One-Page Funnel when ready.

## What Changes (Reference Files)

- `reference/core/offer.md` — Added Training Portal Ecosystem section after Value Ladder. Documents portal architecture, two new trainings (The One-Page Funnel $57, The Plug & Play Funnel Snapshot $97), delivery upgrade, GHL affiliate layer, and multiple entry point strategy. Updated Funnel Metrics table.
- `CLAUDE.md` — Updated funnel table with both new standalone trainings and GHL affiliate recurring revenue.
- `reference/domain/classroom/modules.md` — Note that the portal replaces Google Doc delivery. Training content aligns with existing module structure.
