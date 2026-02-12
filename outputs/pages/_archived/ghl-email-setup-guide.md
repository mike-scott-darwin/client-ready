---
type: output
status: active
date: 2026-01-25
format: Implementation Guide
platform: GoHighLevel
---

# GoHighLevel Email Sequence Setup Guide

Step-by-step instructions for implementing the Non-Buyer and Buyer email sequences in GHL.

---

## Prerequisites

Before starting:
- [ ] GoHighLevel account with email sending enabled
- [ ] Domain verified for sending
- [ ] Sales page URL ready
- [ ] Checkout/payment processor connected (Stripe recommended)
- [ ] Products created in GHL ($27, $17, $37, $67, $297, $397, $47/mo)

---

## Part 1: Create Tags

Go to **Settings → Tags** and create all of these tags before building triggers or workflows.

### Purchase Tags (auto-added by products on payment — see Part 3 for setup)
| Tag Name | Purpose |
|----------|---------|
| `purchased-27` | Bought $27 front-end |
| `purchased-bump-dm-scripts` | Bought $17 DM Scripts bump |
| `purchased-bump-templates` | Bought $37 Templates bump |
| `purchased-bump-playbook` | Bought $67 First $5K Client Playbook bump |
| `purchased-sprint` | Bought $297 Sprint |
| `purchased-blueprint` | Bought $397 Blueprint |
| `purchased-community` | Bought $47/mo Community |

### Routing Tags (added by triggers — see Part 3)
| Tag Name | Purpose |
|----------|---------|
| `lead` | Entered email on checkout Step 1 (auto-tagged by order form) |
| `buyer-core` | Confirmed $27 buyer (added by Trigger 2) |
| `buyer-sprint` | Confirmed Sprint buyer (added by Trigger 3) |
| `buyer-blueprint` | Confirmed Blueprint buyer (added by Trigger 4) |

### Sequence Status Tags (added/removed by workflows)
| Tag Name | Purpose |
|----------|---------|
| `non-buyer-sequence` | Currently in non-buyer workflow |
| `non-buyer-30-day-complete` | Finished non-buyer sequence |
| `buyer-sequence` | Currently in buyer workflow |
| `buyer-30-day-complete` | Finished buyer sequence |

### Engagement Tags (added by detection workflows — see Parts 8-9)
| Tag Name | Purpose |
|----------|---------|
| `engaged-non-buyer` | Opens emails but hasn't bought |
| `cold-lead` | No opens for 14+ days |
| `backend-interested` | Replied "BUILD" |
| `interested-launch-kit` | Replied "LAUNCH" or "24HR" |

### Link Tracking Tags (added by trigger links — see Part 7)
| Tag Name | Purpose |
|----------|---------|
| `clicked-sales-page` | Clicked $27 sales page link in email |
| `clicked-sprint` | Clicked Sprint page link in email |
| `clicked-blueprint` | Clicked Blueprint page link in email |

---

## Part 2: Create Custom Fields

Go to **Settings → Custom Fields** and create:

| Field Name | Type | Purpose |
|------------|------|---------|
| `purchase_date` | Date | When they bought |
| `products_purchased` | Multi-select | Track all products bought |
| `sequence_start_date` | Date | When sequence started |
| `last_email_opened` | Date | Track engagement |

---

## Part 3: How Triggers and Workflows Connect

**Important:** GHL has two automation systems that work together:

- **Triggers** (Settings → Automations → Triggers) — Simple tag routing. Can only add/remove tags, add to pipeline, send notifications. **Cannot** start workflows, stop workflows, skip to steps, or wait.
- **Workflows** (Automations → Workflows) — Full automation. Each workflow has its own built-in trigger (entry event) plus steps like wait, if/else, send email, add/remove tags.

**The pattern:** Triggers add tags → Workflows listen for those tags and run the sequences. The workflows also check for purchase tags before every email, so they stop themselves when someone buys.

### How the "lead" Tag Gets Added

