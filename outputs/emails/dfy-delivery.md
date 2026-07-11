---
type: output
status: active
date: 2026-07-11
purpose: Intake + delivery emails for the OTO1 DFY Offer Build ($197) and DFY Lite ($97)
trigger: Purchase of DFY Offer Build / DFY Lite
linked_docs:
  - outputs/products/internal/dfy-offer-build-process.md
  - outputs/products/oto1-dfy-offer-build.md
  - reference/domain/delivery/dfy-intake-questionnaire.md
---

# DFY Delivery Emails

**Two-email handoff for the DFY Offer Build. Email is the delivery AND support channel — never gate behind the community.**

---

## Overview

The DFY build has two buyer-facing emails, and until now neither existed as a file — the flow only had "email → Skool." These replace that.

| Email | File | Trigger | Send |
|-------|------|---------|------|
| DFY01 — Intake | `dfy-sequence/DFY01-intake.html` | Tag `purchased-dfy` (or `purchased-dfy-lite`) added | Immediate (on purchase) |
| DFY02 — Delivery | `dfy-sequence/DFY02-delivery.html` | Tag `dfy-delivered` added (Michael sends after review) | Manual, within 48 hrs of intake |

**Design principles (see [dfy-offer-build-process.md](../products/internal/dfy-offer-build-process.md)):**
- **Email is the spine.** Reply-to is the buyer's direct line to Michael and where the included revision runs. Google Doc comments also work.
- **Portal is the backup copy.** The same Google Doc link is surfaced in the buyer's GHL portal so the deliverable lives with everything else they bought.
- **Community is an ascension invite, not a delivery step.** No "go to Skool to get your build." The weekly-call invite is framed as *deploy it live with me* — a P.S., never the path to the deliverable.

**Merge fields:** `[NAME]` → `{{contact.first_name}}` in GHL. `[DOC LINK]`, `[LOOM LINK]`, `[SKOOL LINK]` → per-build links (populated at send). `[PORTAL LINK]` → buyer's portal home.

---

## Email DFY01: Intake

**Trigger:** Tag `purchased-dfy` or `purchased-dfy-lite` added
**File:** `dfy-sequence/DFY01-intake.html`
**Send:** Immediate (on purchase event)

**Subject:** You bought the build — now give me the raw material (10 minutes)

**Body:**

Hey [NAME],

Right call. You could spend three weeks writing your own offer and second-guessing every line. Instead you're going to hand me the raw material and get the whole thing back — built and reviewed — in 48 hours.

Here's the one thing standing between you and your offer:

**Fill out this questionnaire → [INTAKE LINK]**

11 questions. 10–15 minutes. Be specific — the more real detail you give me, the sharper what comes back. Vague in, vague out. Don't dress it up. Just tell me the truth about who you help and what you do.

**What happens next:**

1. You submit the questionnaire (today, while you're here)
2. I build your complete package — Dream Client Blueprint, validated offer, ready-to-send sales doc, plug-and-play sales page, 5-email sequence, 5 ad hooks
3. I personally review every piece before it hits your inbox
4. Your package lands within 48 hours of your submission

The 48-hour clock starts when you submit — not when you bought. So the faster you fill it out, the faster you're holding your offer.

Questions? Just hit reply. This email is your direct line to me the whole way through.

Go fill it out. Let's build your offer.

Michael

*P.S. Your 30-day Client Ready Community trial is already active — that's the bonus. You don't need it to get your build; it's where I help you deploy the offer live once it's done. More on that when your package arrives.*

---

## Email DFY02: Delivery

**Trigger:** Tag `dfy-delivered` added (Michael sends after review + package)
**File:** `dfy-sequence/DFY02-delivery.html`
**Send:** Manual, within 48 hrs of intake submission

**Subject:** Your offer is built — open this, then do one thing

**Body:**

Hey [NAME],

It's done. Your complete offer is built, reviewed, and ready to use.

**Your build → [DOC LINK]**

**Watch this first (2–3 min) → [LOOM LINK]**

I recorded a short walkthrough of what I built and why — the key decisions, where your voice shows up, and what to do with each piece. Watch it before you read the doc. It'll save you time.

Inside the doc:

- **Dream Client Blueprint** — the one person this offer is for
- **Your Validated Offer** — positioning, mechanism, price
- **Ready-to-Send Sales Doc** — copy this into a Google Doc and send it to your warm list *today* to get hand-raisers
- **Plug-and-Play Sales Page** — paste into GHL when you point cold traffic at it
- **5-Email Sequence** — load into GHL to nurture new leads toward the offer
- **5 Ad Hooks** — drop into Meta Ads Manager when you run cold traffic

(A copy also lives in your portal → [PORTAL LINK], so you'll never have to dig for this email.)

**Do one thing right now:** open the Sales Doc, read it top to bottom, and send it to ONE person on your warm list. Not tomorrow. Today. That's how you find out your offer works — you test it on a real human, not by staring at it.

**Want a change?** Reply to this email or comment right on the doc. One revision round is included — tone, voice, tightening. I'll turn it around in 24 hours.

You've got the offer. Now go put it in front of someone.

Michael

*P.S. Now that your offer is built, the work shifts to deploying it — landing page live, first messages out, first conversations. That's exactly what we do on the weekly community calls. Your 30-day trial is active, so bring your build to the next one and I'll help you get it live: [SKOOL LINK]*

---

## Notes for GHL Setup

- **DFY01** fires automatically on the purchase tag. It carries the intake link — this is the same link pinned in the community "Start Here" post and available in Michael's DM, so completion never depends on one channel (see intake principle in the process doc).
- **DFY02** is sent manually (or semi-automated) once Michael has reviewed and packaged the build and adds the `dfy-delivered` tag. Populate `[DOC LINK]`, `[LOOM LINK]`, `[PORTAL LINK]` per build before sending.
- **DFY Lite** ($97) uses the same two emails; trim DFY02's deliverable list to the two Lite pieces (Dream Client Blueprint + Validated Offer) and drop the sales-page/sequence/ad-hook bullets.
- Reply-to on both must route to Michael's monitored inbox — it's the support and revision channel by design.
