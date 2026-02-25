---
type: research
status: active
date: 2026-02-25
sources:
  - 2026-02-21-devon-autonomous-agents-skool.md
  - 2026-02-21-devon-openclaw-5-day-setup-skool.md
  - 2026-02-25-devon-drbang-iva-openclaw-review.md (Skool gist review)
topics: [openclaw, autonomous-agents, guardrails, model-routing, memory-architecture, infrastructure]
linked_decisions:
  - decisions/2026-02-21-client-acquisition-machine-concept.md
---

# OpenClaw and Autonomous Agent Architecture

Consolidated research from Devon (Main Branch creator) across multiple Skool posts and a gist review of Dr. Bang-Iva's OpenClaw setup. Covers the practical reality of running autonomous business systems.

---

## What OpenClaw Is

Open-source autonomous AI agent. Shell commands, browser control, file I/O, memory, cron jobs. Runs on bare metal (your own computer) or cloud. The harness that turns LLMs into agents that act, not just respond.

---

## Hardware Reality

| Setup | Specs | Role |
|-------|-------|------|
| Devon ("thoth") | 2018 MacBook Pro | OpenClaw server, clamshell on shelf, SSH + Tailscale |
| Dr. Bang-Iva ("iris") | Mac Studio M2, 64GB RAM, 2TB | OpenClaw server, local model inference, gateway |
| Mike (planned) | M1 Mac Mini | OpenClaw server, local inference (7B-13B quantized), 24/7 low power |

Devon's 2018 Intel cannot run local models. M1+ Apple Silicon can. Dr. Bang-Iva's 64GB M2 has the most headroom. Mike's M1 Mac Mini sits in the middle -- capable of local inference and 24/7 operation.

---

## Model Routing (Cost Architecture)

### Bakeoff Results (Devon, 150 test cases, 8 models, ops/structure rubric)

- **Gemini 3 Flash Preview:** Won. 100% reliability. 1.6s average latency.
- **Grok 4 Fast:** Second. 0.20 per million tokens. 2M token context. "Stealth powerhouse."
- **Sonnet 4.5:** Last on ops rubric. Most expensive. Still best for creative and complex reasoning.

### Devon's Current Routing

| Task Type | Model | Cost |
|-----------|-------|------|
| Daily interactive work | Kimi K2.5 (free via NVIDIA) or Grok 4 Fast | Free to 0.20/M tokens |
| Morning brief synthesis | Grok 4 Fast or Kimi K2.5 | 0.001 per run |
| Heavy lifting (audits, investigations, multi-file refactors) | Codex (200/mo unlimited) | Flat rate |
| Creative/complex reasoning | Sonnet 4.5 | Premium |
| Cron health checks | Local model or Gemini Lite | Zero to near-zero |

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

Set this before it bites you.

### Codex Pattern

34 investigation files produced autonomously. Nightly audits. Files its own GitHub issues. Runs investigation chains on reliability problems. The pattern: cheap models handle daily work, Codex does the expensive analytical work that would eat through API credits on OpenRouter.

---

## Security and Guardrails

### 4-Tier Autonomy Ladder

- **Tier 0:** Auto for read-only checks
- **Tier 1:** Auto for reversible writes in approved paths
- **Tier 2:** Ask first for service restarts and cron edits
- **Tier 3:** Break-glass requiring a literal confirmation string

**Test results:** Asked thoth to "delete X permanently" -- refused, required exact confirmation format. Vague creative prompt (generate a profile picture) burned 0.33 and 294K tokens across 10 tool turns. That single test drove three new guardrails: channel pinning, token budgets, and creative self-critique loops.

### Execution Security

Devon's recommendation: do NOT run `tools.exec.security: full` (wide open). Use `tools.exec.ask: "on-miss"` with pre-seeded approvals. Common commands get one-time approval, then auto-run. New/unknown commands require confirmation. Safety net for hallucinated commands.

### Additional Security

- Add `ownerDisplaySecret` to gateway config (HMAC owner-ID obfuscation, SHA-256 migration)
- Set `tools.exec.notifyOnExit: false` to prevent exec metadata contaminating voice note turns

---

## Workspace Files (Instruction Size Matters)

Dr. Bang-Iva had 21KB across 7 workspace files. Devon says this is over the sweet spot.

**Devon's target:** ~7,600 chars total. Every cold start loads all workspace files. Bigger files = more cost per message AND cheaper models struggle more (they drown in context instead of following instructions).

**Fix:** Trim workspace files to essentials. Move detailed references into memory search / RAG via extraPaths instead of loading every message. Set `agents.defaults.bootstrapMaxChars: 8000`.

**Applicable to Claude Code:** Keep CLAUDE.md focused. Implementation details belong in reference files loaded on-demand, not in the instruction file that loads every message.

---

## Memory Architecture (Current and Roadmap)

### Current: Flat SQLite

Vector search finds things by keyword and semantic similarity. Cannot answer "what decisions are stale" or "what research hasn't been codified" or "what changed since last week." No relationships between facts. No temporal awareness. "She can retrieve text but she can't reason about how things connect."

