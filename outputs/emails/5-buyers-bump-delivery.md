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

## Email BD01: First-Sale DM Scripts + 48-Hour Warm-List Cash Campaign Delivery

**Trigger:** Tag `purchased-bump-dm-scripts` added
**File:** `bd-sequence/BD01-dm-scripts-delivery.html`

**Subject:** Your First-Sale DM Scripts are ready — send one in the next 5 minutes

**Body:**

Hey [NAME],

Smart move grabbing the First-Sale DM Scripts + 48-Hour Warm-List Cash Campaign.

Here's your access: [PRODUCT LINK]

You now have 10 copy-paste DM scripts (Core 5 + Quick Cash 5), the A-C-A conversation flow, word-for-word objection handlers, and a fill-in-the-blank first message built from the offer doc you just made. That's a complete 48-hour campaign to turn your offer into cash — from people who already know you, no ad spend.

**Do this right now (takes 5 minutes):**

1. Open the campaign doc
2. Go to the "Who to message first" send-order
3. Pick ONE person from the top of the list
4. Drop your offer into the fill-in-the-blank first message
5. Send it

That's it. First conversation started.

Then work down your send-order — 5 a day. The tracker template at the bottom keeps anyone from falling through the cracks.

**One thing to know:** DMs start conversations. But when someone says "send me the details," you need a page to send them to — not a Google Doc.

That's exactly what the Plug & Play Sales Page Kit + 1-Hour AI Fill-In System is for — paste your offer doc in, get a finished sales page out.

If you grabbed it too, you're set. If not, reply "SALES PAGE" and I'll send you the link.

Go send that first message.

Michael

---

## Email BD02: Sales Page Kit + 1-Hour AI Fill-In System Delivery

**Trigger:** Tag `purchased-bump-templates` added
**File:** `bd-sequence/BD02-templates-delivery.html`

**Subject:** Your Sales Page Kit is ready — build the page in one hour

**Body:**

Hey [NAME],

Good call on the Plug & Play Sales Page Kit + 1-Hour AI Fill-In System.

Here's your access: [PRODUCT LINK]

You now have 3 landing-page swipe files (short-form, long-form, VSL), a 30-day email sequence, 50+ headlines, and promo campaign templates — **plus the AI prompts that auto-fill all of it straight from the offer doc you built.** You're not writing a page from scratch. You're filling one in.

**Do this first (takes about an hour):**

1. Open the kit and go to the AI Fill-In prompts
2. Paste in your offer doc
3. Run the prompt for the page that fits your traffic — short-form for warm, long-form for cold, VSL if you have a video
4. Drop the output into your page builder and publish

One hour, not one week. The offer you built this week has a home by tonight.

**One thing most people miss:** the promo campaign templates — flash sales, founding-member pricing, referral drives, cash-injection campaigns. These are money-on-demand when you need quick revenue. Bookmark that section.

**What's next after the page?** A live page gets you leads. But leads don't close themselves. When a warm lead turns into a real buying conversation, the $5K Client Close Scripts show you — word for word, across 3 real annotated calls — exactly what to say. Reply "CLOSE" and I'll send you the link.

Already have those? Then go build your page.

Michael

---

## Email BD03: $5K Client Close Scripts + 3 Real Annotated Calls Delivery

**Trigger:** Tag `purchased-bump-playbook` added
**File:** `bd-sequence/BD03-playbook-delivery.html`

**Subject:** Your $5K Close Scripts are ready — watch call #1 first

**Body:**

Hey [NAME],

This is the one that changes things. The $5K Client Close Scripts + 3 Real Annotated Calls are ready.

Here's your access: [PRODUCT LINK]

You now have 3 real closing calls (fully annotated), the objection playbook, 5 conversation frameworks, the pricing psychology behind $5K offers, and the Warm 50 activation plan.

**Do this first (takes 20 minutes):**

1. Open the doc and go to the 3 Annotated Calls
2. Watch call #1 — read the margin notes as you go
3. Mark the exact moment the price gets said (watch how it's framed)
4. Notice what the close is *not* — no pressure, no pitch

That's the whole game. You're not learning a script — you're watching a real one land, then copying what works.

**Before you reach out, read the Pricing Psychology section.** The Pricing Confidence Framework has 3 questions. If you can answer all three clearly, you're ready to charge premium. It resets how you think about pricing before any conversation happens.

**When they respond — and they will — use the conversation frameworks.** Not scripts. Structures. The Discovery Conversation for initial interest. The Offer Walkthrough when they want details. The DM Close for messaging-only sales.

**When someone says "too expensive":** Go straight to the objection playbook. It has the exact words for the 5 things every prospect says. Every objection is a question in disguise — these responses answer the real question.

**One thing to remember:** the Warm 50 gets you conversations. But conversations need an offer with a home. If you haven't built your sales page yet, the Plug & Play Sales Page Kit fills one in from your offer doc in an hour — reply "SALES PAGE" and I'll send you the link.

Already have it? Then open the Warm 50 and start listing names.

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
| First-Sale DM Scripts (37) | DMs need a page to send interested people to | Sales Page Kit (67) |
| Sales Page Kit (67) | A live page gets leads — leads still need closing | $5K Close Scripts (97) |
| $5K Close Scripts (97) | The Warm 50 needs an offer with a home | Sales Page Kit (67) |

If they already own the cross-sell product, the bridge paragraph is irrelevant but not harmful (just says "if you grabbed those too, you're set").

---

## Expected Results

| Metric | Target |
|--------|--------|
| Open rate | 60-80% (transactional emails get high opens) |
| Click rate | 15-25% (product access link) |
| Cross-sell click rate | 3-5% |
| Cross-sell conversion | 1-2% of bump buyers buy another bump from delivery email |
