---
type: reference
status: active
date: 2026-03-08
linked_decisions:
  - decisions/2026-02-24-content-automation-rollout.md
linked_reference:
  - reference/domain/openclaw-automation.md
---

# OpenClaw Status — M1 Mac Mini

Last updated: 2026-03-08

---

## Two Machines

| Machine | Hostname | Role |
|---------|----------|------|
| M1 Mac Mini | Michaels-Mac-mini (192.168.1.124) | Always-on server. OpenClaw + gateway + Telegram |
| MacBook Pro M2 | Michaels-MacBook-Pro | Development. Claude Code + poster LaunchAgents |

---

## What Is Running (M1 Mac Mini)

Confirmed from `openclaw status` output (Mar 4-6):

- [x] **OpenClaw 2026.3.2** installed and running
- [x] **Gateway** — LaunchAgent installed, loaded, running (pid 9211), loopback ws://127.0.0.1:18789
- [x] **Telegram** — ON, connected (t.me/client_ready_bot, token configured)
- [x] **OpenRouter** — configured (openrouter/auto model)
- [x] **Onboard wizard** — completed Mar 4 (local mode)
- [x] **Agent** — 1 agent (main), 1 session active, openrouter/auto (200k ctx)
- [x] **12/51 skills ready** — coding-agent, github, gemini, obsidian, apple-notes, apple-reminders, weather, nano-banana-pro, healthcheck, model-usage, skill-creator, gh-issues
- [x] **Heartbeat** — 30m interval
- [x] **Security** — 0 critical, 2 warn, 1 info (loopback-only binding)
- [x] **Content approval flow working** — agent reads drafts, presents batches for YES/NO/EDIT approval

---

## What Is Running (MacBook Pro)

- [x] **LaunchAgents** — com.clientready.xposter, com.clientready.linkedinposter, com.clientready.enrichmentscanner
- [x] **Node 25**, npm 11, Python 3.9, tweepy, markdown
- [x] **Content pipeline** — content/drafts/ to content/published/ with state tracking

---

## Two Blockers to Fix

### Blocker 1: Agent cannot read local files

The TUI transcript from Mar 4 shows the agent repeatedly saying "I can't access your local filesystem" when asked to read CLAUDE.md. The tools.profile was "messaging" (restricted), then changed to "full", but the agent still could not read files.

**Fix (run on M1):**
```bash
# Point the agent workspace to the client-ready repo
openclaw config set agents.defaults.workspace "/Users/michaelscott/Documents/GitHub/client-ready"

# Verify tools profile is full
openclaw config set tools.profile "full"

# Restart the agent to pick up changes
openclaw restart
```

Then test:
```
> Read the file at /Users/michaelscott/Documents/GitHub/client-ready/CLAUDE.md
```

If the agent can read it, this blocker is resolved.

### Blocker 2: Telegram group messages silently dropped

Doctor warning: `channels.telegram.groupPolicy is "allowlist" but groupAllowFrom is empty — all group messages will be silently dropped.`

**Fix (run on M1):**
```bash
# Option A: Open policy (simplest, fine for private group)
openclaw config set channels.telegram.groupPolicy "open"

# Option B: Allowlist your Telegram user ID (more secure)
# First get your Telegram user ID from the bot:
# curl "https://api.telegram.org/bot<TOKEN>/getUpdates" | python3 -m json.tool
# Then:
# openclaw config set channels.telegram.groupAllowFrom '["YOUR_USER_ID"]'
```

---

## Not Yet Done

