---
type: reference
status: active
date: 2026-02-03
linked_decisions:
  - decisions/2026-02-03-content-strategy.md
  - decisions/2026-02-24-content-automation-rollout.md
---

# Content Strategy

Newsletter-first content system for Client Ready.

---

## The Model

```
Weekly Newsletter (keystone)
    ↓
Deconstruct → 2 X threads + 3-5 LinkedIn posts
    ↓
Daily → 3-5 tweets (observations, one-liners, replies)
    ↓
High-intent signals → DM conversations
    ↓
$47 → DFY / Community → Accelerator
```

```mermaid
graph TD
    NL["<b>Weekly Newsletter</b><br/>Keystone — Tuesday"] --> TH["2 X Threads<br/>Tuesday + Thursday"]
    NL --> LI["3-5 LinkedIn Posts<br/>Weekdays"]
    NL --> TW["3-5 Daily Tweets<br/>Observations + Replies"]
    
    TH --> ENG["Engagement<br/>Replies + DMs"]
    LI --> ENG
    TW --> ENG
    
    ENG --> SUB["Newsletter Signup<br/>Bio Link + Thread CTA"]
    SUB --> NL
    
    ENG --> DM["DM Conversations<br/>High-Intent Signals"]
    DM --> FE["47 Front-End"]
    FE --> SP["DFY / Community + Accelerator"]
    
    style NL fill:#4a9eff,color:#fff
    style FE fill:#ff6b35,color:#fff
    style SP fill:#ff6b35,color:#fff
```


**Philosophy:** Write once, repurpose everywhere. Email is the revenue engine; social is discovery.

---

## Platforms

| Platform | Role | Frequency | Format |
|----------|------|-----------|--------|
| **Beehiiv** | Engine | 1x/week (Tuesday) | Long-form newsletter |
| **X/Twitter** | Primary discovery | 3-5 tweets/day + 1-2 threads/week | Text, threads |
| **LinkedIn** | Secondary discovery | 3-5 posts/week | Text, carousels |

**Not using:** Instagram, TikTok, YouTube (for now)

---

## Weekly Rhythm

| Day | Newsletter | X/Twitter | LinkedIn |
|-----|------------|-----------|----------|
| **Monday** | Write newsletter | 3-5 tweets | — |
| **Tuesday** | Send newsletter | Thread from newsletter + tweets | Post adapted from newsletter |
| **Wednesday** | — | 3-5 tweets | Post (pillar content) |
| **Thursday** | — | Thread (standalone) + tweets | Post (behind the scenes) |
| **Friday** | — | 3-5 tweets | Post (contrarian take) |
| **Weekend** | Batch next week | Light engagement | — |

**Time investment:** ~2-3 hrs/week (Phase 0 — batch-draft with Claude, manual posting)

---

## Content Pillars

| Pillar | What It Covers | Example Topics |
|--------|----------------|----------------|
| **Offer Creation** | Validation, pricing, positioning | "How to validate before you build", "The $47 test", "Why your offer isn't selling" |
| **Funnel Strategy** | Value ladders, bumps, OTOs, email | "Why most coaches build backwards", "The bump nobody talks about", "Email > content" |
| **Anti-Guru** | Contrarian takes, no-BS truth | "You can't grow into pain", "Stop posting, start selling", "The guru lie" |
| **Behind the Scenes** | Real numbers, real struggles | "114 sales: what I learned", "What actually happened this week", "The mistake I made" |

**Rotation:** Hit each pillar at least once per week across platforms.

---

## Hooks Library

### Contrarian Hooks
- "Most coaches have it backwards."
- "You don't need a bigger audience. You need a better offer."
- "Stop posting. Start selling."
- "The content treadmill is a trap."
- "Engagement doesn't pay rent."

### Direct Address Hooks
- "If you're still posting free content hoping someone buys..."
- "You've been told to 'add value first.' Wrong."
- "Here's what nobody tells you about high-ticket..."
- "The reason you're stuck isn't what you think."

