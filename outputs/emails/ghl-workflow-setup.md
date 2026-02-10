---
type: output
status: active
date: 2026-02-10
purpose: GHL workflow configuration for email sequences
updated: Explicit step-by-step for every workflow — no shortcuts
---

# GHL Workflow Setup

Complete GoHighLevel workflow configuration for the Client Ready email backend. Every step spelled out.

---

## What You're Building

6 workflows that handle the entire buyer journey automatically:

| # | Workflow Name | Trigger | Emails | HTML Files |
|---|---------------|---------|--------|------------|
| 1 | Non-Buyer Nurture | Entered email, no purchase | 12 emails / 30 days | `nb-sequence/NB01-NB12` |
| 2 | Buyer Welcome | Purchased $27 | 10 emails / 10 days | `bw-sequence/BW01-BW10` |
| 3 | Bump Recovery | Purchased $27, missed bumps | 3 emails (Days 2,4,6) | `br-sequence/BR01-BR03` |
| 4 | OTO Recovery | Purchased $27, no Sprint/Blueprint | 3 emails (Days 3,5,7) | `or-sequence/OR01-OR03` |
| 5 | Community Recovery | Purchased $27, no upsells at all | 1 email (Day 8) | `cr-sequence/CR01` |
| 6 | Daily Broadcast | Day 11+ | Ongoing (7 templates) | `db-sequence/DB01-DB07` |

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

### Sequence Tags
- `in-nonbuyer-sequence`
- `in-welcome-sequence`
- `completed-welcome`
- `in-daily-broadcast`

**Total: 12 tags.**

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
| $27 Client Ready Offer System | Payments → Products → Client Ready → Tags | `purchased-27` |
| $17 DM Scripts (Order Bump 1) | Payments → Products → DM Scripts → Tags | `purchased-bump-dm-scripts` |
| $37 Templates (Order Bump 2) | Payments → Products → Templates → Tags | `purchased-bump-templates` |
| $67 First $5K Client Playbook (Order Bump 3) | Payments → Products → Playbook → Tags | `purchased-bump-playbook` |
| $297 Sprint (OTO 1) | Payments → Products → Sprint → Tags | `purchased-sprint` |
| $397 Blueprint (OTO 2) | Payments → Products → Blueprint → Tags | `purchased-blueprint` |
| $47/mo Community (OTO 3) | Payments → Products → Community → Tags | `purchased-community` |

**If using Stripe directly (not GHL payments):** Set up Zapier or GHL's Stripe integration to add the same tags on purchase events.

### 1C: GHL Triggers (Simple Tag Routing)

**Where:** Settings → Automations → Triggers

Create these 2 triggers:

**Trigger 1: "Non-Buyer Start"**
- Event: Tag Added → `lead`
- Action: Add tag → `in-nonbuyer-sequence`

**Trigger 2: "Buyer Start"**
- Event: Tag Added → `purchased-27`
- Actions (in order):
  1. Add tag → `in-welcome-sequence`
  2. Remove tag → `in-nonbuyer-sequence`
  3. Remove tag → `lead`

That's it for triggers. Everything else happens inside workflows.

---

## STEP 2: Build Workflow 1 — Non-Buyer Nurture

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Non-Buyer Nurture (Abandoned Checkout)`

### Workflow Trigger
- Click "Add New Trigger"
- Type: **Tag Added**
- Tag: `in-nonbuyer-sequence`
- Save trigger

### Build the Steps (in order)

Click "+" after the trigger to add each step. Build this exact sequence:

```
Step 1:  WAIT → Wait for 30 minutes
Step 2:  IF/ELSE → Contact Tag → Has tag "purchased-27"
           ├── YES branch:
           │     Step 2a: REMOVE TAG → "in-nonbuyer-sequence"
           │     (branch ends — workflow exits)
           └── NO branch: (continue below)

Step 3:  SEND EMAIL → NB01-soft-abandon.html
           Subject: "You left something behind"
           From: Michael Scott

