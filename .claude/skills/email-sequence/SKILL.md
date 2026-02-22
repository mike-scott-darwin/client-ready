# Email Sequence

Draft GHL-ready email sequences for the Client Ready funnel.

Use when: adding emails for a new product, creating recovery sequences, updating welcome sequences, or adding standalone training delivery emails.

---

## Step 1: Read Reference Files

Read these before generating anything:

1. `reference/domain/funnel/email-rhythm.md` — architecture, timing, sequence types
2. `outputs/emails/README.md` — backend overview, sequence map
3. `reference/core/voice.md` — tone and signature phrases
4. `reference/core/offer.md` — value ladder for cross-sell bridges

## Step 2: Read an Existing Example

Read ONE existing sequence to match the format. Pick the closest type:

| Type | Example File |
|------|-------------|
| Welcome/Relationship | `outputs/emails/2-buyers-welcome-10-day.md` |
| Recovery (bumps) | `outputs/emails/3-buyers-recovery-bumps.md` |
| Recovery (OTOs) | `outputs/emails/3-buyers-recovery-otos.md` |
| Delivery | `outputs/emails/5-buyers-bump-delivery.md` |
| Broadcast | `outputs/emails/4-buyers-daily-broadcast.md` |
| Non-buyer | `outputs/emails/1-non-buyers-30-day.md` |

## Step 3: Triage Sequence Type

| Type | Trigger | Emails | Timing |
|------|---------|--------|--------|
| Delivery | Product purchased | 1-3 | Immediate or Day 0 |
| Recovery | Product NOT purchased | 3 | Days 2,4,6 (PM) |
| Welcome | New buyer | 10 | Daily (AM) |
| Broadcast | Day 11+ | Templates | Daily (AM) |

## Step 4: Gather From User

Ask for (skip any already provided):

1. **Which product** triggers this sequence?
2. **Sequence type** — delivery, recovery, welcome, or broadcast?
3. **How many emails?** (Standard: 1-3 delivery, 3 recovery, 10 welcome)
4. **Sequence prefix** — existing prefixes: BD (bump delivery), BR (bump recovery), OR (OTO recovery), CR (community recovery), DB (daily broadcast), BW (welcome), NB (non-buyer). Or a new prefix for standalone products.
5. **GHL tags** — what tags trigger/filter this sequence?

## Step 5: Generate Sequence

Follow this format (matches existing sequence files):

```markdown
---
type: reference
status: active
date: [YYYY-MM-DD]
purpose: [One line — what this sequence does]
trigger: [What event starts this sequence]
duration: [How many days]
---

# [Sequence Name]

**Trigger:** [What starts it]
**Goal:** [Primary objective]
**Tone:** [Voice reference]
**Emails:** [Count] over [duration]

---

## Sequence Overview

| Day | Subject | Focus | Ascension |
|-----|---------|-------|-----------|
| 1 | [Subject line] | [What this email does] | [Cross-sell or —] |
| 2 | [Subject line] | [What this email does] | [Cross-sell or —] |
[etc.]

---

## Day 1: [Email Title]

**Subject:** [Subject line — under 50 characters]

---

[Full email body copy. 200-400 words. Story-first, then offer.]

[Use Michael's voice: direct, specific, personal. Short paragraphs. No hype.]

---

**P.S.** [Optional — used for soft cross-sell or callback to main point]

---

## Day 2: [Email Title]

[Continue pattern for all emails in the sequence...]
```

## Timing Rules

From `email-rhythm.md`:

- Welcome/Value emails: **8:00 AM**
- Recovery/Upsell emails: **2:00 PM**
- Max **2 emails per day** to any contact
- Never stack recovery on the same day as delivery
- Check existing sequences before assigning days to avoid collisions

## The Daily Email Framework

For broadcast/ongoing emails:

- **Story (60%):** Personal story, client story, lesson learned
- **Offer (30%):** One product from the ladder, rotated
- **CTA (10%):** Single clear action

Rotation: Monday (front-end), Tuesday (value), Wednesday (bumps), Thursday (Blueprint), Friday (Accelerator), Saturday (story), Sunday (community)

## Step 6: Quality Checklist

- [ ] Subject lines under 50 characters
- [ ] Story before pitch in every email
- [ ] One CTA per email (not multiple offers)
- [ ] Voice matches `voice.md` — direct, no hype, story-first
- [ ] Cross-sell bridges match value ladder position
- [ ] Timing doesn't stack with existing sequences
- [ ] No banned words (revolutionary, incredible, etc.)
- [ ] No income claims or earnings promises
- [ ] GHL tags specified for each email trigger

## Step 7: Offer HTML Generation (Optional)

After the markdown sequence is approved, ask:

"Want me to generate the HTML per-email files for GHL? These go to `outputs/emails/[prefix]-sequence/[PREFIX]01-[slug].html`"

If yes, generate HTML files matching the format in existing sequence folders (e.g., `outputs/emails/bw-sequence/BW01-welcome-quick-win.html`).

## Output Path

Markdown sequence: `outputs/emails/[N]-[segment]-[slug].md`

HTML per-email files: `outputs/emails/[prefix]-sequence/[PREFIX]01-[slug].html`

## Recovery from Compaction

If resuming after context compaction: re-read `reference/domain/funnel/email-rhythm.md` for timing rules and `outputs/emails/README.md` for the sequence map. Check git log for in-progress work.
