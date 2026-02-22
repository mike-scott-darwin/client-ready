# Mine

Structured competitor intelligence mining for Client Ready.

Use when: analyzing competitor ads, mining email sequences, reviewing funnel structures, or extracting positioning patterns. Produces structured research files that feed `/think decide`.

Do NOT use for: general research (use `/think`), creating ads from existing research (use `/ads`), or analyzing your own performance.

---

## Step 1: Read Positioning Context

Read these to know what you're comparing against:

1. `reference/core/offer.md` — our positioning, value ladder, pricing
2. `reference/core/audience.md` — our audience, their language

## Step 2: Check Existing Competitor Profiles

List existing competitor research:

```bash
ls research/competitors/ 2>/dev/null
```

Known competitors with profiles:
- Miles Stutz — `research/competitors/miles-stutz.md`
- Cat Howell — `research/competitors/cat-howell.md`
- Hernan Vazquez — `research/competitors/hernan-vazquez.md`

Read the relevant profile before mining to build on existing knowledge.

## Step 3: Triage Mining Type

Ask the user what they're mining (or detect from context):

| Source | What to Extract | Output Suffix |
|--------|----------------|---------------|
| Ad library (screenshots or text) | Creative types, copy patterns, angle distribution, volume, CTA patterns | `-ad-library-mining.md` |
| Email sequences | Subject lines, story patterns, offer rotation, timing, CTA patterns | `-email-mining.md` |
| Funnel pages | Page structure, pricing, headline patterns, proof elements, guarantee | `-funnel-mining.md` |
| Instagram/content | Content types, posting frequency, engagement patterns, hooks | `-content-mining.md` |
| Transcript (video/podcast) | Key frameworks, positioning statements, tactical advice | `-transcript-mining.md` |

## Step 4: Read Existing Mining Example

Read ONE existing mining file to match the format:

| Type | Example |
|------|---------|
| Ad library | Search `research/` for files ending in `-ad-library-mining.md` |
| Email | Search `research/` for files ending in `-email-mining.md` |
| General | Any recent file in `research/` with `source: mining` in frontmatter |

## Step 5: Extract and Structure

Follow this template for ALL mining types:

```markdown
---
type: research
date: [YYYY-MM-DD]
source: mining
topics: [competitor-analysis, specific-topics]
linked_decisions: []
status: complete
---

# [Competitor Name] [Source Type] Mining

**Source:** [What was analyzed — e.g., "47 Facebook ads from Meta Ad Library, Feb 2026"]

**One-sentence summary:** [Distill the entire mining session into one line]

---

## Key Findings

[Structured tables and breakdowns. Use tables for data, not prose walls.]

### [Category 1 — e.g., Creative Types]

| Type | Count | % | Notes |
|------|-------|---|-------|
| ... | ... | ... | ... |

### [Category 2 — e.g., Copy Patterns]

[Continue with relevant categories for this mining type]

---

## Patterns

[What's working for them. 3-5 bullet points. Specific, not generic.]

- [Pattern 1 — with evidence]
- [Pattern 2 — with evidence]
- [Pattern 3 — with evidence]

---

## vs Client Ready

[How does this inform our approach? Where are we different? Where should we be?]

| Aspect | [Competitor] | Client Ready | Gap/Opportunity |
|--------|-------------|-------------|-----------------|
| ... | ... | ... | ... |

---

## What to Steal

[Specific actionable items. "Do X" or "Test Y" — not vague observations.]

1. **[Action]** — [Why and how to adapt it]
2. **[Action]** — [Why and how to adapt it]
3. **[Action]** — [Why and how to adapt it]

---

## Open Questions

[What needs further research. Each should lead to a next action.]

- [ ] [Question → suggested next step]
- [ ] [Question → suggested next step]
```

## Step 6: Update Competitor Profile (If Needed)

If this is the first mining session for a competitor, or findings significantly update the profile, offer to create/update `research/competitors/[name].md`.

## Step 7: Bridge to /think

After delivering the mining output:

"Mining complete. Ready to make decisions based on this? Run `/think decide` to document what changes."

## Quality Checklist

- [ ] One-sentence summary is genuinely one sentence (under 25 words)
- [ ] Tables used for structured data (not prose walls)
- [ ] "vs Client Ready" section is specific to our business, not generic
- [ ] "What to Steal" items are actionable — "do X" not "consider Y"
- [ ] Open Questions each have a suggested next step
- [ ] No raw data dumps — everything synthesized
- [ ] Source clearly identified (what, when, how much was analyzed)

## Output Path

Write to: `research/[YYYY-MM-DD]-[competitor]-[source]-mining.md`

## Recovery from Compaction

If resuming after context compaction: re-read `reference/core/offer.md` for positioning context and check `research/competitors/` for existing profiles. Check git log for in-progress work.
