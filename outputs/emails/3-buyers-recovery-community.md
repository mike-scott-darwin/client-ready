---
type: resource
status: active
date: 2026-03-07
module: 2.6.3
format: Google Doc
updated_from: Community downsell ($47/mo, $1 trial) → Community direct sign-up ($47/mo)
---

# Community Recovery Sequence

**1 email to recover missed Community sign-up**

---

## Overview

When someone buys the $27 but doesn't have a community trial (didn't buy DFY), this email offers direct community access.

**Trigger:** Purchased $27, did NOT purchase DFY ($197) or DFY Lite ($97) — meaning no community trial bundled
**Timing:** Day 8 after purchase
**Send Time:** 2:00 PM (Welcome sequence sends at 8:00 AM — avoids stacking)
**Goal:** Convert 3-5% to community members

---

## Why Day 8?

- Days 3, 5, 7 already pitched DFY (OTO Recovery)
- Day 8 = they've seen the DFY option and said no
- This offers the community standalone: "Not ready for DFY? At least don't build alone"

---

## Email 1: Day 8 — "The part nobody warns you about"

**Subject:** The part nobody warns you about

---

Hey [NAME],

Over the past few days, I've mentioned the DFY Offer Build.

Maybe you thought: "I'll do it myself."

Great. You can. The system works.

But here's the part nobody warns you about:

Building alone is brutal.

You finish your offer doc. Is it good? Who knows. There's nobody to ask.

You write landing page copy. Does it convert? You won't find out for weeks.

You run your first ad. Nothing happens. Now what?

**The Client Ready Community exists for this exact moment.**

$47/month. Cancel anytime.

What you get:

- Weekly hot seat calls with me (bring your offer, your copy, your questions — get real-time feedback)
- Sprint curriculum (Extract → Validate → Build → Launch — self-paced, always available)
- DFY templates of the month (tested assets you can use immediately)
- DM me directly for quick questions
- A room full of coaches at every stage — some starting, some already generating clients

This isn't a course. It's the room where people build.

Month-to-month. No contracts. Stay as long as it's useful. Leave when you've outgrown it (or upgraded to working with me 1:1).

If building alone is getting old: [SKOOL LINK]

If you're good solo: respect. Keep going.

Michael

P.S. — The community includes everything that used to be in the $297 Sprint — the weekly calls, the curriculum, the accountability. It's all there. You just pay monthly instead of up front.

---

## Automation Logic

```
IF purchased $27
AND NOT purchased DFY ($197)
AND NOT purchased DFY Lite ($97)
AND NOT has tag "purchased-community"
THEN send this email on Day 8 at 2:00 PM

IF purchased DFY or DFY Lite
THEN skip this sequence entirely (they have a community trial)

IF already a community member
THEN skip this sequence
```

---

## Expected Results

| Metric | Target |
|--------|--------|
| Open rate | 30-40% |
| Click rate | 3-5% |
| Community conversion | 3-5% of eligible |
| Revenue per 100 buyers | $25-40 additional (recurring) |
| Month 1 → Month 2 retention | 70%+ |

---

## Integration with Other Sequences

| Day | Time | Sequence | Email |
|-----|------|----------|-------|
| 8 | 8:00 AM | Welcome | FAQ / Objection |
| 8 | 2:00 PM | **Community Recovery** | **This email** |

No conflict. Morning = value. Afternoon = offer.

---

## Voice Notes

- Acknowledge they said "no" to DFY — don't pretend they didn't
- Position as "the room where people build" — not a consolation prize
- $47/mo is justified: weekly calls, curriculum, templates, DM access
- Month-to-month framing: "cancel anytime, no contracts"
- Mention that Sprint content is now in the community
- No pressure, no fake urgency
