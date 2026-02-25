---
type: research
status: active
date: 2026-02-25
sources:
  - 2026-02-21-devon-autonomous-agents-skool.md
  - 2026-02-21-devon-openclaw-5-day-setup-skool.md
  - 2026-02-25-devon-drbang-iva-openclaw-review.md (Skool gist review)
  - 2026-02-25-devon-openclaw-setup-guide-gist.md (GitHub gist, 15 revisions)
topics: [openclaw, autonomous-agents, guardrails, model-routing, memory-architecture, infrastructure, content-automation]
linked_decisions:
  - decisions/2026-02-21-client-acquisition-machine-concept.md
---

# OpenClaw and Autonomous Agent Architecture

Consolidated research from Devon (Main Branch creator) across Skool posts, gist reviews, and the official OpenClaw + Main Branch setup guide. Covers the full deployment path from terminal to always-on autonomous business systems.

---

## What OpenClaw Is

Open-source autonomous AI agent. Shell commands, browser control, file I/O, memory, cron jobs. Runs on bare metal (your own computer) or cloud. The harness that turns LLMs into agents that act, not just respond.

**Core thesis:** "Main Branch is a thinking system. OpenClaw is how it runs while you sleep."

---

## The 3-Phase Path

| Phase | What | Cost | Setup |
|-------|------|------|-------|
| **1. Terminal** | Claude Code + Main Branch skills | ~100/mo (Claude subscription) | Local dev, manual invocation |
| **2. Personal Cloud** | OpenClaw on DigitalOcean 1-Click | 12/mo + API costs | 15-minute setup, 99.99% SLA, always-on |
| **3. Home Hardware** | OpenClaw on Mac Mini or MacBook Pro | One-time hardware + electricity + API | Total ownership, multi-agent, local inference |

Most people stay at Phase 2. Phase 3 exists for those who want total control.

**Phase 2 why DigitalOcean:** Official OpenClaw partnership, co-developed 1-Click image, 99.99% SLA with credits, no WebSocket timeouts (Railway has 15-min timeout that breaks always-on messaging), flat 12/mo (no usage surprises). Hetzner at 5/mo is an alternative but requires manual SSH + Docker Compose setup.

**Phase 2 to Phase 3 migration:** Same OpenClaw, different machine. Reference files, config, and workflow transfer directly. Get Mac Mini, install Tailscale, install OpenClaw natively, set up LaunchAgent, configure Telegram, clone business repo, set up auto-snapshot cron.

---

## Hardware Reality

| Setup | Specs | Role |
|-------|-------|------|
| Devon ("thoth") | 2018 MacBook Pro | OpenClaw server, clamshell on shelf, SSH + Tailscale |
| Dr. Bang-Iva ("iris") | Mac Studio M2, 64GB RAM, 2TB | OpenClaw server, local model inference, gateway |
| Mike (planned) | M1 Mac Mini | OpenClaw server, local inference (7B-13B quantized), 24/7 low power |

Devon's 2018 Intel cannot run local models. M1+ Apple Silicon can. Mike's M1 Mac Mini sits in the middle -- capable of local inference and 24/7 operation.

**Phase 3 honest tradeoff:** Internet outage = agent down. Power outage = agent down. No 99.99% SLA. Devon says "been fine." If guaranteed uptime needed, stay on DigitalOcean.

---

## Three Canons (Keep These Separate)

| Canon | Location | Content | Writer |
|-------|----------|---------|--------|
| **Business** | Main Branch repo | Offer, audience, voice, soul, research, decisions, content | Human (via Claude Code) |
| **Agent** | OpenClaw workspace | Agent personality, operational memory, tool configs (SOUL.md, AGENTS.md, MEMORY.md, TOOLS.md) | Agent |
| **Ops State** | State repo (Phase 3) | Redacted config snapshots, bake-off results, cron definitions, incidents, agent configs | Automated snapshots + PRs |

**Rule:** OpenClaw READS from business repo. Business truth stays in business repo. Agent behavior stays in workspace. Ops state stays in state repo.

**Important:** soul.md exists in TWO places with different purposes. reference/core/soul.md = business identity (why you do this). workspace/SOUL.md = agent personality (how it talks). Do not merge them.

---

## Content Flow Pipeline (How Automation Actually Works)

This is the bridge between Main Branch thinking and autonomous content distribution:

