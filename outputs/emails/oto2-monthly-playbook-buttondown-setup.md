---
type: output
status: ready-to-build
date: 2026-07-11
product: OTO2 — The Monthly Playbook ($37/mo)
purpose: Click-by-click setup — GHL→Buttondown sync webhooks + the Buttondown welcome automation (immediate delivery)
architecture: A (GHL bills the OTO, Buttondown sends)
depends_on: oto2-monthly-playbook-delivery.md (runbook), buttondown-poster.py (monthly send)
---

# Buttondown Setup — Click-by-Click

Everything that's a **one-time** setup for Architecture A. After this, your only recurring action is
`python3 scripts/buttondown-poster.py --send` once a month. Three things to build:

1. **Welcome automation** (Buttondown) — delivers "first issue immediately"
2. **Subscribe webhook** (GHL) — paid buyer → Buttondown paid list
3. **Churn webhook** (GHL) — cancel/fail → off the paid list

Do them in this order. Total time ~30 min.

> **⚠️ Plan prerequisite (verified against the live account 2026-07-11):** the Buttondown account
> (key `e071e1fe…` in `.env`) authenticates fine but is on the **Free plan**. Tags require **Basic**;
> API sending + the welcome automation + paid subscriptions require **Standard ($29/mo)**. On Free, tag
> creation returns `403 feature_disabled` and none of the three steps below will run. **Upgrade to Standard
> first:** https://buttondown.com/pricing
>
> Also confirm this is the right account for Client Ready's *paid* newsletter — it already holds unrelated
> tags (`elmproaudience`, `12 weeks coaching`, `au`, `us`), so keep the `monthly-playbook` list cleanly
> separated (or use a dedicated account) so paid content never leaks to another list.

---

## 0. Tag — DONE ✅

The paid tag already exists in the Client Ready Buttondown account (created + verified 2026-07-11):
- **Name:** `monthly-playbook`
- **TAG_ID:** `sub_tag_635jft10559rxr9jt8mxgpg014`  ← use this in the GHL webhooks below

The monthly poster resolves the name→ID automatically, so it only needs the name in `.env`. The GHL webhooks
are static, so they use the ID above.

> **Firewall note (verified live):** the account's Buttondown **firewall** blocked a test signup
> (`subscriber_blocked`). Real GHL buyers should pass, but before launch confirm your firewall settings
> (Buttondown → Settings → Firewall) won't reject legitimate buyer emails coming from the webhook.

---

## 1. Buttondown welcome automation — "first issue delivered immediately"

