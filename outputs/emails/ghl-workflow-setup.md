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

7 workflows that handle the entire buyer journey automatically:

| # | Workflow Name | Trigger | Emails | HTML Files |
|---|---------------|---------|--------|------------|
| 1 | Non-Buyer Nurture | Entered email, no purchase | 12 emails / 30 days | `nb-sequence/NB01-NB12` |
| 2 | Buyer Welcome | Purchased $47 | 10 emails / 10 days (Day 3 branches) | `bw-sequence/BW01-BW10` + `BW03a/BW03b` |
| 3 | Bump Recovery | Purchased $47, missed bumps | 3 emails (Days 2,4,6) | `br-sequence/BR01-BR03` |
| 4 | OTO Recovery | Purchased $47, no Sprint/Blueprint | 3 emails (Days 3,5,7) | `or-sequence/OR01-OR03` |
| 5 | Community Recovery | Purchased $47, no upsells at all | 1 email (Day 8) | `cr-sequence/CR01` |
| 6 | Daily Broadcast | Day 11+ | Ongoing (7 templates) | `db-sequence/DB01-DB07` |
| 7 | Accountability DM | Purchased Sprint or Blueprint | Manual DM trigger | (no HTML — manual outreach) |

---

## STEP 0: Create All Tags

Go to **Settings → Tags** in GHL. Create each tag exactly as written (copy-paste the tag names).

### Lead Tag
- `lead`

### Purchase Tags
- `purchased-27`
- `purchased-bump-dm-scripts`
- `purchased-bump-templates`
- `purchased-bump-playbook`
- `purchased-sprint`
- `purchased-blueprint`
- `purchased-community`

### Routing Tags
- `buyer-core`
- `non-buyer-sequence`
- `buyer-sequence`
- `buyer-30-day-complete`
- `in-daily-broadcast`

### Consumption Tracking Tags
- `product-accessed`

### Accountability Tags
- `needs-accountability-dm`

**Total: 15 tags.**

---

## STEP 1: Configure Tag Sources

Tags need to fire automatically when things happen. Set up these sources BEFORE building workflows.

### 1A: 2-Step Order Form → `lead` Tag

**Where:** Your checkout page form settings (ClickFunnels / GHL funnel page)

1. Open your checkout page editor
2. Find the 2-step order form
3. In form settings, find "On Step 1 Submit" or "Form Submission" actions
4. Add action: **Add Tag → `lead`**
5. This fires when someone enters their email, even if they don't pay

### 1B: Products → Purchase Tags

**Where:** Payments → Products → [each product] → Settings → Tags

For each product, add the corresponding tag on purchase:

| Product | Go To | Add Tag |
|---------|-------|---------|
| $47 Client Ready Offer System | Payments → Products → Client Ready → Tags | `purchased-27` |
| $37 DM Scripts (Order Bump 1) | Payments → Products → DM Scripts → Tags | `purchased-bump-dm-scripts` |
| $67 Templates (Order Bump 2) | Payments → Products → Templates → Tags | `purchased-bump-templates` |
| $97 First $5K Client Playbook (Order Bump 3) | Payments → Products → Playbook → Tags | `purchased-bump-playbook` |
| $297 Sprint (OTO 1) | Payments → Products → Sprint → Tags | `purchased-sprint` |
| $397 Blueprint (OTO 2) | Payments → Products → Blueprint → Tags | `purchased-blueprint` |
| $47/mo Community (OTO 3) | Payments → Products → Community → Tags | `purchased-community` |

**If using Stripe directly (not GHL payments):** Set up Zapier or GHL's Stripe integration to add the same tags on purchase events.

### 1C: GHL Triggers (Simple Tag Routing)

**Where:** Settings → Automations → Triggers

Create these 2 triggers:

**Trigger 1: "Non-Buyer Start"**
- Event: Tag Added → `lead`
- Action: Add tag → `non-buyer-sequence`

**Trigger 2: "Buyer Start"**
- Event: Tag Added → `purchased-27`
- Actions (in order):
  1. Add tag → `buyer-core`
  2. Add tag → `buyer-sequence`
  3. Remove tag → `non-buyer-sequence`
  4. Remove tag → `lead`

