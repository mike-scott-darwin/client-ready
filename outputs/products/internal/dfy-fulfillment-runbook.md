---
type: output
status: active
date: 2026-07-12
purpose: Repeatable SOP to fulfill the $197 DFY Offer Build using the Codify extraction method (/co-extract → co-* generate → review → deliver), and capture each build as Codify social proof.
supersedes_mechanism: scripts/dfy/webhook_server.py (reference stub — on_complete() does not deliver; not deployed)
related:
  - outputs/products/internal/dfy-offer-build-process.md
  - reference/domain/delivery/dfy-intake-questionnaire.md
  - outputs/dfy-upsell/system-prompt.md
  - outputs/emails/dfy-sequence/DFY01-intake.html
  - outputs/emails/dfy-sequence/DFY02-delivery.html
---

# DFY Fulfillment Runbook — the Codify way

**One line:** The $197 DFY Offer Build is a **Codify Snapshot for the buyer's offer**. Fulfill it by running the buyer's intake through `/co-extract` and the `co-*` generators — not the stubbed webhook. Every build leaves a real before/after artifact that becomes proof for Codify.

> **Why this, not the automation:** `scripts/dfy/webhook_server.py` is a reference stub (`on_complete()` only prints; nothing is deployed; there's no live GHL intake form). Rebuilding that pipeline is wasted effort when the Codify extraction machinery already exists and keeps Michael's review in the loop — which is the quality promise. This runbook IS the fulfillment path.

---

## The mapping (why /co-extract fits)

| DFY deliverable (from `system-prompt.md`) | Produced by |
|---|---|
| 1. Dream Client Blueprint (ICP) | `/co-extract` → the buyer's `audience.md` |
| 2. Validated Offer Document | `/co-extract` + `/co-think` → `offer.md` |
| 3. Ready-to-Send Sales Doc (warm, PRIMARY) | `/co-content` (or `/co-pitch`) from the codified offer |
| 4. Plug-and-Play Sales Page (cold) | `/co-landing` |
| 5. 5-Email Sequence | `/co-email` |
| 6. 5 Ad Hooks | `/co-ad` |

The buyer's 11 intake answers are the raw extraction. `/co-extract` turns them into a scoped context (offer / audience / voice), and each `co-*` skill reads that context to generate one deliverable — exactly how Codify runs, just scoped to one offer.

**Speed fallback:** `outputs/dfy-upsell/system-prompt.md` still does a one-shot generation of all six. Use it when you want a fast first draft, then refine with the `co-*` skills. The extraction path is the primary because it produces the reusable context artifact (the proof).

---

## Per-buyer workspace

One folder per build:

```
outputs/dfy-runs/<YYYY-MM-DD>-<buyer-slug>/
├── intake.md          # the 11 answers, verbatim
├── context/
│   ├── offer.md       # /co-extract output
│   ├── audience.md    # /co-extract output (= Dream Client Blueprint)
│   └── voice.md       # /co-extract output
├── deliverables/
│   ├── 1-dream-client-blueprint.md
│   ├── 2-offer-doc.md
│   ├── 3-sales-doc-warm.md
│   ├── 4-sales-page.md
│   ├── 5-email-sequence.md
│   └── 6-ad-hooks.md
└── proof.md           # before/after + follow-up capture (see Step 6)
```

Keep these out of the main funnel `reference/` — this is per-buyer context, not Client Ready's own.

---

## The loop

### Step 0 — Spot the buyer
Live trigger tag is **`cro-dfy-purchaser`** (NOT `purchased-dfy` — that scheme is doc-only, 0 contacts). Until the tag/workflow is reconciled, check for new `cro-dfy-purchaser` contacts manually (or watch the OTO1 purchase notification).

### Step 1 — Intake
The 11 questions live in `reference/domain/delivery/dfy-intake-questionnaire.md` (fields: `what_you_do, best_client, result, process, differentiator, story, pricing, stuck_point, client_language, failed_solutions, objections` + optional `content_links`). Paste the buyer's answers verbatim into `intake.md`. If they sent content links, run `/co-import` on them to enrich voice.

### Step 2 — Extract
Run `/co-extract` seeded with `intake.md`, scoped to the buyer's `context/` folder. Goal: `offer.md`, `audience.md`, `voice.md` filled to "Compounding," not "Draft." This is the Dream Client Blueprint + the offer's backbone.

### Step 3 — Generate the six
From the codified context, run each generator into `deliverables/`:
- `/co-content` (or `/co-pitch`) → **warm sales doc** (D3, the one they send today)
- `/co-landing` → **sales page** (D4, cold)
- `/co-email` → **5-email sequence** (D5)
- `/co-ad` → **5 ad hooks** (D6)
- Offer doc (D2) + Blueprint (D1) come straight from Step 2.

**Consistency rule (from `system-prompt.md`):** same offer name, mechanism, positioning, and language across all six. The warm sales doc and the cold sales page sell the SAME offer to different-temperature audiences — don't let them drift.

### Step 4 — Review (the quality gate)
Run Michael's checklist from `dfy-offer-build-process.md` (ICP feels like a real person, mechanism named, sounds like THEM, no invented testimonials, no income claims, price fits market, bridge to backend is natural). Spot-check, don't rewrite — if the extraction was good, edits are light.

### Step 5 — Package & deliver
Assemble the six into one Google Doc (comment access) + record the 2–3 min Loom. Deliver with the **`DFY02` template** (`outputs/emails/dfy-sequence/DFY02-delivery.html`) — email + portal copy, reply-to for the included revision. Drop the same doc into the buyer's GHL portal. (Delivery is email/portal-first; the community is the deploy-it-live invite, not the delivery path.)

### Step 6 — Capture the proof (do NOT skip)
This is what makes each build compound for Codify. In `proof.md`, record:
- **Before:** the 11 raw answers (vague idea).
- **After:** links to the six deliverables (codified offer + assets).
- **Speed:** intake-submitted → delivered timestamp (target < 48h).
- **Consent:** did they ok using it as an anonymized/named example?
- **Results (later):** at the 14-day and 30-day check-ins already in `dfy-offer-build-process.md`, log — did they send the warm sales doc? get hand-raisers? put the page live? make a sale? One quotable line from their reply.

Then run `/co-case-study` on `proof.md` when results land. This directly fills the **#1 gap in CLAUDE.md — testimonials.**

### Step 7 — Ascend to Codify
The DFY buyer just experienced a scoped Codify. That's the warmest possible Codify lead. At the 30-day mark (or when they hit a result), pitch the upgrade: *"We codified your offer. Now codify the whole business — every ad, email, and page run from your files."* This is the "here's what I did next" thread from the reactivation-202 draft and the 2026-06-28 codify-for-coaches decision. The DFY run list = the Codify prospect list.

---

## The compounding picture

```
$197 DFY  =  Codify Snapshot (your offer)
   │  produces → codified offer + 6 assets + a documented before/after
   │  proof feeds ↓                               ascension feeds ↓
Testimonials (fills CLAUDE.md #1 gap)     →   Codify (codify the whole business)
   │                                                    │
   └──────────── social proof for both ────────────→  Accelerator
```

Every fulfillment is a paid, at-scale Codify demo that manufactures its own proof.

---

## Time budget
~45–60 min/build (extract 15 + generate 20 + review 15 + package 10). Same order of magnitude as the current process, but the output is a reusable context vault, not a throwaway.

## Open wiring items (track separately)
1. **Tag scheme:** live = `cro-dfy-purchaser`; templates/docs assume `purchased-dfy`. Reconcile before any automation keys off it.
2. **No GHL intake form** (0 surveys live). Decide: GHL form → this runbook, or keep email-reply intake. Either way, answers land in `intake.md`.
3. **Confirm the live "OTO1 - DFY Build - Fulfillment Email"** — verify (UI/backend read) which template it sends, so the intake step (`DFY01`) isn't duplicated or missing.
4. **Retire** `scripts/dfy/webhook_server.py` from the "live plan" or clearly mark it experimental — this runbook is the fulfillment path of record.
