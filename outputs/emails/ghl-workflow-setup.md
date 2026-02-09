---
type: output
status: active
date: 2026-02-04
purpose: GHL workflow configuration for email sequences
---

# GHL Workflow Setup

Complete GoHighLevel workflow configuration for the Client Ready email backend.

---

## Overview

You'll create **6 workflows** in GHL:

| # | Workflow Name | Trigger | Emails |
|---|---------------|---------|--------|
| 1 | Non-Buyer Nurture | Started checkout, no purchase (30 min) | 12 emails / 30 days |
| 2 | Buyer Welcome | Purchased $27 | 10 emails / 10 days |
| 3 | Bump Recovery | Purchased $27, no bumps | 3 emails (Days 2,4,6) |
| 4 | OTO Recovery | Purchased $27, no Sprint/Blueprint | 3 emails (Days 3,5,7) |
| 5 | Community Recovery | Purchased $27, no upsells at all | 1 email (Day 8) |
| 6 | Daily Broadcast | Day 11+ (manual or scheduled) | Ongoing |

---

## Tags Required

Create these tags in GHL first:

**Purchase Tags:**
- `purchased-27` — Bought front-end
- `purchased-bump-dm-scripts` — Bought $17 DM Scripts
- `purchased-bump-templates` — Bought $37 Templates
- `purchased-bump-traffic` — Bought $67 Traffic Kit
- `purchased-sprint` — Bought $297 Sprint
- `purchased-blueprint` — Bought $397 Blueprint
- `purchased-community` — Bought $47/mo Community

**Sequence Tags:**
- `in-nonbuyer-sequence` — Currently in non-buyer nurture
- `in-welcome-sequence` — Currently in welcome sequence
- `completed-welcome` — Finished welcome, ready for broadcast
- `in-daily-broadcast` — Receiving daily emails

---

## How Triggers and Workflows Connect

GHL has two automation systems:

- **Triggers** (Settings → Automations → Triggers) — Simple tag routing only. Can add/remove tags. **Cannot** start workflows, stop workflows, skip to steps, or wait.
- **Workflows** (Automations → Workflows) — Full automation. Each workflow has its own built-in trigger (entry event) plus steps: wait, if/else, send email, add/remove tags, etc.

**The pattern:** Tags are the glue. Triggers add tags based on events → Workflows listen for those tags and run sequences. Workflows also check for purchase tags before every email, so they stop themselves when someone buys.

### Tag Source Setup

Before building workflows, configure these tag sources:

**2-step order form:** In your checkout page form settings, add tag `lead` on Step 1 submission. This captures anyone who enters their email, even if they don't pay.

**Products:** Configure each product to auto-tag on purchase:

| Product | Auto-Tag on Purchase |
|---------|---------------------|
| $27 Client Ready | `purchased-27` |
| $17 DM Scripts (bump) | `purchased-bump-dm-scripts` |
| $37 Templates (bump) | `purchased-bump-templates` |
| $67 Traffic Kit (bump) | `purchased-bump-traffic` |
| $297 Sprint | `purchased-sprint` |
| $397 Blueprint | `purchased-blueprint` |
| $47/mo Community | `purchased-community` |

Set these in **Payments → Products → [Product] → Settings → Tags**.

### GHL Triggers (Simple Tag Routing)

Create these in **Settings → Automations → Triggers**:

| Trigger Name | Event | Action |
|-------------|-------|--------|
| Non-Buyer Start | Tag Added → `lead` | Add tag `in-nonbuyer-sequence` |
| Buyer Start | Tag Added → `purchased-27` | Add tag `in-welcome-sequence`, Remove tag `in-nonbuyer-sequence`, Remove tag `lead` |
| Sprint Purchase | Tag Added → `purchased-sprint` | (optional — workflow checks this tag directly) |
| Blueprint Purchase | Tag Added → `purchased-blueprint` | (optional — workflow checks this tag directly) |

---

## Workflow 1: Non-Buyer Nurture (Abandoned Checkout)

**Who this is for:** Someone who started checkout but didn't complete the purchase. NOT lead magnet downloaders.

**Built-in workflow trigger:** Tag Added → `in-nonbuyer-sequence`

The workflow handles the 30-minute wait and purchase check internally — triggers can't do this.

