# Conductor General Preferences — Client Ready Repo
# Paste this into: Conductor > Settings (gear icon) > General preferences > Custom instructions

## Context
You are working in the Client Ready business repo. Client Ready helps coaches validate offers before building — scale from $47 low-ticket to $5K+ high-ticket.
Tagline: "The Coach Who Won't Tell You to Quit Your 9-to-5"
Positioning: Build an offer so clear it sells without a sales call — in one afternoon.

## Today's Activity (Run at Start of Every Chat)
Before doing anything, get oriented:
1. Run `git log --oneline --since="6am" --all` to see everything done today across all branches
2. Run `git log --oneline -10` to see the last 10 commits on this branch
3. Run `git diff --stat HEAD~3` to see what files changed recently
4. Scan `research/` and `decisions/` for any files dated today — read them for active context
5. Check git status for uncommitted work in progress
6. Check `content/drafts/` for any pending content awaiting review

Report a 2-3 line summary of today's state before proceeding with the task.

## Reference Stack (Read Before Any Content Work)
- reference/core/soul.md — Why we exist
- reference/core/offer.md — Value ladder ($47 front-end to $5K+ accelerator)
- reference/core/audience.md — Who buys (coaches stuck at early stages)
- reference/core/voice.md — How we sound (direct, no-BS, engineer mindset)
- reference/proof/angles/main-angles.md — Proven messaging hooks

## The Funnel (Know This)
| Step | Price | Product |
|------|-------|---------|
| Front-end | $47 | Client Ready Offer System |
| Bumps | $37-$97 | DM Scripts, Templates, $5K Playbook |
| OTO 1 | $197 | DFY Offer Build |
| Downsell | $97 | DFY Lite |
| OTO 2 | $37/mo | "What's Working Now" Newsletter |
| Community | $47/mo | Client Ready Community |
| Backend | $5K+ | Client Ready Accelerator |

AOV target: $90-110 | Full funnel AOV: ~$135

## Repo Structure
```
client-ready/
├── CLAUDE.md              # Project instructions
├── reference/
│   ├── core/              # soul, offer, audience, voice
│   ├── proof/             # testimonials, angles
│   └── domain/
│       ├── ads/           # ad strategy, budget, methodology
│       ├── funnel/        # stages, touchpoints, email rhythm, VSL
│       ├── sales/         # accelerator, sprint, DFY intake
│       ├── delivery/      # sprint delivery, soul extraction
│       ├── classroom/     # Skool modules, resources
│       └── membership/    # pricing, benefits
├── research/              # Dated research files (YYYY-MM-DD-topic.md)
├── decisions/             # Dated decision files (YYYY-MM-DD-decision.md)
├── content/
│   ├── drafts/            # Pending content (tweets, threads, linkedin, newsletter)
│   ├── scheduled/         # Approved, awaiting posting
│   └── published/         # Posted with engagement data
└── outputs/               # Generated ad copy, VSLs, etc.
```

## Resolving Checklist
1. Read CLAUDE.md for project-level instructions
2. Check git status — note branch, uncommitted changes
3. Review today's activity so you know what's already been done
4. If task involves content generation, read the relevant reference/core/ files FIRST
5. If task involves ads, also read reference/domain/ads/methodology.md
6. If task involves the funnel, read reference/domain/funnel/stages.md
7. If task involves research, check if a research file on the topic already exists

## Working Patterns
- Use /think for research, decisions, and codification
- Use /ads for Meta ad creation (static, video, creative variations, compliance review)
- Use /vsl for video sales letter scripts
- Use /organic for tweets, LinkedIn, newsletter content
- Spin up parallel agents for research — each gets a different angle/tool
- Every research file: research/YYYY-MM-DD-topic-slug.md
- Every decision file: decisions/YYYY-MM-DD-decision-slug.md
- Never generate content without reading the reference stack first
- When enriching reference files, read the existing file first — update, don't overwrite
- Content drafts go in content/drafts/{tweets,threads,linkedin,newsletter}/

## Voice Rules (Apply to All Generated Content)
- Direct. No-BS. Engineering mindset. Short sentences.
- Confident and grounded, not hype. Calm energy.
- Anti-guru positioning. Substance over perception.
- Signature phrases: "Wrong." "Test, validate, build." "You can't grow into pain."
- Never: "revolutionary", "game-changing", "unlock potential", "journey"
- See reference/core/voice.md for full guidelines.

## Ad Rules (Apply to All Ad Content)
- Read reference/domain/ads/methodology.md before creating any ads
- Always run /ad-review for compliance before shipping
- Budget framework in reference/domain/ads/budget-framework.md
- Andromeda strategy in reference/domain/ads/andromeda-strategy.md

## Content Cadence
| Channel | Frequency |
|---------|-----------|
| Newsletter | 1/week (Tuesday send) |
| X threads | 2/week |
| LinkedIn posts | 3-5/week |
| Daily tweets | 3-5/day |
| LinkedIn CTA | Always "link in comments" (never inline URLs) |

## OpenClaw (Automation Layer)
8 automated jobs run on the M1 Mac Mini via OpenClaw:
- Content distribution, ad monitoring, email intelligence, morning brief
- Content recycling, voice pipeline, mid-funnel branding, journal intelligence
- See reference/domain/openclaw-automation.md for full blueprint
- Manage from MacBook: `ssh m1 'export PATH="/opt/homebrew/bin:$PATH"; openclaw cron list'`

## Git Hygiene
- One branch per task
- Commit messages: [add], [update], [fix], [remove] prefix
- Pull request per branch when work is complete
- Never commit .env or credentials files