**Design choice:** the welcome email **links to the archive**, it does NOT embed the current issue. That
means you set it once and never touch it again — the link always resolves to your latest issue. (Embedding
would force you to re-edit this email every month, which is exactly the trap we're leaving.)

### Build it
1. Buttondown → **Automations** → New automation.
2. **Trigger:** subscriber tagged `monthly-playbook` (fires the moment the GHL webhook adds them).
   - If your plan triggers automations on *subscribe* rather than *tag*, that's fine too — the only people
     hitting this list are paid buyers synced from GHL, so subscribe == paid.
3. **Delay:** send immediately (0 minutes).
4. **Email:** paste the markdown below.
5. Set the archive link:
   - Buttondown → **Settings → Paid subscriptions / Archive** → copy your subscriber-facing archive URL.
   - Replace `{{ARCHIVE_URL}}` below with it. (Docs: https://docs.buttondown.com/paid-subscriptions)

### Welcome email (markdown — paste as-is)
```markdown
Subject: You're in — your first Playbook is ready

You're in.

The Monthly Playbook is one thing done well: each month, one play I actually ran — the
build, the real numbers, and the piece you can steal and use this week. No theory. No
predictions. What's working right now.

You don't have to wait for the 1st. **Your latest issue is here → [Read it now]({{ARCHIVE_URL}})**

Every issue lives in your archive at that same link, so bookmark it. The next one hits on
the 1st.

Reply and tell me what you're testing — I read every one.

— Michael

*The Monthly Playbook · $37/mo · Cancel anytime.*
```

> This one email replaces the GHL `MP01` HTML entirely. You never paste HTML for delivery again.

---

## 2. GHL Subscribe Webhook — paid buyer → Buttondown

Adds every $37/mo buyer to the Buttondown paid list, tagged. **One-time build in the GHL UI.**

### Where
GHL (buyers location `AKRQpXEUDgloSAbxzDmh`) → **Automation → Workflows** → open the workflow that fires on
the Monthly Playbook purchase (the one adding `purchased-newsletter`). If it doesn't exist yet, create it:
- **Trigger:** Tag Added → `purchased-newsletter`

### Add the webhook step
Click **+** → **Custom Webhook** (aka "Webhook — Premium" / "Custom Webhook LC Premium").
Guide: https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action

Fill in **exactly**:

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `https://api.buttondown.com/v1/subscribers` |
| Headers → key 1 | `Authorization` |
| Headers → value 1 | `Token YOUR_BUTTONDOWN_API_KEY` |
| Headers → key 2 | `Content-Type` |
| Headers → value 2 | `application/json` |
| Body type | `JSON` / Raw |
| Body | see below |

**Body (JSON):** — uses the confirmed tag ID (subscriber `tags` field takes tag IDs — verified live):
```json
{
  "email_address": "{{contact.email}}",
  "tags": ["sub_tag_635jft10559rxr9jt8mxgpg014"]
}
```
- `{{contact.email}}` — use GHL's merge-field picker so it inserts the real token for your account.
- Shape verified against the live API 2026-07-11 (POST `/v1/subscribers`).
  Schema ref: https://docs.buttondown.com/api-subscribers-type

Save. Set the workflow **Active**.

### No-code fallback
If Custom Webhook isn't on your GHL plan: GHL trigger → **Zapier/Make** → Buttondown "Create/Update
Subscriber" with tag `monthly-playbook`. Same result.
GHL outbound webhook overview: https://help.gohighlevel.com/support/solutions/articles/155000003299-workflow-action-webhook-outbound-

---

## 3. GHL Churn Webhook — cancel/fail → off the paid list

Stops sending paid issues to people who stopped paying.

### Where
New workflow, **Trigger:** Subscription Cancelled **OR** Payment Failed (after final retry), filtered to
**The Monthly Playbook ($37/mo)**.

### Add the webhook step
Custom Webhook, to **remove** the paid tag from the subscriber:

| Field | Value |
|-------|-------|
| Method | `PATCH` (partial update — clears the tag) |
| URL | `https://api.buttondown.com/v1/subscribers/{{contact.email}}` |
| Headers | same `Authorization: Token …` + `Content-Type: application/json` |
| Body | `{ "tags": [] }` |

- ⚠️ Buttondown addresses a subscriber by email or ID depending on API version — confirm the URL form and
  whether PATCH replaces vs merges tags: https://docs.buttondown.com/api-subscribers-type
- Alternative if PATCH-by-email isn't supported: `DELETE https://api.buttondown.com/v1/subscribers/{{contact.email}}`
  to remove them entirely, or use the Zapier "Unsubscribe/Remove tag" action.

In GHL, also keep `purchased-newsletter` on the contact (historical + pitch-suppression) — only the
Buttondown-side tag needs to go.

---

## 4. Test protocol (do this before real traffic)

1. In Buttondown, create a test subscriber (your own alt email), add tag `monthly-playbook` manually.
   → Confirm the **welcome automation** fires and the archive link works.
2. In GHL, run the purchase workflow against a test contact (or add `purchased-newsletter` manually).
   → Confirm the **subscribe webhook** returns 2xx and the contact appears in Buttondown with the tag.
3. `python3 scripts/buttondown-poster.py` → review the draft in Buttondown → send to just the test tag.
   → Confirm formatting (markdown renders, table + swipe blocks look right).
4. Trigger the churn workflow on the test contact.
   → Confirm the **churn webhook** removes the tag and the next send skips them.

If any webhook returns 400/401/403, the poster/webhook hints point to the fix (bad key, wrong plan, or the
tag-field schema). Fix once, never again.

---

## What you touch monthly (for reference)
Just this:
```
1. Write content/drafts/monthly-playbook/YYYY-MM-issue.md   (from the template)
2. python3 scripts/buttondown-poster.py --send
```
No GHL. No HTML. No re-paste. The welcome automation + archive handle new buyers automatically.

---

## Supporting links
- Buttondown paid subscriptions: https://docs.buttondown.com/paid-subscriptions
- Buttondown subscriber/tag schema: https://docs.buttondown.com/api-subscribers-type
- Buttondown email create/send: https://docs.buttondown.com/api-emails-create
- GHL Custom Webhook action: https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action
- Runbook: [oto2-monthly-playbook-delivery.md](oto2-monthly-playbook-delivery.md)
- Monthly poster: `scripts/buttondown-poster.py`
- Issue template: [oto2-monthly-playbook-issue-template.md](../products/oto2-monthly-playbook-issue-template.md)
