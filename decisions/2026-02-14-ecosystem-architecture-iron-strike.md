---
type: decision
date: 2026-02-14
status: codified
urgency: high
linked_research:
  - research/2026-02-14-low-ticket-to-high-ticket-ecosystem-gemini.md
linked_decisions:
  - decisions/2026-02-12-scaling-architecture.md
---

# Ecosystem Architecture — Iron Strike System

## Situation

Gemini deep research into low-ticket to high-ticket practitioner architectures (Cat Howell, Miles Stutz, Hernan Vazquez, Alisha Conlin-Hurd, Ravi Abuvala, Jeremy Haynes) revealed five challenges to Client Ready's current architecture. Three are actionable pre-launch without changing products or pricing. Two are scaling decisions to park.

## Research

### low-ticket-to-high-ticket-ecosystem
**Date:** 2026-02-14
**Source:** Gemini Deep Research
See: `research/2026-02-14-low-ticket-to-high-ticket-ecosystem-gemini.md`

**Key finding:** The 7-21 day "iron strike" window after purchase is when ascension probability is highest. After 3 weeks, probability drops significantly. Client Ready's 10-day welcome sequence is relationship-only — no ascension pressure. Every successful practitioner builds ascension into this window.

---

## Decision: Option B — Launch + Iron Strike System

Three additions to the launch architecture. No new products. No pricing changes. All buildable in GHL within a week.

### 1. Ascension Pressure in Welcome Sequence

**Current:** 10-day welcome sequence is relationship-only. All upsell offers handled by separate parallel recovery sequences (bump recovery Days 2/4/6, OTO recovery Days 3/5/7, community recovery Day 8).

**Change:** Add soft ascension CTAs within the main welcome emails on Days 5, 7, and 9. Not separate pitches — a natural close within the relationship email.

| Day | Current Focus | Addition |
|-----|---------------|----------|
| 5 | "The 2-minute test for your offer" (quick tip) | End with: "If you've done the test and you're ready for the next step, the Sprint is where we build it together in 30 days. [link]" |
| 7 | "What my morning actually looks like" (behind the scenes) | End with: "This is what it looks like when the system runs. If you want help building yours, here's how. [link to Sprint or Blueprint]" |
| 9 | "What happens after $27" (the roadmap) | This email already maps the path — make the CTA explicit. "You're here [point to $27]. The next step is [Sprint/Blueprint]. Here's the difference. [comparison + links]" |

**Why these days:** Days 5/7/9 hit the sweet spot of the iron strike window. Early enough to catch peak motivation, late enough that they've consumed some of the $27 product. Alternates with the parallel recovery sequences (which run on even days) so buyers aren't double-pitched.

**Voice guard:** These are NOT hard sells. They're the natural answer to "what's next?" within a relationship email. Same tone as the rest of the sequence. If it reads like a pitch, rewrite it.

### 2. Accountability Outreach for Sprint/Blueprint Buyers

**Current:** No post-purchase outreach beyond automated emails.

**Change:** Manual DM within 48 hours of Sprint or Blueprint purchase.

**Script:**
> "Hey [name] — saw you grabbed the [Sprint/Blueprint]. Just wanted to make sure you got access to everything. What are you working on right now?"

**Why this works (from research):**
- Stutz and Vazquez both use this pattern — catches buyer at peak motivation
- Framed as accountability/support, not sales
- Opens a conversation that naturally leads to deeper engagement
- Sprint/Blueprint buyers are your highest-value customers — a 2-minute DM is worth it

**Who does it:** Michael, manually. At current volume (pre-scale), this is 1-3 DMs per week. When volume exceeds ~20/week, hire a setter.

**Trigger:** GHL notification on Sprint or Blueprint purchase → manual DM within 48 hours.

### 3. Consumption Tracking Trigger

**Current:** All $27 buyers get the same email sequence regardless of whether they open the product.

**Change:** GHL tracks whether buyers access the product (login/download). Day 3 email splits based on engagement:

| Buyer Behavior | Day 3 Email | Purpose |
|----------------|-------------|---------|
| **Opened product** | "Advanced Tips" — "Now that you've started, here's how to get the most out of Prompt 3..." | Reward engagement, deepen usage |
| **Hasn't opened** | "Quick Start" — "Hey, noticed you haven't jumped in yet. Here's the single fastest win — takes 5 minutes..." | Accountability nudge, reduce shelf-ware |

**Why this matters (from research):**
- Vazquez: "If product is shelf-ware (long boring course), trust erodes. Fast win sets up the high-ticket call."
- Buyers who consume the product are exponentially more likely to ascend
- Non-consumers need a different intervention — not more pitching, but accountability

**Implementation:** GHL workflow checks for product access event by Day 3. If event exists → Advanced Tips path. If no event → Quick Start path. Single branch, two emails.

---

## What's Parked (Post-Validation)

These patterns from the research are real but premature. Revisit after 30+ sales and confirmed $100+ AOV:

| Pattern | Source | Why Wait |
|---------|--------|----------|
| **Bridge product redesign** — Community as sustained bridge, not downsell | Cat Howell ($111/mo membership) | Need data on Community conversion and retention first |
| **Conditional payment** — Sprint as "$97 now, $200 after launch" | Miles Stutz | Need data on Sprint conversion rate at $297 first |
| **AI Coach concept** — Repeat-engagement mechanism replacing static PDF | Perry Belcher | Product already IS AI prompts — natural fit but needs validation data |
| **Setter model** — Human callers within 5-15 min of $27 purchase | Vazquez, Haynes, Abuvala | Start with manual DM for Sprint/Blueprint only. Scale to setter model if volume justifies it |
| **Multiple entry points** — Bumps as standalone front-ends | Cat Howell (already decided in scaling-architecture) | Same sequencing: validate → optimize → scale |

---

## What Changes

Reference files affected:
- `reference/core/offer.md` — Update email ascension system section: add ascension pressure to Days 5/7/9, add consumption tracking branch at Day 3, add accountability DM for Sprint/Blueprint buyers
- No new reference files needed — this extends existing architecture
- GHL implementation needed: consumption tracking workflow, DM notification trigger

