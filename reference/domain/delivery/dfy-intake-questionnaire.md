---
type: reference
status: active
updated: 2026-07-04
---

# DFY Offer Build — Intake (5 questions + uploads)

**Purpose:** The minimal intake for DFY Offer Build ($197) and DFY Lite ($97). It
does not map one question per deliverable — it gives the **extractor**
(`scripts/dfy/dfy_seed_vault.py`, the headless `co-extract`) enough raw material
to build the four context files that every deliverable is then generated from.

**Design principle:** fewer, richer questions + **document uploads**. The
extractor synthesises messy input, so 5 broad questions beat 11 narrow ones, and
a buyer's real sales page / testimonial / call transcript is denser and more
authentic than a text box. Uploads **multiply** the answers — they don't replace
them. (This is the Codify `/co-import` pattern.)

**Form:** GHL form "Your Offer Builder — Quick Intake" · ~7 minutes.

---

## The 5 questions (+ a price line + a catch-all)

Each question has an **optional "…or upload something that shows this" dropzone**
(a GHL File Upload field). Accepts PDF, DOCX, TXT/MD, HTML, and images.

### 1. What do you do, and who do you do it for?
**Field:** `what_you_do` (long text)
**Upload:** current sales page / website / offer doc
Plus a short line:
**Field:** `pricing` (short text) — "What do you charge now, and what do you want to charge?"

### 2. Tell me about your best client — where they were before, where they ended up.
**Field:** `best_client` (long text) — "Include what they kept *saying* before they bought, in their exact words."
**Upload:** a testimonial, case study, or a real client DM/email

### 3. Walk me through how you actually get them that result.
**Field:** `process` (long text)
**Upload:** your framework / SOP / curriculum / onboarding doc

### 4. Why you — what's your story, and what makes your approach different?
**Field:** `story` (long text)
**Upload:** your About page / bio / a founder post

### 5. What makes people hesitate before buying — and what have they tried that didn't work?
**Field:** `objections` (long text)
**Upload:** sales-call notes / objection emails

### Catch-all: Anything else that sounds like you
**Field:** `content_links` (long text) — best posts, emails, a link to a call recording
**Upload:** drop any file that captures your voice

---

## Guidelines for buyers (put on the form)

- ~7 minutes. Be specific — first instinct is usually right.
- **Upload where you can** — your real materials make the output sharper than any answer.
- No wrong answers; honesty beats polish.
- Make at least Q1–Q3 count (they're the spine). New businesses: describe the
  person you'd most love to serve and your best hypothesis.

---

## Question → Context-file map

The intake feeds four context files (not deliverables directly). Two of the
files **are** deliverables 1 and 2.

| Question / field | offer.md | audience.md (**Deliv. 1**) | voice.md | soul.md |
|---|---|---|---|---|
| 1. What you do (`what_you_do`) | **x** | x | | |
| 1b. Price (`pricing`) | **x** | | | |
| 2. Best client (`best_client`) | transformation | **PRIMARY** | client language | |
| 3. Process (`process`) | **mechanism** | | | |
| 4. Story + edge (`story`) | differentiator | | | **PRIMARY** |
| 5. Hesitation + fails (`objections`) | **objections** | | | |
| Catch-all + uploads | proof | psychographics | **voice** | |

`offer.md` itself is **Deliverable 2 (Your Validated Offer)**.

---

## Uploads — how they flow through

- GHL **File Upload** fields produce file URLs in the form-submission payload.
- The webhook payload should carry those URLs. The seeder auto-collects any key
  ending in `_upload` or `_url` (plus an explicit `documents: [...]` list).
- The seeder fetches each file and passes it to the extractor as a native block:
  **PDF** → document block, **images** → image block, **TXT/MD/HTML** → text,
  **DOCX** → text (needs `python-docx`). Cap: ~25 MB/file.

---

## Automation

- Form is sent immediately after DFY purchase (GHL), in parallel with community
  access + Michael's DM — never gate intake behind the community. See
  `outputs/products/internal/dfy-offer-build-process.md` Steps 1–2.
- Form submission → GHL webhook → **seed per-buyer vault** (answers + uploads) →
  **generate deliverables 3–6** → Michael reviews → deliver.
- Pipeline + field keys: `scripts/dfy/README.md`. The extractor's prompt lives in
  `scripts/dfy/dfy_seed_vault.py`; generation in `dfy_build_campaign.py`.
