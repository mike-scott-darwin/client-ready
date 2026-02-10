---
type: decision
date: 2026-02-10
status: codified
urgency: high
---

# Ad Creative Structure — Adopt 5-Primary × 5-Headline Framework

## Situation

Client Ready currently has:
- 30 one-liner hooks (outputs/ads/2026-02-10-one-liners-cold-traffic-scale/)
- 4 priority messaging angles (Before the Funnel, Misalignment, Content Merry-Go-Round, Clarity Unlock)
- 6 codified testimonials with proof mapped to each angle
- No long-form ad copy, no UGC-style copy, no testimonial-as-ad copy

Analysis of Devon's Main Branch ad batch (5 angles × 5 primaries × 5 headlines) and Miles Stutz email patterns (story-first, case study format) reveals a structural gap: Client Ready has strong angles and proof but limited creative formats to test them through.

## Research

### Devon Ad Copy Analysis
**Date:** 2026-02-10
**Source:** Main Branch static-ads-batch-001.md
Devon runs 5 primary text types per angle (Deep, UGC/Native, Direct Response, Pattern Interrupt, Testimonial) plus 5 headline types (Proof, Mechanism, Outcome, Curiosity, Benefit). This creates 125 testable combinations per batch.
See: `research/2026-02-10-devon-ad-copy-analysis.md`

### Miles Stutz Email Mining
**Date:** 2026-02-10
**Source:** Gmail mining of 40 emails
Miles' structural patterns: story-first openings, reply-based CTAs, case study format (person → backstory → tried → changed → result), price anchoring via team cost comparison.
See: `research/2026-02-10-miles-stutz-email-mining.md`

## Decision

Adopt the 5-Primary × 5-Headline framework for Client Ready's next ad batch, adapted for the $27 offer and coaching audience.

### The 5 Primary Types (Adapted for Client Ready)

| Type | Purpose | Client Ready Fit |
|------|---------|-----------------|
| **Deep Ad (P1)** | Story-led, 500+ words, full mechanism | Misalignment origin story, Clarity Unlock testimonial stack |
| **UGC/Native (P2)** | First-person, feels organic | "Here's how even coaches without a clear niche..." — Michael's own journey |
| **Direct Response (P3)** | Scannable, benefit-led | "This eliminates offer confusion, content that doesn't sell, without courses or agencies" |
| **Pattern Interrupt (P4)** | 4-6 lines, one sharp idea | "6 coaches. 6 niches. Same problem. Same fix." |
| **Testimonial (P5)** | One person's story IS the ad | Renee (10 yrs → 90 min), Wendy (stuck → first sales calls) |

### The 5 Headline Types

| Type | Purpose |
|------|---------|
| **Proof-led** | Specific result: "10 Years Stuck → Clear Niche in 90 Minutes" |
| **Mechanism-led** | How it works: "5 AI Prompts Extract Your $5K Offer in One Afternoon" |
| **Outcome-led** | What they get: "Know Exactly What You Sell — Before You Build Anything" |
| **Curiosity-led** | Pattern interrupt: "Why 6 Out of 6 Coaches Had the Same Hidden Problem" |
| **Benefit-led** | Direct benefit: "Stop Guessing at Your Offer — Validate It for $27" |

### Which Angles Get the Full Treatment

Start with 2 angles (not all 4), to keep the first batch manageable:

| Priority | Angle | Why First |
|----------|-------|-----------|
| 1 | **Before the Funnel** | Strongest cold traffic angle, positions against competitors |
| 2 | **Clarity Unlock** | 6/6 testimonial proof, earliest-stage entry point |

This produces: 2 angles × 5 primaries × 5 headlines = 50 testable combinations.

Misalignment and Content Merry-Go-Round get the same treatment in Batch 002 once we have data from Batch 001.

### What Carries Over From Miles Stutz

| Pattern | How to Use |
|---------|-----------|
| Story-first openings | Deep Ad (P1) and UGC/Native (P2) both open with a story, not a claim |
| Case study format | Testimonial (P5) follows person → backstory → tried → changed → result → timeframe |
| Price anchoring | Direct Response (P3) anchors $27 against agency costs ($3K-$5K) and course costs ($997+) |
| Reply-based CTA | Not for ads, but adopt for email sequences (future) |

## What Changes

Reference files affected:
- None — this is an output structure decision, not a reference change

Next action:
- Generate Batch 002 using `/ads` with the 5-primary × 5-headline structure
- Start with Before the Funnel and Clarity Unlock angles
- Use existing one-liners batch as Pattern Interrupt (P4) source material
