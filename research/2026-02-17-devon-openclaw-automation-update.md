---
type: research
date: 2026-02-17
source: Devon (Main Branch) — Skool post
topic: OpenClaw deployment learnings, automation philosophy, and distribution infrastructure
relevance: OpenClaw deployment plan, content pipeline, X lead gen strategy
---

# Devon's OpenClaw + Main Branch Update — What Happened and What Matters

## One-Sentence Summary

Devon deployed OpenClaw on bare metal (old MacBook), generated 89 research files in 5 days using parallel AI agents, built a $0.04/mo morning brief system, and is launching an intent-sniping pipeline on X — confirming the "better input not better output" philosophy that Client Ready's repo architecture already follows.

## What Devon Built (5-Day Sprint)

### 1. OpenClaw on Bare Metal

- Wiped a 2018 MacBook Pro, installed OpenClaw, named it "thoth"
- SSH access from main machine, Tailscale for secure remote access
- Clamshell mode on a shelf — auto-starts, morning brief fires at 7 AM
- 14 hours for initial setup, **80 documented gotchas** (available in Main Branch repo)
- Key lesson: the bot hallucinated a config key and crashed its own config file — guardrails matter

**Client Ready relevance:** Our OpenClaw deployment plan (decisions/2026-02-15) calls for DigitalOcean, not bare metal. Devon's 80 gotchas doc is directly useful when we deploy. His experience confirms the architecture works. **Not relevant to do NOW** — we're in launch phase, not infrastructure phase.

### 2. Research Velocity — 89 Files in 5 Days

- 89 research files, 12 decision documents, 16 PRs merged
- Used parallel research agents (6 agents, 293K tokens in one session)
- Topics: memory optimization, Kimi Claw deep dive, marketing automations
- His framing: "This is NOT too many. I now have a ton of meat for parallel agents and OpenClaw to play with for content."

**Client Ready relevance:** We're already doing this. Our research/ folder has 37 files. Our decisions/ folder has 31 documents. Our ad copy, email sequences, and funnel architecture all flow from these research files. **We're living the philosophy — we just haven't automated the distribution layer yet.**

### 3. Model Bakeoff (Daily Automated Testing)

- 150 test cases across 8 models, runs daily at 4:20 AM
- Results: Gemini 3 Flash Preview won for ops/structure work (100% reliability, 1.6s latency)
- Grok 4 Fast: $0.20/million tokens, 2M token context window — "stealth powerhouse"
- Sonnet 4.5 came last on ops/structure rubric (still best for creative/complex reasoning)
- System auto-proposes routing changes but requires Devon's approval

**Client Ready relevance:** Not relevant now. We use one model (Opus) for deep work through Claude Code. Model routing matters when running always-on automation with high token volume. **Park for Phase 3.**

### 4. Morning Brief System ($0.04/month)

- Multi-card Telegram delivery with urgency tiers (CRITIC, FLASH, IMMEDIATE, PRIORITY, ROUTINE)
- Runs on Grok 4 Fast — $0.001 per run
- Delivers: open decisions needing attention, fresh research summaries, suggested priorities
- Devon reads it while making coffee, voice dumps a response

**Client Ready relevance:** Directly useful AFTER launch. Once ads are running and sales are flowing, a daily brief showing ad spend, conversion rates, decisions needing attention, and content to approve would save 30+ minutes of manual checking. **Phase 2 — build into OpenClaw deployment.**

### 5. X Article + Content Pipeline

- Wrote "OpenClaw is about extending the human, not replacing it"
- 4 AI drafts before manual editing — generated 14 new voice rules
- 7 emotional reaction patterns (parenthetical asides, gut-punch reactions, "love you bye")
- 7 anti-AI polish rules (break clean punchlines, no image words, rewrite SaaS-sounding sentences)
- Pipeline: research files → content → thoth distributes → Devon approves

**Client Ready relevance:** The content pipeline pattern maps directly. Our research files and decision docs ARE content raw material. Each one could become an X post, Skool post, or organic content piece. The voice rule extraction is interesting — we already have voice.md but could enrich it using Devon's anti-AI polish approach. **Relevant now for content strategy; automation later.**

### 6. Intent Sniping Pipeline (Coming This Week for Devon)

- AI scout reads X, finds people asking questions Devon can answer
- 5-7 intent replies per day from verified account
- 75 seconds of attention per reply — rest is automated
- Also building: algo scout that reads For You feed, extracts what algorithm rewards

**Client Ready relevance:** THIS IS THE MOST RELEVANT PIECE. Coaches post things like "I don't know what to charge" and "been posting for months with no clients" on X every day. Those are our P1-P5 audiences in the wild. An intent sniping system for Client Ready would:**
- Find coaches expressing offer confusion, content fatigue, course graveyard frustration
- Draft a value-first reply (not a pitch)
- Michael approves and posts
- Warm lead enters orbit

**This is free warm lead gen that compounds over time. Each reply builds authority. Deploy AFTER funnel is live so there's somewhere to send people.**

### 7. 4-Tier Autonomy Ladder

- Tier 0: auto for read-only checks
- Tier 1: auto for reversible writes in approved paths
- Tier 2: ask first for service restarts and cron edits
- Tier 3: break-glass requiring literal confirmation string
- Tested by asking agent to "delete X permanently" — refused correctly
- Vague prompt test ($0.33, 294K tokens, 10 tool turns) drove 3 new guardrails: channel pinning, token budgets, creative self-critique loops

**Client Ready relevance:** Good architecture to adopt when we deploy OpenClaw. Prevents the bot from burning money or doing damage. **Phase 2 — implement during OpenClaw setup.**

---

## Key Takeaway for Client Ready

Devon is in **infrastructure + distribution phase**. We are in **launch + first sales phase**. The philosophy is identical — we're already doing "better input not better output" through our repo structure. The gap is:

1. We haven't turned on distribution (content pipeline from research → social)
2. We haven't deployed OpenClaw (decision accepted, not implemented)
3. We haven't started intent sniping on X (most immediate ROI opportunity)

The sequencing matters: **Launch funnel → Run ads → First sales → Then automate distribution and monitoring.**

---

## Actionable Items (Prioritized by Phase)

| Priority | Item | Phase | Depends On |
|----------|------|-------|------------|
| 1 | Intent sniping keywords list — define the X searches that find our audience | Pre-launch | Nothing — can draft now |
| 2 | Content pipeline mapping — which research files become what content | Pre-launch | Nothing — can map now |
| 3 | Morning brief spec — what metrics matter once ads run | Post-first-sales | Live funnel + ad data |
| 4 | OpenClaw deployment — follow existing plan + Devon's 80 gotchas | Post-validation | 30+ sales confirmed |
| 5 | Model routing — multi-tier for cost optimization | Post-OpenClaw | Running always-on agent |
| 6 | Algo scout — extract what X algorithm rewards | Post-OpenClaw | Running intent pipeline |
