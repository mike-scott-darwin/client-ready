---
type: output
status: active
date: 2026-02-14
purpose: GHL workflow configuration for email sequences
updated: Iron Strike system — consumption branch, soft ascension, accountability DMs
---

# GHL Workflow Setup

Complete GoHighLevel workflow configuration for the Client Ready email backend. Every step spelled out.

---

## What You're Building

8 workflows that handle the entire buyer journey automatically:

| # | Workflow Name | Trigger | Emails | HTML Files |
|---|---------------|---------|--------|------------|
| 1 | Non-Buyer Nurture | Entered email, no purchase | 12 emails / 30 days | `nb-sequence/NB01-NB12` |
| 2 | Buyer Welcome | Tag: `purchased-47` | 10 emails / 10 days (Day 3 branches) | `bw-sequence/BW01-BW10` + `BW03a/BW03b` |
| 3 | Bump Recovery | Purchased $47, missed bumps | 3 emails (Days 2,4,6) | `br-sequence/BR01-BR03` |
| 4 | Bump Delivery | Purchased bump product | 3 emails (immediate) | `bd-sequence/BD01-BD03` |
| 5 | OTO Recovery | Purchased $47, no DFY/DFY Lite | 3 emails (Days 3,5,7) | `or-sequence/OR01-OR03` |
| 6 | Community Recovery | Purchased $47, no upsells at all | 1 email (Day 8) | `cr-sequence/CR01` |
| 7 | Accountability DM | Purchased DFY or DFY Lite | Manual DM trigger | (no HTML — manual outreach) |
| 8 | Daily Broadcast | Day 11+ | Ongoing (7 templates) | `db-sequence/DB01-DB07` |

---

## STEP 0: Create All Tags

Go to **Settings → Tags** in GHL. Create each tag exactly as written (copy-paste the tag names).

### Lead Tag
- `lead`

### Purchase Tags
- `purchased-47`
- `purchased-bump-dm-scripts`
- `purchased-bump-templates`
- `purchased-bump-playbook`
- `purchased-dfy`
- `purchased-dfy-lite`
- `purchased-newsletter`
- `purchased-community`

### Routing Tags
- `non-buyer-sequence`
- `buyer-30-day-complete`
- `in-daily-broadcast`

### Consumption Tracking Tags
- `product-accessed`

### Accountability Tags
- `needs-accountability-dm`

**Total: 15 tags.**

---

## STEP 1: Create All Triggers

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

All workflows run on tags. Triggers convert events (form submissions, purchases) into tags. Set up each trigger as a simple 1-step Workflow.

### Purchase Triggers

One trigger per product. Each fires on **Payment Received** (or **Order Submitted**), filtered to the specific product.

| # | Trigger Name | Event Filter | Action |
|---|-------------|--------------|--------|
| 1 | Lead Capture | Order Form Submission Started | Add tag → `lead` |
| 2 | Core Purchase | Payment Received → Client Ready ($47) | Add tag → `purchased-47` |
| 3 | DM Scripts Purchase | Payment Received → DM Scripts ($37) | Add tag → `purchased-bump-dm-scripts` |
| 4 | Templates Purchase | Payment Received → Templates ($67) | Add tag → `purchased-bump-templates` |
| 5 | Playbook Purchase | Payment Received → Playbook ($97) | Add tag → `purchased-bump-playbook` |
| 6 | DFY Purchase | Payment Received → DFY Offer Build ($197) | Add tag → `purchased-dfy` |
| 7 | DFY Lite Purchase | Payment Received → DFY Lite ($97) | Add tag → `purchased-dfy-lite` |
| 8 | Newsletter Purchase | Payment Received → Newsletter ($37/mo) | Add tag → `purchased-newsletter` |
| 9 | Community Purchase | Payment Received → Community ($97/mo) | Add tag → `purchased-community` |

**For Trigger 1 (Lead Capture):** If "Order Form Submission Started" isn't available in your GHL version, use **"Form Submitted"** or **"Contact Created"** instead.

**If using Stripe directly (not GHL payments):** Use Zapier or GHL's Stripe integration to fire the same tags on purchase events.

### Routing Triggers

One routing trigger for non-buyers. Buyer routing is handled inside the Buyer Welcome workflow itself (no extra trigger needed).

| # | Trigger Name | Event | Actions |
|---|-------------|-------|---------|
| 9 | Non-Buyer Start | Tag Added → `lead` | Add tag → `non-buyer-sequence` |

**Total: 10 triggers.** That's it. Everything else happens inside workflows.

---

## STEP 2: Build Workflow 1 — Non-Buyer Nurture

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Non-Buyer Nurture (Abandoned Checkout)`

### Workflow Trigger
- Click "Add New Trigger"
- Type: **Tag Added**
- Tag: `non-buyer-sequence`
- Save trigger

### Build the Steps (in order)

Click "+" after the trigger to add each step. Build this exact sequence:

```
Step 1:  WAIT → Wait for 30 minutes
Step 2:  IF/ELSE → Contact Tag → Has tag "purchased-47"
           ├── YES branch:
           │     Step 2a: REMOVE TAG → "non-buyer-sequence"
           │     (branch ends — workflow exits)
           └── NO branch: (continue below)