### Transformation Hooks
- "From 0 to 114 sales in 30 days. Here's the system."
- "I validated a $5K offer in one afternoon. Here's how."
- "What changed when I stopped chasing followers."
- "The $47 offer that funds my entire business."

### Anti-Guru Hooks
- "I'm not going to tell you to quit your 9-to-5."
- "No webinar. No VSL. Just a $47 offer and a system."
- "The 'guru playbook' is broken. Here's what works instead."
- "You don't need a personal brand. You need paying clients."
- "Stop buying prompt packs. Start building your context."
- "ChatGPT writes garbage because you gave it nothing to work with."
- "AI is an amplifier. Feed it chaos, get polished chaos back."
- "Everyone's chasing the perfect prompt. The answer is a system, not a sentence."
- "Prompts without a system are ingredients without a kitchen."

### Thread Starters
- "I spent [X] learning [Y]. Here's what actually works:"
- "The exact system I use to [outcome]:"
- "Everyone's overcomplicating [topic]. Here's the simple version:"
- "[Number] things I'd do differently if I started over:"

---

## Thread Frameworks

### Problem → Solution (5-7 tweets)
1. Hook: State the problem boldly
2. Agitate: Why it's worse than they think
3. Bridge: What they've tried that doesn't work
4. Solution: Your framework (3-4 steps)
5. Proof: Your result or client result
6. CTA: Soft pitch or engagement ask

### "Here's the System" (7-10 tweets)
1. Hook: Promise the system
2. Context: Why you built it
3. Step 1-5: The actual steps
4. Result: What happens when you follow it
5. CTA: Where to get more

### Contrarian Take (5 tweets)
1. Hook: Bold contrarian statement
2. Why most people believe the opposite
3. What you've seen instead
4. The reframe
5. CTA: Agree/disagree engagement

---

## Conversion Path

### From Content to Cash

```
Content (value)
    ↓
Engagement (replies, DMs)
    ↓
Newsletter signup (bio link, thread CTA)
    ↓
Daily emails (trust + offers)
    ↓
$47 front-end
    ↓
Bumps + OTOs (DFY Offer Build, Newsletter, Community)
    ↓
Email ascension
    ↓
$5K Accelerator
```

### CTAs by Platform

| Platform | Primary CTA | Secondary CTA |
|----------|-------------|---------------|
| X/Twitter | "Follow for more" / Newsletter link in bio | "DM me [word] for [thing]" |
| LinkedIn | Link to $47 offer | "DM me if this resonates" |
| Newsletter | Relevant offer from value ladder | Reply to build relationship |

---

## DM Strategy

**Triggers to DM:**
- Engaged with 3+ posts
- Replied with a question
- Shared their struggle
- Fits ideal client profile

**DM Framework:**
1. Acknowledge their comment/situation
2. Ask one clarifying question
3. Listen
4. Offer relevant resource (free or $47)

**Not:** Pitch slapping. Relationship first.

---

## Metrics to Track

| Metric | Where | Baseline | 30-Day | 90-Day |
|--------|-------|----------|--------|--------|
| Newsletter subscribers | Beehiiv | — | +200 | +1,000 |
| X followers | X | — | +500 | +2,000 |
| LinkedIn followers | LinkedIn | — | +200 | +1,000 |
| Newsletter open rate | Beehiiv | — | 40%+ | 40%+ |
| DM conversations/week | Manual | 0 | 5 | 15 |
| Organic → $47 sales/week | Funnel tracking | 0 | 2 | 10 |

**Review cadence:** Weekly (Sunday)

---

## Content Bank

_Add winning posts, high-engagement hooks, and proven frameworks here as you discover them._

### Top Performers (X)
| Date | Post | Engagement | Why It Worked |
|------|------|------------|---------------|
| — | — | — | — |

### Top Performers (LinkedIn)
| Date | Post | Engagement | Why It Worked |
|------|------|------------|---------------|
| — | — | — | — |

### Newsletter Issues (Best)
| Date | Subject | Open Rate | Click Rate | Why It Worked |
|------|---------|-----------|------------|---------------|
| — | — | — | — | — |

---

## Framework Library

_Add frameworks extracted from mining and research here._

