---
type: research
date: 2026-07-05
source: mining
topics: [competitor-analysis, creative-strategy, meta-ads, miles-stutz, ad-creative]
linked_decisions: []
status: complete
---

# Miles Stutz — Oldest / Winning Ad Creative (Fresh Pull)

**Source:** Live Apify scrape of Miles's Meta Ad Library (page 226368730568005, "Miles Stutz - 4-Hour Consultant"), pulled 2026-07-05, sorted by impressions. 90 of 125 active ads analyzed. Images downloaded to `.context/miles-creative/`.

**One-sentence summary:** Miles reset his entire ad account on **2026-06-04**; the oldest surviving cohort (June 4–11) that is *also* highest-impression are his proven winners — and they are almost entirely **native-app screenshot mockups and typographic design cards, NOT photorealistic people**.

## Why "oldest" = winners
- The whole account's active ads start **2026-06-04 or later**. Everything from the Feb/2026 era (the "women lifestyle photo" cohort) is now inactive/killed.
- Sorted by impressions (spend proxy), the June-4→June-11 ads sit at the top. Long runtime + high spend = Meta-validated winners. `total_active_time` was null in this actor build, so age is inferred from `start_date` + impression rank.

## The 7 winning creative archetypes (with evidence)

| # | Format | Example (title) | First seen | Built with |
|---|--------|-----------------|-----------|-----------|
| 1 | **Fake iMessage/text convo** | "Close $15K Clients in 5 Minutes" (#1 by impressions) | Jun 4 | HTML/design mockup |
| 2 | **Fake Gmail inbox** — stacked Stripe/PayPal payment alerts ($15K, $12K, $7K…) | "A steady floor beats a big month" | Jun 25 | HTML/design mockup |
| 3 | **Fake ChatGPT screenshot** — "ChatGPT 5.4" answering the prospect's exact question | "The Answer Was Always Obvious" | Jun 18 | HTML/design mockup |
| 4 | **Value-stack "Order Summary"** — gold/navy checkout, $1,587 → $17 | "$1,580 of Tools for $17" | Jun 15 | HTML/design mockup |
| 5 | **"Breaking News" tabloid** — red banner, bold caps, green checks, yellow CTA | "$17 → $7,500 in 5 days" | Jun 11 | Designed graphic |
| 6 | **Handwritten note** — aged paper, coffee stain, croissant; personal story | "Chess Coach…" collation | Jun 11 | AI photo (Flux-able) + baked text |
| 7 | **Bold typographic card** — big black type on cream, one word in red | "It's Not You — It's the Offer" | Jun 4 | HTML/design or Flux bg + text |

### The big shift vs. Feb 2026
The Feb mining (`2026-02-10-miles-stutz-ad-library-mining.md`) found ~40% **stock women lifestyle photos**. Those are **gone**. The surviving winners are native "ugly"/screenshot formats and typographic cards. Trust/scroll-stop now comes from **feeling like organic content** (a text from a friend, your own inbox, a ChatGPT answer), not from a pretty stock photo.

### Copy patterns riding on top (unchanged from prior mining)
- Every winner leads a specific number: **$17 → $7,500 / $15K in 5 min / $127,000 in 6 months**.
- Angles: no-sales-calls (dominant), offer-clarity ("it's not you, it's the offer"), income-rollercoaster, anti-content, value-stack.
- CTAs: "Learn more" / "See details" / "Shop now". Link descriptions carry proof: "AI-powered system. 1,090+ students. $17 today."

## Implication for Client Ready creative (the mirror)

**Critical tooling finding:** 6 of 7 winning formats are **text-exact designed graphics** (UI chrome, precise numbers, checkout rows). Flux/fal.ai **cannot** render these — it garbles UI text and numbers. fal.ai is the RIGHT tool only for archetype #6 (photoreal lifestyle scene with room for a headline).

So mirroring Miles means adding a **second creative engine**: HTML/CSS templates rendered to PNG (Devon's "pure Python printing CSS from the design system" method), one per screenshot format, filled with OUR angles + FTC-safe copy (transformation/clarity claims, NOT income claims — see `main-angles.md` Counterintuitive Reveal rules).

### Proposed Client-Ready mirrors (angle-mapped, compliance-safe)
- **iMessage** → "wait, you validated your offer in ONE afternoon?" / "yep. one AI prompt. no course."
- **Gmail inbox** → stack of "New Stripe payment" *replaced* with clarity moments: "New buyer — $27", "DM: I need this", "Landing page is live" (avoid fabricated income totals).
- **ChatGPT screenshot** → "how do I know if my offer will actually sell?" → our mechanism answer.
- **Order Summary** → our value stack, $X value → $27 today (matches our real bump/stack).
- **Tabloid "Breaking News"** → best as our "ugly static" test; pairs with Don't-Buy-This / No-47-page angles.
- **Handwritten note** → the ONE fal.ai job: photoreal desk + handwritten "You can't grow into pain." story.
- **Typographic card** → trivial to render; maps to every one-liner in `outputs/ads/one-liners.md`.

## Next action
Build an HTML→PNG template renderer (`scripts/ad-templates/`) for the top 2 formats first — **iMessage** and **Order Summary** — since those are the #1 impression winner and the value-stack workhorse. Keep fal.ai for the handwritten/lifestyle format. See TOOLS.md.
