---
type: output
status: active
date: 2026-02-15
purpose: Delivery/onboarding emails for bump purchases
trigger: Purchase of any order bump
linked_decisions:
  - decisions/2026-02-15-bump-conversion-improvements.md
---

# Bump Delivery Emails

**Onboarding emails for bump buyers — quick-start + lead to limitation.**

---

## Overview

When someone buys a bump on checkout, they get the product instantly but no onboarding email. These fix that gap.

**Pattern (Miles Stutz "Install Offer"):**
1. Congratulate the decision
2. Tell them exactly where to start (one action, 5 minutes)
3. Lead to the LIMITATION of what they just bought
4. Bridge naturally to the next product that solves the limitation

**Trigger:** Purchase of specific bump product
**Timing:** Immediate (within 5 minutes of purchase)
**Send Time:** Immediate (not scheduled — fires on purchase event)

---

## Email BD01: DM Scripts Delivery

**Trigger:** Tag `purchased-bump-dm-scripts` added
**File:** `bd-sequence/BD01-dm-scripts-delivery.html`

**Subject:** Your DM scripts are ready — do this in the next 5 minutes

**Body:**

Hey [NAME],

Smart move grabbing the Quick Win DM Scripts.

Here's your access: [PRODUCT LINK]

You now have 10 copy-paste scripts, a complete conversation system, and word-for-word objection handlers. That's more than most coaches will ever have for warm outreach.

**Do this right now (takes 5 minutes):**

1. Open the PDF
2. Go to Script 1: The Reconnection
3. Think of ONE person you haven't talked to in a while who might need help with their business
4. Customize the script with their name
5. Send it

That's it. First conversation started.

Then tomorrow, send 5 more. The scripts have a tracker template at the bottom — use it.

**One thing to know:** The scripts start conversations. But conversations need somewhere to go. If someone says "tell me more" or "send me info," you need a landing page, an email sequence, and copy that converts.

That's exactly what the Plug & Play Templates are for — 8 complete template packs so you're never starting from a blank page.

If you grabbed those too, you're set. If not, they're still available here: [TEMPLATES LINK]

Go send that first DM.

Michael

---

## Email BD02: Templates Delivery

**Trigger:** Tag `purchased-bump-templates` added
**File:** `bd-sequence/BD02-templates-delivery.html`

**Subject:** Your templates are ready — start with this one

**Body:**

Hey [NAME],

Good call on the Plug & Play Templates.

Here's your access: [PRODUCT LINK]

You now have 8 complete template packs — offer document, 3 landing page layouts, 30-day email sequence, 50+ headlines, awareness-level messaging maps, promo campaign templates, and client profiles.

That's a lot. Don't try to use everything at once.

**Do this first (takes 15 minutes):**

1. Open the PDF
2. Go to Part 1: Offer Document Template
3. Look at the filled Client Ready example — that's what "done" looks like
4. Open a blank doc and fill in YOUR version using the template structure

Your offer document is the foundation. Everything else — landing page, emails, headlines — builds from it.

**After your offer doc is done:** Open the landing page swipe files (Part 2) and pick the layout that fits your traffic. Short-form for warm traffic. Long-form for cold. VSL if you have a video.

**One thing most people miss:** Part 7 has 8 complete promo campaign templates — flash sales, founding member pricing, referral drives, cash injection campaigns. These are money-on-demand when you need quick revenue. Bookmark that section.

**What's next after templates?** Templates get you built. But built isn't sold. If you don't have a system for having sales conversations, the Quick Win DM Scripts give you 10 scripts plus a complete conversation framework for turning warm contacts into clients.

Already have those? Then you're ready to build.

Michael

---

## Email BD03: First 5K Client Playbook Delivery

**Trigger:** Tag `purchased-bump-playbook` added
**File:** `bd-sequence/BD03-playbook-delivery.html`

**Subject:** Your playbook is ready — start with the Warm 50

**Body:**

Hey [NAME],

This is the one that changes things. The First 5K Client Playbook is ready.

Here's your access: [PRODUCT LINK]

You now have pricing psychology, 5 conversation frameworks, the Warm 50 activation plan, word-for-word objection handlers, and 3 annotated real closing conversations.

**Do this first (takes 20 minutes):**

1. Open the PDF
2. Go to Part 3: The Warm 50 Activation Plan
3. Read the 5 categories of warm contacts
4. Write down 10 names — just 10 to start

Don't overthink this. Past colleagues, industry connections, people who've asked for your help before, social media contacts you've actually talked to. You already know these people.

**Then read Part 1 (Pricing Psychology) before you reach out.** The Pricing Confidence Framework has 3 questions. If you can answer all three clearly, you're ready to charge premium. This resets how you think about pricing before any conversation happens.

**When they respond — and they will — use the conversation frameworks in Part 2.** Not scripts. Structures. The Discovery Conversation for initial interest. The Offer Walkthrough when they want details. The DM Close for messaging-only sales.

**When someone says "too expensive":** Go straight to Part 4. The objection playbook has the exact words for the 5 things every prospect says. Every objection is a question in disguise — these responses answer the real question.

**One thing to remember:** The Warm 50 gets you conversations. But conversations need an offer that's ready to share. If you haven't built your landing page and funnel yet, the Plug & Play Templates give you everything — 3 proven layouts, 50+ headlines, and a 30-day email sequence pre-written.

Already have those? Then open the Warm 50 and start listing names.

Michael

---

## Automation Logic

```
FOR EACH bump purchased at checkout:

IF purchased-bump-dm-scripts tag added
   → Wait 5 minutes (let all tags settle)
   → Send BD01-dm-scripts-delivery.html

IF purchased-bump-templates tag added
   → Wait 5 minutes
   → Send BD02-templates-delivery.html

IF purchased-bump-playbook tag added
   → Wait 5 minutes
   → Send BD03-playbook-delivery.html

Each fires independently — buyer could get 1, 2, or all 3.
All send within minutes of purchase.
```

---

## Cross-Sell Logic

Each delivery email bridges to the most relevant missing product:

| Bump Purchased | Limitation | Bridges To |
|----------------|------------|------------|
| DM Scripts (37) | Conversations need a funnel to point to | Templates (67) |
| Templates (67) | Built isn't sold — need conversations | DM Scripts (37) |
| Playbook (97) | Need a built funnel to share with Warm 50 | Templates (67) |

If they already own the cross-sell product, the bridge paragraph is irrelevant but not harmful (just says "if you grabbed those too, you're set").

---

## Expected Results

| Metric | Target |
|--------|--------|
| Open rate | 60-80% (transactional emails get high opens) |
| Click rate | 15-25% (product access link) |
| Cross-sell click rate | 3-5% |
| Cross-sell conversion | 1-2% of bump buyers buy another bump from delivery email |