1. User runs /organic or /ads in Claude Code
2. Content saved to content/drafts/ and git pushed
3. OpenClaw detects new drafts (cron: git pull every 15 min)
4. Agent sends drafts to user for review (Telegram, Signal, WhatsApp, or Slack)
5. User replies "yes" / "no" / "edit: [change]"
6. Approved content moves to content/scheduled/
7. Agent posts on schedule (Typefully for X/LinkedIn, direct API for others)
8. After posting, content moves to content/published/ with engagement metadata
9. Morning brief includes yesterday's numbers and today's queue
10. Performance data feeds next /think session

**Repository write access strategy:**

| Directory | Permission | Why |
|-----------|-----------|-----|
| reference/, decisions/, research/ | Read-only | Identity work is human-supervised |
| content/drafts/ | Read/Write | Agent drafts, human reviews |
| content/scheduled/ | Read/Write | Approved content awaiting posting |
| content/published/ | Read/Write | Archived posts with engagement metrics |
| outputs/ | Read/Write | Generated batches |

**Recommended approach:** Agent creates branches and opens PRs. User reviews and merges from phone.

---

## Model Routing (Cost Architecture)

### Bakeoff Results (Devon, 150 test cases, 8+ models, ops/structure rubric)

- **Gemini 3 Flash Preview:** Won. 100% reliability. 1.6s average latency.
- **Grok 4 Fast:** Second. 0.20 per million tokens. 2M token context. "Stealth powerhouse."
- **Qwen 3.5+:** Top performer alongside Gemini and Grok (Feb 2026 results).
- **Sonnet 4.5:** Last on ops rubric. Most expensive. Still best for creative and complex reasoning.

### Devon's Model Aliases (OpenRouter)

| Alias | Model | Use Case |
|-------|-------|----------|
| fast | Gemini 3 Flash | Default daily work, briefs, background tasks |
| reasoning | Grok 4 Fast | Complex analysis, multi-step reasoning |
| creative | Kimi K2 | Personality-heavy, creative writing |
| haiku | Claude Haiku 4.5 | Heartbeats, cheap background checks |
| opus | Claude Opus 4.6 | Deep reasoning, complex orchestration |

**Cost control:** Set monthly cap on OpenRouter dashboard (Guardrails). Devon recommends starting at 75/mo.

### Kimi K2.5 Warning

Context overflow problem is real. Devon had a cascading failure: Kimi hit context limits, started looping, caused OpenRouter delivery failures, caused morning brief to fail. Fix is compaction config:

```json
"compaction": {
  "mode": "safeguard",
  "reserveTokens": 40000,
  "keepRecentTokens": 25000,
  "reserveTokensFloor": 25000,
  "memoryFlush": { "enabled": true }
}
```

### Codex Pattern

200/mo flat rate, unlimited. 34 investigation files produced autonomously. Nightly audits. Files its own GitHub issues. Runs investigation chains on reliability problems. Pattern: cheap models (Kimi, Grok) handle daily interactive work, Codex does the expensive analytical work.

### Venice (Optional Privacy Mode)

Private inference on open-source models (Llama, DeepSeek). Prompts never stored or logged. Use for sensitive notes or strategy.

---

## Security and Guardrails

### 4-Tier Autonomy Ladder

- **Tier 0:** Auto for read-only checks
- **Tier 1:** Auto for reversible writes in approved paths
- **Tier 2:** Ask first for service restarts and cron edits
- **Tier 3:** Break-glass requiring a literal confirmation string

**Test results:** Asked thoth to "delete X permanently" -- refused, required exact confirmation format. Vague creative prompt burned 0.33 and 294K tokens across 10 tool turns. Drove three new guardrails: channel pinning, token budgets, creative self-critique loops.

### Execution Security

Do NOT run tools.exec.security: full. Use tools.exec.ask: "on-miss" with pre-seeded approvals. Common commands auto-run after one-time approval. Unknown commands require confirmation. Safety net for hallucinated commands.

### Battle-Tested Agent Guardrails

1. **CLI-first:** Always use openclaw config set, never edit JSON directly (a Telegram subagent bricked the gateway by editing config files directly)
2. **Discovery before action:** Run openclaw docs "query" before unfamiliar operations
3. **Atomic operations:** Multi-file config changes through CLI for state sync
4. **Snapshot before changes:** Back up config before modifying
5. **Ambient observation:** Agents log anomalies, file GitHub issues. System self-heals.

### Critical CLI Pattern