```
WORKFLOW TRIGGER: Tag Added → "in-nonbuyer-sequence"
    ↓
WAIT: 30 minutes
    ↓
IF/ELSE: Contact has tag "purchased-27"?
    ├── YES → Remove tag "in-nonbuyer-sequence" → End workflow
    └── NO → Continue (abandoned checkout)
            ↓
        EMAIL 1: "You left something behind"
            ↓
        WAIT: 1 day
            ↓
        IF/ELSE: Has tag "purchased-27"?
            ├── YES → Remove tag "in-nonbuyer-sequence" → End
            └── NO → EMAIL 2: "What's an unclear offer costing you?"
            ↓
        [Continue pattern for all 12 emails...]
            ↓
        WAIT: Until Day 30
            ↓
        EMAIL 12: "Closing the loop on this"
            ↓
        REMOVE TAG: "in-nonbuyer-sequence"
            ↓
        END
```

**Key Settings:**
- Send time: 9:00 AM local
- Check for purchase before EVERY email
- If they buy at any point → workflow exits via If/Else check

---

## Workflow 2: Buyer Welcome (10-Day)

**Trigger:** Tag added: `purchased-27`

```
TRIGGER: Tag Added "purchased-27"
    ↓
REMOVE TAG: "in-nonbuyer-sequence" (if exists)
    ↓
ADD TAG: "in-welcome-sequence"
    ↓
EMAIL 1: "You're in — here's your first win"
    (Send immediately or next 8 AM)
    ↓
WAIT: 1 day (until 8:00 AM)
    ↓
EMAIL 2: "Why I do this (honest answer)"
    ↓
WAIT: 1 day (until 8:00 AM)
    ↓
EMAIL 3: "She validated in 3 days"
    ↓
[Continue for all 10 emails...]
    ↓
WAIT: 1 day (until 8:00 AM)
    ↓
EMAIL 10: "Come hang out"
    ↓
REMOVE TAG: "in-welcome-sequence"
    ↓
ADD TAG: "completed-welcome"
    ↓
ADD TAG: "in-daily-broadcast"
    ↓
END
```

