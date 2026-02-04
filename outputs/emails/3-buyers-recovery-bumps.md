---
type: resource
status: active
date: 2026-02-04
module: 2.6.3
format: Google Doc
---

# Install Offer Recovery Sequence

**3 emails to recover missed order bumps**

---

## Overview

When someone buys the $27 but skips the order bumps, this sequence re-pitches them over the next week.

**Trigger:** Purchased $27, did NOT purchase Bump 1 (DM Scripts), Bump 2 (Templates), or Bump 3 (Traffic Kit)
**Timing:** Days 2, 4, and 6 after purchase
**Send Time:** 2:00 PM (Welcome sequence sends at 8:00 AM — avoids stacking)
**Goal:** Recover 10-20% of missed bump revenue

---

## Email 1: Day 2 — "One thing I forgot to mention"

**Subject:** One thing I forgot to mention...

**Body:**

Hey [NAME],

Quick follow-up on your Client Ready purchase.

There was something I didn't mention clearly on the checkout page, and I want to fix that.

The offer extraction is step one. But the fastest path to your first client? **Starting conversations.**

That's why I created the Quick Win DM Scripts — 5 copy-paste messages for warm outreach:

1. **The Reconnection** — Reach out to someone you haven't talked to in months
2. **The Value Drop** — Share something helpful without pitching
3. **The Soft Pitch** — Introduce your offer without being salesy
4. **The "I'm Building Something"** — Get feedback that turns into sales
5. **The Follow-Up** — Re-engage someone who went quiet

These aren't cold DM templates. They're for people who already know you.

Originally $97. Yours for $17: [LINK]

Use them today. Have a conversation by tonight.

Michael

---

## Email 2: Day 4 — "The blank page problem"

**Subject:** The blank page problem

**Body:**

Hey [NAME],

How's the extraction going?

If you're staring at a blank landing page wondering what to write... you're not alone.

That's the hardest part for most people. Not the strategy — the execution.

Which is why I put together the Plug & Play Templates:

- **Offer document template** (with filled example)
- **Landing page swipe files** (proven layouts)
- **30-day email sequence** (pre-written, tested)
- **Messaging maps and client profiles**
- **Copy-paste headlines and hooks**

You don't start from scratch. You start from something that works and make it yours.

Originally $197. Yours for $37: [LINK]

Skip the blank page.

Michael

---

## Email 3: Day 6 — "Before you move on"

**Subject:** Before you move on...

**Body:**

Hey [NAME],

Last email about the add-ons. Promise.

You've got the Client Ready system. You're doing the extraction. Good.

But before you move to the next phase, quick inventory:

**Do you have a way to start conversations?**
→ If not: Quick Win DM Scripts ($17) [LINK]

**Do you have templates so you're not starting from scratch?**
→ If not: Plug & Play Templates ($37) [LINK]

**Do you know how to get your first 10 buyers?**
→ If not: Traffic & Launch Kit ($67) [LINK]

If you have all three, ignore this. You're set.

If you're missing one, grab it now before you forget. These prices won't last forever.

That's it. Back to regular emails tomorrow.

Michael

---

## Automation Logic

```
IF purchased $27
AND NOT purchased any bump
THEN send all 3 emails

IF purchased $27
AND purchased some bumps but not others
THEN send emails pitching only the missed bumps

IF purchased all bumps
THEN skip this sequence entirely
```

---

## Expected Results

| Metric | Target |
|--------|--------|
| Open rate | 35-45% |
| Click rate | 3-5% |
| Recovery rate | 10-20% of missed bumps |
| Revenue per 100 buyers | $50-100 additional |
