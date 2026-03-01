---
type: decision
date: 2026-02-17
status: codified
urgency: high
linked_decisions:
  - decisions/2026-02-14-funnel-congruence-audit.md
---

# Skool About Page Congruence Fix

## Situation

The Skool about page (skool.com/high-ticket-playbook-9467/about) has 10 incongruences with the current offer architecture. Wrong prices, wrong product name, wrong audience stage, and mixed promises from products across different tiers.

## Audit

| # | Current Copy | Problem | Correct |
|---|-------------|---------|---------|
| 1 | "Turn Your Low Ticket Customers Into High Ticket Clients" | Assumes they already have customers. Audience can't articulate their offer yet. | Headline about offer clarity → clients |
| 2 | "$7 low ticket offers" (sidebar) | No $7 product exists in funnel | $47 |
| 3 | "$2K+ client funnel" | Offer promises $5K+ | $5K+ |
| 4 | "The High Ticket Playbook" | Product is "Client Ready Offer System" | Client Ready Offer System |
| 5 | "systematic $2K+ client funnel in 24 hours" | $47 product validates an offer, not builds a funnel. Funnel = Sprint. | Validate your offer in one afternoon |
| 6 | "Know their zone of genius" | Product EXTRACTS zone of genius — they don't know it yet | "Have expertise but can't package it" |
| 7 | "24-Hour Funnel Installation" | Sprint/Blueprint promise, not community or $47 deliverable | Remove — not a community feature |
| 8 | "14-day money-back guarantee" | offer.md says 30-day money-back | 30-day |
| 9 | "Free" (Skool setting) | Community is $47/mo ($1 trial) per OTO 3 | Update Skool pricing config |
| 10 | Mixed product promises | Bullets mix $47 (extraction), Sprint (funnel install), Blueprint (scaling), community (calls) | Match bullets to community deliverables only |

## Decision: Rewrite About Page

### Headline

```
Build a Coaching Offer So Clear It Sells Without a Sales Call
```

### Sidebar Description

```
Extract your zone of genius, validate your $5K+ offer, and stop guessing — in one afternoon.
```

### Full Body Copy

```
For coaches who:

• Have real expertise but can't explain their offer in one sentence
• Are tired of posting content that nobody buys
• Bought courses that didn't fit their situation
• Want to stop guessing and start selling

We built the Client Ready Offer System for exactly this.

5 AI prompts extract your zone of genius, ideal client, and complete offer
— in one afternoon. Then you validate before you build anything.

Inside the community:

✅ Weekly hot seat calls with Michael — bring your offer, get live feedback
✅ Direct access to Michael in the comments — no gatekeepers
✅ See what's working for other coaches building right now
✅ Resource library — templates, swipes, frameworks
✅ The full classroom: Extract → Build → Launch

30-day money-back guarantee. If you don't get results, reply to any
email and get a full refund. No questions asked.

Join now

— Michael

P.S. I'm The Coach Who Won't Tell You to Quit Your 9-to-5 yet!
```

### Skool Settings to Update

- **Pricing:** Change from "Free" to match OTO 3 pricing ($47/mo, $1 trial) — or keep free if community is open to all buyers (Sprint/Blueprint buyers get access anyway). Decide based on whether free members see the classroom.
- **Group name display:** "Client Ready Community" (already correct)

## What Changes

- Skool about page copy updated manually in Skool admin
- No reference files affected — this aligns the external page with existing offer.md

## Resolution (2026-02-27)

Copy applied to live Skool about page. Pricing model confirmed: community is free for buyers who enter through the OTO funnel. Direct access available at 47/month as a downsell for non-buyers.
