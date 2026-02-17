---
type: decision
date: 2026-02-15
status: accepted
urgency: normal
---

# OpenClaw Deployment Plan

## Situation

Main Branch handles deep work (research, decisions, ads, content) through Claude Code on Mac. The missing piece is an always-on agent that can handle distribution, approvals, and monitoring without opening a laptop. OpenClaw fills that gap -- a self-hosted AI agent on a DigitalOcean droplet that connects to your phone via messaging and reads from the same business repo.

## Architecture

Git is the spine. Three interfaces, one repo:

**Mac** -- Deep work (Claude Code, /think, /ads, /organic)

**Server** -- Always-on automation (OpenClaw on DigitalOcean)

**Phone** -- Approvals and quick input (Signal, WhatsApp, Telegram, or Slack)

All three read from and write to client-ready. Business truth stays in the repo. Agent behavior stays in the OpenClaw workspace. Two canons, never mixed.

## Implementation Steps

### Phase 1: Accounts and Keys

- DigitalOcean account with payment method
- OpenRouter account with credits and spending limit (start 75-100/mo)
- GitHub Personal Access Token (fine-grained, scoped to client-ready, read access)
- Pick messaging channel: Signal (most private), WhatsApp (easiest), Telegram (most bot-friendly), or Slack (team use)

### Phase 2: Deploy the Droplet

- Spin up OpenClaw from DigitalOcean 1-Click Marketplace
- Plan: 12/mo (2GB RAM, 1 CPU, 50GB SSD)
- SSH in using your key
- Grab gateway token from droplet for dashboard access

### Phase 3: Wire It Up

- Enable messaging plugin via CLI commands on the droplet
- Clone client-ready to the droplet using GitHub PAT
- Set file ownership permissions
- Add as read-only bind mount to Docker container
- Set up cron job for auto-pull every 3 hours
- Configure models via OpenRouter: Sonnet for default, Haiku for heartbeats, Opus for creative

### Phase 4: Security Hardening

- UFW firewall: only ports 80 and 443 open
- Tailscale mesh VPN: SSH and dashboard only accessible through private network
- fail2ban: blocks SSH brute-force attempts
- SSH key-only auth: disable password login
- File permissions: .env at 600, credential dirs at 700
- unattended-upgrades for automatic security updates

### Phase 5: Content Pipeline

Once running, the flow works like this:

1. Create content in Claude Code (Mac)
2. Git push to client-ready
3. OpenClaw pulls automatically (cron)
4. Agent sends drafts for review on phone
5. Approve or edit via message reply
6. Approved content moves to scheduled folder
7. Agent posts on schedule
8. Published content archived with engagement metadata
9. Morning brief sent to phone
10. Performance data feeds back into next /think session

Every step creates a git commit for full traceability.

## Cost

- DigitalOcean: 12/mo flat (no usage-based billing)
- API costs: variable via OpenRouter (depends on model selection and usage)
- No additional software costs (self-hosted)

## Graduation Path

- **Phase 1 (current):** Terminal with Claude Code
- **Phase 2 (this plan):** Personal cloud on DigitalOcean
- **Phase 3 (future):** Own hardware, depend on no one

## Source

OpenClaw + Main Branch setup guide from Devon

## What Changes

No reference files affected yet. This is an infrastructure decision. When ready to implement:

- content/drafts, content/scheduled, content/published folders become active pipeline locations
- content-strategy.md may need a section on distribution automation
- Morning brief format and approval workflow to be defined during setup
