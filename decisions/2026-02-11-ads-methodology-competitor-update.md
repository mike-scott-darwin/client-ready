---
type: decision
date: 2026-02-11
status: codified
urgency: normal
---

# Ads Methodology — Competitor Research Update

## Situation

Scraped all active Meta ads from 3 competitors and Devon's Main Branch on Feb 11 2026 via Apify. Cross-referenced against current Client Ready ad strategy (batches 002-004, one-liners, ads-methodology.md). Found 7 convergent patterns across competitors that Client Ready's methodology didn't address.

## Research

### cat-howell-apify-scrape
**Date:** 2026-02-11
**Source:** Apify Meta Ad Library (28 ads)
Key findings: Funnel-level awareness matching (4 URLs for same $67 product), ultra-short video (4-8s thumb-stoppers), client case study format, comment-to-DM in 4 ads, 6-7 distinct copy blocks.
See: `research/2026-02-11-cat-howell-apify-scrape-synthesis.md`

### miles-stutz-apify-scrape
**Date:** 2026-02-11
**Source:** Apify Meta Ad Library (23 ads)
Key findings: Belief-shift ads (3 ads selling mechanism without product), 61% video (up from estimated 10%), comment-to-DM in 3 ads, anti-proof angle, two parallel front-end products, ultra-short video (5-9s).
See: `research/2026-02-11-miles-stutz-apify-scrape-synthesis.md`

### hernan-vazquez-apify-scrape
**Date:** 2026-02-11
**Source:** Apify Meta Ad Library (26 ads)
Key findings: Copy length spectrum (1-sentence to 1,800 words for same $5 product), transparent upsell disclosure pattern, comment-to-DM in 31% of ads (oldest running 9+ months), 50-100 AI creatives per week, format segmentation (long copy on image, short copy on video — never mixed).
See: `research/2026-02-11-hernan-vazquez-apify-scrape-synthesis.md`

### the-main-branch-ad-audit
**Date:** 2026-02-11
**Source:** Apify Meta Ad Library (26 ads, page ID 324212004102365)
Devon's ads. 3 copy blocks, same gaps as Client Ready: no short-form video, no carousel, no social proof, price mentioned in only 2/26 ads.
See: `research/2026-02-11-the-main-branch-ad-audit.md`

## Decision

Added 6 new sections to `reference/domain/ads-methodology.md` (Parts 11-16) covering patterns validated across all 3 competitors:

1. **Format Spectrum** (Part 11) — Copy length spectrum testing, format segmentation rules, ultra-short video as a format category
2. **Belief-Shift Ads** (Part 12) — Dedicated ads that sell the mechanism without selling the product
3. **Price Transparency** (Part 13) — Leading with price as a feature of low-ticket
4. **Transparent Upsell Disclosure** (Part 14) — Hernan's verbatim trust pattern
5. **Comment-to-DM Automation** (Part 15) — Engagement-first ad format with benchmarks
6. **Angle Volume & Diversity** (Part 16) — Minimum 5-6 copy blocks before scaling, with expansion method

Also updated:
- Ad naming convention to include format length and new ad types
- Quick reference message types to include Belief Shift and Price-Forward
- Video vs Static section with Feb 2026 competitor format distribution data
- Source list in frontmatter

## What Changes

Reference files affected:
- `reference/domain/ads-methodology.md` — 6 new sections (Parts 11-16), updated naming convention, message types, and format data

## Rationale

These patterns are convergent — they appear independently across 3 competitors operating at different scales ($5-$67 front-ends, different audience sizes, different niches within coaching/marketing). When multiple competitors converge on the same structural pattern, it's a signal about what the market and algorithm are rewarding, not a coincidence.

The methodology needed these patterns documented as reference so future ad batches can test against them systematically rather than rediscovering them.