openclaw gateway restart does NOT sync config token to LaunchAgent plist. If you rotate token and restart, service may start with old token. Use instead: openclaw gateway install --force (atomic update of both config and service definition).

### Network Security

| Layer | Phase 2 (Cloud) | Phase 3 (Home) |
|-------|-----------------|----------------|
| SSH | Key-only, fail2ban, port 22 closed to public | Tailscale mesh VPN only |
| Dashboard | Tailscale Serve (zero public) | Loopback-only bind (127.0.0.1) |
| Firewall | UFW (ports 80/443 only) | Tailscale (invisible to internet) |
| Sandbox | Docker sandbox mode: all | Native execution |
| Repo access | Read-only mounts (:ro flag) | Read-only mounts |

### CVE-2026-25253

OpenClaw Control UI authentication bypass (CVSS 9.8). On cloud VPS with public dashboard = critical. On home server with loopback binding + Tailscale = zero attack surface (service cannot receive internet connections).

### Additional Security

- Add ownerDisplaySecret to gateway config (HMAC owner-ID obfuscation)
- Set tools.exec.notifyOnExit: false (prevents exec metadata contaminating voice turns)
- File permissions: .env at 600, credential/agent/workspace dirs at 700
- No PATs on disk -- use gh CLI with device-code auth
- Domain HTTPS via Caddy + Let's Encrypt (public-facing only, not dashboard)

---

## Workspace Files (Instruction Size Matters)

Dr. Bang-Iva had 21KB across 7 workspace files. Devon says this is over the sweet spot.

**Devon's target:** ~7,600 chars total. Every cold start loads all workspace files. Bigger files = more cost per message AND cheaper models struggle more (they drown in context).

**Fix:** Trim workspace files to essentials. Move detailed references into memory search / RAG via extraPaths. Set agents.defaults.bootstrapMaxChars: 8000.

**Applicable to Claude Code:** Keep CLAUDE.md focused. Implementation details belong in reference files loaded on-demand, not in the instruction file that loads every message.

---

## Token Efficiency Settings

| Setting | What | Config Path |
|---------|------|-------------|
| Context pruning | Auto-cleans old tool results (older than 1 hour) | agents.defaults.contextPruning |
| Compaction | Summarizes old messages before token limit | agents.defaults.compaction.mode: "safeguard" |
| Memory flush | Saves important context before compaction | agents.defaults.compaction.memoryFlush.enabled: true |
| Message chunk limit | Caps message length | channels.CHANNEL.textChunkLimit: 3000 |

---

## Memory Architecture (Current and Roadmap)

### Current: Flat SQLite

Vector search finds things by keyword and semantic similarity. Cannot answer "what decisions are stale" or "what research hasn't been codified" or "what changed since last week." No relationships. No temporal awareness.

### Phase 1: QMD Backend (Next)

Local search sidecar with BM25 + vectors + reranking via Reciprocal Rank Fusion. Community reports "orders of magnitude better" than SQLite. Config change + install. Zero cost. 10+ open bugs to watch.

### Phase 2: Knowledge Graph Layer

Evaluating Graphiti (23K stars, bi-temporal, best temporal queries) vs Cognee (8K stars, native MCP, self-improving memory with RL-weighted edges, simpler setup). Both need Docker. Devon will run both against his corpus and ship the winner to members.

### Phase 2.5: Langfuse Observability

Self-hosted measurement layer. RAGAS scoring to prove whether knowledge graph actually improves quality. "If I can't measure it I can't ship it to members with confidence."

### Local Embeddings

embeddinggemma (300M model through Ollama). Completely local and free. M1+ Apple Silicon runs it easily. Alternative to OpenAI API embeddings (which cost tokens and send data off-network).

---

## Messaging Channels

| Channel | Privacy | Setup Time | Best For |
|---------|---------|-----------|----------|
| Telegram | Good | 10 min | Bot-native, rich formatting, multi-agent friendly |
| Signal | Highest (E2E + sealed sender) | 30-60 min | Private notes, strategy dumps |
| WhatsApp | Good (E2E) | 10 min | Quick setup, familiar interface |
| Slack | Standard | 15 min | Teams, multi-user, bot-to-bot |

**DigitalOcean gotcha:** Two config locations. /root/.openclaw/openclaw.json (CLI writes here) vs /home/openclaw/.openclaw/openclaw.json (gateway reads here). After any plugin/channel setup, verify config exists in both.

