---
type: reference
status: active
date: 2026-03-12
---

# Parallel Agent Briefs

Configuration for spawning parallel Claude Code agents for content production and research.

**Repo root:** `/Users/michaelscott/Documents/GitHub/client-ready`

All paths below are relative to this root. Agents MUST read files using the full absolute path (e.g. `/Users/michaelscott/Documents/GitHub/client-ready/reference/core/voice.md`). All output files MUST be written to the same repo using absolute paths.

---

## Content Batch Briefs

### Newsletter Agent

```yaml
agent: newsletter
output: content/drafts/YYYY-MM-DD-newsletter-SLUG.md
reads:
  - reference/core/soul.md
  - reference/core/voice.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/domain/content-strategy.md
```

**Instructions:**
- Format: Markdown (Buttondown native)
- Length: 800-1200 words
- Structure: Hook → story/insight → practical takeaway → soft CTA
- Pillar: rotate weekly (Offer Creation → Funnel Strategy → Alignment-First → Behind the Scenes)
- CTA: soft push to $27 front-end at clientreadyoffer.com — never hard sell
- Sign-off: "Talk soon, Michael"
- Tone: direct, practical, alignment-first. Like a smart friend explaining what works.
- No emojis. No hype words. No "incredible" or "revolutionary."
- One-word sentences for emphasis are good. "Wrong." "Today."

---

### LinkedIn Agent

```yaml
agent: linkedin
output: content/drafts/linkedin/YYYY-MM-DD-linkedin-post-SLUG.md
count: 5 posts per batch
reads:
  - reference/core/voice.md
  - reference/core/audience.md
  - reference/domain/content-strategy.md
```

**Instructions:**
- Length: 150-300 words per post
- Format: short paragraphs (2-3 sentences), lots of white space
- Open with hook (Pattern 1-8 from voice.md)
- Each post covers one idea from one pillar
- Mix: 2 contrarian takes, 1 behind-the-scenes, 1 practical tip, 1 story
- CTA: vary between "Follow for more", "DM me if this resonates", link to newsletter
- No hashtags. No "thoughts?" at the end.

**Frontmatter per post:**
```yaml
---
type: content
platform: linkedin
pillar: [offer-creation | funnel-strategy | alignment-first | behind-the-scenes]
status: draft
scheduled_date: YYYY-MM-DD
---
```

---

### X Thread Agent

```yaml
agent: x-threads
output: content/drafts/tweets/YYYY-MM-DD-N.md (5 files per thread, 2 threads per batch)
count: 2 threads (10 files total)
reads:
  - reference/core/voice.md
  - reference/core/audience.md
  - reference/domain/content-strategy.md
```

**Instructions:**
- Each thread = 5 tweets posted as a reply chain
- Tweet 1: hook (stop the scroll — bold claim or contrarian statement)
- Tweets 2-4: the substance (framework, steps, insight)
- Tweet 5: CTA (follow, newsletter link, or engagement ask)
- Max 280 chars per tweet
- Use thread frameworks from content-strategy.md (Problem→Solution, "Here's the System", Contrarian Take)
- One thread per pillar — don't repeat pillars within a batch
- File naming: YYYY-MM-DD-1.md through YYYY-MM-DD-5.md per thread

**Frontmatter per tweet:**
```yaml
---
type: content
platform: x
format: thread
thread_position: N
pillar: [offer-creation | funnel-strategy | alignment-first | behind-the-scenes]
status: draft
scheduled_date: YYYY-MM-DD
---
```

---

### Daily Tweets Agent

```yaml
agent: daily-tweets
output: content/drafts/tweets/YYYY-MM-DD-daily-N.md
count: 15-25 standalone tweets (3-5 per day for a week)
reads:
  - reference/core/voice.md
  - reference/domain/content-strategy.md
```

**Instructions:**
- Standalone tweets, not threads
- Mix: observations, one-liners, reframes, questions
- Pull from hooks library in content-strategy.md
- Each tweet should work on its own — no context needed
- Max 280 chars
- No links in daily tweets (save links for threads)
- Tone: punchy, confident, sometimes provocative

---

## Research Briefs

### YouTube Mining Agent

```yaml
agent: youtube-mining
tool: Apify (mcp__apify__call-actor)
output: research/YYYY-MM-DD-TOPIC-yt-mining.md
reads:
  - reference/core/soul.md
  - reference/core/offer.md
```

**Instructions:**
- Extract transcript via Apify YouTube scraper
- Summarize: 1-sentence summary + 5-10 key findings
- Extract: frameworks, quotes, tactical advice
- Assess: what transfers to Client Ready context?
- Flag: contradictions with current reference files
- End with: implications for reference files + open questions

---

### X Sentiment Agent

```yaml
agent: x-sentiment
tool: Grok (if available) or WebSearch
output: research/YYYY-MM-DD-TOPIC-x-social.md
reads:
  - reference/core/audience.md
```

**Instructions:**
- Search X/Twitter for discourse on the topic
- Capture: dominant narratives, contrarian takes, recurring complaints
- Note: language patterns the audience uses (voice of customer gold)
- Assess: what angles are underserved?
- End with: implications for content + open questions

---

### Deep Research Agent

```yaml
agent: deep-research
tool: Gemini (if available) or WebSearch
output: research/YYYY-MM-DD-TOPIC-gemini.md
reads:
  - reference/core/soul.md
  - reference/core/offer.md
```

**Instructions:**
- Comprehensive multi-source research on the topic
- Synthesize across 5+ sources minimum
- Structure: summary → key findings → implications → open questions
- Prioritize: practitioner insights over theory
- Flag: anything that challenges current reference file assumptions

---

## Batch Command Patterns

### "Batch me next week's content"

Spawns 4 agents simultaneously:
1. **Newsletter agent** — 1 newsletter for Tuesday
2. **LinkedIn agent** — 5 posts (Mon-Fri)
3. **X thread agent** — 2 threads (Tue + Thu)
4. **Daily tweets agent** — 15-25 standalone tweets

Each writes to `content/drafts/` with correct dates and frontmatter.
Existing posting scripts (x-poster.py, linkedin-poster.py) pick up automatically.
Newsletter goes through Buttondown → Telegram approval flow.

**Estimated tokens:** ~200-300K total across 4 agents
**Estimated cost:** ~$3-8
**Estimated time:** ~60-90 seconds (parallel)

### "Research [topic] from all angles"

Spawns 2-3 agents simultaneously:
1. **YouTube mining agent** — if URL provided
2. **X sentiment agent** — what people are saying
3. **Deep research agent** — comprehensive web research

Each writes its own research file. Main conversation synthesizes.

**Estimated tokens:** ~150-250K total
**Estimated cost:** ~$2-6
**Estimated time:** ~45-90 seconds (parallel)

---

## Rules

1. **Every agent reads voice.md** — non-negotiable for content agents
2. **Every agent verifies its write** — reads the file back after writing
3. **Main conversation synthesizes** — agents return summaries, main conversation connects dots
4. **Pillar rotation is tracked** — don't repeat the same pillar across agents in the same batch
5. **Dates are sequential** — LinkedIn posts get Mon-Fri dates, threads get Tue+Thu, newsletter gets Tuesday
6. **Never run content agents in background** — they need MCP tool access for permissions

---

*Linked from: [content-strategy.md](content-strategy.md)*
