---
type: research
date: 2026-02-11
source: mining
topics: [ad-audit, meta-ads, own-ads, the-main-branch]
linked_decisions: []
status: complete
---

# The Main Branch — Active Meta Ads Audit

**Source:** Apify Meta Ad Library scrape (26 ads, page ID 324212004102365, Feb 11 2026)
**Raw data:** `2026-02-11-the-main-branch-meta-ads-apify.json`
**One-sentence summary:** 26 active ads across 3 copy blocks, heavily weighted toward the "Own Your AI" angle (16 ads), with only image + long-form video formats and no short-form video, carousel, or social proof in any ad.

## Current Ads: 3 Copy Blocks

### Copy Block A — "Own Your AI" (16 ads, all image, launched Jan 30)

> Every AI tool gets smarter over time. And raises prices.
>
> Meanwhile, your stuff should get better on your own computer.
>
> Files you control. Data you own. Your ideas stay private.
>
> That's what Main Branch is. A system where your business knowledge grows instead of disappearing every time you close a chat window.
>
> Your business. Your files. Outputs that actually sound like you.

**Headline:** "Own your AI. Don't rent it."
**Link description:** "Build the machine that makes the ads (previously The Ads Lab)"
**CTA:** Learn more → skool.com/main/about
**Testing:** 16 unique image creatives, identical copy. Massive visual creative test.

### Copy Block B — "Context Reset" (9 ads, 3 video + 6 image, launched Feb 8-9)

> Most entrepreneurs spend hours explaining their business to AI every single conversation.
>
> Context. Offer. Audience. Voice. Every. Single. Time.
>
> What if AI already knew all of it?
>
> Main Branch loads everything about your business in seconds. Once it's set up, every output builds on what came before.
>
> The setup takes effort. Then the work shrinks.

**Headline:** "Your business knowledge should grow, not reset."
**CTA:** Learn More → skool.com/main (video) or skool.com/main/about (image)
**Testing:** 6 unique images + 1 long-form video (~14 min) across 3 entries. Format + creative test.

### Copy Block C — "SaaS Cancellation Story" (2 ads, both video, launched Feb 9)

> Last year one business owner canceled every SaaS subscription he had and rebuilt it all from the terminal. Here is what happened.
>
> Costs went down. Speed went up. And the system he built now generates ads, content, and scripts from files he owns on his own computer.
>
> No agency. No SaaS. No starting fresh every conversation.
>
> The system is called Main Branch. 7-day free trial.

**Headline:** "Codify Once. Generate Ads, Content, and Scripts Forever."
**CTA:** Learn More → skool.com/main
**Testing:** 1 long-form video (~14 min) across 2 entries. Toe-in-the-water test.

## Format Distribution

| Format | Count | % |
|--------|-------|---|
| Static Image | 21 | 78% |
| Long-Form Video (~14 min) | 5 | 19% |
| Short-Form Video | 0 | 0% |
| Carousel | 0 | 0% |

## Launch Waves

| Wave | Date | Ads | Copy Block | Format |
|------|------|-----|------------|--------|
| Wave 1 | Jan 30 | 16 | A (Own Your AI) | All image |
| Wave 2 | Feb 8-9 | 10 | B (Context Reset) + C (SaaS Story) | Image + video |

## Testing Strategy

| Copy Block | Ads | % of Library | Creative Variants | Focus |
|------------|-----|-------------|-------------------|-------|
| A (Own Your AI) | 16 | 59% | 16 unique images | Image creative testing |
| B (Context Reset) | 9 | 33% | 6 images + 1 video (x3) | Format + creative testing |
| C (SaaS Story) | 2 | 7% | 1 video (x2) | Early test |

**3 unique copy blocks across 26 ads.** Testing is almost entirely visual creative variation, not copy variation.

## Destination URLs

| Destination | Ads | Copy Blocks |
|-------------|-----|-------------|
| skool.com/main/about | 22 | A (all), B (image variants) |
| skool.com/main | 5 | B (video), C (all) |

## What's Working (Structural Strengths)

- Clean creative testing methodology — same copy, many images, isolating the visual variable
- Wave structure lets you read Block A results before launching B and C
- Three copy blocks cover distinct psychological entry points:
  - **A:** Fear/protection (ownership, privacy)
  - **B:** Frustration/efficiency (stop re-explaining)
  - **C:** Curiosity/narrative (cancel everything, go terminal)

## Gaps Compared to Competitors

Based on today's Cat Howell and Miles Stutz scrapes:

| Gap | Competitors | Main Branch Current |
|-----|------------|-------------------|
| **Short-form video** | Cat: 5 ads (4-8s), Miles: 4 ads (5-9s) | None |
| **Carousel** | Cat: 6 carousels (4-8 images each) | None |
| **Social proof / testimonials** | Cat: revenue stories, Miles: "1,090+ students" | None in any ad |
| **Price / offer mention** | Cat: "$67" in body, Miles: "$9" in body | Only Copy Block C mentions free trial |
| **Comment-to-DM automation** | Cat: 4 ads, Miles: 3 ads | None |
| **Copy variation** | Cat: 6-7 copy blocks, Miles: ~8 copy blocks | 3 copy blocks |
| **Case studies** | Miles: named client story, Cat: client case study | None |
| **Belief-shift ads** | Miles: 3 dedicated ads selling the mechanism | None — all sell the product directly |

## Action Items to Consider

### Quick Wins (Low Effort)
1. **Add price/trial to Copy Blocks A and B** — Only C mentions free trial. A and B give no reason to click NOW.
2. **Fix "previously The Ads Lab" legacy text** — Still showing in link description on 13 ads.
3. **Fix 3 ads with missing link titles** — 3 Copy Block A ads have blank headlines (body text in CTA field instead).

### Medium Effort
4. **Create 4-8 second thumb-stopper videos** — Both competitors use ultra-short animated clips. Pair with existing copy blocks. Low production cost.
5. **Add a testimonial/social proof copy block** — Neither competitor runs zero-proof ads. Even a single "member result" ad would diversify messaging.
6. **Test carousel format** — Cat runs 6 carousels. Could show the workflow: confused → clear → converting in image sequence.

### Strategic (Requires Decision)
7. **Build a belief-shift ad** — An ad that sells the idea of "owning your business knowledge" without mentioning Main Branch at all. Pre-sell the mechanism.
8. **Expand copy diversity** — 3 copy blocks is lean. Cat runs 6-7, Miles runs 8+. More angles = more audience segments reached.
9. **Landing page split test** — Cat tests 4 different landing pages for one product. Currently testing 2 (about vs main).

## Open Questions
- Which of the 16 image creatives in Block A is performing best? (Check Ads Manager)
- Is the /about page or /main page converting better for Block B?
- Should the next wave prioritize new copy angles or new formats?