### From Research (2026-02-03)

**Justin Welsh's "Hub and Spoke":**
- Newsletter = hub (80% effort)
- Social posts = spokes (20% effort)
- One piece of content → full week of posts

**Dickie Bush's Testing Method:**
- Test 8-10 single tweets per week
- Expand top 2 performers into threads
- Let engagement data guide effort

**LinkedIn Carousel Formula:**
- 6-10 slides (sweet spot)
- Hook on slide 1
- One idea per slide
- CTA on last slide

---

## Automation Pipeline

Git-tracked content production. All content lives in `content/` with full audit trail.

```
content/
├── drafts/       → Agent or human creates content here
├── scheduled/    → Approved content waiting to publish
└── published/    → Posted content with engagement metadata
```

### Phases

| Phase | What | Time/Week | Cost/Mo | Status |
|-------|------|-----------|---------|--------|
| **0: Manual** | Batch-draft with Claude, manual posting | 2-3 hrs | $0 | **Active** |
| **1: Scheduled** | Typefully + Buffer APIs, agent drafts, human reviews | <1 hr | ~$30 | March 2026 |
| **2: OpenClaw** | Always-on agent, Telegram approvals, auto-publish | 15 min/day | ~$87 | Q2 2026 |
| **3: Voice-Note** | Talk → transcribe → agent shapes → posts | 15 min/day | TBD | Q3 2026 |

**Phase gates:** Each phase requires 4+ weeks of proven performance before graduating.

### Phase 0 Workflow (Current)

1. Monday: Batch-draft a week of content using `/organic` or Claude Code
2. Save to `content/drafts/` — each piece gets frontmatter (platform, type, angle, pillar)
3. Review and edit
4. Post manually via Typefully (X) and LinkedIn native
5. Move to `content/published/` with engagement data after posting
6. Sunday: Review metrics, update Content Bank tables

**Trigger to enter Phase 1:** Consistent 4+ weeks of content shipping with measurable engagement data.

### Key Principle

> "OpenClaw READS from your business repo. Business truth stays in the business repo."

Reference files are the canon. Content is derivative. The automation layer never touches the source of truth — it only reads from `reference/` and writes to `content/`.

---

## Tools

| Purpose | Tool | Phase |
|---------|------|-------|
| Newsletter | Beehiiv | 0+ |
| Scheduling (X) | Typefully (manual → API) | 0 (manual), 1+ (API) |
| Scheduling (LinkedIn) | Native or Buffer | 0 (native), 1+ (Buffer) |
| Analytics | Platform native + spreadsheet | 0-1 |
| Content calendar | Git (`content/drafts/` directory) | 0+ |
| Automation | OpenClaw + DigitalOcean | 2+ |
| Transcription | whisper-cpp (local) | 3 |

---

## Next Actions

- [x] Set up Beehiiv account
- [x] Optimize X bio with newsletter link
- [x] Optimize LinkedIn headline and about section
- [x] Write first newsletter
- [x] Create first week of content
- [x] Set up `content/` pipeline directories (drafts, scheduled, published)
- [ ] Set up weekly metrics tracking
- [ ] Ship 4 consecutive weeks of content (Phase 0 → Phase 1 gate)
- [ ] Set up Typefully API connection (Phase 1 prerequisite)
- [ ] Set up Buffer for LinkedIn scheduling (Phase 1 prerequisite)

---

*Last updated: 2026-02-28*
*Decisions: [2026-02-03-content-strategy.md](../../decisions/2026-02-03-content-strategy.md), [2026-02-24-content-automation-rollout.md](../../decisions/2026-02-24-content-automation-rollout.md)*

---

## See Also

- [soul.md](../core/soul.md) — WHY behind the content
- [audience.md](../core/audience.md) — WHO we are creating for
- [voice.md](../core/voice.md) — HOW we write and speak
- [offer.md](../core/offer.md) — The value ladder content promotes
- [main-angles.md](../proof/angles/main-angles.md) — Angles that map to content pillars
- [testimonials.md](../proof/testimonials.md) — Proof points to weave into content