Step 4:  WAIT → Wait 1 day (until 9:00 AM)

Step 5:  IF/ELSE → Contact Tag → Has tag "purchased-27"
           ├── YES: REMOVE TAG "in-nonbuyer-sequence" → End
           └── NO: continue

Step 6:  SEND EMAIL → NB02-cost-of-waiting.html
           Subject: "What's an unclear offer costing you?"

Step 7:  WAIT → Wait 2 days (until 9:00 AM) [Day 4]

Step 8:  IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 9:  SEND EMAIL → NB03-objection-killer.html
           Subject: "I already know my offer"

Step 10: WAIT → Wait 2 days (until 9:00 AM) [Day 6]

Step 11: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 12: SEND EMAIL → NB04-contrarian-hook.html
           Subject: "Stop niching down"

Step 13: WAIT → Wait 2 days (until 9:00 AM) [Day 8]

Step 14: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 15: SEND EMAIL → NB05-social-proof.html
           Subject: "I finally stopped second-guessing myself"

Step 16: WAIT → Wait 2 days (until 9:00 AM) [Day 10]

Step 17: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 18: SEND EMAIL → NB06-direct-close.html
           Subject: "Last thing on this"

Step 19: WAIT → Wait 4 days (until 9:00 AM) [Day 14]

Step 20: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 21: SEND EMAIL → NB07-pivot-to-value.html
           Subject: "Forget the pitch - here's something useful"

Step 22: WAIT → Wait 2 days (until 9:00 AM) [Day 16]

Step 23: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 24: SEND EMAIL → NB08-wrong-wrong-wrong.html
           Subject: "Build it and they will come"

Step 25: WAIT → Wait 3 days (until 9:00 AM) [Day 19]

Step 26: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 27: SEND EMAIL → NB09-the-transformation.html
           Subject: "From 'I help people' to $5K clients"

Step 28: WAIT → Wait 3 days (until 9:00 AM) [Day 22]

Step 29: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 30: SEND EMAIL → NB10-the-calculator.html
           Subject: "What's another month of 'figuring it out' cost you?"

Step 31: WAIT → Wait 4 days (until 9:00 AM) [Day 26]

Step 32: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 33: SEND EMAIL → NB11-cant-go-it-alone.html
           Subject: "Free resources won't save you"

Step 34: WAIT → Wait 4 days (until 9:00 AM) [Day 30]

Step 35: IF/ELSE → Has tag "purchased-27"
           ├── YES: REMOVE TAG → End
           └── NO: continue

Step 36: SEND EMAIL → NB12-last-call.html
           Subject: "Closing the loop on this"

Step 37: REMOVE TAG → "in-nonbuyer-sequence"

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
- **Exit condition:** IF/ELSE checks for `purchased-27` before EVERY email
- **If they buy at any point:** Workflow exits, tag gets removed, buyer workflows take over

---

## STEP 3: Build Workflow 2 — Buyer Welcome (10-Day)

**Where:** Automations → Workflows → Create Workflow → Start from Scratch

**Name:** `Buyer Welcome (10-Day)`

### Workflow Trigger
- Type: **Tag Added**
- Tag: `in-welcome-sequence`

### Build the Steps

