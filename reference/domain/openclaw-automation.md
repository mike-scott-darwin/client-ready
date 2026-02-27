---
type: reference
status: draft
date: 2026-02-27
linked_research:
  - research/consolidated/openclaw-autonomous-agents.md
linked_decisions:
  - decisions/2026-02-24-content-automation-rollout.md
  - decisions/2026-02-03-content-strategy.md
---

# OpenClaw Automation Blueprint

How OpenClaw serves Client Ready -- not a generic overview, but the specific jobs mapped to this business.

---

## What OpenClaw Does Here

OpenClaw is the execution layer. Client Ready's reference files (soul, offer, audience, voice) are the guardrails. The agent reads from reference and acts on content, ads, email, and community -- but never touches the source of truth.

One sentence: OpenClaw turns the thinking work you already do in Claude Code into outputs that ship while you sleep.

---

## Phase 0 vs Phase 3

Phase 0 (now): Claude Code + Python scripts + launchd for scheduling. You create content in Claude Code, scripts post on schedule. Works for most jobs but requires your Mac to be open and has no approval loop from your phone.

Phase 3 (M1 Mac Mini): OpenClaw gateway running 24/7 with Telegram/Discord approval. Content distribution, monitoring, voice pipeline, morning briefs -- all running autonomously with human-in-the-loop via messaging. The M1 runs headless in clamshell mode as a dedicated agent workstation.

Phase 2 (DigitalOcean cloud) is skipped. The Feb 25 evaluation concluded that Claude Code + Python + launchd handles most jobs, and the M1 handles everything else. No cloud server needed.

---

## Job 1: Content Distribution Pipeline

The content strategy defines a newsletter-first system: weekly Beehiiv newsletter deconstructed into X threads, LinkedIn posts, and daily tweets. The content automation rollout decision documents four phases. OpenClaw handles this end-to-end on the M1.

**How it works:**

You run /organic or /newsletter in Claude Code. Drafts save to content/drafts/ and push to GitHub. OpenClaw detects new drafts (cron: git pull every 15 minutes). Agent sends each draft to a dedicated Content topic for review. You reply yes, no, or edit from your phone. Approved content moves to content/scheduled/. Agent posts on schedule via Typefully (X), LinkedIn API, or Beehiiv API. After posting, content moves to content/published/ with engagement data. Morning brief includes yesterday's numbers.

**What already exists:** 13 drafts for week 1 (Feb 24 - Mar 2). Daily tweets, LinkedIn posts, X threads, and the first newsletter. X API credentials, LinkedIn OAuth token, and Beehiiv API key are configured in .env. Python poster scripts exist for X and LinkedIn.

**Cadence the agent manages:**

| Day | Newsletter | X | LinkedIn |
|-----|------------|---|----------|
| Monday | Draft queued | 3-5 tweets | -- |
| Tuesday | Send | Thread + tweets | Adapted post |
| Wednesday | -- | 3-5 tweets | Pillar content |
| Thursday | -- | Thread + tweets | Behind the scenes |
| Friday | -- | 3-5 tweets | Contrarian take |
| Weekend | Batch next week | Light | -- |

**Autonomy tier:** Tier 1 (auto for reversible writes in content/). Human approves every post via messaging before it goes live.

---

## Job 2: Ad Performance Monitor

The ad strategy framework defines a three-stage pipeline: ABO testing, CBO winners, ASC scaling. Each has specific kill/scale thresholds.

**What the agent watches:**

- CPA above 150: flag for kill decision
- CPA below 80: flag for 20% scale increase
- 300 spent without a sale on any concept: alert to change the creative, not optimize it
- 20 spent per concept with no signal: flag as dead concept
- Bump conversion above 40%: flag as headline signal (pull that copy to front-end headline)
- AOV dropping below 90: alert before scaling

**How it works:** Agent pulls Meta Ads data via API (or Pipeboard integration). Compares against thresholds from the ad strategy framework. Sends alerts to Ops topic with the specific threshold that triggered. Does not make changes to campaigns -- only flags decisions for you.

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

A single message every morning with everything you need to decide where to spend your time. Runs at 5:00 AM via OpenClaw cron using a cheap model (Gemini 2.5 Flash-Lite or Grok 4 Fast).

