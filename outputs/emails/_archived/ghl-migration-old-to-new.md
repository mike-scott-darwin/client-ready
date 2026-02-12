---
type: output
status: active
date: 2026-02-10
purpose: Migration guide — old GHL setup (live) vs new GHL setup
---

# GHL Migration: Old Setup → New Setup

Your live GHL uses tags and workflows from the **old guide** (`ghl-email-setup-guide.md`, Jan 25). The **new guide** (`ghl-workflow-setup.md`, Feb 10) restructured everything. This document maps what changed so you can update your live GHL without breaking anything.

---

## Summary of Changes

| Area | Old Guide (Live in GHL) | New Guide |
|------|------------------------|-----------|
| **Workflows** | 2 main + 3 helper | 6 workflows (separated concerns) |
| **Buyer sequence** | 1 monolith (14 emails, 30 days) | Welcome (10 emails) + 3 Recovery sequences + Daily Broadcast |
| **Upsell logic** | Inside buyer workflow (If/Else skips) | Separate parallel recovery workflows |
| **Daily broadcast** | Not included | Workflow 6 with 7 templates |
| **Tag naming** | `buyer-core`, `buyer-sprint`, `buyer-sequence` | `purchased-27`, `purchased-sprint`, `in-welcome-sequence` |
| **Triggers** | 4 triggers | 2 triggers (simpler) |
| **Send times** | Business hours (8am-6pm) | Fixed: Welcome 8AM, Recovery 2PM, Non-buyer 9AM |

---

## TAG CHANGES

### Tags You Already Have (Keep These)

These tags exist in your live GHL and are used in BOTH versions:

| Old Tag | Still Used? | Notes |
|---------|-------------|-------|
| `lead` | YES | Same in both versions |
| `purchased-27` | YES | Same in both |
| `purchased-bump-dm-scripts` | YES | Same in both |
| `purchased-bump-templates` | YES | Same in both |
| `purchased-bump-playbook` | YES | Same in both |
| `purchased-sprint` | YES | Same in both |
| `purchased-blueprint` | YES | Same in both |
| `purchased-community` | YES | Same in both |

### Tags to RENAME (Old → New)

These tags changed names. In GHL, you can't rename tags — you need to create the new one and update workflows to use it.

| Old Tag (Live) | New Tag | Why Changed |
|----------------|---------|-------------|
| `non-buyer-sequence` | `in-nonbuyer-sequence` | Clearer naming — "in-" prefix shows active state |
| `buyer-sequence` | `in-welcome-sequence` | Sequence renamed from "buyer 30-day" to "welcome 10-day" |
| `buyer-30-day-complete` | `completed-welcome` | Sequence is now 10 days, not 30 |
| `non-buyer-30-day-complete` | *(removed)* | Non-buyer cleanup now just removes `in-nonbuyer-sequence` |

### Tags to ADD (New Only)

| New Tag | Purpose |
|---------|---------|
| `in-daily-broadcast` | Marks contacts ready for daily emails (Day 11+) |
| `completed-welcome` | Finished the 10-day welcome sequence |

### Tags to RETIRE (Old Only)

These exist in your live GHL but are NOT in the new system. Don't delete yet — retire after migration.

| Old Tag | Why Removed |
|---------|-------------|
| `buyer-core` | Redundant with `purchased-27`. New system uses `purchased-27` directly. |
| `buyer-sprint` | Redundant with `purchased-sprint`. New system checks purchase tag directly. |
| `buyer-blueprint` | Redundant with `purchased-blueprint`. Same reason. |
| `buyer-30-day-complete` | Replaced by `completed-welcome` + `in-daily-broadcast` |
| `non-buyer-30-day-complete` | Removed — not needed |
| `engaged-non-buyer` | Nice-to-have engagement tracking — not in new core system. Can re-add later. |
| `cold-lead` | Same — engagement tracking, not core. Can re-add later. |
| `backend-interested` | Reply detection — not in new core system. Can re-add later as enhancement. |
| `interested-launch-kit` | Reply detection — same. |
| `clicked-sales-page` | Link tracking — not in new core. Can re-add. |
| `clicked-sprint` | Link tracking — same. |
| `clicked-blueprint` | Link tracking — same. |

---

## TRIGGER CHANGES

### Old Triggers (4)

| # | Old Trigger | Event | Actions |
|---|-------------|-------|---------|
| 1 | Non-Buyer Start | Tag Added → `lead` | Add `non-buyer-sequence` |
| 2 | Buyer Sequence Start | Tag Added → `purchased-27` | Add `buyer-core`, `buyer-sequence`, Remove `non-buyer-sequence`, `lead` |
| 3 | Sprint Purchase | Tag Added → `purchased-sprint` | Add `buyer-sprint` |
| 4 | Blueprint Purchase | Tag Added → `purchased-blueprint` | Add `buyer-blueprint` |

### New Triggers (2)

| # | New Trigger | Event | Actions |
|---|-------------|-------|---------|
| 1 | Non-Buyer Start | Tag Added → `lead` | Add `in-nonbuyer-sequence` |
| 2 | Buyer Start | Tag Added → `purchased-27` | Add `in-welcome-sequence`, Remove `in-nonbuyer-sequence`, Remove `lead` |

### What Changed

- **Triggers 3 and 4 removed.** The new system doesn't need `buyer-sprint` or `buyer-blueprint` routing tags. Recovery workflows check `purchased-sprint` and `purchased-blueprint` directly via IF/ELSE steps.
- **Trigger 2 simplified.** No more `buyer-core` tag. Just adds `in-welcome-sequence` and cleans up non-buyer tags.
- **Trigger 1 tag renamed.** `non-buyer-sequence` → `in-nonbuyer-sequence`.

---

## WORKFLOW CHANGES