That's it for triggers. Everything else happens inside workflows.

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
Step 2:  IF/ELSE → Contact Tag → Has tag "buyer-core"
           ├── YES branch:
           │     Step 2a: REMOVE TAG → "non-buyer-sequence"
           │     (branch ends — workflow exits)
           └── NO branch: (continue below)

Step 3:  SEND EMAIL → NB01-soft-abandon.html
           Subject: "You left something behind"
           From: Michael Scott

Step 4:  WAIT → Wait 1 day (until 9:00 AM)

Step 5:  IF/ELSE → Contact Tag → Has tag "buyer-core"
           ├── YES: REMOVE TAG "non-buyer-sequence" → End
           └── NO: continue

Step 6:  SEND EMAIL → NB02-cost-of-waiting.html
           Subject: "What's an unclear offer costing you?"

Step 7:  WAIT → Wait 2 days (until 9:00 AM) [Day 4]

Step 8:  IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 9:  SEND EMAIL → NB03-objection-killer.html
           Subject: "I already know my offer"

Step 10: WAIT → Wait 2 days (until 9:00 AM) [Day 6]

Step 11: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 12: SEND EMAIL → NB04-contrarian-hook.html
           Subject: "Stop niching down"

Step 13: WAIT → Wait 2 days (until 9:00 AM) [Day 8]

Step 14: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 15: SEND EMAIL → NB05-social-proof.html
           Subject: "I finally stopped second-guessing myself"

Step 16: WAIT → Wait 2 days (until 9:00 AM) [Day 10]

Step 17: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 18: SEND EMAIL → NB06-direct-close.html
           Subject: "Last thing on this"

Step 19: WAIT → Wait 4 days (until 9:00 AM) [Day 14]

Step 20: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 21: SEND EMAIL → NB07-pivot-to-value.html
           Subject: "Forget the pitch - here's something useful"

Step 22: WAIT → Wait 2 days (until 9:00 AM) [Day 16]

Step 23: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 24: SEND EMAIL → NB08-wrong-wrong-wrong.html
           Subject: "Build it and they will come"

Step 25: WAIT → Wait 3 days (until 9:00 AM) [Day 19]

Step 26: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 27: SEND EMAIL → NB09-the-transformation.html
           Subject: "From 'I help people' to $5K clients"

Step 28: WAIT → Wait 3 days (until 9:00 AM) [Day 22]

Step 29: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 30: SEND EMAIL → NB10-the-calculator.html
           Subject: "What's another month of 'figuring it out' cost you?"

Step 31: WAIT → Wait 4 days (until 9:00 AM) [Day 26]

Step 32: IF/ELSE → Has tag "buyer-core"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 33: SEND EMAIL → NB11-cant-go-it-alone.html
           Subject: "Free resources won't save you"

Step 34: WAIT → Wait 4 days (until 9:00 AM) [Day 30]

Step 35: IF/ELSE → Has tag "buyer-core"
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
- **Exit condition:** IF/ELSE checks for `buyer-core` before EVERY email
- **If they buy at any point:** Workflow exits, tag gets removed, buyer workflows take over

---