**Client Ready morning brief contains:**

- Content queue: what is scheduled for today, what needs review in drafts/
- Ad performance: spend, CPA, AOV, any threshold alerts from Job 2
- Email metrics: open rates, recovery conversions, consumption rates
- Community: new Skool members, unanswered questions, upcoming calls
- Open decisions: any decision files in the repo that are still in draft status
- Git summary: what changed in the last 24 hours

**Cost:** Less than 1 cent per day using cheap model tiers.

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

## Job 6: Voice-Note Pipeline

The voice dump process already exists in the domain reference. With whisper-cpp on the M1, the agent can:

- Accept voice memos via Telegram/Discord
- Transcribe locally (audio never leaves the machine)
- Shape into content drafts using voice.md as the style guide
- Save to content/drafts/ for review in the Content topic

This is the "talk into phone at 6am, posts go out by 9am" workflow from the content automation decision.

**Performance:** whisper-cpp runs on Intel at 2-4 seconds per 30-second memo (CPU-only). M1 will be significantly faster with Metal acceleration. Model: ggml-base.en.bin (142MB).

---

## Job 7: Mid-Funnel Branding Automation

The ad strategy defines mid-funnel branding campaigns (engagement campaigns for through-play video views at 5/day per ad). After 50-100 front-end sales:

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

## Topics-Based Session Isolation

OpenClaw supports isolated conversation topics. Each topic has separate context, memory, and system prompt. For Client Ready:

| Topic | Purpose | System Prompt Focus |
|-------|---------|-------------------|
| **General** | Lightweight routing, thought capture, quick questions | Default voice, minimal guardrails |
| **Content** | Draft review, approval loop, posting confirmation | Voice-aware, self-critique guardrails, content-strategy.md loaded |
| **Ops** | Ad alerts, email metrics, morning briefs, diagnostics | Numbers-focused, safety ladder enforcement |
| **Research** | Think cycle support, research file creation | Reference-heavy, decision-linking prompts |

Each topic maintains completely separate context. A content approval conversation does not pollute the ops alert stream.

---

## Model Routing Strategy

Multi-tier architecture saves approximately 69% versus single-model. Based on Devon's Feb 2026 bakeoff results (150 test cases):

| Tier | Model | Purpose | Cost per 1M tokens (in/out) |
|------|-------|---------|---------------------------|
| Primary | Grok 4 Fast | Interactive default, content review | 0.20 / 0.50 |
| Fallback | Gemini 3 Flash Preview | Strong alternative when primary fails | 0.50 / 3.00 |
| Cheap | Gemini 2.5 Flash-Lite | Heartbeats, morning briefs, crons | 0.10 / 0.40 |
| Escalation | Sonnet 4.6 | Complex reasoning, cross-repo synthesis | 3.00 / 15.00 |

Nine model aliases configured. Daily bakeoff at 4:20 AM rotates candidates weekly based on reliability and cost.

---

## Deployment Path

| Phase | When | What | Monthly Cost |
|-------|------|------|-------------|
| Phase 0 (now) | Feb 2026 | Claude Code + Python scripts + launchd | ~100 (Claude subscription) |
| Phase 3 | When M1 Mac Mini arrives | Native OpenClaw + local inference + whisper-cpp | One-time hardware + ~52 API |

Phase 2 (DigitalOcean cloud) is skipped. Claude Code + Python + launchd handles most jobs during Phase 0. The M1 adds the always-on gateway, Telegram/Discord approval loop, voice pipeline, and autonomous cron suite.

**Trigger for Phase 3 setup:** M1 Mac Mini arrives and is connected to network.

---

## M1 Setup Guide (Day 1 Checklist)

Based on Devon's 12-day production setup (thoth workstation, Feb 2026). Adapted for Client Ready on M1 Mac Mini.

### Hardware Prep

- Connect M1 to power and ethernet (or WiFi)
- Enable Remote Login (SSH) in System Settings > General > Sharing
- Set Energy Saver to never sleep (display can sleep)
- Set networkoversleep to 1 (prevents SSH drops in clamshell mode)
- Assign static DHCP reservation on router
- Install Tailscale from Mac App Store (mesh VPN for remote access from phone/laptop)

