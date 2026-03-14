---
type: research
status: complete
date: 2026-03-12
source: claude-code
linked_decisions: []
---

# Parallel Agents for Dedicated Tasks

**Context:** Devon mentioned parallel agents on the 2026-03-12 Skool call. Exploring what this looks like for Client Ready workflows.

## Summary

Parallel agents spawn multiple Claude Code subagents simultaneously, each with a fresh context window. Trades tokens for speed and context quality.

## Key Findings

1. **What it is** -- The Agent tool spawns independent subagents in a single message. Each gets its own full context window, reads reference files independently, and returns results. All run at the same time.

2. **Content production use case** -- Weekly batch: spawn 3 agents simultaneously (LinkedIn posts, X threads, newsletter draft). Each reads soul.md/voice.md/content-strategy.md. All return in ~30 seconds vs doing sequentially.

3. **Research use case** -- Multi-source research: Agent 1 mines YouTube (Apify), Agent 2 checks X sentiment (Grok), Agent 3 runs deep web research (Gemini). Each writes its own research file. Main conversation synthesizes.

4. **Ad creative use case** -- Multiple angle variations and image prompts generated simultaneously.

5. **Token usage per agent (typical):**
   - ~10-50K input tokens (reference files + prompt)
   - ~5-20K output tokens (content/research produced)
   - ~15-70K total tokens per agent per task

6. **Cost estimates (Opus 4.6 -- $15/M input, $75/M output):**
   - 3-agent content batch: ~$1-5
   - 3-agent research sweep: ~$2-8
   - Tradeoff: 3x tokens, 1/3 wall-clock time

7. **Hidden benefit: context window management** -- Without subagents, heavy work burns through the main context window and triggers compaction (losing context and quality). Subagents keep heavy work isolated -- only summaries return to main. Three focused agents with clean context often produce better output than one overloaded conversation.

## Implications for Reference Files

- content-strategy.md: Phase 1/2 automation could leverage parallel agents for batch content production
- No changes needed yet -- this informs future automation decisions

## Open Questions

- What's the optimal agent count before diminishing returns? (context: API rate limits)
- Should content batch agents share a brief or get independent prompts?
- How does this interact with the newsletter-first model? (agent for newsletter, then agents for derivative content?)
