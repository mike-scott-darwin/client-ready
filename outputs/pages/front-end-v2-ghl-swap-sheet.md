---
type: output
status: ready-to-build
date: 2026-06-28
product: Front-End — Client Ready Offer v2 (Codify)
format: GHL Swap Sheet — block-by-block replacement for the LIVE page
live_page: https://clientreadyoffer.com/digital_snacks22-3475-662204
location: AKRQpXEUDgloSAbxzDmh
based_on:
  - outputs/pages/front-end-sales-page-v2-codify.md
  - decisions/2026-06-28-codify-for-coaches-positioning.md
---

# GHL Swap Sheet — Live Front-End Page → v2 (Codify)

Work top to bottom. Each entry = one block on the live page, in order, with an **ACTION** and the exact copy to paste. P0 hygiene fixes are baked in.

---

## 🧊 COLD-TRAFFIC COPY RULE (read first)

This page is **cold traffic.** Lead with the **burning pain** and the **plain outcome** — clients, getting paid, an offer people say yes to. **NO mechanism jargon:** never say "reference files," "codify," "compound," "sovereign," or "starter stack" on this page. Nobody cold knows what those mean. That language is backstage — it lives on the **backend** (DFY "we build it for you," Client Ready OS), where buyers are warm. The offer still holds; we just sell the *ache*, not the machine.

---

## ⚠️ TWO DECISIONS REQUIRED BEFORE PUBLISH (fill these in)

**1. The ONE true student/customer count.** The live page says both "150+" and "1090+" — pick one. **Integrity check:** GHL shows ~16 actual CRO purchasers. If neither 150+ nor 1090+ is genuinely true across your full history, do NOT publish either — it's fabricated proof on a page that already has FTC exposure. Options, best first:
   - (a) Use a *true* number if you have one, everywhere.
   - (b) Drop the numeric star-rating block entirely; lean on the Renee testimonial + Stripe proof (real assets).
   - (c) Honest early-stage framing: "Join our first customers" — no invented count.
   **→ Decide: `_______`**