## STEP 3: Build Workflow 2 — Buyer Welcome (10-Day)

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Buyer Welcome (10-Day) — Iron Strike`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `buyer-sequence`

### Build the Steps

```
Step 1:  REMOVE TAG → "non-buyer-sequence" (cleanup — may not exist, that's fine)

Step 2:  SEND EMAIL → BW01-welcome-quick-win.html
           Subject: "You're in — here's your first win"
           (Send immediately — don't wait)

Step 3:  WAIT → Wait 1 day (until 8:00 AM) [Day 2]

Step 4:  SEND EMAIL → BW02-origin-story.html
           Subject: "Why I do this (honest answer)"

Step 5:  WAIT → Wait 1 day (until 8:00 AM) [Day 3]

         ┌─── CONSUMPTION BRANCH ───┐
Step 6:  IF/ELSE → Contact Tag → Has tag "product-accessed"
           ├── YES (opened product):
           │     Step 6a: SEND EMAIL → BW03a-advanced-tips.html
           │              Subject: "Now that you've started — get the most out of Prompt 3"
           └── NO (hasn't opened):
                 Step 6b: SEND EMAIL → BW03b-quick-start.html
                          Subject: "Haven't started yet? Here's the 5-minute version"
         └─── BOTH PATHS CONTINUE ──┘

Step 7:  WAIT → Wait 1 day (until 8:00 AM) [Day 4]

Step 8:  SEND EMAIL → BW04-common-mistake.html
           Subject: "The mistake that cost me 6 months"

Step 9:  WAIT → Wait 1 day (until 8:00 AM) [Day 5]

Step 10: SEND EMAIL → BW05-quick-tip.html
           Subject: "The 2-minute test for your offer"
           (Includes soft ascension P.S. — Sprint link)

Step 11: WAIT → Wait 1 day (until 8:00 AM) [Day 6]

Step 12: SEND EMAIL → BW06-transformation-story.html
           Subject: "From stuck to first client in 30 days"

Step 13: WAIT → Wait 1 day (until 8:00 AM) [Day 7]

Step 14: SEND EMAIL → BW07-behind-the-scenes.html
           Subject: "What my morning actually looks like"
           (Includes soft ascension P.S. — Sprint/Blueprint links)

Step 15: WAIT → Wait 1 day (until 8:00 AM) [Day 8]

Step 16: SEND EMAIL → BW08-faq-objection.html
           Subject: "What if I'm not ready?"

Step 17: WAIT → Wait 1 day (until 8:00 AM) [Day 9]

Step 18: SEND EMAIL → BW09-the-roadmap.html
           Subject: "What happens after $47"
           (Includes explicit Sprint vs Blueprint comparison CTA)

Step 19: WAIT → Wait 1 day (until 8:00 AM) [Day 10]

Step 20: SEND EMAIL → BW10-community-invite.html
           Subject: "Come hang out"

Step 21: REMOVE TAG → "buyer-sequence"

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
- **Day 5:** Sprint link after the quick tip (natural "if you passed the test, here's the next step")
- **Day 7:** Sprint/Blueprint comparison after behind-the-scenes (natural "this is the system — want help building yours?")
- **Day 9:** Explicit Sprint vs Blueprint CTA within the roadmap email (natural "you're at Stage 1 — here's how to move to Stage 2-4")

**Voice guard:** These are P.S. additions, not hard sells. The body of each email is unchanged. If the P.S. feels out of place or pushy, remove it — the parallel recovery sequences still handle direct pitching.

### Buyer Welcome Schedule Summary

| Email | File | Day | Time | Subject | Ascension |
|-------|------|-----|------|---------|-----------|
| BW01 | BW01-welcome-quick-win.html | 1 | Immediate | You're in — here's your first win | — |
| BW02 | BW02-origin-story.html | 2 | 8:00 AM | Why I do this (honest answer) | — |
| BW03a | BW03a-advanced-tips.html | 3 | 8:00 AM | Now that you've started — get the most out of Prompt 3 | Consumption: opened |
| BW03b | BW03b-quick-start.html | 3 | 8:00 AM | Haven't started yet? Here's the 5-minute version | Consumption: not opened |
| BW04 | BW04-common-mistake.html | 4 | 8:00 AM | The mistake that cost me 6 months | — |
| BW05 | BW05-quick-tip.html | 5 | 8:00 AM | The 2-minute test for your offer | Soft close (Sprint) |
| BW06 | BW06-transformation-story.html | 6 | 8:00 AM | From stuck to first client in 30 days | — |
| BW07 | BW07-behind-the-scenes.html | 7 | 8:00 AM | What my morning actually looks like | Soft close (Sprint/Blueprint) |
| BW08 | BW08-faq-objection.html | 8 | 8:00 AM | "What if I'm not ready?" | — |
| BW09 | BW09-the-roadmap.html | 9 | 8:00 AM | What happens after $47 | Explicit CTA (Sprint vs Blueprint) |
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
- Tag: `purchased-27`

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

## STEP 5: Build Workflow 4 — OTO Recovery

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `OTO Recovery (Sprint + Blueprint)`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-27`

### Build the Steps

```
Step 1:  WAIT → Wait 5 minutes
           (Let OTO purchase tags settle)

Step 2:  IF/ELSE → Contact Tag → Has tag "purchased-sprint" OR "purchased-blueprint"
           ├── YES: End workflow — they already upgraded
           └── NO: continue

Step 3:  WAIT → Wait until Day 3, 2:00 PM

Step 4:  IF/ELSE → Contact Tag → Has tag "purchased-sprint"
           ├── YES: skip (bought Sprint since workflow started)
           └── NO:
                 SEND EMAIL → OR01-sprint-pitch.html
                 Subject: "Most people do this alone (you don't have to)"

Step 5:  WAIT → Wait until Day 5, 2:00 PM

Step 6:  IF/ELSE → Contact Tag → Has tag "purchased-sprint"
           ├── YES: skip
           └── NO:
                 SEND EMAIL → OR02-sprint-story.html
                 Subject: "From 'maybe someday' to first client in 28 days"

Step 7:  WAIT → Wait until Day 7, 2:00 PM

Step 8:  IF/ELSE → Contact Tag → Has tag "purchased-blueprint"
           ├── YES: skip (already bought Blueprint)
           └── NO:
                 SEND EMAIL → OR03-blueprint-pitch.html
                 Subject: "What if I just built your strategy for you?"

(Workflow ends)
```

### OTO Recovery Schedule Summary

| Email | File | Day | Time | Subject | Pitches |
|-------|------|-----|------|---------|---------|
| OR01 | OR01-sprint-pitch.html | 3 | 2:00 PM | Most people do this alone... | $297 Sprint |
| OR02 | OR02-sprint-story.html | 5 | 2:00 PM | From "maybe someday" to first client in 28 days | $297 Sprint |
| OR03 | OR03-blueprint-pitch.html | 7 | 2:00 PM | What if I just built your strategy for you? | $397 Blueprint |

### Key Settings
- **Send time:** 2:00 PM local
- **Days 3 and 5 pitch Sprint.** Day 7 pivots to Blueprint.
- **If they buy Sprint mid-sequence:** Day 5 and 7 emails skip the Sprint pitch. Day 7 still offers Blueprint.
- **If they buy Blueprint at any point:** Email 3 skips (they got something better)

---

## STEP 6: Build Workflow 5 — Community Recovery

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Community Recovery (Downsell)`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-27`

### Build the Steps

```
Step 1:  WAIT → Wait until Day 8, 2:00 PM

Step 2:  IF/ELSE → Contact Tag → Has ANY of these tags:
           "purchased-sprint" OR
           "purchased-blueprint" OR
           "purchased-community"
           ├── YES: End workflow (they already upgraded to something)
           └── NO: continue (said no to everything)

Step 3:  SEND EMAIL → CR01-community-downsell.html
           Subject: "Not ready yet? (That's okay)"

(Workflow ends)
```

### Community Recovery Schedule Summary

| Email | File | Day | Time | Subject | Pitches |
|-------|------|-----|------|---------|---------|
| CR01 | CR01-community-downsell.html | 8 | 2:00 PM | Not ready yet? (That's okay) | $47/mo Community ($1 trial) |

### Key Settings
- **Only 1 email** — this is the downsell for people who said no to Sprint AND Blueprint
- **Day 8** = after OTO Recovery is done (Days 3, 5, 7)
- **Checks all three upgrade tags** — if they bought anything higher, skip this entirely

---

## STEP 7: Set Up Daily Broadcast (Workflow 6)

**Where:** This is NOT a workflow in the same sense. It's a segment + manual/scheduled sends.

### 7A: Create the Segment

Go to **Contacts → Smart Lists** (or Segments):

**Name:** `Daily Broadcast List`

**Filter:**
```
Tag: "in-daily-broadcast" = TRUE
AND
Tag: "unsubscribed" ≠ TRUE
```

### 7B: Choose Your Send Method

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
| Wednesday | DB03-wednesday-sprint.html | The difference between "knowing" and "doing" | $297 Sprint |
| Thursday | DB04-thursday-blueprint.html | Some people have time. Some people have money. | $397 Blueprint |
| Friday | DB05-friday-backend.html | When you're ready for the next level | $5K Accelerator (reply "BUILD") |
| Saturday | DB06-saturday-community.html | The loneliest part of building | $47/mo Community |
| Sunday | DB07-sunday-free-value.html | The question that changes everything | No pitch |

3. Schedule each to send at 8:00 AM on its corresponding day
4. Set to recurring weekly
5. Target: `Daily Broadcast List` segment

### 7C: Segmentation for Owned Products

As buyers ascend, they should stop seeing pitches for products they already own. In each broadcast email:

- Use GHL's conditional content blocks (IF tag exists → show alternative CTA)
- Or create separate email versions per segment

| If Buyer Has | Skip Pitch For | On Day |
|--------------|----------------|--------|
| `purchased-bump-templates` | $67 Templates | Tuesday |
| `purchased-sprint` | $297 Sprint | Wednesday |
| `purchased-blueprint` | $397 Blueprint | Thursday |
| `purchased-community` | $47/mo Community | Saturday |

**Keep the story. Swap the CTA.** The story is the value — just change what you link to at the end.

---

## STEP 8: Build Workflow 7 — Accountability DM (Sprint/Blueprint)

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Accountability DM (Sprint/Blueprint Buyers)`

### Purpose

Manual outreach within 48 hours of Sprint or Blueprint purchase. Not automated email — a real DM from Michael. This catches high-value buyers at peak motivation.

### Workflow Trigger
- Type: **Tag Added**
- Tag: `purchased-sprint` OR `purchased-blueprint`

### Build the Steps

```
Step 1:  WAIT → Wait 1 hour
           (Let purchase settle, don't DM instantly)

Step 2:  INTERNAL NOTIFICATION → Send to Michael
           Channel: Email or SMS (whichever you check most)
           Message: "🔔 New [Sprint/Blueprint] buyer: {{contact.name}} ({{contact.email}})
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

> "Hey [name] — saw you grabbed the [Sprint/Blueprint]. Just wanted to make sure you got access to everything. What are you working on right now?"

### After Sending the DM

Remove the `needs-accountability-dm` tag manually after you've sent the DM. This prevents the 48-hour reminder from firing.

### Key Settings
- **Not an automated email** — this is a manual DM triggered by a notification
- **48-hour reminder** ensures no buyer falls through the cracks
- **Remove tag after sending** to mark it done
- **At scale (20+ per week):** Hire a setter to handle these. Same script. Same energy.

---

## Complete Buyer Journey — Day by Day

Here's exactly what a buyer who purchased ONLY the $47 (no bumps, no OTOs) receives:

| Day | Time | Sequence | Email | Subject | Notes |
|-----|------|----------|-------|---------|-------|
| 1 | Immediate | Welcome | BW01 | You're in — here's your first win | |
| 2 | 8:00 AM | Welcome | BW02 | Why I do this (honest answer) | |
| 2 | 2:00 PM | Bump Recovery | BR01 | One thing I forgot to mention... | |
| 3 | 8:00 AM | Welcome | BW03a or BW03b | Advanced Tips / Quick Start | **Consumption branch** |
| 3 | 2:00 PM | OTO Recovery | OR01 | Most people do this alone... | |
| 4 | 8:00 AM | Welcome | BW04 | The mistake that cost me 6 months | |
| 4 | 2:00 PM | Bump Recovery | BR02 | The blank page problem | |
| 5 | 8:00 AM | Welcome | BW05 | The 2-minute test for your offer | **Soft ascension P.S.** |
| 5 | 2:00 PM | OTO Recovery | OR02 | From "maybe someday" to first client in 28 days | |
| 6 | 8:00 AM | Welcome | BW06 | From stuck to first client in 30 days | |
| 6 | 2:00 PM | Bump Recovery | BR03 | Before you move on... | |
| 7 | 8:00 AM | Welcome | BW07 | What my morning actually looks like | **Soft ascension P.S.** |
| 7 | 2:00 PM | OTO Recovery | OR03 | What if I just built your strategy for you? | |
| 8 | 8:00 AM | Welcome | BW08 | "What if I'm not ready?" | |
| 8 | 2:00 PM | Community Recovery | CR01 | Not ready yet? (That's okay) | |
| 9 | 8:00 AM | Welcome | BW09 | What happens after $47 | **Explicit ascension CTA** |
| 10 | 8:00 AM | Welcome | BW10 | Come hang out | |
| 11+ | 8:00 AM | Daily Broadcast | DB01-07 | (rotating daily) | |

**Max 2 emails per day.** Morning (8 AM) = relationship. Afternoon (2 PM) = offers.

**Iron Strike additions (Days 3-9):**
- Day 3 branches based on product consumption (different email for openers vs non-openers)
- Days 5, 7 add soft ascension P.S. to existing relationship emails
- Day 9 adds explicit Sprint vs Blueprint comparison CTA
- Sprint/Blueprint buyers also get a manual accountability DM within 48 hours (Workflow 7)

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
- [ ] All 15 tags created in GHL (including `product-accessed` and `needs-accountability-dm`)
- [ ] 2-step order form adds `lead` tag on Step 1
- [ ] Each product adds correct purchase tag
- [ ] Product access link in BW01 is a GHL tracked link → triggers `product-accessed` tag
- [ ] Both GHL triggers created and active
- [ ] All 7 workflows built and set to ACTIVE

### Test Path 1: Non-Buyer
- [ ] Enter email on checkout, don't pay
- [ ] Verify `lead` tag applied
- [ ] Verify `non-buyer-sequence` tag applied (from trigger)
- [ ] Wait 30 min — verify NB01 sends
- [ ] Verify purchase check works: manually add `buyer-core` tag → confirm workflow exits

### Test Path 2: Buyer (No Bumps)
- [ ] Complete $47 purchase (no bumps)
- [ ] Verify `purchased-27` tag applied
- [ ] Verify `non-buyer-sequence` removed (from trigger)
- [ ] Verify `buyer-sequence` added (from trigger)
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
- [ ] Day 5: BW05 sends with Sprint P.S. link — verify link works
- [ ] Day 7: BW07 sends with Sprint/Blueprint P.S. links — verify both work
- [ ] Day 9: BW09 sends with explicit Sprint vs Blueprint comparison — verify links

### Test Path 2d: Accountability DM (Sprint/Blueprint)
- [ ] Purchase Sprint → verify `purchased-sprint` tag applied
- [ ] Verify internal notification sent within 1 hour
- [ ] Verify `needs-accountability-dm` tag applied
- [ ] Send DM manually, remove tag
- [ ] Verify 48-hour reminder does NOT fire (tag removed)
- [ ] Test reminder: don't remove tag → verify overdue notification at 48 hours

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
- [ ] After Day 10: verify `buyer-sequence` removed
- [ ] Verify `buyer-30-day-complete` added
- [ ] Verify `in-daily-broadcast` added
- [ ] Verify contact appears in Daily Broadcast segment

---

## Troubleshooting

**Contact getting duplicate emails:**
- Check they're not in both non-buyer AND buyer sequences (trigger should remove `non-buyer-sequence` on purchase)
- Verify the "Buyer Start" trigger removes `non-buyer-sequence` tag

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

**Total: 38 HTML email files.**

---

## See Also

- [README.md](README.md) — Email sequence overview
- [1-non-buyers-30-day.md](1-non-buyers-30-day.md) — Full non-buyer copy (markdown source)
- [2-buyers-welcome-10-day.md](2-buyers-welcome-10-day.md) — Full welcome copy (markdown source)
- [3-buyers-recovery-bumps.md](3-buyers-recovery-bumps.md) — Bump recovery copy
- [3-buyers-recovery-otos.md](3-buyers-recovery-otos.md) — OTO recovery copy
- [3-buyers-recovery-community.md](3-buyers-recovery-community.md) — Community recovery copy
- [4-buyers-daily-broadcast.md](4-buyers-daily-broadcast.md) — Daily broadcast templates
- [reference/domain/email-rhythm.md](../../reference/domain/email-rhythm.md) — Strategy reference
