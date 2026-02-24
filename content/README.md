# Content Pipeline

Git-tracked content production for Client Ready.

## How It Works

```
drafts/       → Agent or human creates content here
scheduled/    → Approved content waiting to publish
published/    → Posted content with engagement metadata
```

Every piece of content is a git commit. Full audit trail.

## File Naming

```
YYYY-MM-DD-platform-type-slug.md
```

Examples:
- `2026-02-25-x-thread-offer-clarity.md`
- `2026-02-25-linkedin-post-anti-guru.md`
- `2026-02-25-newsletter-before-the-funnel.md`
- `2026-02-25-x-tweet-daily-01.md`

## Metadata

Each file includes frontmatter:

```yaml
---
platform: x | linkedin | newsletter
type: thread | post | tweet | newsletter
angle: before-the-funnel | clarity-unlock | anti-guru | etc.
pillar: offer-creation | funnel-strategy | anti-guru | behind-the-scenes
status: draft | approved | scheduled | published
published_date: null
engagement: null
---
```

## Workflow

1. Draft content (Claude Code, `/organic`, or manual)
2. Save to `content/drafts/`
3. Review and edit
4. Move to `content/scheduled/` (approved)
5. Publish via Typefully / LinkedIn / Beehiiv
6. Move to `content/published/` with engagement data

## Phase 2 (OpenClaw)

When OpenClaw is active, the agent:
- Reads from `reference/` (voice, angles, hooks, audience)
- Writes to `content/drafts/`
- Sends to Telegram for approval
- Posts on schedule after approval
- Archives to `content/published/` with metrics