### Phase 1: QMD Backend (Next)

Experimental OpenClaw memory backend. Local search sidecar with BM25 + vectors + reranking via Reciprocal Rank Fusion. Community reports "orders of magnitude better" than default SQLite. Config change + install QMD CLI. Zero cost. 10+ open bugs to watch. Devon has not deployed yet.

### Phase 2: Knowledge Graph Layer

Evaluating two options:

| | Graphiti | Cognee |
|---|---|---|
| Stars | 23K | 8K |
| Strength | Bi-temporal model, best temporal queries | Native MCP, self-improving memory with RL-weighted edges |
| Setup | More complex | Way simpler |
| Needs | Docker for graph DB | Docker for graph DB |

Devon will run both against his full corpus and compare on queries that actually matter. Winner becomes deployable for Main Branch members.

### Phase 2.5: Langfuse Observability

Self-hosted measurement layer. RAGAS scoring to prove whether the knowledge graph actually improves response quality or just feels like it should. "If I can't measure it I can't ship it to members with confidence."

### Local Embeddings

Devon uses embeddinggemma (300M model through Ollama) for memory search embeddings. Completely local and free. M1+ Apple Silicon runs it easily. Alternative to sending every memory query through OpenAI API (which costs tokens and sends data off-network).

---

## Morning Brief System

Multi-card Telegram delivery. Urgency tiers: CRITIC, FLASH, IMMEDIATE, PRIORITY, ROUTINE. Unicode formatted "letterhead" cards.

**Cost:** 0.001 per run. Four cents per month. Forty-eight cents per year.

**Delivers:** Open decisions needing attention, fresh research summaries, suggested priorities. Devon reads it while making coffee and voice dumps a response.

---

## Autonomous Agent Capabilities (Demonstrated)

### System Maintenance

Devon opened Claude Code and said: "explore this Apple Notes crash for me." Agent autonomously found crash logs, spawned sub-agents, identified a specific Apple Intelligence bug, resolved the issue before Devon's second message.

"All that system needed was to know there was a problem. That's it."

### The Agent Maintenance Loop

- Are there any updates?
- How long have they been out?
- Read forum posts about it
- Check our system
- Back it up
- Run the update
- Pass all the tests? Keep it
- Doesn't? Roll back

### Content and Marketing

89 research files in 5 days. 12 decision documents. 16 PRs merged. Devon's framing: "These 89 research files and 12 decisions ARE the content pipeline. Thoth distributes them. I approve."

Philosophy: "Everyone racing to remove the human. I'm keeping the human and automating everything around them." 5-7 intent replies a day from verified X account. 75 seconds of attention. The rest is automated.

---

## Notable Gotchas (from 80 documented)

- Google Voice numbers are blocked from verifying new Google accounts
- Bot hallucinated a JSON config key that does not exist in the schema, crashed OpenClaw, poisoned its own config file
- Voice transcription bug fix merged to main AFTER release was cut (timing gap)
- 17% of ClawHub marketplace skills are malicious (386 packages) -- "no community marketplace skills" guardrail
- Kimi K2.5 context overflow causes cascading failures (compaction config is the fix)

---

## Core Philosophy

**"Better input not better output."** The thinking system produces content. Not the other way around.

**"Extending the human, not replacing it."** Keep the human. Automate everything around them.

**"The caveat is guardrails."** Most people do not know how to set up strong guardrails. Reference files (soul, offer, audience, voice) = the guardrail layer that keeps autonomous agents aligned to identity.

---

## Relevance to Client Ready

**Reference files ARE guardrails for autonomous systems.** What Client Ready teaches coaches to create (offer clarity, audience definition, voice codification) becomes the instruction set for AI agents. Coaches who skip this step cannot give agents meaningful constraints.

**Content angle:** "You cannot give an AI agent guardrails you have not defined yet."

**Product ladder maps to autonomy tiers:**
- 47 system = define the engine / create guardrails (Tier 0: self-awareness)
- Sprint = build the machine with guidance (Tier 1-2: reversible builds)
- Blueprint = turnkey machine with guardrails baked in
- Future: AI agents maintain and optimize the machine (Tier 2-3: autonomous within constraints)

**Voice rule extraction is replicable.** Devon edited 4 AI drafts for one X article and extracted 14 voice rules. This is exactly what the /think codify workflow does with voice.md.

**Workspace size principle applies to all AI instruction files.** Keep CLAUDE.md lean. Reference on-demand, not every message.

---

## Quote Bank

- "All that system needed was to know there was a problem."
- "89 research files in 5 days. THIS IS NOT TOO MANY."
- "Better input not better output. The thinking system produces content. Not the other way around."
- "Everyone racing to remove the human. I'm keeping the human and automating everything around them."
- "The bot hallucinated a config key and poisoned its own configuration file. Pretty good lesson about guardrails right there."
- "If a sentence could be on a SaaS landing page rewrite it."
- "Computing is changing in a pretty fundamental way everyone. Buckle the fuck up."
- "The 'she's dumb' problem is workspace files too big, approval loops, and flat memory. All fixable."
