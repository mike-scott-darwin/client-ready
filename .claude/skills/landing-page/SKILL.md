# Landing Page

Generate GHL-ready landing page copy using the Hybrid VSL format.

Use when: building a landing page for a new product, rewriting an existing sales page, or creating page copy for a standalone training entering cold traffic.

Do NOT use for: OTO interrupt pages (captive audience, different format), bump checkout add-ons, or video scripts only (use /vsl).

---

## Step 1: Read Reference Files

Read these before generating anything:

1. `reference/domain/funnel/hybrid-vsl-reference.md` — THE framework (7 sections, 5-Second Test)
2. `reference/core/offer.md` — value ladder, pricing, positioning
3. `reference/core/voice.md` — tone, signature phrases
4. `reference/core/audience.md` — pain points, their language
5. `reference/proof/testimonials.md` — available social proof
6. `reference/proof/angles/main-angles.md` — messaging angles

## Step 2: Check Product Doc Exists

The product doc MUST exist before generating page copy. Check `outputs/products/` for the matching product doc.

If missing: "The product doc for [product] doesn't exist yet. Run `/product-doc` first — the landing page needs to reference the actual deliverables."

## Step 3: Read Existing Page Example

Read `outputs/pages/front-end-sales-page.md` to match the GHL-ready section marker format.

## Step 4: Gather From User

Ask for (skip any already provided):

1. **Which product?** — match to existing product doc
2. **Price and anchor price** — e.g., ~~$147~~ $57
3. **Which angle?** — from `reference/proof/angles/` or new
4. **Available proof** — testimonials, screenshots, results to include
5. **Ad headline** — for ad-to-page congruence (what headline is the ad using?)

## Step 5: Generate Landing Page Copy

Follow the 7-section Hybrid VSL structure. Output as GHL-ready copy with section markers.

```markdown
---
type: output
status: draft
date: [YYYY-MM-DD]
product: [Product Name]
format: Sales Page Copy (GHL Ready)
price: $XX
---

# [Product Name] — Sales Page Copy

**Instructions:** Each section below maps to a section on the GHL page. Copy-paste into the page builder. Notes in [brackets] are for you, not for the page.

---

## BANNER

[Launch pricing or urgency banner. Must be honest — no fake countdowns.]

---

## HERO SECTION

### Pre-headline

> [WHO THIS IS FOR — one line identifying the reader]

### Headline

> [TRANSFORMATION PROMISE — under 15 words. Must match ad headline.]

### Sub-headline

> [Who it's for + what they get + timeframe + one "without" statement. 2-3 sentences max.]

### CTA Button

> [ACTION — $XX]
> [Guarantee line]

---

## VIDEO OUTLINE

[Not the script — the outline for what the video should cover.]

- Hook (0-30 sec): [restate headline promise]
- Problem (30 sec - 2 min): [articulate their pain]
- Solution (2-5 min): [what the product is, walk through it]
- Proof (5-8 min): [results, screen share the product]
- CTA (last 30 sec): [scroll down and grab it]

---

## PROBLEM SECTION

[3-5 short paragraphs. Written like you're in their head. Use THEIR language from audience.md. Be specific — "spending 45 minutes on sales calls with people who ghost you" not "stuck."]

---

## SOLUTION SECTION

### How It Works

[3 steps max. Simple. Clear.]

**Step 1:** [Action] → [Result]
**Step 2:** [Action] → [Result]
**Step 3:** [Action] → [Result]

### What's Inside

[Components from the product doc, listed as deliverables with one-line descriptions.]

1. **[Component Name]** — [What it does for them]
2. **[Component Name]** — [What it does for them]
[etc.]

---

## VISUAL EVIDENCE

[Callouts for screenshots and GIFs. Be specific about what to capture.]

- [Screenshot: product component 1 — show the actual template/prompt/framework]
- [Screenshot: product component 2 — show it in use]
- [GIF: walkthrough of the product — 10-15 sec screen recording]

[Developer note: Real screenshots only. Not mockup generators, not stock photos. GIFs > static images.]

---

## SOCIAL PROOF

[Available testimonials from testimonials.md. Use specific results, not generic praise.]

> "[Direct quote with specific result]" — [Name], [Role]

[If no testimonials available for this specific product: use founder results or be honest — "This is new. Here's my guarantee instead."]

---

## CTA SECTION

### Price

> Only ~~$[anchor]~~ $[price]

### What You Get (Recap)

[Bullet list of all deliverables from the product doc]

- ✅ [Component 1]
- ✅ [Component 2]
- ✅ [Component 3]
[etc.]

### Guarantee

[30-day money-back or product-specific guarantee. Honest framing.]

### Button

> [CTA TEXT — $XX]

---

## DEVELOPER NOTES

[Implementation notes for the page builder. Key points about design, mobile, and compliance.]
```

## Step 6: Run 5-Second Test

After generating, evaluate the output against the 5-Second Test from `hybrid-vsl-reference.md`:

| # | Question | Pass? |
|---|----------|-------|
| 1 | Who is this for? | |
| 2 | Why am I here? | |
| 3 | Why should I care? | |
| 4 | Why should I believe? | |
| 5 | What do I do next? | |

If any fail, fix before delivering.

## Step 7: Quality Checklist

- [ ] Headline under 15 words, states transformation promise
- [ ] Headline matches the ad (ad-to-page congruence)
- [ ] Sub-headline includes who + timeframe + "without"
- [ ] Problem section uses THEIR language, not ours
- [ ] Components listed as deliverables, not features
- [ ] Visual evidence callouts describe real screenshots (not mockups)
- [ ] One CTA, one action, one button
- [ ] Price with anchor
- [ ] Mobile-first notes included
- [ ] No hype words (revolutionary, incredible, game-changing)
- [ ] No income claims

## Output Path

Write to: `outputs/pages/[tier]-[slug]-sales-page.md`

## Recovery from Compaction

If resuming after context compaction: re-read `reference/domain/funnel/hybrid-vsl-reference.md` for the 7-section framework and `outputs/pages/front-end-sales-page.md` for the GHL-ready format. Check git log for in-progress work.
