---
type: decision
date: 2026-03-14
status: accepted
linked_research:
  - decisions/2026-03-10-all-in-codification-business-plan.md
---

# Decision: Codify App Product Model — Freemium to BYOK

## Context

Codify app V1 is deployed with 4 interview flows, preview pages, and AI enrichment using our API key. A non-technical client is interested. Need to make it work for business owners who may not have an LLM account or GitHub.

## Decision

### LLM Agnostic — Key Marketing Message

"Your reference files work with any AI." The app helps you build structured reference files. How you USE them is your choice — Claude, ChatGPT, Gemini, whatever. We recommend Claude but never lock you in.

### Tiered Access Model

| Tier | What They Get | Business Purpose |
|------|--------------|-----------------|
| **Free (no account)** | Fill interviews, raw formatted files, "Use with AI" copy button | Lead magnet. Shows value. Captures email. |
| **Free account (email)** | Save progress, come back, re-edit, 10 free enrichments (our key) | Lead capture + nurture pipeline |
| **BYOK** | Unlimited enrichments on their key, any provider | Self-serve power users |
| **License ($147/mo)** | Full engine access via Skool, community, live sessions | The real product |

### "Use with AI" — The Killer Feature

One button generates a single copy-paste block combining all 4 reference files with instructions. User pastes it into ANY AI chat. No API keys, no GitHub, no technical setup. This is the LLM-agnostic delivery mechanism.

### Multi-Provider Enrichment (BYOK)

When users bring their own key, support:
- Anthropic (Claude) — recommended
- OpenAI (GPT)
- Google (Gemini)

Settings page with clear setup instructions per provider. Keys encrypted, stored server-side only.

### Tech Stack Addition

- Supabase (free tier) for auth + database
- Magic link email login (no passwords)
- Saved answers persist across sessions
- Usage tracking for free tier limits

## What Changes

- Codify app gets Supabase auth + database
- New "Use with AI" export feature on assessment page
- Settings page for BYOK API key management
- Multi-provider API route (Claude, GPT, Gemini)
- Free tier usage counter (10 enrichments)
- Landing page email capture before first use

## Consequences

- Users never need GitHub or terminal knowledge
- App becomes the self-serve version of the $197 workshop
- Every free user is a lead for the email nurture sequence
- BYOK eliminates our LLM costs for active users
- LLM-agnostic positioning differentiates from platform-locked tools