Step 3:  SEND EMAIL → NB01-soft-abandon.html
           Subject: "You left something behind"
           From: Michael Scott

Step 4:  WAIT → Wait 1 day (until 9:00 AM)

Step 5:  IF/ELSE → Contact Tag → Has tag "purchased-47"
           ├── YES: REMOVE TAG "non-buyer-sequence" → End
           └── NO: continue

Step 6:  SEND EMAIL → NB02-cost-of-waiting.html
           Subject: "What's an unclear offer costing you?"

Step 7:  WAIT → Wait 2 days (until 9:00 AM) [Day 4]

Step 8:  IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 9:  SEND EMAIL → NB03-objection-killer.html
           Subject: "I already know my offer"

Step 10: WAIT → Wait 2 days (until 9:00 AM) [Day 6]

Step 11: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 12: SEND EMAIL → NB04-contrarian-hook.html
           Subject: "Stop niching down"

Step 13: WAIT → Wait 2 days (until 9:00 AM) [Day 8]

Step 14: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 15: SEND EMAIL → NB05-social-proof.html
           Subject: "I finally stopped second-guessing myself"

Step 16: WAIT → Wait 2 days (until 9:00 AM) [Day 10]

Step 17: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 18: SEND EMAIL → NB06-direct-close.html
           Subject: "Last thing on this"

Step 19: WAIT → Wait 4 days (until 9:00 AM) [Day 14]

Step 20: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 21: SEND EMAIL → NB07-pivot-to-value.html
           Subject: "Forget the pitch - here's something useful"

Step 22: WAIT → Wait 2 days (until 9:00 AM) [Day 16]

Step 23: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 24: SEND EMAIL → NB08-wrong-wrong-wrong.html
           Subject: "Build it and they will come"

Step 25: WAIT → Wait 3 days (until 9:00 AM) [Day 19]

Step 26: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 27: SEND EMAIL → NB09-the-transformation.html
           Subject: "From 'I help people' to $5K clients"

Step 28: WAIT → Wait 3 days (until 9:00 AM) [Day 22]

Step 29: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 30: SEND EMAIL → NB10-the-calculator.html
           Subject: "What's another month of 'figuring it out' cost you?"

Step 31: WAIT → Wait 4 days (until 9:00 AM) [Day 26]

Step 32: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 33: SEND EMAIL → NB11-cant-go-it-alone.html
           Subject: "Free resources won't save you"

Step 34: WAIT → Wait 4 days (until 9:00 AM) [Day 30]

Step 35: IF/ELSE → Has tag "purchased-47"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 36: SEND EMAIL → NB12-last-call.html
           Subject: "Closing the loop on this"

Step 37: REMOVE TAG → "non-buyer-sequence"

