---
type: output
status: ready-to-build
date: 2026-07-11
product: OTO2 — The Monthly Playbook ($37/mo)
purpose: Full A-to-Z delivery runbook — how the paid newsletter gets SENT every month WITHOUT hand-pasting HTML into GHL
supersedes: the GHL-email-send version of this file (2026-07-11 draft)
depends_on: oto2-monthly-playbook-issue-template.md (content), ghl-workflow-setup.md (tag scheme)
---

# The Monthly Playbook — Delivery Runbook (A → Z)

**The problem this solves:** The $37/mo Playbook has billing but no fulfillment, and building/sending in
GHL means hand-pasting HTML into GHL's email builder every month (the MCP can't build it — it's authed to
the wrong sub-account and 403s on the buyers location). You do not want to be tied to that. This runbook
moves the **send** to Buttondown so you write once, in markdown, and never paste HTML again.

---

## 0. The decision: two clean architectures

There are exactly two ways to run a paid newsletter. Pick one.

| | **A — GHL bills, Buttondown sends** | **B — Buttondown bills AND sends** |
|---|---|---|
| Billing | GHL checkout (the $37/mo OTO bump) | Buttondown + Stripe |
| How they buy | One-click checkbox at the $27 checkout | Click a link, enter card |
| Sync needed | Yes — one GHL webhook (set up once) | None |
| Monthly work | Write markdown → send in Buttondown | Write markdown → send in Buttondown |
| GHL touched monthly? | No | No |
| Keeps the checkout OTO economics? | ✅ Yes | ❌ No (lower attach-rate) |
| Moving parts | Medium (one webhook) | Minimal |

**Recommendation: Architecture A.** It keeps the one-click checkout bump — which is the entire reason the
Playbook is OTO2 and where continuity attach-rate actually comes from — *and* still gets you out of monthly
HTML pasting, because the only GHL step is a one-time webhook. You never touch GHL for this again after setup.

**Choose B instead if** you'd rather have zero moving parts and are willing to trade the frictionless
checkout bump for "share a link." B is genuinely the simplest system that exists; it just converts worse
than a checkout OTO. If the Playbook stops being a checkout bump and becomes a "reply PLAYBOOK" / link
offer (which is how DB04 already pitches it), B is a fine fit.

Everything below builds **Architecture A** and notes where **B** diverges.

---

## Why Buttondown (not Beehiiv, not GHL)

