---
type: decision
status: active
date: 2026-07-04
trigger: Funnel analytics showed reframed bump hit 44.4% attach vs 14% on vague-named originals
linked_output: outputs/order-bumps/ghl-bump-copy.md
related: decisions/2026-07-04-front-end-27-digital-snack.md
---

# Decision: Revamp Order Bumps — Reposition (not rebuild) for Attach

> Bump **prices hold at $37 / $67 / $97.** Names, promises, and framing change to the pattern that already won. Ship as a checkout A/B (Variant C) against the current control.

## The evidence

Funnel analytics (2026-07-04), two live landing-page variants, same traffic:

| Bump | Framing style | Price | Attach |
|------|---------------|-------|--------|
| "Plug & Play Templates" / "Quick Win DM Scripts" (Variant A) | vague category name | $37/$67/$97 | **~14%** each |
| "AI Offer Extraction Prompt + 24-Hour Launch System" (Variant B) | mechanism + time-bound outcome | $37 | **44.4%** |
| "My Proven Low-Ticket Funnel + 30-Day Email Sequence" (Variant B) | mechanism + time-bound outcome | $27 | **22.2%** |

Same price, same traffic, **3× the attach** — the difference was positioning. Variant B's cheap bumps ($27–37) proved high attach but capped avg cart at $39; Variant A's expensive bumps ($97) had the price but 14% attach. **The synthesis: Variant B's framing on Variant A's prices.**

## What changed (framing only — content preserved)

Formula: **`[concrete AI/mechanism asset] + [time-bound done-for-you system]`**

| # | Was | Now |
|---|-----|-----|
| 1 ($37) | Quick Win DM Scripts | **First-Sale DM Scripts + 48-Hour Warm-List Cash Campaign** |
| 2 ($67) | Plug & Play Templates | **Plug & Play Sales Page Kit + 1-Hour AI Fill-In System** |
| 3 ($97) | The First $5K Client Playbook | **The $5K Client Close Scripts + 3 Real Annotated Calls** |

Each also gets one high-perceived-value add: Bump 1 → fill-in-the-blank first-message generator; Bump 2 → AI prompts that auto-fill templates from the offer doc; Bump 3 → lead with the 3 annotated real calls.

## Why (beyond the data)

- **Congruence:** the front-end sells "AI prompts → offer doc → warm list → sales." Each bump is now the buyer's literal next step (get the first sale → build the page → close the $5K client), mirroring the AI-prompt mechanism they just bought.
- **Model math:** at a $27 front-end, ~44/35/22% attach on $37/$67/$97 → **≈ $88 checkout AOV** = the self-liquidation target (see [front-end-27 decision](2026-07-04-front-end-27-digital-snack.md)).

## Guardrails

- **Hold the prices.** Do not drop to lift attach — cheap bumps cap avg cart (Variant B = $39).
- **It's a test.** Grounded in one winning data point, not proven at these prices. Run Variant C vs control, ≥30 orders/arm.
- **Watch:** per-bump attach (44/35/22% target) + blended avg cart (~$88 target). If the $67/$97 bumps stay near 14% after reframing, the ceiling is the *offer*, not the copy — replace, don't just rename.

## Not changed

Bump prices, underlying product contents, front-end ($27), OTOs, community ($47/mo). This is positioning + light value-adds only.
