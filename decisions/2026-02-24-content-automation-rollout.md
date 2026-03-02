---
type: decision
status: codified
date: 2026-02-24
linked_research:
  - research/archived/2026-02-21-devon-openclaw-5-day-setup-skool.md
  - research/archived/2026-02-21-devon-autonomous-agents-skool.md
linked_decisions:
  - decisions/2026-02-03-content-strategy.md
  - decisions/2026-02-17-automation-phase-sequencing.md
---

# Content Automation Rollout — OpenClaw-Inspired Pipeline

## Context

Devon published a comprehensive guide on using OpenClaw + Main Branch for always-on content automation. The core idea: git repos as the operational spine, agents draft content, humans approve via messaging, content flows through `drafts/ → scheduled/ → published/`. Every step is a git commit.

Client Ready already has the business truth codified (voice, audience, offer, angles, hooks). What's missing is the pipeline to ship content consistently. The content strategy defines the cadence — 1 newsletter/week, 2 X threads, 3-5 LinkedIn posts, 3-5 daily tweets — but there's no system to produce and publish it.

## Decision

Adopt a three-phase content automation rollout, starting manual and graduating to always-on agents.

## The Phases

### Phase 0: Manual Pipeline (Now — Feb 2026)

**What:**
- Add `content/` directory to this repo with `drafts/`, `scheduled/`, `published/`
- Use `/organic` or Claude Code to batch-draft a week of content at a time
- Review in repo, then manually post via Typefully (X) and LinkedIn native
- Track performance manually in `content-strategy.md` Content Bank tables

**Cost:** $0 additional
**Time:** ~2-3 hours/week content production (down from 6-8 with manual writing)

**Why start here:**
- Validates the content cadence before automating it
- Builds a library of what works (hooks, formats, engagement patterns)
- No infrastructure overhead during launch week
- Performance data feeds Phase 1 strategy

### Phase 1: Scheduled Automation (Post-Launch — March 2026)

**What:**
- Connect Typefully for X scheduling (API-based, not just manual)
- Buffer or native scheduling for LinkedIn
- Beehiiv API for newsletter scheduling
- Agent drafts full week of content → saves to `content/drafts/`
- Human reviews, approves → moves to `content/scheduled/`
- Tools publish on schedule
- After posting → `content/published/` with engagement metadata

**Cost:** ~$30/mo (Typefully Pro + Buffer Free)
**Time:** ~1 hour/week review time

### Phase 2: OpenClaw Always-On (When Volume Justifies — Q2 2026)

**What:**
- DigitalOcean droplet ($12/mo) running OpenClaw
- Mounts this repo read-only (except `content/` write access)
- Agent checks for new research/decisions → drafts content automatically
- Sends drafts to Telegram for approval
- Morning brief with yesterday's performance
- Performance data feeds back into next strategy session

**Cost:** ~$87/mo (DO $12 + OpenRouter ~$75)
**Time:** ~15 min/day approvals via phone

**Trigger to enter Phase 2:** Consistent 4+ weeks of manual content shipping with measurable engagement data.

### Phase 3: Voice-Note Pipeline (When Proven — Q3 2026)

**What:**
- Home server with whisper-cpp for on-device transcription
- Voice memo → transcription → agent shapes into content using `voice.md`
- "Talk into phone at 6am, posts go out by 9am"
- Multi-agent: one for content, one for ad monitoring, one for community

**Trigger:** Phase 2 running smoothly for 4+ weeks, content quality validated.

## What Changes

1. **New directory:** `content/` added to repo root with `drafts/`, `scheduled/`, `published/` subdirectories
2. **content-strategy.md:** Next Actions updated — "Create first week of content" moves from TODO to in-progress
3. **Weekly workflow:** Monday batch-draft, Tuesday publish newsletter + repurpose, daily tweet posting
4. **Git tracking:** All content becomes version-controlled with dates and performance metadata

## Why This Over Alternatives

| Alternative | Problem |
|-------------|---------|
| Just post ad hoc | Inconsistent. Content strategy exists but nothing ships. |
| Jump straight to OpenClaw | Premature. No performance data to train the agent. No content history to pattern-match. |
| Hire a VA | Expensive for this stage. Voice is too specific. AI + human review is more aligned. |
| Use a social media tool only | Missing the git-tracking and feedback loop. Content disappears into the tool. |

## Key Principle from Devon

> "OpenClaw READS from your business repo. Business truth stays in the business repo."

This is already how Client Ready works. `reference/` is the canon. Content is derivative. The automation layer never touches the source of truth — it only reads from it and writes to `content/`.

## Risk

- **Content quality drift:** Mitigated by human review at every phase. Agent never publishes autonomously.
- **Over-automation too early:** Mitigated by phase gates. Each phase requires 4+ weeks of proven performance before graduating.
- **Voice consistency:** Mitigated by `voice.md` being comprehensive (250 lines of tone, patterns, anti-patterns, examples).

## Success Metrics

| Metric | Phase 0 Target | Phase 1 Target |
|--------|----------------|----------------|
| Content shipped/week | 5+ posts (any platform) | Full cadence (15+ touchpoints) |
| Newsletter sent | 1x/week | 1x/week automated |
| Review time | 2-3 hrs/week | <1 hr/week |
| Engagement growth | Baseline established | 20% MoM growth |

---

## Related Files

**Research:**
  - [2026-02-21-devon-openclaw-5-day-setup-skool.md](../research/archived/2026-02-21-devon-openclaw-5-day-setup-skool.md)
  - [2026-02-21-devon-autonomous-agents-skool.md](../research/archived/2026-02-21-devon-autonomous-agents-skool.md)

**Decisions:**
  - [2026-02-03-content-strategy.md](./2026-02-03-content-strategy.md)
  - [2026-02-17-automation-phase-sequencing.md](./2026-02-17-automation-phase-sequencing.md)