(Workflow ends)
```

### Non-Buyer Email Schedule Summary

| Email | File | Day | Subject |
|-------|------|-----|---------|
| NB01 | NB01-soft-abandon.html | 0 (30 min after abandon) | You left something behind |
| NB02 | NB02-cost-of-waiting.html | 2 | What's an unclear offer costing you? |
| NB03 | NB03-objection-killer.html | 4 | "I already know my offer" |
| NB04 | NB04-contrarian-hook.html | 6 | Stop niching down |
| NB05 | NB05-social-proof.html | 8 | "I finally stopped second-guessing myself" |
| NB06 | NB06-direct-close.html | 10 | Last thing on this |
| NB07 | NB07-pivot-to-value.html | 14 | Forget the pitch - here's something useful |
| NB08 | NB08-wrong-wrong-wrong.html | 16 | "Build it and they will come" |
| NB09 | NB09-the-transformation.html | 19 | From "I help people" to $5K clients |
| NB10 | NB10-the-calculator.html | 22 | What's another month of "figuring it out" cost you? |
| NB11 | NB11-cant-go-it-alone.html | 26 | Free resources won't save you |
| NB12 | NB12-last-call.html | 30 | Closing the loop on this |

### Key Settings
- **Send time:** 9:00 AM local (except NB01 which sends 30 min after abandon)
- **Exit condition:** IF/ELSE checks for `purchased-47` before EVERY email
- **If they buy at any point:** Workflow exits, non-buyer tag gets removed, buyer workflows take over

---

## STEP 3: Build Workflow 2 — Buyer Welcome (10-Day)

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Buyer Welcome (10-Day) — Iron Strike`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-47`

### Build the Steps

```
Step 1:  REMOVE TAG → "non-buyer-sequence" (cleanup — may not exist, that's fine)
Step 2:  REMOVE TAG → "lead" (cleanup)

Step 3:  SEND EMAIL → BW01-welcome-quick-win.html
           Subject: "You're in — here's your first win"
           (Send immediately — don't wait)

Step 4:  WAIT → Wait 1 day (until 8:00 AM) [Day 2]

Step 5:  SEND EMAIL → BW02-origin-story.html
           Subject: "Why I do this (honest answer)"

Step 6:  WAIT → Wait 1 day (until 8:00 AM) [Day 3]

         ┌─── CONSUMPTION BRANCH ───┐
Step 7:  IF/ELSE → Contact Tag → Has tag "product-accessed"
           ├── YES (opened product):
           │     Step 7a: SEND EMAIL → BW03a-advanced-tips.html
           │              Subject: "Now that you've started — get the most out of Prompt 3"
           └── NO (hasn't opened):
                 Step 7b: SEND EMAIL → BW03b-quick-start.html
                          Subject: "Haven't started yet? Here's the 5-minute version"
         └─── BOTH PATHS CONTINUE ──┘

Step 8:  WAIT → Wait 1 day (until 8:00 AM) [Day 4]

Step 9:  SEND EMAIL → BW04-common-mistake.html
           Subject: "The mistake that cost me 6 months"

Step 10: WAIT → Wait 1 day (until 8:00 AM) [Day 5]

Step 11: SEND EMAIL → BW05-quick-tip.html
           Subject: "The 2-minute test for your offer"
           (Includes soft ascension P.S. — DFY link)

Step 12: WAIT → Wait 1 day (until 8:00 AM) [Day 6]

Step 13: SEND EMAIL → BW06-transformation-story.html
           Subject: "From stuck to first client in 30 days"

Step 14: WAIT → Wait 1 day (until 8:00 AM) [Day 7]

Step 15: SEND EMAIL → BW07-behind-the-scenes.html
           Subject: "What my morning actually looks like"
           (Includes soft ascension P.S. — DFY links)

Step 16: WAIT → Wait 1 day (until 8:00 AM) [Day 8]

Step 17: SEND EMAIL → BW08-faq-objection.html
           Subject: "What if I'm not ready?"

Step 18: WAIT → Wait 1 day (until 8:00 AM) [Day 9]

Step 19: SEND EMAIL → BW09-the-roadmap.html
           Subject: "What happens after $47"
           (Includes explicit DFY Offer Build CTA)

Step 20: WAIT → Wait 1 day (until 8:00 AM) [Day 10]

Step 21: SEND EMAIL → BW10-community-invite.html
           Subject: "Come hang out"

Step 22: ADD TAG → "buyer-30-day-complete"

Step 23: ADD TAG → "in-daily-broadcast"

(Workflow ends)
```

### Consumption Branch Setup (Day 3)

**How `product-accessed` tag gets set:**

Option A (GHL Membership Area):
- If product is delivered via GHL Membership → Settings → Triggers → "Course Started" or "First Login" → Add tag `product-accessed`

Option B (External delivery — PDF/link):
- Track click on product access link in BW01 email → GHL link tracking → Add tag `product-accessed` on click
- In BW01, make the product access link a GHL tracked link: Contacts → Triggers → "Link Clicked" → specific link → Add tag `product-accessed`

Option C (Manual fallback):
- Check download/access logs daily for first 3 days. Add tag manually for buyers who accessed.

**Recommendation:** Option B is simplest — if they click the product link in BW01, they get tagged. No membership area needed.

### Iron Strike Ascension Notes

Days 5, 7, and 9 now include soft ascension closes as P.S. sections:
- **Day 5:** DFY link after the quick tip (natural "if you passed the test, here's the next step")
- **Day 7:** DFY pitch after behind-the-scenes (natural "this is the system — want help building yours?")
- **Day 9:** Explicit DFY CTA within the roadmap email (natural "you're at Stage 1 — here's how to move to Stage 2-4")

**Voice guard:** These are P.S. additions, not hard sells. The body of each email is unchanged. If the P.S. feels out of place or pushy, remove it — the parallel recovery sequences still handle direct pitching.

### Buyer Welcome Schedule Summary

| Email | File | Day | Time | Subject | Ascension |
|-------|------|-----|------|---------|-----------|
| BW01 | BW01-welcome-quick-win.html | 1 | Immediate | You're in — here's your first win | — |
| BW02 | BW02-origin-story.html | 2 | 8:00 AM | Why I do this (honest answer) | — |
| BW03a | BW03a-advanced-tips.html | 3 | 8:00 AM | Now that you've started — get the most out of Prompt 3 | Consumption: opened |
| BW03b | BW03b-quick-start.html | 3 | 8:00 AM | Haven't started yet? Here's the 5-minute version | Consumption: not opened |
| BW04 | BW04-common-mistake.html | 4 | 8:00 AM | The mistake that cost me 6 months | — |
| BW05 | BW05-quick-tip.html | 5 | 8:00 AM | The 2-minute test for your offer | Soft close (DFY) |
| BW06 | BW06-transformation-story.html | 6 | 8:00 AM | From stuck to first client in 30 days | — |
| BW07 | BW07-behind-the-scenes.html | 7 | 8:00 AM | What my morning actually looks like | Soft close (DFY) |
| BW08 | BW08-faq-objection.html | 8 | 8:00 AM | "What if I'm not ready?" | — |
| BW09 | BW09-the-roadmap.html | 9 | 8:00 AM | What happens after $47 | Explicit CTA (DFY) |
| BW10 | BW10-community-invite.html | 10 | 8:00 AM | Come hang out | — |

### Key Settings
- **Send time:** 8:00 AM local (except BW01 which sends immediately on purchase)
- **Day 3 branches** based on `product-accessed` tag (consumption tracking)
- **Days 5, 7, 9** include soft ascension P.S. sections (iron strike window)
- **After Day 10:** Tags flip to `buyer-30-day-complete` + `in-daily-broadcast`

---

## STEP 4: Build Workflow 3 — Bump Recovery

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Bump Recovery (Missed Order Bumps)`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-47`

### Build the Steps

```
Step 1:  WAIT → Wait 5 minutes
           (Let all purchase tags settle — bumps tag at same time as $47)

Step 2:  IF/ELSE → Contact Tag → Has ALL of these tags:
           "purchased-bump-dm-scripts" AND
           "purchased-bump-templates" AND
           "purchased-bump-playbook"
           ├── YES (has all 3 bumps): End workflow — nothing to recover
           └── NO (missing at least one): continue

Step 3:  WAIT → Wait until Day 2, 2:00 PM

Step 4:  IF/ELSE → Contact Tag → Has tag "purchased-bump-dm-scripts"
           ├── YES: (skip — they already have DM Scripts)
           └── NO:
                 SEND EMAIL → BR01-dm-scripts.html
                 Subject: "One thing I forgot to mention..."

Step 5:  WAIT → Wait until Day 4, 2:00 PM

Step 6:  IF/ELSE → Contact Tag → Has tag "purchased-bump-templates"
           ├── YES: (skip — they already have Templates)
           └── NO:
                 SEND EMAIL → BR02-templates.html
                 Subject: "The blank page problem"

Step 7:  WAIT → Wait until Day 6, 2:00 PM

Step 8:  IF/ELSE → Contact Tag → Has ANY missing bump tags
           (Check: does NOT have dm-scripts OR does NOT have templates OR does NOT have playbook)
           ├── All bumps now owned: (skip)
           └── Still missing something:
                 SEND EMAIL → BR03-last-chance.html
                 Subject: "Before you move on..."

(Workflow ends)
```

### Bump Recovery Schedule Summary

| Email | File | Day | Time | Subject | Pitches |
|-------|------|-----|------|---------|---------|
| BR01 | BR01-dm-scripts.html | 2 | 2:00 PM | One thing I forgot to mention... | $37 DM Scripts |
| BR02 | BR02-templates.html | 4 | 2:00 PM | The blank page problem | $67 Templates |
| BR03 | BR03-last-chance.html | 6 | 2:00 PM | Before you move on... | All missed bumps |

### Key Settings
- **Send time:** 2:00 PM local (afternoon = offers, morning = welcome)
- **Smart skipping:** Checks which bumps are missing before each email — only pitches what they don't have
- **5-minute initial wait:** Critical — gives bump purchase tags time to register

---

## STEP 5: Build Workflow 4 — Bump Delivery

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Bump Delivery (Onboarding)`

### About This Workflow

Unlike recovery workflows that pitch missed products, bump delivery onboards what they already bought. Each bump gets its own simple workflow — deliver the product, give a quick-start action, and bridge to the most relevant next product.

### Build 3 Simple Workflows (One Per Bump)

**Workflow 4a: DM Scripts Delivery**

Trigger: Tag Added → `purchased-bump-dm-scripts`

```
Step 1:  WAIT → Wait 5 minutes (let all tags settle)
Step 2:  SEND EMAIL → BD01-dm-scripts-delivery.html
           Subject: "Your DM scripts are ready — do this in the next 5 minutes"
```

**Workflow 4b: Templates Delivery**

Trigger: Tag Added → `purchased-bump-templates`

```
Step 1:  WAIT → Wait 5 minutes
Step 2:  SEND EMAIL → BD02-templates-delivery.html
           Subject: "Your templates are ready — start with this one"
```

**Workflow 4c: Playbook Delivery**

Trigger: Tag Added → `purchased-bump-playbook`

```
Step 1:  WAIT → Wait 5 minutes
Step 2:  SEND EMAIL → BD03-playbook-delivery.html
           Subject: "Your playbook is ready — start with the Warm 50"
```

### Bump Delivery Schedule Summary

| Email | File | Trigger Tag | Time | Subject |
|-------|------|-------------|------|---------|
| BD01 | BD01-dm-scripts-delivery.html | `purchased-bump-dm-scripts` | +5 min | Your DM scripts are ready — do this in the next 5 minutes |
| BD02 | BD02-templates-delivery.html | `purchased-bump-templates` | +5 min | Your templates are ready — start with this one |
| BD03 | BD03-playbook-delivery.html | `purchased-bump-playbook` | +5 min | Your playbook is ready — start with the Warm 50 |

### Key Settings
- **5-minute wait:** Let all purchase tags settle before sending
- **Each fires independently** — buyer could get 1, 2, or all 3
- **Immediate delivery** — these are onboarding emails, not scheduled sends
- **Cross-sell bridges:** Each email leads to the limitation of what they bought and bridges to the next product (see 5-buyers-bump-delivery.md for full copy)

---

## STEP 6: Build Workflow 5 — OTO Recovery

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `OTO Recovery (DFY Offer Build)`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-47`

### Build the Steps

```
Step 1:  WAIT → Wait 5 minutes
           (Let OTO purchase tags settle)

Step 2:  IF/ELSE → Contact Tag → Has tag "purchased-dfy" OR "purchased-dfy-lite"
           ├── YES: End workflow — they already upgraded
           └── NO: continue

Step 3:  WAIT → Wait until Day 3, 2:00 PM

Step 4:  IF/ELSE → Contact Tag → Has tag "purchased-dfy" OR "purchased-dfy-lite"
           ├── YES: skip (bought DFY since workflow started)
           └── NO:
                 SEND EMAIL → OR01-dfy-pitch.html
                 Subject: "You have the system. But do you have YOUR offer built?"

Step 5:  WAIT → Wait until Day 5, 2:00 PM

Step 6:  IF/ELSE → Contact Tag → Has tag "purchased-dfy" OR "purchased-dfy-lite"
           ├── YES: skip
           └── NO:
                 SEND EMAIL → OR02-dfy-story.html
                 Subject: "She had the system for 3 weeks. Nothing happened. Then this."

Step 7:  WAIT → Wait until Day 7, 2:00 PM

Step 8:  IF/ELSE → Contact Tag → Has tag "purchased-dfy" OR "purchased-dfy-lite"
           ├── YES: skip
           └── NO:
                 SEND EMAIL → OR03-dfy-final.html
                 Subject: "What 48 hours could save you"

(Workflow ends)
```

### OTO Recovery Schedule Summary

| Email | File | Day | Time | Subject | Pitches |
|-------|------|-----|------|---------|---------|
| OR01 | OR01-dfy-pitch.html | 3 | 2:00 PM | You have the system. But do you have YOUR offer built? | $197 DFY |
| OR02 | OR02-dfy-story.html | 5 | 2:00 PM | She had the system for 3 weeks. Nothing happened. | $197 DFY |
| OR03 | OR03-dfy-final.html | 7 | 2:00 PM | What 48 hours could save you | $197 DFY |

### Key Settings
- **Send time:** 2:00 PM local
- **All 3 emails pitch DFY Offer Build ($197).** Different angles each day.
- **If they buy DFY or DFY Lite mid-sequence:** Remaining emails skip.
- **DFY page includes downsell to DFY Lite ($97)** — no separate email needed for the downsell.

---

## STEP 7: Build Workflow 6 — Community Recovery

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Community Recovery (Downsell)`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-47`

### Build the Steps

```
Step 1:  WAIT → Wait until Day 8, 2:00 PM

Step 2:  IF/ELSE → Contact Tag → Has ANY of these tags:
           "purchased-dfy" OR
           "purchased-dfy-lite" OR
           "purchased-community"
           ├── YES: End workflow (DFY buyers have community trial; community members already in)
           └── NO: continue (said no to everything)

Step 3:  SEND EMAIL → CR01-community-downsell.html
           Subject: "Not ready yet? (That's okay)"

(Workflow ends)
```

### Community Recovery Schedule Summary

| Email | File | Day | Time | Subject | Pitches |
|-------|------|-----|------|---------|---------|
| CR01 | CR01-community-recovery.html | 8 | 2:00 PM | The part nobody warns you about | $97/mo Community |

### Key Settings
- **Only 1 email** — this is the community pitch for people who said no to DFY
- **Day 8** = after OTO Recovery is done (Days 3, 5, 7)
- **Checks DFY + community tags** — DFY buyers already have a community trial, skip this

---

## STEP 8: Build Workflow 7 — Accountability DM (DFY Buyers)

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Accountability DM (DFY Buyers)`

### Purpose

Manual outreach within 48 hours of DFY or DFY Lite purchase. Not automated email — a real DM from Michael. This catches high-value buyers at peak motivation.

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-dfy` OR `purchased-dfy-lite`

### Build the Steps

```
Step 1:  WAIT → Wait 1 hour
           (Let purchase settle, don't DM instantly)

Step 2:  INTERNAL NOTIFICATION → Send to Michael
           Channel: Email or SMS (whichever you check most)
           Message: "🔔 New [DFY/DFY Lite] buyer: {{contact.name}} ({{contact.email}})
                     Purchased: {{trigger.tag}}
                     ACTION: Send accountability DM within 48 hours"

Step 3:  ADD TAG → "needs-accountability-dm"

Step 4:  WAIT → Wait 48 hours

Step 5:  IF/ELSE → Contact Tag → Has tag "needs-accountability-dm"
           ├── YES (DM not sent yet):
           │     INTERNAL NOTIFICATION → "⚠️ OVERDUE: Accountability DM for {{contact.name}} not sent yet"
           └── NO (tag removed = DM was sent):
                 (Workflow ends)
```

### The DM Script

Send via Skool DM, Instagram DM, or email reply — wherever the buyer is most active:

> "Hey [name] — saw you grabbed the DFY Offer Build. Your deliverables are being built now. Just wanted to make sure you got the onboarding form. What are you working on right now?"

### After Sending the DM

Remove the `needs-accountability-dm` tag manually after you've sent the DM. This prevents the 48-hour reminder from firing.

### Key Settings
- **Not an automated email** — this is a manual DM triggered by a notification
- **48-hour reminder** ensures no buyer falls through the cracks
- **Remove tag after sending** to mark it done
- **At scale (20+ per week):** Hire a setter to handle these. Same script. Same energy.

---

## STEP 9: Set Up Daily Broadcast (Workflow 8)

**Where:** This is NOT a workflow in the same sense. It's a segment + manual/scheduled sends.

### 9A: Create the Segment

Go to **Contacts → Smart Lists** (or Segments):

**Name:** `Daily Broadcast List`

**Filter:**
```
Tag: "in-daily-broadcast" = TRUE
AND
Tag: "unsubscribed" ≠ TRUE
```

### 9B: Choose Your Send Method

**Option A: Manual Daily Send (Recommended to Start)**
1. Each morning, write your email (15-20 min)
2. Go to **Marketing → Emails → Create Email**
3. Select the `Daily Broadcast List` segment
4. Write or paste your email
5. Send

**Option B: Pre-Loaded Weekly Rotation**
1. Go to **Marketing → Emails → Campaigns**
2. Create 7 email templates using the HTML files:

| Day | File | Subject | Offer Pitched |
|-----|------|---------|---------------|
| Monday | DB01-monday-frontend.html | The coach who couldn't explain what she does | $47 Front-end |
| Tuesday | DB02-tuesday-templates.html | I stared at the blank page for 3 hours | $67 Templates |
| Wednesday | DB03-wednesday-sprint.html | The difference between "knowing" and "doing" | $197 DFY / Sprint |
| Thursday | DB04-thursday-newsletter.html | What's working right now (and what quietly stopped) | $37/mo Monthly Playbook (reply "PLAYBOOK") |
| Friday | DB05-friday-backend.html | When you're ready for the next level | $5K Accelerator (reply "ACCELERATOR") |
| Saturday | DB06-saturday-community.html | The loneliest part of building | $97/mo Community |
| Sunday | DB07-sunday-free-value.html | The question that changes everything | No pitch |

3. Schedule each to send at 8:00 AM on its corresponding day
4. Set to recurring weekly
5. Target: `Daily Broadcast List` segment

### 9C: Segmentation for Owned Products

As buyers ascend, they should stop seeing pitches for products they already own. In each broadcast email:

- Use GHL's conditional content blocks (IF tag exists → show alternative CTA)
- Or create separate email versions per segment

| If Buyer Has | Skip Pitch For | On Day |
|--------------|----------------|--------|
| `purchased-bump-templates` | $67 Templates | Tuesday |
| `purchased-dfy` | $197 DFY Offer Build | Wednesday |
| `purchased-community` | $97/mo Community | Thursday |
| `purchased-newsletter` | $37/mo Newsletter | Saturday |

**Keep the story. Swap the CTA.** The story is the value — just change what you link to at the end.

---

## Complete Buyer Journey — Day by Day

Here's exactly what a buyer who purchased ONLY the $47 (no bumps, no OTOs) receives:

| Day | Time | Sequence | Email | Subject | Notes |
|-----|------|----------|-------|---------|-------|
| 1 | Immediate | Welcome | BW01 | You're in — here's your first win | |
| 2 | 8:00 AM | Welcome | BW02 | Why I do this (honest answer) | |
| 2 | 2:00 PM | Bump Recovery | BR01 | One thing I forgot to mention... | |
| 3 | 8:00 AM | Welcome | BW03a or BW03b | Advanced Tips / Quick Start | **Consumption branch** |
| 3 | 2:00 PM | OTO Recovery | OR01 | You have the system. But do you have YOUR offer built? | |
| 4 | 8:00 AM | Welcome | BW04 | The mistake that cost me 6 months | |
| 4 | 2:00 PM | Bump Recovery | BR02 | The blank page problem | |
| 5 | 8:00 AM | Welcome | BW05 | The 2-minute test for your offer | **Soft ascension P.S.** |
| 5 | 2:00 PM | OTO Recovery | OR02 | She had the system for 3 weeks. Nothing happened. | |
| 6 | 8:00 AM | Welcome | BW06 | From stuck to first client in 30 days | |
| 6 | 2:00 PM | Bump Recovery | BR03 | Before you move on... | |
| 7 | 8:00 AM | Welcome | BW07 | What my morning actually looks like | **Soft ascension P.S.** |
| 7 | 2:00 PM | OTO Recovery | OR03 | What 48 hours could save you | |
| 8 | 8:00 AM | Welcome | BW08 | "What if I'm not ready?" | |
| 8 | 2:00 PM | Community Recovery | CR01 | The part nobody warns you about | |
| 9 | 8:00 AM | Welcome | BW09 | What happens after $47 | **Explicit ascension CTA** |
| 10 | 8:00 AM | Welcome | BW10 | Come hang out | |
| 11+ | 8:00 AM | Daily Broadcast | DB01-07 | (rotating daily) | |

**Max 2 emails per day.** Morning (8 AM) = relationship. Afternoon (2 PM) = offers.

**Bump delivery (if bumps purchased):**
- Within 5 minutes of purchase: BD01/BD02/BD03 (whichever bumps they bought)
- These fire at checkout, before the welcome sequence starts

**Iron Strike additions (Days 3-9):**
- Day 3 branches based on product consumption (different email for openers vs non-openers)
- Days 5, 7 add soft ascension P.S. to existing relationship emails
- Day 9 adds explicit DFY CTA
- DFY/DFY Lite buyers also get a manual accountability DM within 48 hours (Workflow 7)

---

## Non-Buyer Journey — Day by Day

What someone who entered their email but didn't buy receives:

| Day | Time | Email | Subject |
|-----|------|-------|---------|
| 0 | +30 min | NB01 | You left something behind |
| 2 | 9:00 AM | NB02 | What's an unclear offer costing you? |
| 4 | 9:00 AM | NB03 | "I already know my offer" |
| 6 | 9:00 AM | NB04 | Stop niching down |
| 8 | 9:00 AM | NB05 | "I finally stopped second-guessing myself" |
| 10 | 9:00 AM | NB06 | Last thing on this |
| 14 | 9:00 AM | NB07 | Forget the pitch - here's something useful |
| 16 | 9:00 AM | NB08 | "Build it and they will come" |
| 19 | 9:00 AM | NB09 | From "I help people" to $5K clients |
| 22 | 9:00 AM | NB10 | What's another month of "figuring it out" cost you? |
| 26 | 9:00 AM | NB11 | Free resources won't save you |
| 30 | 9:00 AM | NB12 | Closing the loop on this |

**If they buy at any point:** Workflow exits immediately. They enter buyer workflows instead.

---

## Testing Checklist

Test with a real contact (yourself or a test email) through each path:

### Pre-Launch
- [ ] All 13 tags created in GHL (including `product-accessed` and `needs-accountability-dm`)
- [ ] All 9 triggers created and active (8 purchase + 1 routing)
- [ ] Product access link in BW01 is a GHL tracked link → triggers `product-accessed` tag
- [ ] All 8 workflows built and set to ACTIVE

### Test Path 1: Non-Buyer
- [ ] Enter email on checkout, don't pay
- [ ] Verify `lead` tag applied
- [ ] Verify `non-buyer-sequence` tag applied (from trigger)
- [ ] Wait 30 min — verify NB01 sends
- [ ] Verify purchase check works: manually add `purchased-47` tag → confirm workflow exits

### Test Path 2: Buyer (No Bumps)
- [ ] Complete $47 purchase (no bumps)
- [ ] Verify `purchased-47` tag applied
- [ ] Verify `non-buyer-sequence` removed (by Buyer Welcome workflow Step 1)
- [ ] Verify BW01 sends immediately
- [ ] Verify Bump Recovery starts (BR01 on Day 2 at 2 PM)
- [ ] Verify OTO Recovery starts (OR01 on Day 3 at 2 PM)
- [ ] Verify Community Recovery sends on Day 8 at 2 PM

### Test Path 2b: Consumption Branch (Day 3)
- [ ] Click product link in BW01 → verify `product-accessed` tag applied
- [ ] Wait for Day 3 email → verify BW03a (advanced tips) sends
- [ ] For a separate test contact: do NOT click product link
- [ ] Wait for Day 3 email → verify BW03b (quick start) sends

### Test Path 2c: Ascension Emails (Days 5, 7, 9)
- [ ] Day 5: BW05 sends with DFY P.S. link — verify link works
- [ ] Day 7: BW07 sends with DFY P.S. link — verify link works
- [ ] Day 9: BW09 sends with explicit DFY CTA — verify link works

### Test Path 2d: Accountability DM (DFY Buyers)
- [ ] Purchase DFY → verify `purchased-dfy` tag applied
- [ ] Verify internal notification sent within 1 hour
- [ ] Verify `needs-accountability-dm` tag applied
- [ ] Send DM manually, remove tag
- [ ] Verify 48-hour reminder does NOT fire (tag removed)
- [ ] Test reminder: don't remove tag → verify overdue notification at 48 hours

### Test Path 2e: Bump Delivery
- [ ] Purchase $47 + DM Scripts bump
- [ ] Verify `purchased-bump-dm-scripts` tag applied
- [ ] Wait 5 min — verify BD01 sends
- [ ] Verify BD01 includes product access link and quick-start action
- [ ] Test with all 3 bumps — verify BD01, BD02, BD03 all send independently
- [ ] Verify cross-sell bridge links work in each email

### Test Path 3: Buyer (With Bumps)
- [ ] Complete $47 + all 3 bumps
- [ ] Verify all bump tags applied
- [ ] Verify Bump Recovery workflow exits at Step 2 (all bumps owned)
- [ ] Verify Welcome still runs normally

### Test Path 4: Mid-Sequence Purchase
- [ ] Start as non-buyer
- [ ] Let NB01 and NB02 send
- [ ] Then complete purchase
- [ ] Verify Non-Buyer workflow exits
- [ ] Verify Buyer workflows start

### Post-Welcome
- [ ] After Day 10: verify workflow completed
- [ ] Verify `buyer-30-day-complete` added
- [ ] Verify `in-daily-broadcast` added
- [ ] Verify contact appears in Daily Broadcast segment

---

## Troubleshooting

**Contact getting duplicate emails:**
- Check they're not in both non-buyer AND buyer sequences (trigger should remove `non-buyer-sequence` on purchase)
- Verify the Buyer Welcome workflow removes `non-buyer-sequence` tag (Step 1)

**Contact not receiving emails:**
- Check tag was added correctly (Settings → Tags → click tag → see contacts)
- Check workflow is set to ACTIVE (not Draft)
- Check contact is not marked as unsubscribed
- Check email sending limits aren't hit

**Timing is off:**
- Verify GHL account timezone (Settings → Business Info → Timezone)
- Use "Wait until specific time" (8:00 AM / 2:00 PM) not just "Wait X hours"
- If using "Wait 1 day until 8:00 AM" — GHL waits until the NEXT occurrence of 8:00 AM after the delay

**Recovery emails sending for products they already own:**
- Check the 5-minute initial wait is in place (Step 1 of Bump/OTO Recovery)
- Verify product purchase tags are firing correctly from your payment processor

**Workflow not triggering:**
- Verify the trigger tag matches exactly (case-sensitive)
- Check workflow is published/active
- Check contact doesn't have "Do Not Disturb" enabled

---

## File Reference

All email HTML files ready to paste into GHL:

| Sequence | Folder | Files |
|----------|--------|-------|
| Non-Buyer | `nb-sequence/` | NB01 through NB12 (12 files) |
| Buyer Welcome | `bw-sequence/` | BW01, BW02, BW03a, BW03b, BW04-BW10 (12 files) |
| Bump Recovery | `br-sequence/` | BR01 through BR03 (3 files) |
| OTO Recovery | `or-sequence/` | OR01 through OR03 (3 files) |
| Community Recovery | `cr-sequence/` | CR01 (1 file) |
| Daily Broadcast | `db-sequence/` | DB01 through DB07 (7 files) |
| Bump Delivery | `bd-sequence/` | BD01 through BD03 (3 files) |

**Total: 41 HTML email files.**

---

## See Also

- [README.md](README.md) — Email sequence overview
- [1-non-buyers-30-day.md](1-non-buyers-30-day.md) — Full non-buyer copy (markdown source)
- [2-buyers-welcome-10-day.md](2-buyers-welcome-10-day.md) — Full welcome copy (markdown source)
- [3-buyers-recovery-bumps.md](3-buyers-recovery-bumps.md) — Bump recovery copy
- [3-buyers-recovery-otos.md](3-buyers-recovery-otos.md) — OTO recovery copy
- [3-buyers-recovery-community.md](3-buyers-recovery-community.md) — Community recovery copy
- [4-buyers-daily-broadcast.md](4-buyers-daily-broadcast.md) — Daily broadcast templates
- [5-buyers-bump-delivery.md](5-buyers-bump-delivery.md) — Bump delivery/onboarding emails
- [reference/domain/funnel/email-rhythm.md](../../reference/domain/funnel/email-rhythm.md) — Strategy reference
