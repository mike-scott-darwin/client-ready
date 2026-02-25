---
type: reference
status: draft
date: 2026-02-25
linked_research:
  - research/consolidated/openclaw-autonomous-agents.md
linked_decisions:
  - decisions/2026-02-24-content-automation-rollout.md
  - decisions/2026-02-03-content-strategy.md
---

# OpenClaw Automation Blueprint

How OpenClaw serves Client Ready — not a generic overview, but the specific jobs mapped to this business.

---

## What OpenClaw Does Here

OpenClaw is the execution layer. Client Ready's reference files (soul, offer, audience, voice) are the guardrails. The agent reads from reference and acts on content, ads, email, and community — but never touches the source of truth.

One sentence: OpenClaw turns the thinking work you already do in Claude Code into outputs that ship while you sleep.

---

## Job 1: Content Distribution Pipeline

The content strategy defines a newsletter-first system: weekly Beehiiv newsletter deconstructed into X threads, LinkedIn posts, and daily tweets. The content automation rollout decision documents four phases. OpenClaw handles Phase 2 and Phase 3.

**How it works:**

You run /organic or /newsletter in Claude Code. Drafts save to content/drafts/ and push to GitHub. OpenClaw detects new drafts (cron: git pull every 15 minutes). Agent sends each draft to Telegram for review. You reply yes, no, or edit from your phone. Approved content moves to content/scheduled/. Agent posts on schedule via Typefully (X), LinkedIn API, or Beehiiv API. After posting, content moves to content/published/ with engagement data. Morning brief includes yesterday's numbers.

**What already exists:** 13 drafts for week 1 (Feb 24 - Mar 2). Daily tweets, LinkedIn posts, X threads, and the first newsletter. The pipeline is ready for an agent to pick up and distribute.

**Cadence the agent manages:**

| Day | Newsletter | X | LinkedIn |
|-----|------------|---|----------|
| Monday | Draft queued | 3-5 tweets | — |
| Tuesday | Send | Thread + tweets | Adapted post |
| Wednesday | — | 3-5 tweets | Pillar content |
| Thursday | — | Thread + tweets | Behind the scenes |
| Friday | — | 3-5 tweets | Contrarian take |
| Weekend | Batch next week | Light | — |

**Autonomy tier:** Tier 1 (auto for reversible writes in content/). Human approves every post via messaging before it goes live.

---

## Job 2: Ad Performance Monitor

The ad strategy framework defines a three-stage pipeline: ABO testing, CBO winners, ASC scaling. Each has specific kill/scale thresholds.

**What the agent watches:**

- CPA above $150: flag for kill decision
- CPA below $80: flag for 20% scale increase
- $300 spent without a sale on any concept: alert to change the creative, not optimize it
- $20 spent per concept with no signal: flag as dead concept
- Bump conversion above 40%: flag as headline signal (pull that copy to front-end headline)
- AOV dropping below $90: alert before scaling

**How it works:** Agent pulls Meta Ads data via API (or Pipeboard integration). Compares against thresholds from the ad strategy framework. Sends alerts to Telegram with the specific threshold that triggered. Does not make changes to campaigns — only flags decisions for you.

**Autonomy tier:** Tier 0 (read-only). The agent observes and reports. You make every ad decision.

---

## Job 3: Email System Intelligence

GHL handles the email workflows (welcome sequence, bump recovery, OTO recovery, community recovery, daily broadcast). OpenClaw does not replace GHL. It adds a monitoring layer.

**What the agent watches:**

- Welcome sequence open rates by day (are Day 5/7/9 ascension emails performing?)
- Consumption tracking: what percentage of buyers access the portal by Day 3?
- Recovery sequence conversion: are declined bumps converting via email?
- Daily broadcast unsubscribe rate (signal for voice drift)
- Sprint/Blueprint purchase notifications for accountability DM trigger

**What the agent does:**

- Morning brief includes email metrics alongside ad and content metrics
- Flags when consumption rate drops below 50% (buyers not using the product)
- Flags when any recovery sequence outperforms the welcome sequence (signal to adjust timing)
- Reminds you to send accountability DMs within 48 hours of Sprint/Blueprint purchases

**Autonomy tier:** Tier 0 (read-only on GHL data). Tier 1 for filing metric summaries to the repo.

---