```
Step 1:  REMOVE TAG → "in-nonbuyer-sequence" (cleanup — may not exist, that's fine)

Step 2:  SEND EMAIL → BW01-welcome-quick-win.html
           Subject: "You're in — here's your first win"
           (Send immediately — don't wait)

Step 3:  WAIT → Wait 1 day (until 8:00 AM) [Day 2]

Step 4:  SEND EMAIL → BW02-origin-story.html
           Subject: "Why I do this (honest answer)"

Step 5:  WAIT → Wait 1 day (until 8:00 AM) [Day 3]

Step 6:  SEND EMAIL → BW03-case-study.html
           Subject: "She validated in 3 days"

Step 7:  WAIT → Wait 1 day (until 8:00 AM) [Day 4]

Step 8:  SEND EMAIL → BW04-common-mistake.html
           Subject: "The mistake that cost me 6 months"

Step 9:  WAIT → Wait 1 day (until 8:00 AM) [Day 5]

Step 10: SEND EMAIL → BW05-quick-tip.html
           Subject: "The 2-minute test for your offer"

Step 11: WAIT → Wait 1 day (until 8:00 AM) [Day 6]

Step 12: SEND EMAIL → BW06-transformation-story.html
           Subject: "From stuck to first client in 30 days"

Step 13: WAIT → Wait 1 day (until 8:00 AM) [Day 7]

Step 14: SEND EMAIL → BW07-behind-the-scenes.html
           Subject: "What my morning actually looks like"

Step 15: WAIT → Wait 1 day (until 8:00 AM) [Day 8]

Step 16: SEND EMAIL → BW08-faq-objection.html
           Subject: "What if I'm not ready?"

Step 17: WAIT → Wait 1 day (until 8:00 AM) [Day 9]

Step 18: SEND EMAIL → BW09-the-roadmap.html
           Subject: "What happens after $27"

Step 19: WAIT → Wait 1 day (until 8:00 AM) [Day 10]

Step 20: SEND EMAIL → BW10-community-invite.html
           Subject: "Come hang out"

Step 21: REMOVE TAG → "in-welcome-sequence"

Step 22: ADD TAG → "completed-welcome"

Step 23: ADD TAG → "in-daily-broadcast"

(Workflow ends)
```

### Buyer Welcome Schedule Summary

| Email | File | Day | Time | Subject |
|-------|------|-----|------|---------|
| BW01 | BW01-welcome-quick-win.html | 1 | Immediate | You're in — here's your first win |
| BW02 | BW02-origin-story.html | 2 | 8:00 AM | Why I do this (honest answer) |
| BW03 | BW03-case-study.html | 3 | 8:00 AM | She validated in 3 days |
| BW04 | BW04-common-mistake.html | 4 | 8:00 AM | The mistake that cost me 6 months |
| BW05 | BW05-quick-tip.html | 5 | 8:00 AM | The 2-minute test for your offer |
| BW06 | BW06-transformation-story.html | 6 | 8:00 AM | From stuck to first client in 30 days |
| BW07 | BW07-behind-the-scenes.html | 7 | 8:00 AM | What my morning actually looks like |
| BW08 | BW08-faq-objection.html | 8 | 8:00 AM | "What if I'm not ready?" |
| BW09 | BW09-the-roadmap.html | 9 | 8:00 AM | What happens after $27 |
| BW10 | BW10-community-invite.html | 10 | 8:00 AM | Come hang out |

### Key Settings
- **Send time:** 8:00 AM local (except BW01 which sends immediately on purchase)
- **No purchase checks needed** — they already bought
- **After Day 10:** Tags flip to `completed-welcome` + `in-daily-broadcast`

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
           (Let all purchase tags settle — bumps tag at same time as $27)

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
| BR01 | BR01-dm-scripts.html | 2 | 2:00 PM | One thing I forgot to mention... | $17 DM Scripts |
| BR02 | BR02-templates.html | 4 | 2:00 PM | The blank page problem | $37 Templates |
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
| Monday | DB01-monday-frontend.html | The coach who couldn't explain what she does | $27 Front-end |
| Tuesday | DB02-tuesday-templates.html | I stared at the blank page for 3 hours | $37 Templates |
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
| `purchased-bump-templates` | $37 Templates | Tuesday |
| `purchased-sprint` | $297 Sprint | Wednesday |
| `purchased-blueprint` | $397 Blueprint | Thursday |
| `purchased-community` | $47/mo Community | Saturday |

**Keep the story. Swap the CTA.** The story is the value — just change what you link to at the end.

---

## Complete Buyer Journey — Day by Day

Here's exactly what a buyer who purchased ONLY the $27 (no bumps, no OTOs) receives:

