---
type: output
format: canva-build-specs
date: 2026-07-04
platform: meta
---

# Canva Build Specs — Tier-1 Static Text Cards

**Two exports per card:** 9:16 (1080×1920) and 1:1 (1080×1080). Design the 9:16 first with all critical text inside the **center 1:1 safe zone** (the middle 1080×1080), then center-crop for the square. One design → two uploads.

**Brand kit (proposed — no visual-style.md exists yet, lock these):**
- Background: near-black `#0F0F0F` or deep navy `#0B1220`
- Primary text: white `#FFFFFF`
- Highlight: warm amber `#F5A623` (used sparingly — the ONE key phrase)
- Font: bold geometric sans (Anton / Montserrat ExtraBold for headline; Inter for subtext)
- Safe margins: 12% padding all sides; nothing critical in outer 15% (feed UI crop)
- **9:16 vertical safe zone:** keep text out of the top ~10% and bottom ~20% (Reels/Stories UI covers these)
- **OCR cap:** on-image text under ~20% of area. For frame-filling type ("1 AFTERNOON", "1 offer > 10 offers"), add generous margins so glyphs don't run edge-to-edge — cap height so text stays under the 20% threshold.

---

## 01_graphic (Concept 1 — Reversal)
- **Headline:** "I don't sell $5K packages."
- **Sub (amber):** "I sell a $27 system that sells the $5K for me."
- Layout: headline top third, amber line center, small "clientreadyoffer.com" bottom.

## 01_interrupt (Concept 1)
- Two-column: **EVERYONE ELSE** (grey) / **ME** (amber)
- Rows: "Chase → Get chased" · "Convince → Get bought"

## 02_graphic (Concept 2 — 3-Step)
- Vertical numbered list, big numerals:
  1. Read
  2. Run 5 AI prompts
  3. Send it today
- Footer amber: "One afternoon."

## 02_interrupt (Concept 2)
- Giant "1 AFTERNOON" fills frame; subtext under: "not 1 month."

## 03_graphic (Concept 3 — No Calls)
- **Headline:** "An offer that needs a sales call to explain"
- **Amber turn:** "isn't clear enough."

## 04_graphic (Concept 4 — Red Ocean)
- **On the photo (`images/cr_red_ocean_concept_01.jpg`): ONE short line only**, in the upper-third negative space → "You have an offer nobody understands." (keeps the photo under Meta's ~20% text limit)
- **Full two-line version** ("You don't have a marketing problem." / "You have an offer nobody understands.") → use on a **solid-background card**, NOT over the photo.

## 05_graphic (Concept 5 — Anti-Custom)
- **Headline:** "Stop customizing."
- **Amber:** "Start scaling."

## 05_interrupt (Concept 5)
- Oversized: "1 offer > 10 offers"

---

## Screenshots (no design needed — you own these)
- `01_lofi` — offer doc in Google Docs, one prompt visible (phone-shot framing)
- `02_lofi` — AI generating a zone-of-genius output, **zoomed for mobile readability**
- `04_lofi` — the demo's "unfair advantage" output frame

## AI images (generated, in `images/`)
- `cr_red_ocean_concept_01.jpg` — Concept 4 interrupt ✅
- `cr_calendar_prison_concept_01.jpg` — Concept 3 interrupt ✅

**OCR rule:** keep on-image text under ~20% of area (Meta delivery). Text cards are fine; on the two AI photos, overlay only a short headline in the reserved negative space.
