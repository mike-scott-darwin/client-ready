---
type: research
status: active
date: 2026-02-21
source: mining
linked_decisions: []
---

# Devon on OpenClaw: 5-Day Deep Setup and Autonomous Agent Architecture (Skool Post, Feb 21 2026)

## Source

Devon (Main Branch creator) posted a long-form update in Skool documenting 5 days of intensive OpenClaw setup, research, and autonomous agent architecture work. This covers the practical reality of running self-driving business systems.

## The Setup

Wiped a 2018 MacBook Pro. Fresh macOS install. OpenClaw bare metal. Named it "thoth" (Egyptian god of writing and record keeping). Set it up entirely via SSH from a newer MacBook Air. No monitor. Tailscale for secure remote access. Clamshell mode on a shelf. Auto-starts, morning brief fires at 7 AM. Runs whether awake or not.

**Setup reality:** 14 hours on day 1. 80 documented gotchas. Every single one numbered and catalogued.

## Notable Gotchas

- Google Voice numbers are blocked from verifying new Google accounts (Google's own product cannot bootstrap Google's own signup)
- The bot hallucinated a JSON config key that does not exist in the schema, crashed OpenClaw, and poisoned its own configuration file (lesson about guardrails)
- A voice transcription bug fix was merged to main AFTER the release was cut -- fix existed but was not installable (timing gap between upstream fix and release)

## Output Volume

89 research files and 12 formal decision documents in 5 days. 16 PRs merged. Devon's framing: "THIS IS NOT TOO MANY. I now have a ton of meat for parallel agents and openclaw to play with for content or whatever."

**Key research topics:**

**Memory optimization:** 6 parallel research agents consumed 293K tokens to synthesize how OpenClaw memory works under the hood. Existing architecture matched community best practices in 6 out of 6 areas. Missing: semantic search and cross-machine sync.

**Kimi Claw deep dive:** Moonshot AI (Beijing, 4.8B valuation) is the first major platform to embed OpenClaw natively. Instead of building proprietary, they adopted the open-source standard. 591 lines of research. Also found 17% of skills in the ClawHub marketplace are malicious (386 packages) -- drove immediate "no community marketplace skills" guardrail.

**Marketing automations:** Evaluated a viral "vibeclawdbotting" thread. 10 strategies analyzed. Decision doc written. X article published about which strategies actually work vs spray-and-pray garbage.

## Model Bakeoff

Automated bakeoff running daily at 4:20 AM. 150 test cases across 8 models.

**Results (for ops/structure rubric):**
- Gemini 3 Flash Preview won. Best non-Anthropic model. 100% reliability. 1.6 second average latency.
- Grok 4 Fast came second. 0.20 per million tokens. 2 million token context window. Devon calls it "a stealth powerhouse nobody is talking about."
- Sonnet 4.5 came last on the ops/structure rubric. Most expensive model finishing dead last. Devon notes this is a specific test with specific criteria -- Sonnet is still his go-to for creative and complex reasoning.

**Takeaway:** Multi-tier routing saves real money. System auto-proposes routing changes but requires human approval before switching.

## Morning Brief System

Multi-card Telegram delivery with urgency tiers: CRITIC, FLASH, IMMEDIATE, PRIORITY, ROUTINE. Unicode formatted "letterhead" cards. Runs on Grok 4 Fast.

**Cost:** 0.001 per run. Four cents per month. Forty-eight cents per year.

Delivers: open decisions needing attention, fresh research summaries, suggested priorities. Devon reads it while making coffee and voice dumps a response.

## 4-Tier Autonomy Ladder

This is the guardrail architecture for giving AI agents appropriate levels of control:

- **Tier 0:** Auto for read-only checks
- **Tier 1:** Auto for reversible writes in approved paths
- **Tier 2:** Ask first for service restarts and cron edits
- **Tier 3:** Break-glass requiring a literal confirmation string

**Test results:** Asked thoth to "delete X permanently" -- it refused and required the exact confirmation format. When asked to generate a profile picture (deliberately vague prompt), it burned 0.33 and 294K tokens across 10 tool turns before delivering. That single test drove three new guardrails: channel pinning, token budgets, and creative self-critique loops.

## The X Article

"OpenClaw is about extending the human, not replacing it." Went through four AI drafts before Devon edited it into something that actually sounded like him.

**Editing process generated 14 new voice rules:**
- 7 emotional reaction patterns (parenthetical asides, gut-punch reactions, "love you bye" as a closer)
- 7 anti-AI polish rules (break clean punchlines, no image words, if a sentence could be on a SaaS landing page rewrite it)

**Philosophy:** Everyone racing to remove the human. Devon is keeping the human and automating everything around them. 5-7 intent replies a day from verified account. 75 seconds of attention. The rest is automated.

## Relevance to Client Ready

**Reference files ARE the "better input":** Devon's philosophy ("better input not better output") maps directly to what Client Ready teaches. The 89 research files and 12 decisions ARE the content pipeline. The thinking system produces content, not the other way around. This is exactly what Main Branch reference files do for coaches.

**The 4-tier autonomy ladder is a content angle:** Coaches building AI-assisted businesses need guardrails proportional to the risk. Read-only checks need no approval. Deleting customer data needs a break-glass confirmation. This maps to the product ladder: the 47 system gives you read-only self-awareness (Tier 0), the Sprint gives you reversible builds with guidance (Tier 1-2), the Blueprint gives you a turnkey machine with guardrails baked in.

**Model routing = cost discipline for coaches:** Most coaches do not need the most expensive model for every task. The bakeoff data shows the cheapest reliable model should handle routine work, with expensive models escalated only for complex reasoning. This principle applies to any business system, not just AI.

**Voice rule extraction process is replicable:** Devon's method of editing AI drafts to extract voice rules (parenthetical asides, anti-polish rules) is exactly what the voice.md codification process does. The 14 rules he extracted in one editing session is proof of concept for the "/think codify" workflow.

## Quote Bank

- "89 research files in 5 days. THIS IS NOT TOO MANY."
- "The bot hallucinated a config key and poisoned its own configuration file. Pretty good lesson about guardrails right there."
- "Better input not better output. The thinking system produces content. Not the other way around."
- "These 89 research files and 12 decisions ARE the content pipeline. Thoth distributes them. I approve."
- "Everyone racing to remove the human. I'm keeping the human and automating everything around them."
- "If a sentence could be on a SaaS landing page rewrite it."
- "I have a baby hitting in like a month or less. Everything needs to be phone-manageable before then."

## What is Next (Devon's Roadmap)

- Intent sniping pipeline: scout that reads X and finds people asking questions Devon can help with
- Typefully integration for post scheduling
- Algo scout: reads For You feed and extracts what the algorithm is rewarding right now
- Everything must be phone-manageable before baby arrives
