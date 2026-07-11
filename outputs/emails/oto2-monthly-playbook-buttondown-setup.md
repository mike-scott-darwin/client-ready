---
type: output
status: ready-to-build
date: 2026-07-11
product: OTO2 — The Monthly Playbook ($37/mo)
purpose: Click-by-click setup — GHL syncs buyers to Buttondown; Buttondown owns ALL subscriber email
architecture: A (GHL bills + owns the tagged list; Buttondown sends the newsletter)
depends_on: oto2-monthly-playbook-delivery.md (runbook), buttondown-poster.py (monthly send)
---

# Buttondown Setup — Click-by-Click

**Model:** GHL is plumbing only — it bills the $37/mo, holds the one tagged contact list, and **syncs each
buyer into Buttondown**. Buttondown owns **every** subscriber-facing email (the newsletter). No GHL emails
in the newsletter flow — one consistent sender.

Two things to build in GHL, both one-time:

1. **Subscribe webhook** — paid buyer → added to Buttondown with the paid tag
2. **Churn webhook** — cancel/fail → tag removed (stops the sends)

After this, your only recurring action is `python3 scripts/buttondown-poster.py --send` once a month.
Total build time ~15 min.

> **Plan:** **Basic ($9/mo)** is enough for this architecture — it unlocks tags + sending to the tagged
> list. (Standard $29 is only needed if you later want Buttondown to send an *automated* welcome email;
> we're deliberately not doing that — see "First issue" below.) Pricing: https://buttondown.com/pricing
>
> **Account note:** this is the shared Client Ready Buttondown account (`buttondown.com/Client_Ready`) —
> it also runs the free newsletter and holds unrelated tags (`elmproaudience`, `12 weeks coaching`, `au`,
> `us`). Paid issues send `private` (not in the public archive) and are filtered to the `monthly-playbook`
> tag, so paid content never reaches the free list. Keep every paid send filtered to that tag.

---

## 0. Tag — DONE ✅

Created + verified live 2026-07-11:
- **Name:** `monthly-playbook`
- **TAG_ID:** `sub_tag_635jft10559rxr9jt8mxgpg014`  ← used in the GHL webhooks below

The monthly poster resolves the name→ID automatically (only needs the name in `.env`). The GHL webhooks are
static, so they use the ID.

> **Firewall note (verified live):** the account's Buttondown **firewall** blocked a test signup
> (`subscriber_blocked`). Real GHL buyers should pass, but before launch confirm Buttondown → Settings →
> Firewall won't reject legitimate buyer emails from the webhook.

---

## 1. GHL Subscribe Webhook — paid buyer → Buttondown

**Automation → Workflows → + Create Workflow → Start from Scratch.** Name: `MP — Delivery`.

### Trigger
- **Contact Tag** (Tag Added) → `purchased-newsletter`

### Step 1 — Custom Webhook (the only step)
Click **+** → **Custom Webhook** (aka "Custom Webhook LC Premium").
Guide: https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `https://api.buttondown.com/v1/subscribers` |
| Headers → key 1 | `Authorization` |
| Headers → value 1 | `Token e071e1fe-8b6d-4dc2-a128-718dd5958c0b` |
| Headers → key 2 | `Content-Type` |
| Headers → value 2 | `application/json` |
| Body type | `JSON` / Raw |
| Body | ↓ |

```json
{
  "email_address": "{{contact.email}}",
  "tags": ["sub_tag_635jft10559rxr9jt8mxgpg014"]
}
```
- `{{contact.email}}` — use GHL's merge-field picker so it inserts the real token.
- Shape verified live 2026-07-11 (POST `/v1/subscribers`; `tags` takes tag IDs).

**Publish** the workflow (Active). That's the entire subscribe path — **no wait step, no email step.**

### No-code fallback
If Custom Webhook isn't on your GHL plan: GHL trigger → **Zapier/Make** → Buttondown "Create/Update
Subscriber" with tag `monthly-playbook`.

---

## 2. GHL Churn Webhook — cancel/fail → off the paid list

Stops sending paid issues to people who stopped paying.

**+ Create Workflow → `MP — Churn Sync`.**
- **Trigger:** Subscription Cancelled **OR** Payment Failed (final retry), filtered to The Monthly Playbook ($37/mo).
- **Step:** Custom Webhook to clear the tag:

| Field | Value |
|-------|-------|
| Method | `PATCH` |
| URL | `https://api.buttondown.com/v1/subscribers/{{contact.email}}` |
| Headers | `Authorization: Token e071e1fe-…` + `Content-Type: application/json` |
| Body | `{ "tags": [] }` |

- ⚠️ Confirm subscriber addressing (email vs ID) and PATCH tag behavior: https://docs.buttondown.com/api-subscribers-type
- Alternative: `DELETE /v1/subscribers/{{contact.email}}`, or a Zapier "remove tag" step.
- Keep `purchased-newsletter` on the GHL contact (historical + pitch-suppression) — only the Buttondown-side
  tag needs to go.

> If your billing doesn't expose a clean cancel trigger, fall back to a monthly manual pass: remove the tag
> in Buttondown for anyone GHL shows as cancelled. Low volume early; automate later.

---

## First issue / welcome — handled by Buttondown, not GHL

We deliberately **do not** send a GHL welcome email (that would be a second sender for a newsletter). On
**Basic $9**, a new mid-month buyer simply gets **the next issue on the 1st** — normal for a monthly paid
newsletter. The page/product copy says "first issue arrives on the 1st" to match.

- The **Community "first month free" CTA** lives in every issue's P.S. (sent by Buttondown), so it reaches
  subscribers without a separate GHL blast.
- If you later want an *immediate* welcome from Buttondown, upgrade to **Standard $29** and add a Buttondown
  Automation (trigger: tag `monthly-playbook` → send a "start here" email). Optional, not required.

---

## 3. Test protocol (before real traffic)

1. In GHL, add `purchased-newsletter` to a test contact (or run a test purchase).
   → Confirm the **subscribe webhook** returns 2xx and the contact appears in Buttondown with tag `monthly-playbook`.
   → If not: check Buttondown → Settings → **Firewall** isn't blocking it.
2. `python3 scripts/buttondown-poster.py` (draft) → review the draft in Buttondown → send to yourself.
   → Confirm markdown renders (table, blockquotes, swipe blocks) and it's `private` (not in public archive).
3. Trigger the churn workflow on the test contact → confirm the tag is removed in Buttondown.

If a webhook returns 400/401/403, the hint points to the fix (bad key, wrong plan, or tag-field schema).

---

## What you touch monthly
```
1. Write content/drafts/monthly-playbook/YYYY-MM-issue.md   (from the template)
2. python3 scripts/buttondown-poster.py --send
```
No GHL. No HTML. New buyers are already synced by the webhook and get the next issue on the 1st.

---

## Supporting links
- Buttondown email audience type (public/private/premium): https://docs.buttondown.com/api-emails-type
- Buttondown subscriber/tag schema: https://docs.buttondown.com/api-subscribers-type
- Buttondown pricing: https://buttondown.com/pricing
- GHL Custom Webhook action: https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action
- Runbook: [oto2-monthly-playbook-delivery.md](oto2-monthly-playbook-delivery.md)
- Monthly poster: `scripts/buttondown-poster.py`
- Issue template: [oto2-monthly-playbook-issue-template.md](../products/oto2-monthly-playbook-issue-template.md)
