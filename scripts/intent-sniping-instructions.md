---
type: reference
status: active
date: 2026-03-06
---

# Intent Sniping Pipeline — Bot Instructions

Daily job that finds Client Ready's audience on X and drafts helpful replies.

## Overview

Every morning at 8:00 AM, search X for people asking questions Mike can answer.
Draft 5-7 replies in Mike's voice. Send batch to Telegram for approval.
Post approved replies.

## Step 1 — Load Context

Read these files:
- /Users/michaelscott/Documents/GitHub/client-ready/scripts/intent-sniping-config.yaml (keywords + reply rules)
- /Users/michaelscott/Documents/GitHub/client-ready/reference/core/voice.md (tone and style)
- /Users/michaelscott/Documents/GitHub/client-ready/reference/core/offer.md (what Mike actually sells — for context, NOT for pitching)

## Step 2 — Find Targets

Pick 2-3 keyword groups from the config (rotate daily so you cover all groups
across the week). Use Gemini search to find recent tweets (last 48 hours)
matching those keywords.

Filter for quality targets:
- Real people asking genuine questions (not bots, not other coaches pitching)
- Tweets with some engagement (2+ likes or replies = proven interest)
- People who look like they could be in Mike's audience (coaches, consultants,
  service providers, or people considering coaching as a business)

Skip:
- Tweets older than 48 hours (stale conversations)
- People with 100K+ followers (they don't need help finding answers)
- Threads where someone already gave a great answer
- Obvious troll posts or rage bait

## Step 3 — Draft Replies

For each target (aim for 5-7 per day):
- Draft a reply following the reply_rules in the config
- Keep it 2-3 sentences max
- Lead with insight, not credentials
- Sound like a peer who's figured this out, not a coach selling something
- Match voice.md tone: direct, practical, no-BS

## Step 4 — Send Batch to Telegram

Send a single Telegram message with all drafts:

INTENT SNIPE BATCH — [date]

[number] replies ready for review:

1. @[username]: "[their tweet, truncated to 100 chars]"
   REPLY: "[your draft reply]"

2. @[username]: "[their tweet]"
   REPLY: "[your draft reply]"

[...continue for all drafts]

Reply with numbers to approve (e.g. "1,3,5")
Reply "all" to approve everything
Reply "skip" to skip today
Reply with edits: "2: [new text]"

## Step 5 — Post Approved Replies

For approved replies:
- Post each reply to the original tweet
- Use the x-poster.py script or X API directly
- Log what was posted to content/published/ (optional — only if tracking)

For edited replies:
- Use the edited text instead of the draft
- Post as above

## Rules

1. NEVER pitch, link, or sell in replies — pure value only
2. NEVER reply to the same person twice in one week
3. NEVER use hashtags in replies
4. NEVER engage with negativity or arguments
5. Keep a natural pace — 5-7 replies is enough, don't spam
6. If you can't find 5 quality targets, send fewer — quality over quantity
7. Rotate keyword groups so all 5 categories get coverage across the week