**2. The ONE discount presentation.** Live page has "50% OFF" / "82% OFF" / "88% OFF" and both $197 and $147 anchors. Standardize to the real ladder anchor from offer.md: **~~$197~~ $27**. Drop the percentage badges (they're wrong and inconsistent). If you want a number, $197→$27 is **76% off**.
   **→ Decide: `_______`**

---

## BLOCK-BY-BLOCK

### 1. Top banner (currently "🔥 50% OFF CODE… ENDS 6TH JULY")
**ACTION: REPLACE** (kill the fake countdown — dates don't even match; your v1 rule was no fake countdowns)
> CLIENT READY V2 LAUNCH PRICING — $27 WHILE WE BUILD CASE STUDIES

### 2. "Questions? Call me maybe: +1 469-327-5358 😉"
**ACTION: FIX** — verify that number is yours (not a Miles/agency number). Drop "call me maybe 😉" → off-voice.
> Questions? Text or call: +1 469-327-5358

### 3. Logo image
**ACTION: VERIFY** it's the Client Ready logo, not a Miles/placeholder asset.

### 4. "Need Help? michael@michaelscott.io"
**ACTION: FIX (P0)** — the link currently points to `mailito:miles@milesstutz.com`. Set href to:
> `mailto:michael@michaelscott.io`

### 5. Hero headline stack (5 competing headlines)
**ACTION: REPLACE** all of it with ONE pain-first hero (plain language, no jargon):
> **Pre-headline:** YOU'RE GOOD AT WHAT YOU DO. SO WHY WON'T THEY BUY?
>
> **Headline (H1):** BUILD AN OFFER SO CLEAR IT SELLS ITSELF — IN ONE AFTERNOON.
>
> **Sub-headline:** Most coaches don't have a marketing problem. They have an offer nobody understands. 5 AI prompts turn the expertise you already have into one offer people say yes to on the spot — no funnel, no daily content, no sales calls.

**A/B headline options (all pain-first — test 1 vs 2 vs the control):**
| # | Headline | Angle |
|---|---|---|
| 1 | Build an offer so clear it sells itself — in one afternoon. | Outcome (recommended default) |
| 2 | It was never your coaching. It was your offer. | Reframe the blame (pairs w/ pre-head "'Let me think about it.' Then they ghost.") |
| Control | Confused to Clarity to Cash. The $27 System That Takes Care of the First Two. | Proven v1 winner |

### 6. "This gets you new customers in 72 hours even if you never ran ads…"
**ACTION: DELETE (P0)** — speed/results claim, FTC risk, and it's Miles's promise style.

### 7. Hero CTA + "30 Day Money Back Guarantee"
**ACTION: KEEP.**

### 8. "4.7 / 5 based on 150+ / 1090+ verified students"
**ACTION: FIX (P0)** — replace every instance with the one true number from Decision #1 (or remove per option b).

### 9. Renee testimonial screenshot
**ACTION: KEEP** — real process testimonial, safe.

### 10. Problem section ("Most coaches can't clearly explain what they sell")
**ACTION: REPLACE** with a pain-first problem (plain language, no jargon):
> **Header:** IF YOU'RE A GREAT COACH WHO STILL CAN'T GET CLIENTS, READ THIS.
>
> You know your stuff. You've changed people's lives. Your bank account doesn't show it.
>
> You post. You show up. You get on the calls. And still — *"let me think about it."* Then silence.
>
> So you assume you need a better funnel. More content. A new platform. Another course on ads.
>
> **Wrong.**
>
> Here's the real problem: when someone asks what you do, they get a different answer every time. *"I help coaches grow their business."* That could mean anything — so people tune out and scroll on.
>
> It's not that you're a bad coach. **It's that your offer is impossible to say yes to.** Nobody buys what they can't understand in ten seconds.
>
> Client Ready fixes the offer — so people get it instantly, and buy.
>
> ❌ No more sounding like every other coach
> ❌ No more discounting because you can't explain the value
> ❌ No more months of posting, hoping someone asks to work with you
> ❌ No more "let me think about it"

### 11. Countdown timer block ("1 days 12 hours…")
**ACTION: DELETE** — fake urgency, mismatched with banner date.

### 12. Pricing block ("Only $197 $27… 82% OFF")
**ACTION: FIX** per Decision #2. Keep the honest V1/V2 launch-pricing paragraph; remove the "% OFF" badge.
> **Only ~~$197~~ $27.00** — Client Ready V2 launch pricing while we build case studies. Not hype — we return to full price once we have the testimonials.

### 13. Case study "HOW I WENT FROM 7 YEARS OF SEARCHING…"
**ACTION: KEEP the story, REPLACE the ending** to add the codify turn. Retitle:
> **Header:** HOW I WENT FROM 7 YEARS OF SEARCHING TO AN OFFER THAT RUNS ITSELF

Keep Parts 1–2 (the search, "that's a design problem"). Replace **"What Changed Everything"** onward with:
> I rebuilt my offer around one principle: if someone can't understand what they're getting in 60 seconds, it isn't clear enough. "I help coaches validate a $5K+ offer before they build anything — in one afternoon." You either want that or you don't.
>
> But here's the part nobody talks about — what happened *after* the offer. I took everything that made it work — who it's for, my story, my voice, my buyers' exact words — and wrote it into reference files an AI can read every time. Then I ran my whole business from them. Every ad, email, VSL — generated from those files, in my voice. No agency. No content treadmill.
>
> **The offer got me clear. The files made it run.** And they compound — the file I write once writes next month's ads.

[DELETE the "$5K–$10K daily profits / 100+ buyers / Wellington" lines that follow — see block 14.]

### 14. "Digital Snacks is the shortcut that took me…" block
**ACTION: DELETE ENTIRELY (P0)** — this is Miles's product ("$20/day ads," "10%+ pages," "100+ buyers daily," "$5K–$10K daily profits"). Not your product, not your claims. Appears TWICE on the page — delete both.

### 15. Stripe proof ("That's a screenshot of my stripe account…")
**ACTION: KEEP**, tighten the line:
> **I make those sales with an offer that does the selling — and files that do the writing.**

### 16. Testimonials (Ryan $14k/mo, Alexia $7,500)
**ACTION: KEEP + ADD DISCLAIMERS** (they're missing on the live page; the repo v1 had them):
> Ryan makes $14k/mo selling a Transformation Fitness Program for men over 40.
> *Results vary. Ryan's results reflect his specific expertise, audience, and effort.*
>
> Alexia generated $7,500 in her first week using a Client Ready Offer — without ads.
> *Results vary. Alexia's results reflect her existing warm audience.*

### 17. Second pricing block ("88% OFF")
**ACTION: FIX** — same standardized pricing block as #12.

### 18. "HERE'S WHAT MAKES CLIENT READY DIFFERENT"
**ACTION: REPLACE** with plain, pain-first copy (no jargon). **Remove** the "→ Turn your existing knowledge into one **No-Phone Offer**" line and the "Wellington/$15k" line.
> **Header:** HERE'S WHAT MAKES CLIENT READY DIFFERENT
>
> Every coach tries to fix slow sales by adding *more* — more content, more value, more funnels, more hustle. Client Ready does the opposite.
>
> You take the one thing you're already great at, package it into a single offer people understand in seconds, and sell that. One clear offer beats ten confusing ones.
>
> → Turn the expertise you already have into one offer people *get* immediately
> → Become the obvious choice — instead of one more coach who "helps everyone"
> → Charge real prices, because the value is finally clear
> → Stop guessing where the next client comes from

Keep the "This requires actual work / get-rich-quick doesn't exist" reality check (good). Keep testimonial bullets **with** the *individual results vary* note.

### 19. Second "Digital Snacks" block (duplicate)
**ACTION: DELETE** (see #14).

### 20. Second "Here's what makes Client Ready different" (duplicate)
**ACTION: DELETE** — the page repeats this whole section; keep only the one rewritten in #18.

### 21. "HERE'S EVERYTHING YOU'RE GETTING" (component cards)
**ACTION: FIX names to match the products.** Current card "**Guide to Selling One Signature Offer**" is described as the 5 AI prompts — rename to match. Use:
> 1. **The Client Ready Case Study** — the 7-year search, the realization, and the 4 principles that changed everything.
> 2. **5 AI Prompts That Pull Your Offer Out of Your Head** — answer the prompts, walk out with a finished offer you can sell today. (No blank page, no guesswork.)
> 3. **"I'm The Only Choice" Positioning** — [keep current copy].
> 4. **Your $5K Offer, Ready Today** — [keep current copy].
> 5. **The 48-Hour Validation Sprint** — pick 5 people, send the message we give you today, and know within 48 hours if it's a winner. (Replaces the vague "Validate Before You Build" card.)
> + **One Offer You Won't Abandon** — [keep current copy].

Add a small callout: **"First win in 10 minutes — run Prompt 1 and walk away with your clearest one-sentence offer."**

### 22. "Plus 9 Bonuses"
**ACTION: KEEP; FIX** the header typo "When You Client Ready Offer™" → "When You **Get** Client Ready Offer™"; anchor "$147" → "$197" (match Decision #2). Light reframe:
> - **Bonus 1 — AI Offer Prompt Library** → "prompts that run against *your* reference files, so the output is yours, not generic."
> - Bonuses 2–9: keep as-is.

### 23. Guarantee section
**ACTION: KEEP; FIX** typo "Client Ready **Systm**" → "System". Copy is otherwise good.

### 24. Footer disclaimer
**ACTION: KEEP** — the get-rich-quick / results disclaimer is good and now consistent with the cleaned body.

### 25. Final CTA + sticky bottom bar
**ACTION: KEEP; standardize** price to ~~$197~~ $27 per Decision #2.

---

## GLOBAL FIND-AND-REPLACE (typos, do all)
- `?ffere` → `?`
- `Client Ready Systm` → `Client Ready System`
- `what your worth` → `what you're worth` (2×)
- `buy solving` → `by solving`
- `thinking they need to have more stuff thinking they need to have more stuff` → `thinking they need more stuff`
- `That's what I built for myself. And that's what this system helps you build..` → single period
- `When You Client Ready Offer™` → `When You Get Client Ready Offer™`
- Remove every remaining instance of: **"No-Phone Offer," "Digital Snacks," "Wellington," "100+ buyers daily," "$5K–$10K in daily profits," "72 hours," "(Works every time)."**

## METADATA (P0)
- `og:author` / `author`: **Miles Stutz → Michael Scott / Client Ready**
- `og:title` / `og:description`: confirm they say Client Ready, not Miles.
- Page slug is `digital_snacks22-…` — cosmetic, but rename to `client-ready-offer` when convenient (set a redirect).

---

## Build path
Copy is in `outputs/pages/front-end-sales-page-v2-codify.md`; this sheet maps it onto the live blocks. To push into GHL, point the MCP at `AKRQ...` (currently authed to `9g4...`) or I drive edits with the v1 key. Nothing goes live until Decisions #1 and #2 are filled.
