---
type: research
date: 2026-02-11
source: mining
topics: [competitor-analysis, ad-copy, meta-ads, cat-howell, funnel-architecture]
linked_decisions: []
status: complete
---

# Cat Howell Apify Scrape Synthesis

**Source:** Apify Meta Ad Library scrape (28 Cat Howell ads, Feb 11 2026)
**Prior research:** `2026-02-10-cat-howell-ad-library-mining.md` (manual screenshot, 78 ads)
**Raw data:** `2026-02-11-cat-howell-meta-ads-apify.json`
**One-sentence summary:** Cat runs one core $67 product across 4 distinct funnel URLs matched to awareness levels, with 6-7 copy blocks repeated across formats — revealing a funnel-level split-testing strategy, not just ad-level.

## Key Findings (New — Not in Feb 10 Mining)

### 1. Funnel-Level Awareness Matching (Biggest Discovery)
She runs 4 distinct URLs for the same $67 product:
- `/lticketads` — awareness/sales page (16 ads)
- `/orderltoads` — direct order page (8 ads)
- `/lticketadsunaware` — cold traffic / problem-unaware page (2 ads, newest)
- `/lticketchallenge` — challenge entry point (2 ads)

Same copy can point to different landing pages. She's testing FUNNEL architecture, not just ad creative. This is more sophisticated than what the manual mining revealed.

### 2. New Product: Low Ticket Codex (Launched Feb 6)
Two brand-new ads for `orderltocodex` appeared 5 days before scrape. Shifts language from tactical ("campaign setup") to strategic ("build your own low ticket ecosystem that feels like peace"). Product ladder becoming visible: Low Ticket Ads (tactical) → Sales Copy Challenge (skill) → Codex (strategic ecosystem).

### 3. The "Crickets" Hook — Problem-Unaware Copy Architecture
Longest copy in the library (~250 words). Structure:
- Opens with reader's current experience: "Your offer sells when you post... But when you stop? Crickets."
- Emoji bullet points for pain amplification
- Handles two specific objections (tried ads and lost money; avoided due to cost)
- Teases specific mechanism ("four specific things the algorithm needs")
- Lists product types reader might sell

This is a distinct "problem-aware → solution-aware" bridge format. **Client Ready's P6/P7 unaware ads are the equivalent — this confirms the strategy is sound.**

### 4. "$1 In / $2 Out" — Simpler Than ATM
"I give the algorithm $1, it gives me $2 back" reduces the entire value proposition to a one-line ROI formula. More visceral than the ATM metaphor, easier to remember. Used with link title "The algorithm wants your mini offer."

### 5. "Meta LOVES Mini Offers" — Platform Alignment Argument
"The Purchase event gets fired A LOT, and the algorithm loves this." Turns potential objection (low ticket = low margin) into algorithmic advantage. This is a mechanism-level claim about WHY it works.

### 6. Client Case Study Angle
One ad uses a full third-person case study: client was spending $300+ per booked sales call, only to be ghosted. Built low ticket ecosystem, now getting PAID to acquire customers. Client objection included and overcome ("Low ticket buyers aren't gonna be the right quality"). **Client Ready doesn't have client case study ads yet.**

### 7. Comment-to-DM Automation
4 ads use "Comment [keyword] and I'll send you the link" — ManyChat or similar. One ad has NO link URL at all, purely comment-driven. This is an engagement strategy that feeds the algorithm while building a DM list.

### 8. Ultra-Short Video as Thumb-Stopper
5 ads are 4-8 second videos — too short for a pitch. Likely animated text or single hook clips. The full pitch lives in the body copy below. **Format Client Ready hasn't tested.**

### 9. Contrarian Double-Debunk (Codex)
Debunks TWO beliefs simultaneously: (1) free content builds trust/grows sales, and (2) you need high ticket for $3K+ days. Double-contrarian is more aggressive than single-belief-shift.

### 10. Price Anchoring via Competitor Cost Comparison
"While most businesses are paying $7 for a webinar registration... $300 for a booked call (only to be ghosted)... I've created a system that PAYS me to acquire new customers." Explicit competitor cost framing.

## Confirmed Findings (Validate Feb 10 Mining)

| Pattern | Feb 10 Finding | Feb 11 Confirmation |
|---------|---------------|---------------------|
| "Stripe notifications" dominant | Yes, identified | Confirmed: 8+ ads, most repeated copy block |
| ATM machine metaphor | Yes, prominent | Only 2 ads use it — less dominant than expected |
| Specific income numbers | Yes, throughout | $500/day, $80K/month, $200/day ad spend confirmed |
| Personal revenue story arc | Yes, strongest | 5+ ads, the core credibility mechanism |
| Benefit bullet stacking | Yes, mid-ad | 3 ads with ">" formatted bullets |
| Volume advantage | 78 active (manual) | 28 in this scrape (different search scope) |

## Format Distribution

| Format | Count | % |
|--------|-------|---|
| Video | 15 | 54% |
| Image | 7 | 25% |
| Carousel | 6 | 21% |

Video durations: ultra-short (4-8s) x5, short (19-46s) x5, medium (85-87s) x2, long (147-185s) x3.

## Copy Repetition Strategy

She runs 6-7 distinct copy blocks, repeated across formats and URLs:
1. **Stripe notifications** — 8+ ads across video, image, and carousel
2. **Long personal narrative** ($80K/month story) — 5+ ads
3. **ATM machine** — 2 carousels
4. **Product type listing** ("ebooks, subliminals, courses") — 3 carousels
5. **Behind-the-scenes 20-min setup** — 2 ads
6. **$1 in / $2 out algorithm** — 2 videos
7. **Crickets / unaware** — 2 ads (newest)

**Strategy: test the same copy in multiple containers, then scale what works.**

## Implications for Client Ready

### Act On (High Signal)
1. **Funnel-level awareness matching** — Client Ready could test different landing pages for the same offer matched to awareness stage. Currently one landing page for all traffic.
2. **Ultra-short video format** — 4-8 second thumb-stoppers with body copy doing the selling. Low production cost, high scroll-stop potential.
3. **Client case study ads** — Third-person proof is a format Client Ready hasn't used. Could build from existing testimonials.
4. **"$1 in / $2 out" simplicity** — The "Confused → Clear → Converting" metaphor is Client Ready's equivalent. Consider a one-line version: "One afternoon. One offer. One system that sells itself."

### Watch (Interesting, Not Urgent)
5. **Comment-to-DM automation** — Requires ManyChat setup. Worth exploring when ad volume increases.
6. **Contrarian double-debunk** — Could work for Client Ready: "You don't need a massive audience AND you don't need to be a copywriter."
7. **Product ladder evolution** — Cat's trajectory (tactical → skill → ecosystem) mirrors Client Ready's funnel (Offer System → Sprint → Blueprint).

### Don't Copy
- Income claims without typicality data. Cat has years of documented revenue. Client Ready doesn't yet.
- "Meta LOVES" claims — risky without platform endorsement. Use mechanism language instead.
- Volume-for-volume's-sake. Cat runs 28+ ads but only 6-7 copy blocks. Quality diversity > raw quantity.

## Open Questions
- Should Client Ready test different landing page URLs for different awareness levels?
- Is a 4-8 second thumb-stopper video worth producing for the next ad batch?
- Which existing testimonials could become full client case study ads?