### Old: 2 Main Workflows + 3 Helpers

| Old Workflow | Emails | Duration |
|-------------|--------|----------|
| Non-Buyer 30-Day Sequence | 12 | 30 days |
| Buyer 30-Day Sequence | 14 (monolith) | 30 days |
| Cold Lead Detection | — | Ongoing |
| Mark Cold Leads | — | Daily |
| Reply Handler | — | Ongoing |

### New: 6 Workflows

| New Workflow | Emails | Duration |
|-------------|--------|----------|
| Non-Buyer Nurture | 12 | 30 days |
| Buyer Welcome (10-Day) | 10 | 10 days |
| Bump Recovery | 3 | Days 2, 4, 6 |
| OTO Recovery | 3 | Days 3, 5, 7 |
| Community Recovery | 1 | Day 8 |
| Daily Broadcast | 7 templates | Day 11+ ongoing |

### The Big Structural Change: Buyer Sequence Split

**Old:** One 14-email, 30-day buyer workflow handled everything — welcome, bump pitches, Sprint pitches, Blueprint pitches, backend seeds. Used IF/ELSE to skip emails if they'd already bought those products.

**New:** Separated into concerns:
- **Welcome (10 emails, 8AM)** — Pure relationship. NO pitches. Just value, stories, quick wins.
- **Bump Recovery (3 emails, 2PM)** — Only pitches missed bumps. Smart-skips per bump.
- **OTO Recovery (3 emails, 2PM)** — Sprint on Days 3/5, Blueprint on Day 7.
- **Community Recovery (1 email, 2PM)** — Downsell for people who said no to everything.
- **Daily Broadcast (Day 11+)** — Ongoing story + rotating offers.

**Why this is better:**
1. Welcome builds relationship without pitch fatigue
2. Recovery sequences only pitch what's missing (smarter)
3. Max 2 emails/day (morning value, afternoon offers)
4. Daily broadcast creates compound advantage long-term
5. Each sequence is smaller and easier to edit/test

### Non-Buyer Workflow: Mostly the Same

| Difference | Old | New |
|------------|-----|-----|
| Trigger tag | `non-buyer-sequence` | `in-nonbuyer-sequence` |
| Purchase check tag | `buyer-core` | `purchased-27` |
| Initial wait | 30 min + 30 min (1 hour total) | 30 minutes |
| End tag | Add `non-buyer-30-day-complete`, Remove `non-buyer-sequence` | Just remove `in-nonbuyer-sequence` |
| Email content | Same 12 emails | Same 12 emails |
| Send time | Business hours | 9:00 AM fixed |

---

## FEATURES REMOVED (From Old, Not in New)

These were in the old guide but are NOT in the new core system. They're nice-to-haves that can be re-added after the core 6 workflows are running:

| Old Feature | What It Did | Re-Add Later? |
|-------------|-------------|---------------|
| Custom Fields (purchase_date, etc.) | Tracked dates | Optional — useful for reporting |
| Cold Lead Detection workflow | Tagged disengaged contacts | Yes — after core is stable |
| Mark Cold Leads (daily schedule) | Auto-tagged cold leads | Yes — same |
| Reply Handler workflow | Detected "BUILD" / "LAUNCH" replies | Yes — especially for $5K backend |
| Link Tracking tags | Tracked which links were clicked | Yes — useful for optimization |
| Business Hours sending | Restricted send to 8am-6pm | New system uses fixed times instead |

---

## FEATURES ADDED (New Only)

| New Feature | What It Does |
|-------------|-------------|
| Separated recovery sequences | 3 parallel workflows instead of 1 monolith |
| Fixed send times (8AM / 2PM / 9AM) | Predictable, avoids email stacking |
| Community Recovery (Day 8) | Downsell for people who declined all upsells |
| Daily Broadcast system | 7-template weekly rotation for Day 11+ buyers |
| HTML file references | Maps every email to its exact HTML file |
| Complete day-by-day journey tables | Shows exactly what each contact type receives |
| 4-path testing checklist | Non-buyer, buyer no bumps, buyer with bumps, mid-sequence purchase |

---

## MIGRATION STEPS (If You Want to Update Live GHL)

### Option A: Clean Rebuild (Recommended)

If you haven't sent many emails yet:

1. **Pause** all existing workflows (don't delete yet)
2. **Create** new tags: `in-nonbuyer-sequence`, `in-welcome-sequence`, `completed-welcome`, `in-daily-broadcast`
3. **Build** all 6 new workflows per the new guide
4. **Update** Trigger 1 to add `in-nonbuyer-sequence` instead of `non-buyer-sequence`
5. **Update** Trigger 2 to add `in-welcome-sequence` instead of `buyer-core` + `buyer-sequence`
6. **Delete** Triggers 3 and 4 (no longer needed)
7. **Test** all 4 paths
8. **Activate** new workflows
9. **Deactivate** old workflows
10. After 30 days: delete old workflows and retire old tags

### Option B: Gradual Migration

If you have contacts already in sequences:

1. Let existing contacts finish their current workflows
2. Build new workflows in parallel (inactive)
3. Update triggers to point to new workflows
4. New contacts enter new system; old contacts finish old system
5. After 30 days: deactivate old workflows

---

## Quick Reference: Tag Mapping

For updating workflows and triggers, here's the find-and-replace:

| Find (Old) | Replace With (New) |
|------------|-------------------|
| `non-buyer-sequence` | `in-nonbuyer-sequence` |
| `buyer-core` | `purchased-27` |
| `buyer-sequence` | `in-welcome-sequence` |
| `buyer-sprint` | `purchased-sprint` |
| `buyer-blueprint` | `purchased-blueprint` |
| `buyer-30-day-complete` | `completed-welcome` |
| `non-buyer-30-day-complete` | *(remove — not needed)* |
