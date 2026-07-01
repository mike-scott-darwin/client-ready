---
type: output
product: Front-End Bonus
date: 2026-07-01
---

# Facebook Ad Tracking Setup

This is a setup guide, not a done-for-you service. Follow it once and your Facebook (Meta) ads will actually know when someone buys — which is the difference between spending blind and spending with data. It's written for a coach who is not technical. No code required beyond copy-and-paste.

---

## What the Pixel Is

The **pixel** is a small piece of tracking that lives on your pages. When someone visits your sales page, starts checkout, or buys, the pixel tells Meta what happened. That's how Meta learns which ads produce buyers and shows your ads to more people like them.

Without the pixel, Meta is guessing. With it, Meta optimizes toward actual purchases.

In practice, you don't hand-code anything. Meta gives you a pixel, and your page builder (like GHL) has a field where you paste the pixel ID. That's the whole install for most setups.

---

## What CAPI Is and Why It Matters

**CAPI (the Conversions API)** is server-side tracking. The pixel runs in the browser, and browsers block a lot of tracking now (iOS updates, ad blockers, privacy settings). When the browser blocks the pixel, Meta misses the event and thinks your ad didn't work — even when it did.

CAPI sends the same events from the server instead of the browser, so they don't get blocked. Running the pixel and CAPI together means Meta sees a much more complete picture.

**Why you care:**
- Fewer missed purchases = Meta optimizes better = lower cost per sale over time.
- It improves your "Event Match Quality" score, which can lower your CPMs (what you pay per 1,000 impressions).

Set up CAPI **before** you spend your first dollar on ads. In GHL and most modern builders, CAPI is a toggle or a built-in integration — you don't build the server piece yourself.

---

## The Key Events to Track

You only need three events for a low-ticket funnel. Each one marks a step in the buyer's path:

1. **View Content** — someone landed on your sales page. Tells you the ad is sending traffic.
2. **Initiate Checkout** — someone started the order form (step 1). Tells you the page is convincing people to begin buying.
3. **Purchase** — someone completed the order. This is the one that matters most; it's what Meta optimizes toward. Make sure Purchase passes the order value so Meta can also learn who spends more.

That's it. Don't over-complicate with a dozen custom events. These three tell the story: they saw it, they started, they bought.

---

## Step-by-Step Setup Outline

1. **Create a Meta Business account** at business.facebook.com if you don't have one.
2. **Open Events Manager** inside Meta Business and **create a pixel** (Meta may call it a "dataset"). Copy the pixel ID.
3. **Paste the pixel ID into your page builder.** In GHL, this is a tracking/pixel field in your funnel or site settings. This installs the pixel across your pages.
4. **Turn on CAPI.** In GHL, connect the Meta integration / enable the Conversions API toggle so events also send server-side. (If your builder needs a "Conversion Token" from Meta, you generate that in Events Manager and paste it in.)
5. **Map the three events:** confirm View Content fires on the sales page, Initiate Checkout fires on step 1 of the order form, and Purchase fires on the order confirmation / thank-you page. Make sure Purchase includes the dollar value.
6. **Test with Meta's Test Events tool** in Events Manager. Open your pages, run a real test purchase, and watch the three events appear. Confirm they show as received from both the browser (pixel) and the server (CAPI).
7. **Check Event Match Quality** in Events Manager after a few real events. Higher is better; passing email and name through helps.
8. **Only then start spending.** Tracking first, traffic second.

If an event doesn't show up in the test tool, fix that before launch. An untracked Purchase event is the most expensive mistake here — it means Meta can't optimize toward sales at all.

---

## The Metrics to Actually Watch

Ignore the vanity numbers. Watch these, and pull them from Stripe or GHL — not Meta, which tends to over-attribute:

| Metric | What it means | Rough target |
|--------|---------------|--------------|
| **CPA** (cost per acquisition) | Ad spend divided by purchases | Under ~$100 for this funnel; kill an ad above ~$150-200; scale one under ~$80 |
| **AOV** (average order value) | Total revenue divided by orders | $100-120 target (front end + bumps); don't scale ads until AOV is consistently $100+ |
| **Checkout conversion** | Completed purchases divided by checkout views | Around 30% on step 2 of the order form; below 20% means fix proof and friction |
| **Bump take-rate** | Orders with any bump divided by total orders | Roughly half of buyers taking at least one bump; individual bumps run lower |

A higher CPA is acceptable **only if** your bumps and any upsells lift AOV enough to absorb it. That's the whole reason bumps exist — they let you afford to pay more per buyer than a bare front-end product could.

One more diagnostic: if you see thousands of clicks at pennies each and no sales, that's usually junk traffic from the wrong regions — a targeting problem, not a tracking or page problem.

---

Tracking is plumbing. It isn't glamorous, but nothing downstream works without it. Set it up once, test it, then let the numbers make your decisions for you.
