# Product Doc

Generate complete product documentation for new value ladder products.

Use when: adding a new standalone training, bump, OTO, or backend product. Produces the actual training content document — what the buyer reads after purchasing.

---

## Step 1: Read Reference Files

Read these before generating anything:

1. `reference/core/offer.md` — value ladder positioning, pricing, where this product sits
2. `reference/core/voice.md` — tone, signature phrases, anti-patterns
3. `reference/core/audience.md` — pain points, language, dream outcomes

## Step 2: Read an Existing Example

Read ONE existing product doc to match the format. Pick the closest tier:

| Tier | Example File |
|------|-------------|
| Front-end | `outputs/products/front-end-client-ready-offer-system.md` |
| Bump | `outputs/products/bump-1-quick-win-dm-scripts.md` |
| Standalone | `outputs/products/standalone-the-one-page-funnel.md` |
| OTO | `outputs/products/oto1-client-ready-sprint-4-week.md` |
| Backend | `outputs/products/backend-client-ready-accelerator.md` |

## Step 3: Gather From User

Ask for (skip any already provided):

1. **Product name** — what is it called?
2. **Price and tier** — front-end, bump, standalone, OTO, or backend?
3. **Deliverables** — what components does the buyer get? (3-7 items)
4. **Who it's for** — which sub-segment of the audience?
5. **Case study angle** — what problem does this solve? What's the story?
6. **Cross-sell bridge** — what comes next in the value ladder?

## Step 4: Generate Product Doc

Follow this exact structure (extracted from all existing product docs):

```markdown
# [Product Name]

**[One-line tagline — what they get + timeframe or outcome.]**

---

## What You Just Got

[2-3 paragraphs setting context. Where the buyer is right now. What this product gives them. Why it matters.]

Here's what's inside:

1. **[Component 1 Name]** — [One sentence describing the deliverable]
2. **[Component 2 Name]** — [One sentence]
3. **[Component 3 Name]** — [One sentence]
[etc.]

[Closing line. Usually "Let's go." or similar.]

---

## The Case Study: [Problem Statement as Title]

[Narrative section. 500-1500 words. Tell a real story that demonstrates the problem this product solves. Use Michael's voice — direct, specific, no fluff. End with the bridge to the solution.]

---

## Component 1: [Name]

[Detailed practical content for this component. Templates, frameworks, examples, step-by-step instructions. This is the actual training material — not marketing copy.]

---

## Component 2: [Name]

[Same depth as above. Each component gets its own full section.]

---

[Continue for all components...]

---

## What to Do Next

[Cross-sell bridge. 2-3 short paragraphs connecting to the next product in the value ladder. Not a hard pitch — a natural "if you want more" bridge.]
```

## Step 5: Voice Check

Before delivering, verify against `reference/core/voice.md`:

- [ ] Short sentences. No compound sentences with 3+ clauses.
- [ ] Deliverables, not features ("5 AI prompts that extract your genius" not "AI-powered extraction")
- [ ] No hype words: revolutionary, incredible, game-changing, transformative, unleash, unlock, skyrocket
- [ ] Signature phrases used naturally (not forced): "Wrong." / "Let's go." / "Test, validate, build."
- [ ] Engineering mindset — practical, specific, no hand-waving
- [ ] Anti-guru tone — honest about limitations, no income promises

## Output Path

Write to: `outputs/products/[tier]-[slug].md`

Naming convention:
- `front-end-[name].md`
- `bump-N-[name].md`
- `standalone-[name].md`
- `otoN-[name].md`
- `backend-[name].md`

## Recovery from Compaction

If resuming after context compaction: re-read `reference/core/offer.md` for value ladder context and the most recent product doc in `outputs/products/` for format reference. Check git log for any in-progress work.