## Job 4: Morning Brief

A single Telegram message every morning with everything you need to decide where to spend your time.

**Client Ready morning brief contains:**

- Content queue: what is scheduled for today, what needs review in drafts/
- Ad performance: spend, CPA, AOV, any threshold alerts from Job 2
- Email metrics: open rates, recovery conversions, consumption rates
- Community: new Skool members, unanswered questions, upcoming calls
- Open decisions: any decision files in the repo that are still in draft status
- Git summary: what changed in the last 24 hours

**Cost:** Less than 5 cents per month. Uses a cheap model (Gemini Flash or Haiku).

---

## Job 5: Content Recycling

Once content/published/ accumulates 30+ posts with engagement data, the agent can identify patterns.

**What the agent does:**

- Ranks published content by engagement
- Identifies which hooks, pillars, and formats perform best
- Populates the Content Bank tables in content-strategy.md (currently empty)
- Suggests which content to recycle or expand into threads/newsletters
- Feeds performance data back into /think sessions

**Autonomy tier:** Tier 1 (writes to content-strategy.md Content Bank section only).

---

## Job 6: Voice-Note Pipeline (Phase 3 Only)

The voice dump process already exists in the domain reference. On the M1 Mac Mini with whisper-cpp, the agent can:

- Accept voice memos via Telegram
- Transcribe locally (audio never leaves the machine)
- Shape into content drafts using voice.md as the style guide
- Save to content/drafts/ for review

This is the "talk into phone at 6am, posts go out by 9am" workflow from the content automation decision.

**Requires:** M1 Mac Mini (Phase 3 hardware). Not available on DigitalOcean Phase 2.

---

## Job 7: Mid-Funnel Branding Automation

The ad strategy defines mid-funnel branding campaigns (engagement campaigns for through-play video views at $5/day per ad). After 50-100 front-end sales:

- Agent monitors video view completion rates
- Flags which videos get highest through-play
- Suggests rotation (swap out underperformers, add new content)
- Tracks frequency against the retargeting audience

**Autonomy tier:** Tier 0. Read and report only.

---

## Repository Access Model

Applied to Client Ready's specific directories:

| Directory | OpenClaw Permission | Why |
|-----------|-------------------|-----|
| reference/ | Read-only | Soul, offer, audience, voice are human-supervised |
| research/ | Read-only | Research informs agent but human writes it |
| decisions/ | Read-only | Decisions are human authority |
| content/drafts/ | Read/Write | Agent drafts, human reviews |
| content/scheduled/ | Read/Write | Approved content awaiting posting |
| content/published/ | Read/Write | Archived posts with engagement metrics |
| outputs/ | Read/Write | Generated batches |

The agent creates branches and opens PRs for anything outside content/ and outputs/. You review and merge from your phone.

---

## Deployment Path for Client Ready

| Phase | When | What | Monthly Cost |
|-------|------|------|-------------|
| Phase 0 (now) | Feb 2026 | Claude Code + manual posting | ~$100 (Claude subscription) |
| Phase 2 | When content ships consistently for 4+ weeks | DigitalOcean 1-Click + Telegram + Typefully | ~$87 ($12 DO + ~$75 API) |
| Phase 3 | When M1 Mac Mini arrives | Native OpenClaw + local inference + whisper-cpp | One-time hardware + ~$75 API |

Phase 1 (Terminal) is where you are now. Phase 2 skips to cloud because the content automation decision already defines the trigger: "Consistent 4+ weeks of manual content shipping with measurable engagement data."

Phase 2 adds Jobs 1-5 and 7. Phase 3 adds Job 6 (voice pipeline) and local model inference.

---

## What This Does NOT Cover

- Building the funnel (that is Claude Code + GHL, not OpenClaw)
- Writing reference files (that is /think, always human-supervised)
- Making strategic decisions (decisions/ stays human-written)
- Replacing GHL for email automation (GHL handles workflows, OpenClaw monitors)

OpenClaw is the monitoring and distribution layer. It does not think for you. It ships what you have already thought through.

---

## The Principle

From Devon: "You cannot give an AI agent guardrails you have not defined yet."

Client Ready has the guardrails. Soul, offer, audience, voice, content strategy, ad strategy, email architecture — all documented. The agent reads these files and acts within them. The more precise the reference, the better the agent performs.