### Software Stack

| Tool | Install | Notes |
|------|---------|-------|
| Node 22 | brew install node@22 | Required for OpenClaw. Keg-only -- needs PATH config |
| OpenClaw | npm install -g @anthropics/openclaw | Install globally for stable daemon |
| Ollama | brew install ollama | Local inference. M1 runs 8B models at ~20-30 tok/sec |
| whisper-cpp | brew install whisper-cpp | Installs as whisper-cli, not whisper |
| Git | Already installed | For repo sync |
| Python 3 | Already installed | For existing poster scripts |

### OpenClaw Configuration

Core settings for Client Ready:

- sandbox.enabled: false (full host access, mitigated via guardrails and tier system)
- tools.exec.ask: "on-miss" (requires approval for unfamiliar commands)
- bootstrapMaxChars: 8000 (workspace file loading budget)

### Workspace Files (under 10K chars total)

Create in the OpenClaw workspace directory:

- MEMORY.md (~2K) -- Persistent facts: Client Ready business context, API keys location, repo paths
- AGENTS.md (~2K) -- Operating contract: autonomy tiers, what to never do, priorities
- USER.md (~1K) -- Identity: Michael Scott, preferences, timezone (ACST)
- TOOLS.md (~1K) -- Infrastructure: repo paths, API endpoints, launchd agents, GHL webhook URLs
- SOUL.md (~700) -- Pointer to reference/core/soul.md with key principles extracted
- HEARTBEAT.md (~600) -- Health check protocol: what to verify, how often, where to report
- IDENTITY.md (~300) -- Agent name and personality

### Messaging Channel Setup

**Discord (recommended for fresh setups):** Components v2 supports buttons, select menus, modals, slash commands, and rich threading. Create a private server with 4 channels matching the topics structure.

**Telegram (proven stable):** Create a Telegram bot via BotFather. Set up a supergroup with 4 topics (General, Content, Ops, Research). Configure OpenClaw gateway on loopback-only (127.0.0.1:18789) with Telegram polling.

### Credential Management

- openclaw.json is authoritative for all config including channel tokens
- .env holds API keys only (OPENROUTER_API_KEY, plus existing X/LinkedIn/Beehiiv keys)
- Never store credentials in git repos, memory files, workspace files, or chat output
- Run openclaw doctor after any credential change
- chmod 600 for config files, chmod 700 for credentials directory

### Cron Schedule (Client Ready)

| Time | Job | Model | Cost/day |
|------|-----|-------|---------|
| 5:00 AM | Morning Brief (Job 4) | Cheap tier | ~0.002 |
| Every 15 min | Git pull + state push | Shell (no model) | 0 |
| 8:00 AM | Content queue check (Job 1) | Primary | ~0.001 |
| 9:00 PM | Daily metrics summary (Jobs 2, 3) | Primary | ~0.001 |
| 3:00 AM | Config backup | Shell (no model) | 0 |
| 4:20 AM | Model bakeoff | Python script | ~0.003 |

Full cron suite: approximately 0.007/day.

### Security Hardening

- Enable macOS firewall with stealth mode
- SSH: disable password auth, disable root login, allow only your user
- Disable ARD agent (allowInsecureDH: 0)
- Disable mDNS to prevent local network discovery
- Log redaction for sensitive tokens
- Tailscale ACLs: only your devices can reach the M1

### Day 1 Validation Checklist

1. SSH into M1 from laptop via Tailscale
2. openclaw doctor passes all checks
3. Send test message to Content topic -- agent responds
4. Send voice memo to General topic -- transcription returns
5. Trigger manual git pull -- agent confirms repo state
6. Run morning brief manually -- message arrives with correct sections
7. Post one test tweet via agent approval flow -- confirm post appears on X

### ClawHub Security Warning

17% of ClawHub marketplace skills flagged as malicious. 60% of exposed instances are RCE-exploitable. Only install skills from the official repository. Do not expose the gateway to the public internet.

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

Client Ready has the guardrails. Soul, offer, audience, voice, content strategy, ad strategy, email architecture -- all documented. The agent reads these files and acts within them. The more precise the reference, the better the agent performs.
