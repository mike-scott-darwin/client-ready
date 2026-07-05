---
type: output
subtype: ad-launch-playbook
status: canonical
date: 2026-07-05
supersedes: [launch-strategy.md, creative-guide.md]
linked_research:
  - research/2026-07-05-miles-creative-oldest-winners.md
---

# 🎯 Ad Launch — Single Source of Truth

**This is the one doc for launching Client Ready ads.** Offer, creative engines, copy, launch plan, compliance. Everything else in this folder is either the copy library (angle files) or archived history.

> Last validated against: `research/2026-07-05-miles-creative-oldest-winners.md` (live Miles Stutz ad-library teardown).

---

## 1. The Offer (what the ads sell)

| | |
|---|---|
| **Front-end** | **$27** — The Client Ready Offer System (buyer-acquisition price, not self-liquidating) |
| **Order bumps** | $37 DM Scripts · $67 Sales Page Kit · $97 Close Scripts (unchecked at launch) |
| **Promise** | Validate a $5K+ offer you won't abandon — in one afternoon |
| **Tagline** | The Coach Who Won't Tell You to Quit Your 9-to-5 |

Full funnel + economics: see root `CLAUDE.md`.

---

## 2. Creative System — two engines

We mirror the **formats that are Miles Stutz's oldest, highest-spend winners** (proven by longevity in his live ad library), rendered with OUR angles. His account reset 2026-06-04; the survivors are almost all **native screenshots + typographic cards, NOT stock photos.** Full teardown: `research/2026-07-05-miles-creative-oldest-winners.md`.

### Engine A — HTML→PNG templates (`scripts/ad-templates/`)
Text-exact native formats fal.ai can't render. Renders via installed Chrome, retina-crisp, ~2s each.

```bash
node scripts/ad-templates/render.mjs --list
node scripts/ad-templates/render.mjs --template imessage --preset all
node scripts/ad-templates/render.mjs --template order-summary --preset front-end-27
node scripts/ad-templates/render.mjs --template chatgpt --preset offer-clarity
node scripts/ad-templates/render.mjs --template typo --preset all
```
Copy lives in `scripts/ad-templates/content.json`; brand tokens in `brand.mjs`.

### Engine B — fal.ai / Flux (`scripts/fal-image.py`)
Photoreal lifestyle scenes (the one format that IS a real photo). Needs `FAL_KEY` in `.env`.

```bash
python3 scripts/fal-image.py --angle all --model schnell --num 4
```

### The 7 winning formats (mirrored)

| Format | Engine | Status |
|--------|--------|--------|
| iMessage convo (his #1 winner) | Template `imessage` | ✅ built |
| Value-stack "Order Summary" | Template `order-summary` | ✅ built |
| ChatGPT answer screenshot | Template `chatgpt` | ✅ built |
| Bold typographic card | Template `typo` | ✅ built |
| Gmail inbox (clarity moments) | Template `gmail` | ⬜ not built |
| "Breaking News" tabloid | Template `tabloid` | ⬜ not built |
| Handwritten note (lifestyle) | fal.ai | ⬜ not built |

All output → `outputs/ad-creative/` with a sidecar `.json` (reproducible swipe file).

---

## 3. Copy — the angle library

Ads pull copy from these files (do not write off-message copy — check `reference/proof/angles/main-angles.md`):

| File | Angle |
|------|-------|
| `before-the-funnel.md` | Before the Funnel (cold traffic positioning) |
| `clarity-unlock.md` | Clarity Unlock (testimonial-proven transformation) |
| `content-merry-go-round.md` | Content Merry-Go-Round (anti-content-treadmill) |
| `misalignment.md` | Misalignment / Alignment Engineer |
| `one-liners.md` | 33 one-liners → feed straight into `typo` cards |

**Template ↔ angle mapping** is baked into `content.json` presets (e.g. `imessage:one-afternoon`, `chatgpt:offer-clarity`, `typo:grow-into-pain`).

---

## 4. Launch Plan — Phase 1: Validate

**Goal:** confirm the $27 front-end sells to cold traffic before OTOs/automation/scaling.
**Budget:** $30/day · **Timeline:** 1–3 weeks · **Exit:** 10+ sales at CPA < $100, bumps 30%+ each.

**Funnel (build only this):** short-form sales page → checkout ($27 + 3 unchecked bumps) → thank-you page. No OTOs in Phase 1.

**Ad = sales page** during validation — 100% message congruence, no creative freedom yet (Miles's rule).

**Creative for first test (Radical Variance — separate ABO ad sets):**
1. `imessage` — one-afternoon
2. `chatgpt` — offer-clarity
3. `typo` — grow-into-pain
4. `order-summary` — front-end-27
5. fal.ai lifestyle (once handwritten format built)

Each: 1 short-form + 1 long-form primary on the same image (Miles's dual-length test).

**Pre-launch checklist:**
- [ ] Pixel + CAPI (server-side) live
- [ ] Sales page (short-form) live in GHL
- [ ] Checkout: $27 + 3 bumps wired in Stripe, bumps unchecked
- [ ] Thank-you page + portal access
- [ ] Welcome email sequence triggers on purchase
- [ ] End-to-end test purchase completed
- [ ] 4–5 creatives rendered (section 2)
- [ ] 1 ABO campaign, one ad set per creative concept

Phase 2 (scale) detail lives in the archived `launch-strategy.md` — do not open until Phase 1 exit criteria are hit.

---

## 5. Compliance — do not skip

- **No fabricated income claims.** We mirror Miles's *formats*, never his "$15K in 5 min" income copy. Use clarity/validation/transformation claims (per `main-angles.md` Counterintuitive Reveal rules).
- **⚠️ Unverified proof is BLOCKED:** "150+ coaches", "4.7/5 rating", "114 sales" — appear in several copy files (`content-merry-go-round.md`, `one-liners.md`, etc.). Do NOT run any ad using these until verified against Stripe/GHL.
- **Testimonials are from coaching, not the $27 product** — keep the disclosure in copy.
- The `order-summary` template's line-item prices are illustrative — confirm they map to real deliverables before running.

---

## 6. Known cleanup backlog
- Stale `$47` → `$27` fixed in active copy files (2026-07-05). Historical/archived files left as-is.
- Verify the blocked proof stats above, then unblock the P3 ads.
- Build the 3 remaining formats (gmail, tabloid, handwritten).