| | Buttondown | Beehiiv | GHL email builder |
|---|---|---|---|
| Author in markdown | ✅ native | ⚠️ editor | ❌ paste HTML |
| Send via API (no paste) | ✅ **on Standard $29/mo** | ❌ **Enterprise only** | ❌ manual |
| Native paid subscriptions | ✅ Stripe, 0% cut | ✅ | via GHL products |
| Auto-hosted archive | ✅ free | ✅ | ❌ (you'd build it) |
| Already in your stack | ✅ (free newsletter capture) | ⚠️ (poster script) | ✅ (billing) |

Beehiiv's Create-Post API is **Enterprise-plan-only** — confirmed in `scripts/beehiiv-poster.py`'s own
docstring ("Beehiiv Create Post API requires Enterprise plan… On lower plans, the script generates HTML +
opens Beehiiv for manual paste") and in current Beehiiv docs. So Beehiiv keeps you pasting. Buttondown's API
is on all plans and paid features unlock at **Standard $29/mo**. Buttondown wins for the "no paste" goal.

> **Keep the paid list separate from the free newsletter.** Your free weekly "Client Ready Playbook" already
> uses Buttondown for capture. Do NOT mix the paid Monthly Playbook subscribers into that same list. Use a
> dedicated **tag** (`monthly-playbook`) and always send the paid issue to that tag only — or, safest, a
> separate Buttondown account for the paid product so a mis-send can never leak paid content to the free list.

---

## Architecture A — full build, step by step

### A. One-time: Buttondown setup (~20 min)
1. Buttondown account on **Standard ($29/mo)** — needed for API automation + paid features.
   Pricing: https://buttondown.com/pricing
2. Create a **tag** `monthly-playbook` (this tag = your paid send list).
3. Get your **API key** (Settings → Programming/API). Docs: https://buttondown.com/features/api
4. (Architecture B only) Connect Stripe + create the $37/mo paid plan:
   https://docs.buttondown.com/paid-subscriptions

### B. GHL billing stays exactly as-is
The $37/mo OTO checkout product already exists (Trigger 8 in `ghl-workflow-setup.md`:
*Payment Received → The Monthly Playbook ($37/mo) → add tag `purchased-newsletter`*). Nothing to change here.
GHL keeps doing what it's good at — billing the one-click bump.

### C. The sync webhook — GHL purchase → Buttondown subscriber (the ONLY new GHL step, one-time)
In the GHL buyers location, add a **Custom Webhook** action to the Monthly Playbook purchase workflow:
- Trigger: tag `purchased-newsletter` added (already fires on payment)
- Action: **Custom Webhook (LC Premium)** — GHL docs:
  https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action
  - Method: `POST`
  - URL: `https://api.buttondown.com/v1/subscribers`
  - Header: `Authorization: Token YOUR_BUTTONDOWN_API_KEY`
  - Body (JSON): the contact's email + the paid tag, e.g.
    ```json
    { "email_address": "{{contact.email}}", "tags": ["monthly-playbook"] }
    ```
  - Exact field names/schema: https://docs.buttondown.com/api-subscribers-type

That's the whole sync. Set once, runs forever. No MCP, no monthly GHL work.

> **No-code fallback if the Custom Webhook action isn't on your GHL plan:** route GHL → Zapier/Make →
> Buttondown "create subscriber." Same result. GHL outbound webhook overview:
> https://help.gohighlevel.com/support/solutions/articles/155000003299-workflow-action-webhook-outbound-

### D. Churn sync — cancel → remove from paid list
Second Custom Webhook, on **Subscription Cancelled / Payment Failed** (final retry) for the Monthly Playbook:
- Method: `DELETE` (or PATCH to remove the tag) against the subscriber
- Removes the `monthly-playbook` tag so the next send skips them
- Keep `purchased-newsletter` in GHL as the historical/suppression flag

### E. "First issue delivered immediately" — Buttondown welcome automation
Set a Buttondown **automation**: when a subscriber gets the `monthly-playbook` tag → send them the current
issue immediately. This replaces the GHL `MP01` email entirely and keeps the page's "first issue hits your
inbox immediately" promise — with zero HTML pasting. (Automations are part of the API-first feature set:
https://buttondown.com/features/api)

### F. Author the issue — markdown in the repo
Write each issue as markdown using `oto2-monthly-playbook-issue-template.md`. Save to
`content/drafts/monthly-playbook/YYYY-MM-issue.md`. Markdown means links, tables, and swipe blocks are
trivial (see "supporting links in every issue" below). No HTML, no builder.

### G. Send — one command or one click
- **Scripted (no paste at all):** POST the issue to Buttondown as a draft/email and send to tag
  `monthly-playbook`. Send-email API: https://docs.buttondown.com/api-subscribers-send-email
  (You can adapt `scripts/beehiiv-poster.py` into a `buttondown-poster.py` — the markdown-parsing and
  frontmatter logic is already written; only the API call changes. Buttondown's API actually supports this
  on your plan, unlike Beehiiv's.)
- **Or in the editor:** paste the markdown (not HTML) into Buttondown's composer, pick tag `monthly-playbook`,
  send. Still no HTML wrangling.

### H. Archive — free, automatic
Buttondown auto-hosts every sent issue at a public/tagged archive URL. That satisfies the product page's
"access to the full archive" promise with **zero extra build** — link the archive on the page. (This is the
gap the GHL path couldn't fill without building a portal tile.)

---

## Architecture B — the dead-simple version (if you drop the checkout OTO)
1. Buttondown Standard + Stripe, create the $37/mo paid plan (step A4).
2. Pitch it with a link — in the DB04 daily broadcast ("reply PLAYBOOK" → send the Buttondown paid link),
   on a page button, in the email footer.
3. Buttondown handles billing, delivery, archive, and cancellation. **No GHL, no webhook, no sync, no paste.**
4. Monthly: write markdown → send to paid subscribers. Done.

Trade-off: you lose the one-click checkout bump, so attach-rate drops. Everything else gets simpler.
Paid-subscriptions setup: https://buttondown.com/features/paid-subscriptions

---

## The new monthly ritual (~60–90 min, no GHL, no HTML)
1. Write the issue in markdown from the template (last week of the month).
2. Voice + compliance pass (see template).
3. Send to tag `monthly-playbook` — script or editor.
4. That's it. New buyers already auto-get the latest via the welcome automation (step E); the archive
   updates itself (step H). **Nothing to re-paste, nothing to sync manually.**

Compare to the old GHL path: no monthly HTML paste, no MP01 re-paste, no manual archive. The one-time webhook
buys you a permanently simpler month.

---

## Supporting links in every issue
Because issues are now markdown, link liberally — this is part of making a $37 issue feel complete ("full A
to Z"): link the swipe-file assets, the tools referenced, the relevant deeper resource, and the archive of
past issues. A reader should be able to act without leaving the email. The issue template's "Steal This"
section is where these links live.

---

## Migration from the GHL-paste plan
The earlier version of this file (and the `mp-sequence/*.html` files) built GHL-native sending. Under
Architecture A/B you don't need them for sending — Buttondown sends. Keep the HTML files only as:
- a content reference for the first issue's copy, and
- a fallback if you ever send a one-off through GHL.
The **content** (issue template + Issue #1) is platform-agnostic — it ports straight to Buttondown markdown.

---

## Full build checklist
- [ ] Buttondown Standard plan + `monthly-playbook` tag + API key
- [ ] (B only) Stripe connected + $37/mo paid plan created
- [ ] GHL Custom Webhook: `purchased-newsletter` added → POST create subscriber w/ tag `monthly-playbook`
- [ ] GHL Custom Webhook: cancel/fail → remove tag `monthly-playbook`
- [ ] Buttondown welcome automation: tag added → send current issue immediately
- [ ] First issue authored as markdown from the template
- [ ] Send path chosen (script `buttondown-poster.py` or editor)
- [ ] Archive URL linked on the product page
- [ ] Reconcile "first issue" copy on page + product doc (immediately, then 1st of month)
- [ ] Resolve Playbook-vs-Community content overlap (keep the written teardown exclusive to the Playbook)
- [ ] Test: buy → confirm subscriber lands in Buttondown w/ tag → welcome issue arrives
- [ ] Test: cancel → confirm tag removed → next send skips them

---

## Supporting links (all)
**Buttondown**
- API overview: https://buttondown.com/features/api
- Send email (API): https://docs.buttondown.com/api-subscribers-send-email
- Subscriber schema/types (API): https://docs.buttondown.com/api-subscribers-type
- Paid subscriptions (docs): https://docs.buttondown.com/paid-subscriptions
- Paid subscriptions (feature): https://buttondown.com/features/paid-subscriptions
- Pricing: https://buttondown.com/pricing

**GoHighLevel**
- Custom Webhook workflow action: https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action
- Outbound Webhook action: https://help.gohighlevel.com/support/solutions/articles/155000003299-workflow-action-webhook-outbound-

**Beehiiv (why we're NOT using it for send)**
- API create-post = Enterprise-only; see `scripts/beehiiv-poster.py` docstring in this repo.

**Repo**
- Issue template: [oto2-monthly-playbook-issue-template.md](../products/oto2-monthly-playbook-issue-template.md)
- Issue #1 (content): [mp-sequence/MP-issue-01-bump-stack.html](mp-sequence/MP-issue-01-bump-stack.html)
- Tag/trigger scheme: [ghl-workflow-setup.md](ghl-workflow-setup.md)
- Reusable poster to adapt: `scripts/beehiiv-poster.py`
- Live page fixes: [oto2-monthly-playbook-ghl-swap-sheet.md](../pages/oto2-monthly-playbook-ghl-swap-sheet.md)