**Key Settings:**
- Send time: 8:00 AM local (morning = value)
- NO purchase checks needed (they're already buyers)
- After Day 10 → add to broadcast list

---

## Workflow 3: Bump Recovery

**Trigger:** Tag added: `purchased-27`
**Condition:** Does NOT have any bump tags

```
TRIGGER: Tag Added "purchased-27"
    ↓
WAIT: 5 minutes (let other tags settle)
    ↓
IF/ELSE: Has ANY of these tags?
    - "purchased-bump-dm-scripts"
    - "purchased-bump-templates"
    - "purchased-bump-traffic"
    ├── YES (has ALL 3) → End workflow
    └── NO or PARTIAL → Continue
            ↓
        WAIT: Until Day 2, 2:00 PM
            ↓
        IF/ELSE: Missing "purchased-bump-dm-scripts"?
            ├── YES → EMAIL: "One thing I forgot to mention" (DM Scripts pitch)
            └── NO → Skip
            ↓
        WAIT: Until Day 4, 2:00 PM
            ↓
        IF/ELSE: Missing "purchased-bump-templates"?
            ├── YES → EMAIL: "The blank page problem" (Templates pitch)
            └── NO → Skip
            ↓
        WAIT: Until Day 6, 2:00 PM
            ↓
        IF/ELSE: Missing any bumps?
            ├── YES → EMAIL: "Before you move on" (Stack pitch)
            └── NO → Skip
            ↓
        END
```

**Key Settings:**
- Send time: 2:00 PM local (afternoon = offers)
- Check which bumps are missing before each email
- Only pitch what they DON'T have

---

## Workflow 4: OTO Recovery

**Trigger:** Tag added: `purchased-27`
**Condition:** Does NOT have Sprint or Blueprint tags

```
TRIGGER: Tag Added "purchased-27"
    ↓
WAIT: 5 minutes
    ↓
IF/ELSE: Has tag "purchased-sprint" OR "purchased-blueprint"?
    ├── YES → End workflow
    └── NO → Continue
            ↓
        WAIT: Until Day 3, 2:00 PM
            ↓
        IF/ELSE: Has tag "purchased-sprint"?
            ├── YES → Skip
            └── NO → EMAIL: "Most people do this alone"
            ↓
        WAIT: Until Day 5, 2:00 PM
            ↓
        IF/ELSE: Has tag "purchased-sprint"?
            ├── YES → Skip
            └── NO → EMAIL: "From 'maybe someday' to $4K in 28 days"
            ↓
        WAIT: Until Day 7, 2:00 PM
            ↓
        IF/ELSE: Has tag "purchased-blueprint"?
            ├── YES → Skip
            └── NO → EMAIL: "What if I just built it for you?"
            ↓
        END
```

**Key Settings:**
- Send time: 2:00 PM local
- Check for purchases before each email
- Day 7 email pivots to Blueprint pitch

---

## Workflow 5: Community Recovery

**Trigger:** Tag added: `purchased-27`
**Condition:** Does NOT have Sprint, Blueprint, or Community tags

```
TRIGGER: Tag Added "purchased-27"
    ↓
WAIT: Until Day 8, 2:00 PM
    ↓
IF/ELSE: Has ANY of these tags?
    - "purchased-sprint"
    - "purchased-blueprint"
    - "purchased-community"
    ├── YES → End workflow (they upgraded)
    └── NO → Continue
            ↓
        EMAIL: "Not ready yet? (That's okay)"
            ↓
        END
```

**Key Settings:**
- Send time: 2:00 PM local (Day 8)
- Only fires if they said NO to everything
- This is the downsell — $1 trial to Community

---

## Workflow 6: Daily Broadcast

**Two options:**

### Option A: Manual Broadcast
- Create a saved segment: Tag = `in-daily-broadcast`
- Write daily email
- Send to segment manually each day

### Option B: Scheduled Campaign
- Create 7 emails (Mon-Sun rotation)
- Set up recurring campaign to segment
- Pulls from `4-buyers-daily-broadcast.md` templates

**Segment Filter:**
```
Tag: "in-daily-broadcast" = TRUE
AND
Tag: "unsubscribed" = FALSE
```

---

## Purchase Tag Automation

Set up these automations in your checkout/payment processor:

**Stripe → GHL (via Zapier or native integration):**

| Product Purchased | Add Tag |
|-------------------|---------|
| $27 Front-End | `purchased-27` |
| $17 DM Scripts | `purchased-bump-dm-scripts` |
| $37 Templates | `purchased-bump-templates` |
| $67 Traffic Kit | `purchased-bump-traffic` |
| $297 Sprint | `purchased-sprint` |
| $397 Blueprint | `purchased-blueprint` |
| $47/mo Community | `purchased-community` |

---

## Timing Summary

| Sequence | Send Time | Days |
|----------|-----------|------|
| Non-Buyer | 9:00 AM | 1-30 |
| Welcome | 8:00 AM | 1-10 |
| Bump Recovery | 2:00 PM | 2,4,6 |
| OTO Recovery | 2:00 PM | 3,5,7 |
| Community Recovery | 2:00 PM | 8 |
| Daily Broadcast | 8:00 AM | 11+ |

**Max emails per day for buyers (Days 1-10):**
- 8:00 AM: 1 welcome email
- 2:00 PM: 0-1 recovery email
- Total: 1-2 emails max

---

## Testing Checklist

Before going live:

- [ ] Create all tags in GHL
- [ ] Set up Stripe → GHL tag automation
- [ ] Build Workflow 1 (Non-Buyer)
- [ ] Build Workflow 2 (Welcome)
- [ ] Build Workflow 3 (Bump Recovery)
- [ ] Build Workflow 4 (OTO Recovery)
- [ ] Build Workflow 5 (Community Recovery)
- [ ] Set up Daily Broadcast segment
- [ ] Test with a test contact through full journey
- [ ] Verify tags add/remove correctly
- [ ] Verify emails send at correct times
- [ ] Verify exit conditions work (purchase → exit)

---

## Troubleshooting

**Contact getting duplicate emails:**
- Check they're not in multiple workflows incorrectly
- Verify tag removal is working on workflow exit

**Contact not receiving emails:**
- Check tag was added correctly
- Check workflow is active
- Check contact is not unsubscribed

**Timing is off:**
- Verify timezone settings in GHL
- Check "Wait until specific time" vs "Wait duration"

---

## See Also

- [README.md](README.md) — Email sequence overview
- [1-non-buyers-30-day.md](1-non-buyers-30-day.md) — Full non-buyer copy
- [2-buyers-welcome-10-day.md](2-buyers-welcome-10-day.md) — Full welcome copy
- [3-buyers-recovery-*.md](.) — Recovery sequence copy
- [4-buyers-daily-broadcast.md](4-buyers-daily-broadcast.md) — Daily templates