| Day | Time | Sequence | Email | Subject |
|-----|------|----------|-------|---------|
| 1 | Immediate | Welcome | BW01 | You're in — here's your first win |
| 2 | 8:00 AM | Welcome | BW02 | Why I do this (honest answer) |
| 2 | 2:00 PM | Bump Recovery | BR01 | One thing I forgot to mention... |
| 3 | 8:00 AM | Welcome | BW03 | She validated in 3 days |
| 3 | 2:00 PM | OTO Recovery | OR01 | Most people do this alone... |
| 4 | 8:00 AM | Welcome | BW04 | The mistake that cost me 6 months |
| 4 | 2:00 PM | Bump Recovery | BR02 | The blank page problem |
| 5 | 8:00 AM | Welcome | BW05 | The 2-minute test for your offer |
| 5 | 2:00 PM | OTO Recovery | OR02 | From "maybe someday" to first client in 28 days |
| 6 | 8:00 AM | Welcome | BW06 | From stuck to first client in 30 days |
| 6 | 2:00 PM | Bump Recovery | BR03 | Before you move on... |
| 7 | 8:00 AM | Welcome | BW07 | What my morning actually looks like |
| 7 | 2:00 PM | OTO Recovery | OR03 | What if I just built your strategy for you? |
| 8 | 8:00 AM | Welcome | BW08 | "What if I'm not ready?" |
| 8 | 2:00 PM | Community Recovery | CR01 | Not ready yet? (That's okay) |
| 9 | 8:00 AM | Welcome | BW09 | What happens after $27 |
| 10 | 8:00 AM | Welcome | BW10 | Come hang out |
| 11+ | 8:00 AM | Daily Broadcast | DB01-07 | (rotating daily) |

**Max 2 emails per day.** Morning (8 AM) = relationship. Afternoon (2 PM) = offers.

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
- [ ] All 12 tags created in GHL
- [ ] 2-step order form adds `lead` tag on Step 1
- [ ] Each product adds correct purchase tag
- [ ] Both GHL triggers created and active
- [ ] All 6 workflows built and set to ACTIVE

### Test Path 1: Non-Buyer
- [ ] Enter email on checkout, don't pay
- [ ] Verify `lead` tag applied
- [ ] Verify `in-nonbuyer-sequence` tag applied (from trigger)
- [ ] Wait 30 min — verify NB01 sends
- [ ] Verify purchase check works: manually add `purchased-27` tag → confirm workflow exits

### Test Path 2: Buyer (No Bumps)
- [ ] Complete $27 purchase (no bumps)
- [ ] Verify `purchased-27` tag applied
- [ ] Verify `in-nonbuyer-sequence` removed (from trigger)
- [ ] Verify `in-welcome-sequence` added (from trigger)
- [ ] Verify BW01 sends immediately
- [ ] Verify Bump Recovery starts (BR01 on Day 2 at 2 PM)
- [ ] Verify OTO Recovery starts (OR01 on Day 3 at 2 PM)
- [ ] Verify Community Recovery sends on Day 8 at 2 PM

### Test Path 3: Buyer (With Bumps)
- [ ] Complete $27 + all 3 bumps
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
- [ ] After Day 10: verify `in-welcome-sequence` removed
- [ ] Verify `completed-welcome` added
- [ ] Verify `in-daily-broadcast` added
- [ ] Verify contact appears in Daily Broadcast segment

---

## Troubleshooting

**Contact getting duplicate emails:**
- Check they're not in both non-buyer AND buyer sequences (trigger should remove `in-nonbuyer-sequence` on purchase)
- Verify the "Buyer Start" trigger removes `in-nonbuyer-sequence` tag

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
| Buyer Welcome | `bw-sequence/` | BW01 through BW10 (10 files) |
| Bump Recovery | `br-sequence/` | BR01 through BR03 (3 files) |
| OTO Recovery | `or-sequence/` | OR01 through OR03 (3 files) |
| Community Recovery | `cr-sequence/` | CR01 (1 file) |
| Daily Broadcast | `db-sequence/` | DB01 through DB07 (7 files) |

**Total: 36 HTML email files.**

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
