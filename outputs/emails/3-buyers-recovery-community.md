---
type: resource
status: active
date: 2026-02-04
module: 2.6.3
format: Google Doc
---

# Community Recovery Sequence

**1 email to recover missed OTO 3 (Community downsell)**

---

## Overview

When someone buys the $47 but says "no" to both Sprint and Blueprint, this email offers the Community as a lower-commitment option.

**Trigger:** Purchased $47, did NOT purchase Sprint ($297) OR Blueprint ($397)
**Timing:** Day 8 after purchase
**Send Time:** 2:00 PM (Welcome sequence sends at 8:00 AM — avoids stacking)
**Goal:** Convert 5-10% of "no" buyers to recurring community members

---

## Why Day 8?

- Days 3, 5, 7 already pitched Sprint and Blueprint (OTO Recovery)
- Day 8 = they've seen the higher-ticket options and said no
- This is the logical downsell: "not ready for that? Here's something smaller"

---

## Email 1: Day 8 — "Not ready for the Sprint? That's okay."

**Subject:** Not ready yet? (That's okay)

---

Hey [NAME],

Over the past few days, I've told you about the Sprint ($297) and the Blueprint ($397).

Maybe you thought: "Not right now."

That's fine. Seriously.

Those are bigger commitments. You might not be there yet. You might want to work through the $47 system first and see results before investing more.

I get it.

But here's the thing:

Building alone is hard.

Not because the information is missing — you have that. Because it's lonely. You second-guess yourself. You wonder if you're on the right track. There's no one to ask.

That's why I built the Client Ready Community.

**$47/month. First month is $1.**

What you get:

- Private Skool community with other coaches building their offers
- Weekly group hot seat calls with me
- DM me directly for quick questions
- See what's working for others in real-time
- Resource library (templates, swipes, frameworks)

No 4-week commitment. No custom blueprint deliverables. Just a place to not build alone.

If you said "no" to Sprint and Blueprint but still want support — this is for you.

Try it for $1: https://www.skool.com/high-ticket-playbook-9467/about

Cancel anytime. No hard feelings.

Michael

P.S. — This isn't a replacement for Sprint or Blueprint. It's for people who want support while they figure things out at their own pace. If you want accountability + guaranteed launch, Sprint is still the move. If you want me to create your complete funnel strategy, Blueprint is there. But if you just want a community and occasional access to me — this is it.

---

## Automation Logic

```
IF purchased $47
AND NOT purchased Sprint ($297)
AND NOT purchased Blueprint ($397)
AND NOT purchased Community ($47/mo)
THEN send this email on Day 8 at 2:00 PM

IF purchased Sprint OR Blueprint
THEN skip this sequence entirely (they have higher-tier access)

IF purchased Community during checkout
THEN skip this sequence (already a member)
```

---

## Expected Results

| Metric | Target |
|--------|--------|
| Open rate | 30-40% |
| Click rate | 3-5% |
| Trial conversion | 5-10% of eligible |
| Revenue per 100 buyers | $20-40 additional (recurring) |
| Trial → Paid retention | 50%+ |

---

## Integration with Other Sequences

| Day | Time | Sequence | Email |
|-----|------|----------|-------|
| 8 | 8:00 AM | Welcome | FAQ / Objection |
| 8 | 2:00 PM | **Community Recovery** | **This email** |

No conflict. Morning = value. Afternoon = offer (downsell).

---

## Voice Notes

- Acknowledge they said "no" — don't pretend they didn't
- Position as "lighter commitment," not "consolation prize"
- $1 trial removes risk
- Clear that Sprint/Blueprint are still better if they're ready
- No pressure, no fake urgency
