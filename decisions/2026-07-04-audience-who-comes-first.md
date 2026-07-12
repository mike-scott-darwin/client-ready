---
type: decision
slug: audience-who-comes-first
status: proposed
date: 2026-07-04
last-updated: 2026-07-04
topics: [audience, positioning, targeting, reconciliation]
needs: operator decision (Michael) — do not codify until confirmed
linked_research:
  - research/2026-07-04-miles-stutz-ad-library-mining.md
builds_on:
  - decisions/2026-07-04-clarity-sells-angle-territory.md
  - decisions/2026-07-04-follow-the-sophistication-curve.md
  - decisions/2026-06-28-codify-for-coaches-positioning.md
tensions:
  - reference/core/audience.md   # v2 (AI-literate codification) vs soul.md (coach-in-transition)
---

## Context

The Miles convergence sharpened CR's positioning on *what* and *why* (validate → alignment → honesty), but exposed an unresolved edge: **who does CR aim at first?** Two audience definitions coexist and don't describe the same person:

- **`soul.md` / `voice.md` / `testimonials.md`:** coaches in transition — real 9-to-5 expertise, can't package/validate an offer, "not cut out for this?" doubt. The 6 named testimonials are all this person. This is the market Miles competes in ("offer that sells itself").
- **`audience.md` v2:** AI-literate business owners ($100K–500K) with tool sprawl / prompt hoarding / "re-explain my business every session." Declared canonical by `2026-06-28-codify-for-coaches-positioning.md` — but that decision's customer-facing "codify your brain" play was **shelved 2026-07-01.** So v2 partly describes the buyer for an angle that no longer exists.

The cold front-end is pain-first, $47, "validate your offer" — which points squarely at the coach/expert, not the AI-knowledge-management operator. The new tool-fatigue angle is the one bridge to the AI-literate buyer.

## Options Considered

- **A: Coach/expert-in-transition first; AI-literacy is a *trait*, not a segment.** The buyer is a coach/expert with real skills who can't package or validate an offer — and who happens to be AI-literate (uses ChatGPT/Claude daily). Fold v2's AI-literacy into the soul.md buyer; reconcile audience.md so it stops describing a separate $100–500K knowledge-management operator.
  - Pros: aligns with soul/voice/testimonials/price/the Miles battleground and the whole brand story; resolves the drift honestly; the 5 AI prompts + tool-fatigue angle still make AI-literacy a live hook. One coherent person.
  - Cons: requires editing audience.md v2 (walk back part of the 6-28 "v2 is canonical" call).

- **B: AI-literate operator first (audience.md v2 as-is).** Keep v2 canonical; target the higher-revenue tool-fatigued operator.
  - Pros: higher-value buyer; v2 is already written.
  - Cons: mismatched with the shelved codify play, the pain-first $47 "validate your offer" front-end, the testimonials, and soul.md. The offer isn't built for "AI knowledge management" — it's built for "package + validate your offer." Highest incoherence risk.

- **C: Hold both; let the ad test decide.** Run the three angles as a natural A/B — absolution + offer-closes-itself skew coach-expert, tool-fatigue skews AI-literate — and let CPA/conversion pick.
  - Pros: data over opinion; we're about to run ads anyway.
  - Cons: not actually a positioning answer — reference files stay contradictory, so every downstream skill keeps generating for two different people until the data lands.

## Recommendation (proposed — needs Michael's call)

**A as the positioning default, using C as the validation mechanism.** Lead everything at the coach/expert-in-transition (soul.md), treat AI-literacy as a defining *trait* of that person (not a separate operator segment), and let the three-angle launch serve as the live test — with tool-fatigue as the deliberate probe of how far the AI-literate framing pulls. If tool-fatigue dramatically out-converts, revisit; otherwise reconcile `audience.md` v2 down to "the AI-literate coach/expert" and retire the orphaned $100–500K knowledge-management framing.

## Why

Four of five substrate files (soul, voice, testimonials, offer/price) and the competitive frame all point to the coach/expert. `audience.md` v2 is the outlier, and it's an outlier because it was written for a play that's been shelved. The cheapest way to resolve drift is to make the strongest-supported person canonical and demote the orphaned one — while still getting real data from the launch before touching the file.

## What Changes (only on Michael's confirmation)

- If **A**: reconcile `reference/core/audience.md` — reframe v2's AI-literacy as a trait of the soul.md coach/expert; retire the standalone "$100–500K knowledge-management operator" segment. Update `last-updated`. Flip this decision to `codified`.
- If **B**: realign soul.md/offer.md language to the operator; re-open the shelved codify angle. (High disruption — flagged, not recommended.)
- If **C only**: leave files as-is, tag the launch as the audience test, set a read date.

## Open Questions
- [ ] Michael: which person is CR *for* first? (A recommended.)
- [ ] If A: does audience.md v2 get reconciled now, or after the three-angle launch reads?
