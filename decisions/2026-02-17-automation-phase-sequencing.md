---
type: decision
date: 2026-02-17
status: superseded
urgency: normal
linked_research:
  - research/2026-02-17-devon-openclaw-automation-update.md
linked_decisions:
  - decisions/2026-02-15-openclaw-deployment-plan.md
  - decisions/2026-02-14-ecosystem-architecture-iron-strike.md
  - decisions/2026-02-03-content-strategy.md
---

# Automation Phase Sequencing — What to Steal from Devon's Build

## Situation

Devon shipped a 5-day sprint: OpenClaw on bare metal, 89 research files via parallel agents, morning brief system, content pipeline, and an intent-sniping pipeline on X. Some of this is directly useful for Client Ready. Most of it is premature. This decision sequences what matters and when.

Core principle: **launch first, automate second.** Devon is optimizing for leverage at scale. We're optimizing for first sales. Same philosophy, different phase.

## Decision: Three-Phase Automation Roadmap

### Phase 0: Pre-Launch (Now)

Do these before or alongside funnel launch. Zero infrastructure needed. Just thinking and documentation.

**1. Intent Sniping Keyword List**

Define the X/Twitter searches that surface our ideal buyers in real-time. These are people expressing the pains our ads target — but organically.

| Search Query | Maps to Angle | Expected Volume |
|--------------|---------------|-----------------|
| "don't know what to charge" coaching | Before the Funnel | Medium |
| "posting every day" "no clients" | Content Merry-Go-Round | High |
| "another course" coaching "didn't work" | Course Graveyard (one-liner cluster) | Medium |
| "coaching business" "side hustle" stuck | Before the Funnel | Medium |
| "high ticket" "how to price" | Clarity Unlock | Medium |
| "quit my job" coaching afraid | Before the Funnel P6/P7 | Low |
| "offer" "confusing" OR "unclear" coach | Clarity Unlock | Medium |

Start with 5-7 searches. Run them manually 1x/day for 10 minutes once funnel is live. Reply with value, not pitch. Link in bio does the selling.

**2. Content Pipeline Map**

Identify which existing research files become organic content:

| Research File | Content Angle | Platform | Format |
|---------------|---------------|----------|--------|
| Meta ads strategies 2026 | "What's actually working in ads right now" | X thread | Authority |
| ABO vs CBO campaign structure | "The testing structure nobody explains" | X thread | Education |
| Miles Stutz hot seat | "What I learned watching a $10M coach give feedback" | Skool post | Story |
| Cat Howell persuasion challenge | "The copywriting framework that changed my ads" | X post | Quick tip |
| Low-ticket to high-ticket ecosystem | "Why your $47 product isn't converting to high-ticket" | X thread | Problem agitation |

Don't produce these yet. Just map them. When OpenClaw deploys, this list becomes the content queue.

**3. Voice Rule Extraction**

Devon generated 14 voice rules from his editing process (7 emotional patterns, 7 anti-AI polish rules). Do the same for Client Ready:

- Review voice.md against actual written output
- Add anti-AI polish rules: if a sentence sounds like a landing page, rewrite it
- Add emotional reaction patterns specific to Michael's voice ("Wrong.", "Period, full stop.", parenthetical gut reactions)

This enriches voice.md and makes all future AI-generated content sound more human.

---

### Phase 1: Post-First-Sales (After 10+ Sales)

Requires a live funnel with real data flowing.

**4. Morning Brief Specification**

Define what goes in the daily brief once there's data to brief on:

| Card | Urgency | Content |
|------|---------|---------|
| Revenue | FLASH | Yesterday's sales, AOV, ad spend, ROAS |
| Ad Performance | PRIORITY | Top 3 and bottom 3 ads by CPA, any ad with CPA > 2x target |
| Funnel Health | PRIORITY | Checkout conversion rate, bump take rates, OTO conversion |
| Open Decisions | ROUTINE | Decision docs in draft status needing review |
| Content Queue | ROUTINE | Research files mapped but not yet converted to content |

Don't build this until there's real data. Spec it now so it's ready when OpenClaw deploys.

**5. Manual Intent Sniping on X**

Once funnel is live and there's somewhere to send people:
- Run the 5-7 searches from the keyword list daily
- Spend 10-15 minutes replying with value
- Track which searches generate profile visits and follows
- This is the manual version of what Devon is automating — do it by hand first to validate the approach

---

### Phase 2: Post-Validation (After 30+ Sales, Confirmed AOV)

This is when the OpenClaw deployment plan (decisions/2026-02-15) activates.

**6. OpenClaw Deployment**

Follow the existing deployment plan. Add Devon's learnings:
- Use his 80 gotchas document (available in Main Branch repo)
- Implement the 4-tier autonomy ladder from day one
- Start with Telegram for morning briefs (most bot-friendly per Devon's experience)
- Use the morning brief spec from Phase 1

**7. Automated Intent Sniping**

Upgrade manual X searches to automated:
- AI scout monitors the keyword list
- Drafts value-first replies
- Michael approves via phone (75 seconds per batch)
- Track conversion: reply → profile visit → funnel entry

**8. Content Distribution Pipeline**

- Research files auto-flagged as content candidates
- Drafts generated in Michael's voice (using enriched voice.md)
- Sent to phone for approval
- Published on schedule via Typefully or direct API
- Engagement data feeds back into research

---

### Phase 3: Post-Scale (After Consistent Revenue)

Park these. Revisit when monthly revenue is consistent and predictable.

| Item | What It Does | Why Wait |
|------|-------------|----------|
| Model bakeoff | Multi-tier routing for cost optimization | Saves money only at scale; one model works fine now |
| Algo scout | Extracts what X algorithm rewards in real-time | Need a content presence first — nothing to optimize yet |
| Multi-machine sync | Semantic search across devices | Only matters with always-on agent + high research volume |
| Bare metal migration | Move from DigitalOcean to own hardware | Phase 3 of graduation path in OpenClaw plan |

---

## What Changes

- No reference files affected yet — this is a sequencing decision
- `decisions/2026-02-15-openclaw-deployment-plan.md` remains the deployment blueprint; this decision adds phasing and Devon's learnings on top
- `decisions/2026-02-03-content-strategy.md` may need a content pipeline section when Phase 1 activates
- When Phase 0 items are completed, they become inputs to existing reference files (voice.md, content-strategy.md)

## Superseded (2026-02-27)

Phase 2 (DigitalOcean) killed. Content pipeline now runs as Phase 0 (Claude Code + Python scripts + launchd). Intent sniping keyword list and content pipeline map remain useful inputs but the phasing described here no longer applies. See decisions/2026-02-24-content-automation-rollout.md and reference/domain/openclaw-automation.md for current architecture.
