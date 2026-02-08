# Handoff: Identity Work Placement + Research Synthesis

**Date:** 2026-02-05
**Session:** Codified identity transformation framework into offer stack

## Goal
Incorporate identity shift work into the offer stack without disrupting front-end conversion — solving the tension between what prospects WANT (tactical answers) vs what they NEED (identity transformation).

## Current State

**Complete.** Decision A+B accepted and codified:
- **Option A (Blueprint Onboarding):** Added Section 8: Identity Foundation (5 questions) to intake form
- **Option B (Sprint Soul Extraction):** Created full Week 0/1 module with prompts, delivery format, positioning guidance

All changes pushed to GitHub (16 files, commit `4619ed4`).

## What We Tried

### Worked
- Framing identity work as "design constraints" not "woo" — tactical positioning that doesn't kill conversion
- Front-end solves surface problem (what they WANT), delivery handles transformation (what they NEED)
- Key insight: "Before we build, let's make sure it fits your life"

### Research Synthesized
10 research files from today:
- Miles Stutz: pilot program, click-go-live stack, AI extraction system, 72-hour install
- Future frameworks: Taki Moore, Iman Gadzhi, Steph Hughson
- Personal mastery framework (Old Character → New Character)
- Million dollar roadmap (5 archetypes, alignment equation)

## Key Files
- `decisions/2026-02-05-identity-work-placement.md` — Decision document (status: codified)
- `reference/domain/funnel/dfy-onboarding-form.md` — Section 8: Identity Foundation added
- `reference/domain/funnel/sprint-soul-extraction.md` — Full module outline with 5 prompts
- `reference/core/offer.md` — Checkout Optimization + Ad Strategy Framework sections added
- `reference/domain/sales/tyler-durden-call-audit.md` — Sales call debrief framework

## Next Steps
1. Record 15-min Loom: "Before We Build: Why Alignment Beats Tactics"
2. Update offer.md Sprint section with "alignment-first approach" positioning
3. Consider open questions from decision:
   - Does identity work justify Sprint price increase ($297 → $397)?
   - Should Soul Extraction become separate sellable asset?
   - How to measure if identity work improves results?

## Notes for Next Session
- Clarity-First Positioning Test decision (`2026-01-26`) still open — may want to address
- Key quote to use in Loom: "Subconsciously, you will not grow into pain"
- Sprint positioning language: "Most people build something they abandon. We build something sustainable."

---

# Previous Session: Email Backend + GHL MCP Setup

**Date:** 2026-02-04
**Session:** Email sequence reorganization and GHL automation setup

## Goal
Consolidate email sequences with clear naming, create GHL workflow guide, and set up GHL MCP for automation.

## Current State

**Email sequences:** Complete and organized in `outputs/emails/`
- All files renamed with numbered prefixes by journey stage
- Stacking issue fixed (8 AM = value, 2 PM = offers)
- Missing Community recovery sequence added (OTO 3 downsell)
- Daily broadcast templates created

**GHL MCP:** Configured and tested successfully
- 253 tools available (contacts, tags, workflows, email templates)
- API key: [REDACTED — stored in ~/.claude.json]
- Location ID: [REDACTED — stored in ~/.claude.json]
- **NEEDS RESTART** to load into Claude Code session

## What We Tried

### Worked
- Consolidated 6 email files with clear segment naming
- Created comprehensive GHL workflow setup guide
- Set up GHL MCP server from mastanley13/GoHighLevel-MCP
- First API key had insufficient scopes → new key with full scopes works
- Connection test successful: 253 tools available

### Didn't Work
- `workflows.write` scope not available in GHL API (UI-only for workflow creation)
- First API key missing `locations.readonly` scope → got 401 error

## Key Files

### Email Sequences
- `outputs/emails/README.md` — Overview with journey map
- `outputs/emails/1-non-buyers-30-day.md` — 12 emails for leads who didn't buy
- `outputs/emails/2-buyers-welcome-10-day.md` — 10 relationship emails (no pitches)
- `outputs/emails/3-buyers-recovery-bumps.md` — Days 2,4,6 re-pitch missed bumps
- `outputs/emails/3-buyers-recovery-otos.md` — Days 3,5,7 re-pitch Sprint/Blueprint
- `outputs/emails/3-buyers-recovery-community.md` — Day 8 downsell to $47/mo
- `outputs/emails/4-buyers-daily-broadcast.md` — Day 11+ with weekly offer rotation

### Configuration
- `outputs/emails/ghl-workflow-setup.md` — Complete GHL workflow build guide
- `reference/domain/email-rhythm.md` — Updated with new file paths
- `~/.claude.json` — GHL MCP server config (lines 463-473)
- `/Users/michaelscott/GoHighLevel-MCP/` — Cloned and built MCP server

## Next Steps

1. **Restart Claude Code** — `Ctrl+C` then `claude` to load GHL MCP
2. **Test GHL MCP** — Verify `mcp__gohighlevel__*` tools are available
3. **Create tags in GHL** — Use MCP or manual:
   - `purchased-27`, `purchased-bump-dm-scripts`, etc.
   - `in-nonbuyer-sequence`, `in-welcome-sequence`, etc.
4. **Build 6 workflows manually** — Follow `ghl-workflow-setup.md`
5. **Create email templates via MCP** — Optional, can do in bulk

## Notes for Next Session

**GHL API limitations:** Can't create/edit workflows via API. Build workflows in UI, but can:
- Add/remove contacts from workflows
- Add/remove tags (which trigger workflows)
- Create email templates
- Manage contacts

**Email timing:**
- Welcome: 8:00 AM (value/relationship)
- Recovery: 2:00 PM (offers)
- Max 2 emails/day for buyers

**Tags to create first:**
```
purchased-27
purchased-bump-dm-scripts
purchased-bump-templates
purchased-bump-traffic
purchased-sprint
purchased-blueprint
purchased-community
in-nonbuyer-sequence
in-welcome-sequence
completed-welcome
in-daily-broadcast
```

**Workflow triggers:**
1. Non-Buyer → Form submit + wait 30 min + no purchase tag
2. Welcome → Tag `purchased-27` added
3. Bump Recovery → Tag `purchased-27` + missing bump tags
4. OTO Recovery → Tag `purchased-27` + no Sprint/Blueprint tags
5. Community Recovery → Tag `purchased-27` + no upsell tags (Day 8)
6. Daily Broadcast → Tag `completed-welcome` added (Day 11+)