Your 2-step order form captures email on Step 1. Configure your order form to auto-add the `lead` tag when Step 1 is submitted:

1. Go to your checkout page in the funnel builder
2. Open the order form settings
3. Look for **Tags** or **Add tag on submission** — add `lead`

This ensures anyone who enters their email (even if they don't pay) gets tagged as a lead.

### Trigger 1: Non-Buyer Sequence Start

Go to **Settings → Automations → Triggers → + Add Trigger**

```
Name: "Trigger 1: Non-Buyer Sequence Start"
Event: Contact Tag → Tag Added → "lead"
Action: Add Contact Tag → "non-buyer-sequence"
```

The Non-Buyer Workflow (Part 4) listens for the `non-buyer-sequence` tag. The workflow itself handles the 30-minute wait and purchase check — triggers can't do that.

### Trigger 2: Buyer Tag Routing

```
Name: "Trigger 2: Buyer Sequence Start"
Event: Contact Tag → Tag Added → "purchased-27"
Action 1: Add Contact Tag → "buyer-core"
Action 2: Add Contact Tag → "buyer-sequence"
Action 3: Remove Contact Tag → "non-buyer-sequence"
Action 4: Remove Contact Tag → "lead"
```

**How `purchased-27` gets added:** Configure your $27 product in GHL to auto-tag with `purchased-27` on successful payment. The Buyer Workflow (Part 5) listens for the `buyer-sequence` tag. The Non-Buyer Workflow stops itself because it checks for `buyer-core` before every email.

### Trigger 3: Sprint Purchase

```
Name: "Trigger 3: Sprint Purchase"
Event: Contact Tag → Tag Added → "purchased-sprint"
Action: Add Contact Tag → "buyer-sprint"
```

Configure your $297 Sprint product to auto-tag with `purchased-sprint` on payment. The Buyer Workflow checks for the `buyer-sprint` tag and skips Sprint pitch emails (handled by If/Else inside the workflow).

### Trigger 4: Blueprint Purchase

```
Name: "Trigger 4: Blueprint Purchase"
Event: Contact Tag → Tag Added → "purchased-blueprint"
Action: Add Contact Tag → "buyer-blueprint"
```

Configure your $397 Blueprint product to auto-tag with `purchased-blueprint` on payment. Same pattern — the Buyer Workflow skips Blueprint pitch emails when it sees this tag.

### Product Tag Setup (Do This First)

Configure each product in GHL to auto-add its purchase tag:

| Product | Auto-Tag on Purchase |
|---------|---------------------|
| $27 Client Ready | `purchased-27` |
| $17 DM Scripts (bump) | `purchased-bump-dm-scripts` |
| $37 Templates (bump) | `purchased-bump-templates` |
| $67 First $5K Client Playbook (bump) | `purchased-bump-playbook` |
| $297 Sprint | `purchased-sprint` |
| $397 Blueprint | `purchased-blueprint` |
| $47/mo Community | `purchased-community` |

To set this up: Go to **Payments → Products → [Product] → Settings → Tags** and add the corresponding tag.

---

## Part 4: Build Non-Buyer Workflow

Go to **Automation → Workflows → Create Workflow**

Name: `Non-Buyer 30-Day Sequence`

### Workflow Structure:

```
[Start Trigger: Tag Added "non-buyer-sequence"]
    ↓
[Wait: 30 minutes]
    ↓
[If/Else: Has tag "buyer-core"?]
    → Yes: [Remove tag "non-buyer-sequence"] → [End Workflow]
    → No: Continue
    ↓
[Wait: 30 minutes]
    ↓
[Email 1: Soft Abandon]
    ↓
[Wait: 1 day]
    ↓
[If/Else: Has tag "buyer-core"?]
    → Yes: [End Workflow]
    → No: Continue
    ↓
[Email 2: The Real Cost of Waiting]
    ↓
[Wait: 2 days]
    ↓
[If/Else: Has tag "buyer-core"?]
    → Yes: [End Workflow]
    → No: Continue
    ↓
[Email 3: Objection Killer]
    ↓
... continue pattern ...
```

### Full Non-Buyer Workflow Steps:

| Step | Type | Timing | Content |
|------|------|--------|---------|
| 1 | Wait | 1 hour | — |
| 2 | Email | — | Email 1: Soft Abandon |
| 3 | Wait | 1 day | — |
| 4 | If/Else | — | Has tag "buyer-core"? → End |
| 5 | Email | — | Email 2: Real Cost of Waiting |
| 6 | Wait | 2 days | — |
| 7 | If/Else | — | Has tag "buyer-core"? → End |
| 8 | Email | — | Email 3: Objection Killer |
| 9 | Wait | 2 days | — |
| 10 | If/Else | — | Has tag "buyer-core"? → End |
| 11 | Email | — | Email 4: Contrarian Hook |
| 12 | Wait | 2 days | — |
| 13 | If/Else | — | Has tag "buyer-core"? → End |
| 14 | Email | — | Email 5: Social Proof |
| 15 | Wait | 2 days | — |
| 16 | If/Else | — | Has tag "buyer-core"? → End |
| 17 | Email | — | Email 6: Direct Close |
| 18 | Wait | 4 days | — |
| 19 | If/Else | — | Has tag "buyer-core"? → End |
| 20 | Email | — | Email 7: Pivot to Value |
| 21 | Wait | 2 days | — |
| 22 | If/Else | — | Has tag "buyer-core"? → End |
| 23 | Email | — | Email 8: Wrong Wrong Wrong |
| 24 | Wait | 3 days | — |
| 25 | If/Else | — | Has tag "buyer-core"? → End |
| 26 | Email | — | Email 9: The Transformation |
| 27 | Wait | 3 days | — |
| 28 | If/Else | — | Has tag "buyer-core"? → End |
| 29 | Email | — | Email 10: The Calculator |
| 30 | Wait | 4 days | — |
| 31 | If/Else | — | Has tag "buyer-core"? → End |
| 32 | Email | — | Email 11: You Can't Go It Alone |
| 33 | Wait | 4 days | — |
| 34 | If/Else | — | Has tag "buyer-core"? → End |
| 35 | Email | — | Email 12: Last Call |
| 36 | Add Tag | — | "non-buyer-30-day-complete" |
| 37 | Remove Tag | — | "non-buyer-sequence" |
| 38 | End | — | — |

---

## Part 5: Build Buyer Workflow

Go to **Automation → Workflows → Create Workflow**

Name: `Buyer 30-Day Sequence`

### Workflow Structure:

```
[Start Trigger: Tag Added "buyer-sequence"]
    ↓
[Email 1: Welcome + Pattern Interrupt] ← Immediate
    ↓
[Wait: 1 day]
    ↓
[Email 2: Did you do it yet?]
    ↓
[Wait: 2 days]
    ↓
[Email 3: Prompt 5 done?]
    ↓
[Wait: 2 days]
    ↓
[Email 4: The Limitation]
    ↓
[Wait: 3 days]
    ↓
[Email 5: The Pattern]
    ↓
[Wait: 2 days]
    ↓
[If/Else: Has tag "buyer-sprint" OR "buyer-sprint"?]
    → Yes: [Go to Email 10]
    → No: Continue
    ↓
[Email 6: Sprint Intro]
    ↓
... continue pattern ...
```

### Full Buyer Workflow Steps:

| Step | Type | Timing | Content | Skip If |
|------|------|--------|---------|---------|
| 1 | Email | Immediate | Email 1: Welcome | — |
| 2 | Wait | 1 day | — | — |
| 3 | Email | — | Email 2: Did you do it yet? | — |
| 4 | Wait | 2 days | — | — |
| 5 | Email | — | Email 3: Prompt 5 done? | — |
| 6 | Wait | 2 days | — | — |
| 7 | Email | — | Email 4: The Limitation | — |
| 8 | Wait | 3 days | — | — |
| 9 | Email | — | Email 5: The Pattern | — |
| 10 | Wait | 2 days | — | — |
| 11 | If/Else | — | Has "buyer-sprint"? → Step 22 | — |
| 12 | Email | — | Email 6: Sprint Intro | Sprint buyers |
| 13 | Wait | 2 days | — | — |
| 14 | Email | — | Email 7: Two Paths | Sprint buyers |
| 15 | Wait | 2 days | — | — |
| 16 | Email | — | Email 8: Sprint Testimonial | Sprint buyers |
| 17 | Wait | 2 days | — | — |
| 18 | Email | — | Email 9: Last Sprint Pitch | Sprint buyers |
| 19 | Wait | 4 days | — | — |
| 20 | If/Else | — | Has "buyer-blueprint"? → Step 28 | — |
| 21 | Email | — | Email 10: No Time Problem | Blueprint buyers |
| 22 | Wait | 2 days | — | — |
| 23 | Email | — | Email 11: Blueprint vs Sprint | Blueprint buyers |
| 24 | Wait | 2 days | — | — |
| 25 | Email | — | Email 12: Blueprint Close | Blueprint buyers |
| 26 | Wait | 4 days | — | — |
| 27 | Email | — | Email 13: $5K Question | — |
| 28 | Wait | 2 days | — | — |
| 29 | Email | — | Email 14: Long Game | — |
| 30 | Add Tag | — | "buyer-30-day-complete" | — |
| 31 | Remove Tag | — | "buyer-sequence" | — |
| 32 | End | — | — | — |

---

## Part 6: Create Email Templates

Go to **Marketing → Emails → Templates**

For each email in both sequences:

### Email Template Settings:
```
From Name: Michael Scott
From Email: michael@yourdomain.com
Reply-To: michael@yourdomain.com
```

### Template Format:
```
Subject: [Subject from sequence doc]

[Body content - plain text, no fancy HTML]

[Signature]
Michael

PS. [PS content]
```

### Merge Fields to Use:
| Field | GHL Code |
|-------|----------|
| First Name | `{{contact.first_name}}` |
| Sales Page Link | Use static URL or create link trigger |

### Pro Tips:
1. **Keep emails plain text** — no fancy templates, just text
2. **Use line breaks liberally** — matches Michael's voice
3. **Bold key phrases** — use `**text**` in rich text editor
4. **Test on mobile** — most opens are mobile

---

## Part 7: Set Up Link Tracking

For each CTA link in emails:

1. Go to **Marketing → Links → Trigger Links**
2. Create trigger link for each product:

| Link Name | Destination | Action on Click |
|-----------|-------------|-----------------|
| `sales-page-$27` | Sales page URL | Add tag "clicked-sales-page" |
| `sprint-page` | Sprint sales page | Add tag "clicked-sprint" |
| `blueprint-page` | Blueprint sales page | Add tag "clicked-blueprint" |

Use these trigger links in your emails instead of raw URLs.

---

## Part 8: Cold Lead Detection

Create a separate workflow for engagement tracking:

Name: `Cold Lead Detection`

```
[Trigger: Email Opened]
    ↓
[Update Custom Field: last_email_opened = Today]
    ↓
[Remove Tag: "cold-lead"]
    ↓
[Add Tag: "engaged-non-buyer"] (if has tag "non-buyer-sequence")
```

Then create a scheduled workflow:

Name: `Mark Cold Leads`

```
[Trigger: Schedule - Daily at 9am]
    ↓
[Filter: last_email_opened < 14 days ago]
    ↓
[Filter: Has tag "non-buyer-sequence"]
    ↓
[Add Tag: "cold-lead"]
```

---

## Part 9: Reply Detection

Create workflow for reply tracking:

Name: `Reply Handler`

```
[Trigger: Email Reply Received]
    ↓
[If/Else: Body contains "BUILD"]
    → Yes: Add tag "backend-interested", Create Task for Michael
    → No: Continue
    ↓
[If/Else: Body contains "LAUNCH" or "24HR"]
    → Yes: Add tag "interested-launch-kit"
    → No: Continue
    ↓
[Create Task: "Review reply from {{contact.name}}"]
```

---

## Part 10: Testing Checklist

Before going live:

### Workflow Tests:
- [ ] Add yourself as test contact
- [ ] Trigger non-buyer sequence
- [ ] Verify Email 1 sends after 1 hour
- [ ] Simulate purchase → verify switches to buyer sequence
- [ ] Verify old workflow stops when new one starts

### Email Tests:
- [ ] Send test of each email to yourself
- [ ] Check formatting on mobile
- [ ] Verify all links work
- [ ] Check merge fields populate correctly
- [ ] Verify from name/email correct

### Timing Tests:
- [ ] Verify wait steps are correct duration
- [ ] Check emails don't send at 3am (set business hours)

### Segmentation Tests:
- [ ] Buy Sprint → verify skips emails 6-9
- [ ] Buy Blueprint → verify skips emails 6-12
- [ ] Buy $27 during non-buyer sequence → verify switches

---

## Part 11: Business Hours Setting

Go to **Settings → Business Profile → Business Hours**

Set email sending hours:
```
Monday-Friday: 8am - 6pm
Saturday: 9am - 12pm
Sunday: Off
```

This prevents emails from sending at odd hours.

---

## Part 12: Launch Sequence

### Day 1: Non-Buyer Sequence
1. Publish workflow
2. Enable trigger
3. Start with small test group (10-20 leads)
4. Monitor deliverability and opens for 48 hours

### Day 3: Buyer Sequence
1. Publish workflow
2. Enable trigger
3. Make a test purchase to verify full flow
4. Monitor first 3 emails

### Day 7: Full Launch
1. Enable for all new leads/buyers
2. Set up weekly reporting
3. Monitor metrics against targets

---

## Part 13: Metrics Dashboard

Create a GHL dashboard or use the reporting tab to track:

### Non-Buyer Sequence
| Metric | Where to Find | Target |
|--------|---------------|--------|
| Open Rate (Emails 1-6) | Email Stats | 40%+ |
| Open Rate (Emails 7-12) | Email Stats | 25%+ |
| Click Rate | Email Stats | 3-5% |
| Conversion to $27 | Tag count: buyer-core | 3-5% |
| Unsubscribe Rate | Email Stats | <1% |

### Buyer Sequence
| Metric | Where to Find | Target |
|--------|---------------|--------|
| Open Rate (Phase 1) | Email Stats | 60%+ |
| Sprint Conversion | Tag count: buyer-sprint | 5-10% |
| Blueprint Conversion | Tag count: buyer-blueprint | 2-5% |
| Backend Interest | Tag count: backend-interested | 1-2% |

---

## Quick Reference: Workflow Names

| Workflow | Purpose |
|----------|---------|
| `Non-Buyer 30-Day Sequence` | Main non-buyer nurture |
| `Buyer 30-Day Sequence` | Main buyer ascension |
| `Cold Lead Detection` | Track engagement |
| `Mark Cold Leads` | Daily cold lead tagging |
| `Reply Handler` | Process email replies |

---

## Troubleshooting

### Emails not sending
1. Check domain verification in Settings → Email
2. Verify workflow is published AND trigger is active
3. Check contact has valid email
4. Review workflow history for errors

### Contact in wrong sequence
1. Manually remove tags
2. Stop current workflow for contact
3. Add correct tag to trigger right workflow

### Duplicate emails
1. Check for multiple active triggers
2. Verify contact isn't in workflow twice
3. Use "only allow contact in workflow once" setting

### Links not tracking
1. Verify using Trigger Links, not raw URLs
2. Check link is active in Marketing → Links
3. Test link in incognito browser

---

## Files Reference

Email content is in your repo:
- `outputs/email-sequence-non-buyers.md` — Non-buyer emails
- `outputs/email-sequence-buyers.md` — Buyer emails

Copy/paste directly from these files into GHL templates.