---

## Morning Brief System

Multi-card Telegram delivery. Urgency tiers: CRITIC, FLASH, IMMEDIATE, PRIORITY, ROUTINE.

**Cost:** 0.001 per run. Four cents per month.

**Delivers:** Open decisions needing attention, reference files updated in last 24 hours, recent git commit summary, suggested priorities.

**Heartbeat:** Proactive checks on schedule. Use Haiku model for 80% cost reduction. Active hours only (8am-10pm).

---

## Local Audio Transcription

Build whisper-cpp from source for privacy-first voice transcription. Audio never leaves the machine.

- DigitalOcean: Use tiny model (75MB)
- Phase 3 (Mac): Use small/medium model (more RAM available)

**Why local:** Cloud APIs are faster but voice data goes to their servers. For strategy dumps and private thinking, local is the correct choice.

---

## Autonomous Agent Capabilities (Demonstrated)

### System Maintenance

Devon said "explore this Apple Notes crash for me." Agent autonomously found crash logs, spawned sub-agents, identified Apple Intelligence bug, resolved before Devon's second message. "All that system needed was to know there was a problem."

### Content and Marketing

89 research files in 5 days. 12 decision documents. 16 PRs merged. "These 89 research files and 12 decisions ARE the content pipeline. Thoth distributes them. I approve."

### Self-Healing Patterns

Agents observe anomalies, file GitHub issues, run investigation chains on reliability problems. 34 investigation files produced autonomously by Codex.

---

## Notable Gotchas (from 80 documented)

- Google Voice numbers blocked from verifying new Google accounts
- Bot hallucinated a JSON config key, crashed OpenClaw, poisoned its own config file
- Voice transcription bug merged to main AFTER release was cut (timing gap)
- 17% of ClawHub marketplace skills are malicious (386 packages) -- "no community marketplace skills" guardrail
- Kimi K2.5 context overflow causes cascading failures (compaction config is the fix)
- Telegram subagent bricked the gateway by editing config JSON directly (drove CLI-first rule)
- openclaw gateway restart does not sync token to LaunchAgent plist (use install --force)

---

## Core Philosophy

**"Better input not better output."** The thinking system produces content. Not the other way around.

**"Extending the human, not replacing it."** Keep the human. Automate everything around them.

**"The caveat is guardrails."** Reference files (soul, offer, audience, voice) = the guardrail layer that keeps autonomous agents aligned to identity.

**"Main Branch is a thinking system. OpenClaw is how it runs while you sleep."**

---

## Relevance to Client Ready

**The content flow pipeline is directly applicable.** Mike already has content/drafts/ with 13 drafts for week 1. The OpenClaw pipeline would automate: detect new drafts, send for review via Telegram, post on approval, track metrics, feed back into /think. This is the bridge between the content automation decision and actual autonomous distribution.

**Phase 2 is an immediate option.** 12/mo DigitalOcean droplet can run the content pipeline before the M1 Mac Mini setup. 15-minute deploy. Could be running this week.

**Reference files ARE guardrails for autonomous systems.** What Client Ready teaches coaches to create (offer clarity, audience definition, voice codification) becomes the instruction set for AI agents.

**Content angle:** "You cannot give an AI agent guardrails you have not defined yet."

**Product ladder maps to autonomy tiers:**
- 47 system = define the engine / create guardrails (Tier 0)
- Sprint = build the machine with guidance (Tier 1-2)
- Blueprint = turnkey machine with guardrails baked in
- Future: AI agents maintain and optimize the machine (Tier 2-3)

**Workspace size principle applies to all AI instruction files.** Keep CLAUDE.md lean. Reference on-demand, not every message.

**Three Canons principle applies now.** Business repo (client-ready) is the spine. If/when OpenClaw runs, it reads from client-ready but writes only to content/drafts/ and outputs/. Reference, decisions, and research stay human-supervised.

---

## Quote Bank

- "Main Branch is a thinking system. OpenClaw is how it runs while you sleep."
- "All that system needed was to know there was a problem."
- "89 research files in 5 days. THIS IS NOT TOO MANY."
- "Better input not better output."
- "Everyone racing to remove the human. I'm keeping the human and automating everything around them."
- "Never edit openclaw.json directly. Always use the CLI."
- "The 'she's dumb' problem is workspace files too big, approval loops, and flat memory. All fixable."
- "If I can't measure it I can't ship it to members with confidence."