| Item | Priority | Notes |
|------|----------|-------|
| Fix file access (Blocker 1) | HIGH | Agent can't read repo files |
| Fix group messages (Blocker 2) | HIGH | Group messages silently dropped |
| Tailscale | LOW | Not installed. Only needed for remote SSH from laptop/phone. Can defer if you access M1 directly |
| Node service LaunchAgent | MEDIUM | Only gateway has LaunchAgent. Agent itself may not survive reboot |
| Memory files | MEDIUM | 0 files, 0 chunks. MEMORY.md, AGENTS.md, TOOLS.md not created in workspace |
| whisper-cpp | LOW | Voice pipeline. Defer until voice-note workflow needed |
| Beehiiv Scale plan | MEDIUM | Upgrade from free to Scale (49/mo) to unlock newsletter API |
| Model routing aliases | LOW | Currently using openrouter/auto. Blueprint calls for 4-tier routing (grok-4-fast/gemini-3-flash/flash-lite/sonnet-4.6) |
| Cron schedule | LOW | Morning brief, journal triage, graduation scan not scheduled yet |
| Poster LaunchAgents on M1 | MEDIUM | Currently running on MacBook Pro. Should migrate to M1 for always-on |

---

## Workspace Config Files to Create (on M1)

These go in the OpenClaw workspace directory. Run on the M1:

### MEMORY.md

```bash
cat > ~/.openclaw/workspace/MEMORY.md << 'OCEOF'
# Client Ready — Agent Memory

## Business
- Michael Scott helps coaches validate offers before building
- Scale from 47 low-ticket to 5K+ high-ticket
- Tagline: "The Coach Who Won't Tell You to Quit Your 9-to-5"
- Front-end: 47 Client Ready Offer System
- Max cart: 1,096 | Target AOV: 90-110

## Repo Paths
- Main repo: /Users/michaelscott/Documents/GitHub/client-ready
- Reference files: reference/ (READ-ONLY)
- Content pipeline: content/drafts/ to content/scheduled/ to content/published/
- Drafts by platform: content/drafts/tweets/, content/drafts/threads/, content/drafts/linkedin/, content/drafts/newsletter/
- Voice guide: reference/core/voice.md
- Content strategy: reference/domain/content-strategy.md
- CLAUDE.md: Full business context and folder structure

## API Credentials
- All in .env at repo root (never read or output these)
- X: tweepy via x-poster.py (5x/day launchd on MacBook Pro)
- LinkedIn: REST API via linkedin-poster.py (1x/day launchd on MacBook Pro)
- Beehiiv: API via beehiiv-poster.py (requires Scale plan upgrade)

## Content Cadence
- Newsletter: 1/week (Tuesday send)
- X threads: 2/week
- LinkedIn posts: 3-5/week
- Daily tweets: 3-5/day
- LinkedIn CTA: always "link in comments" (never inline URLs)

## Key URLs
- Skool: https://www.skool.com/high-ticket-playbook-9467
- Offer: https://clientreadyoffer.com/implement

## Content File Format
- Filename: YYYY-MM-DD-platform-type-slug.md (or YYYY-MM-DD-N.md for tweets)
- Frontmatter: platform, type, angle, pillar, status, scheduled_date, published_date
- One tweet per file in content/drafts/tweets/
OCEOF
```

### AGENTS.md

