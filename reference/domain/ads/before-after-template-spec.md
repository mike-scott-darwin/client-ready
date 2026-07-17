---
type: reference
subtype: image-ad-template
status: active
date: 2026-07-08
source: Miles Stutz Jul-2026 mining (100% static, containsAiMedia=false) + CR offer-clarity thesis
render_input: outputs/ad-creative/20260708-before-after-vague-clear.json
---

# `before-after` — Image-Ad Template Spec

New template for the render system (the one that produces `order-summary`, `imessage`, `typo` — clean HTML→image, NOT fal/AI). Add it alongside those.

## Why it exists
Miles's July scrape: **100% static, video retired, `containsAiMedia: false` on 30/30 ads.** He uses **zero AI images** — his creative is headline-as-image + long confession body. The AI `ladder` lifestyle photo (fal `flux/schnell`) is off-strategy on two counts (AI-generated + no message/proof). This replaces it with an honest, text-only transformation card in the brand's own voice.

## Template: `before-after`
Two stacked panels, transformation top→bottom. **No photos, no AI — pure type on brand background.**

**Data schema:**
```json
{
  "template": "before-after",
  "preset": "<slug>",
  "size": "1080x1350",
  "data": {
    "before": { "label": "BEFORE", "quote": "...", "caption": "..." },
    "after":  { "label": "AFTER",  "quote": "...", "caption": "..." },
    "footer": "..."
  }
}
```

**Layout / styling (match `order-summary` brand kit):**
- Background: cream `#F5F1E8` (same as order-summary)
- **BEFORE panel (top ~45%):** muted — grey text `#8A8A8A`, "BEFORE" label in grey, quote in a lighter/struck tone; subtle grey wash. Reads "dull."
- Divider: a downward arrow (↓) or thin rule, amber `#D99A2B`.
- **AFTER panel (bottom ~45%):** bright — quote in dark green `#1C3A2E` bold, "AFTER" label in amber `#D99A2B`, caption in dark. Reads "alive."
- **Footer:** small centered, dark green: the offer + price.
- Type: same bold sans as the other templates. Quotes are the hero — large. Captions small/muted.
- Safe zones: 12% padding; nothing critical in outer 15% (1:1 crop) or top-10%/bottom-20% (9:16).

## Ready-to-render preset — `vague-clear-offer` (Ad4)
See `outputs/ad-creative/20260708-before-after-vague-clear.json`:
- BEFORE: "I help coaches grow their business." · *vague. could mean 50 things. nobody buys.*
- AFTER: "I help coaches build a $5K+ offer so clear it sells without a sales call — in one afternoon." · *clear. you either want it or you don't.*
- Footer: "The Client Ready Offer System · $27"

Source: Michael's own origin story (offer.md / the live page). Honest — no fabricated proof.

## Canva fallback (if the render system can't add the template yet)
Two rectangles, cream bg. Top: grey "BEFORE" + the vague quote (greyed). Amber ↓. Bottom: dark-green bold AFTER quote + amber "AFTER" tag. Footer line. Export 1080×1350 (1:1 + 9:16).

## After rendering
Drop the PNG in `outputs/ad-creative/`, push, and the public raw-GitHub URL wires straight into Ad4 (both ad sets) via the API — swaps out the two `ladder` ads.
