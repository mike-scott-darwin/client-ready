---
type: output
status: ready-to-ship
date: 2026-07-12
purpose: Standalone DFY Offer Build intake page — the intake MEDIUM referenced in the fulfillment runbook
related:
  - outputs/products/internal/dfy-fulfillment-runbook.md
  - reference/domain/delivery/dfy-intake-questionnaire.md
---

# DFY Intake Page

A self-contained, multi-step questionnaire page (`index.html`) — the intake **surface** for the $197 DFY Offer Build. Replaces the leaky email-reply intake. One file, no dependencies, no build step.

## What it does
- 11 core questions (one per screen) + optional content links + optional file upload, matching `reference/domain/delivery/dfy-intake-questionnaire.md` field names exactly (`what_you_do`, `best_client`, `result`, `process`, `differentiator`, `story`, `pricing`, `stuck_point`, `client_language`, `failed_solutions`, `objections`, `content_links`).
- Captures `full_name` + `email` first so the submission matches the GHL contact.
- Progress bar, Back/Next, autosaves to `localStorage` (a refresh never loses answers).
- On submit: **POSTs JSON to a GHL Inbound Webhook.** If the webhook is unset or fails, it falls back to a one-tap `mailto` with all answers — so an intake is **never lost**.

## Configure (2 values, top of the `<script>` in `index.html`)
```js
const CONFIG = {
  webhookUrl: "PASTE_GHL_INBOUND_WEBHOOK_URL_HERE",   // see below
  fallbackEmail: "michael@michaelscott.io",
  maxUploadMB: 2
};
```

### Get the webhook URL (GHL)
1. GHL → Automation → Workflows → **Create Workflow**.
2. Add trigger **"Inbound Webhook"** → copy the generated URL → paste into `webhookUrl`.
3. In that workflow: map inbound fields → contact custom fields (match on `email`), then add the fulfillment steps (notify Michael, tag, etc.).
4. Create matching **custom fields** in GHL for each question key so the answers store cleanly.

> Payload is flat JSON: `{ full_name, email, what_you_do, ..., objections, content_links, source, product, submitted_at }`. If a file is attached it's added as `content_file: { name, type, dataBase64 }` (small files only — over `maxUploadMB` the page tells them to paste a link instead; real file storage needs a backend, so links are the primary path).

## Host it
Static file — host anywhere:
- **Cloudflare Pages** (matches the `co-site` stack): drop `index.html` in, deploy, custom domain e.g. `build.clientreadyoffer.com`.
- Or GHL: paste the HTML into a GHL **Custom Page / funnel step** and use it as the **OTO1 thank-you page** (best — captures them at peak momentum right after purchase).
- Link the same URL from the `DFY01` email as the backup path.

## How it feeds fulfillment
Submission → GHL (custom fields) → you copy the answers into the buyer's `intake.md`, then run the [fulfillment runbook](../internal/dfy-fulfillment-runbook.md) (`/co-extract` → `co-*` → review → deliver). The field names are identical to `intake.md`, so it's a straight paste.

## Preview locally
Open `index.html` in a browser. With `webhookUrl` left as the placeholder, Submit exercises the email fallback — so you can test the full flow before wiring GHL.