```bash
cat > ~/.openclaw/workspace/AGENTS.md << 'OCEOF'
# Operating Contract

## Autonomy Tiers
- Tier 0 (read-only): Ad data, email metrics, GHL data. Observe and report only.
- Tier 1 (auto-write): content/drafts/, content/scheduled/, content/published/, journal/, outputs/. Human approves every post before it goes live.
- Tier 2 (PR required): Anything in reference/, research/, decisions/. Create branch + PR. Never merge.

## Never Do
- Modify reference/ files directly
- Post content without human approval
- Make ad spend decisions
- Store credentials in memory, chat, or files
- Expose the gateway to public internet
- Install ClawHub marketplace skills (17% malicious rate)

## Priorities
1. Ship approved content on schedule
2. Flag threshold breaches (ads, email, community)
3. Capture journal entries accurately
4. Keep morning brief under 200 words

## Content Approval Flow
1. Read drafts from content/drafts/{tweets,threads,linkedin,newsletter}/
2. Present each draft in Content topic with full text
3. Wait for YES (approve), NO (skip), or EDIT (with changes)
4. Approved content: update status to scheduled, move to content/scheduled/
5. Never post without explicit approval

## Journal Triage Rules
- Default: save to journal/YYYY-MM-DD.md with timestamp
- "content:" prefix: route to content/drafts/ and Content topic
- "thread:" prefix: route to content/drafts/threads/ and Content topic
- Link entries to existing reference files with [[wiki links]]
- Tag with content pillars where applicable
- Flag entries mentioning same topic as previous entry (pattern signal)

## Graduation Rules (Weekly Sunday Scan)
- Theme appeared 3+ times in 7 days: graduation candidate
- Each candidate becomes either content draft or reference update suggestion
- Send to Research topic for review. Never auto-graduate.

## Voice
Read reference/core/voice.md before drafting any content.
- Direct. No-BS. Engineering mindset. Short sentences.
- Signature: "Wrong." "Test, validate, build." "You can't grow into pain."
- Alignment-first positioning. Substance over perception.
OCEOF
```

### TOOLS.md

```bash
cat > ~/.openclaw/workspace/TOOLS.md << 'OCEOF'
# Infrastructure

## Repo
- Path: /Users/michaelscott/Documents/GitHub/client-ready
- Remote: git@github.com:mike-scott-darwin/client-ready.git
- Main branch: main

## Scripts (currently on MacBook Pro, migrating to M1)
- x-poster.py: Posts tweets from content/drafts/tweets/ (tweepy, launchd 5x/day)
- linkedin-poster.py: Posts from content/drafts/linkedin/ (REST API, launchd 1x/day)
- beehiiv-poster.py: Posts from content/drafts/newsletter/ (Beehiiv API, needs Scale plan)
- enrichment-scanner.py: Daily journal triage

## State Files (repo root)
- .x-poster-state.json: Tweet posting history with IDs and URLs
- .linkedin-poster-state.json: LinkedIn posting history with post IDs
- .beehiiv-poster-state.json: Newsletter posting history

## APIs
- X: OAuth 1.0a (consumer key + access token in .env)
- LinkedIn: OAuth 2.0 (access token in .env, needs periodic refresh)
- Beehiiv: Bearer token (requires Scale plan at 49/mo)
- GHL: Available via MCP (LinkedIn posting, contact management)
OCEOF
```

### USER.md

```bash
cat > ~/.openclaw/workspace/USER.md << 'OCEOF'
# User Profile

Name: Michael Scott
Timezone: ACST (UTC+9:30)
Role: Founder, Client Ready

## Preferences
- Direct communication, no fluff
- Engineering mindset: test, validate, build
- Prefers "link in comments" for LinkedIn (algorithm suppresses inline links)
- Alignment-first positioning
- Action over perfection
- Show content in full before approval (no summaries)
OCEOF
```

---

## Quick Fix Commands (Run on M1)

Copy-paste these in order to resolve the two blockers and set up workspace files:

```bash
# Fix Blocker 1: File access
openclaw config set agents.defaults.workspace "/Users/michaelscott/Documents/GitHub/client-ready"
openclaw config set tools.profile "full"

# Fix Blocker 2: Group messages
openclaw config set channels.telegram.groupPolicy "open"

# Create workspace files (run the MEMORY.md, AGENTS.md, TOOLS.md, USER.md cat commands above)

# Restart
openclaw restart

# Verify
openclaw status
openclaw doctor
```

---

## Monthly Cost (Current)

| Item | Cost |
|------|------|
| OpenRouter API | ~75/mo |
| Beehiiv (free, upgrade to Scale when ready) | 0 (will be 49/mo) |
| Tailscale (free tier) | 0 |
| Telegram | 0 |
| **Total now** | **~75/mo** |
| **Total after Beehiiv upgrade** | **~124/mo** |
