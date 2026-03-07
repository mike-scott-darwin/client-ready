---
type: output
status: draft
date: 2026-03-07
---

# Live Demo Script -- 4 Minutes

Run this from the client-ready repo in Claude Code.
Goal: Show the audience the loop from reference to output in real time.

---

## Setup (before you go on stage)

- Have Claude Code open in the client-ready repo
- Have Telegram open on your phone (for the bot demo)
- Have Obsidian open with the home dashboard visible
- Terminal font size: 18+ (readable from back of room)

---

## Demo Flow (4 minutes)

### Beat 1: Show the Reference Stack (45 seconds)

WHAT TO SAY:
"This is my entire business in a terminal. Let me show you
what's under the hood."

WHAT TO DO:
- Run: ls reference/core/
- Open soul.md briefly -- scroll to the operating principles
- Say: "This is my WHY. Every piece of content, every ad, every
  email reads from this file. When I update this, everything
  downstream changes."

WHAT TO SAY:
"Four files. Soul, offer, audience, voice. That's the entire
instruction set for AI. No prompting tricks. No 50-page briefs.
Four files."

---

### Beat 2: Show a Decision (30 seconds)

WHAT TO DO:
- Run: ls decisions/ | tail -5
- Open one recent decision file briefly

WHAT TO SAY:
"38 strategic decisions, all documented. When I decided to price
at 47 instead of 27, the reasoning is here. When I chose
newsletter-first over social-first, it's here. Every decision
updates the reference files. The system gets smarter over time."

---

### Beat 3: Generate Something Live (90 seconds)

WHAT TO SAY:
"Let me show you what happens when you ask AI to create from
a real reference stack versus a blank prompt."

WHAT TO DO:
- Type: "Write me one tweet about offer validation in my voice"
- Let Claude read voice.md and offer.md automatically
- Show the output

WHAT TO SAY:
"Notice it didn't say 'unlock your potential' or 'level up.'
It matched my voice -- direct, no-BS, specific. Because voice.md
has anti-patterns. It knows what NOT to say. That's the difference
between AI-generated slop and AI-amplified content."

---

### Beat 4: Show the Bot (60 seconds)

WHAT TO DO:
- Pull up your phone with Telegram
- Show a recent bot message (daily tweets or research summary)
- If timing works, trigger a cron job live:
  openclaw cron run [daily-tweets-id]

WHAT TO SAY:
"This is my M1 Mac Mini running at home. At 2 AM it researches
topics related to my offer using Gemini. At 5:30 it sends me
a summary. At 6 AM it drafts my daily tweets. At 8 AM it finds
people on X asking questions I can answer and drafts replies.

I wake up, check Telegram, tap approve. That's my morning.

But here's the key -- the bot reads from the same reference files.
If I update my offer tomorrow, tomorrow's content reflects that.
No rebrief. No onboarding a new VA. Just update the file."

---

### Beat 5: The Obsidian View (30 seconds)

WHAT TO DO:
- Switch to Obsidian
- Show the graph view briefly (all the interconnected files)
- Show one dashboard (decisions or content tracker)

WHAT TO SAY:
"Everything is connected. Research feeds decisions. Decisions
update reference. Reference drives output. And I can see the
whole thing as a graph. 322 commits of documented thinking."

---

## Transition Back to Slides

WHAT TO SAY:
"That's the system. Reference files are the product.
Everything else -- ads, emails, tweets, research -- is derivative.
The human decides what matters. AI handles how much gets done."

[Switch back to Slide 9 or 10]

---

## Emergency Fallbacks

IF CLAUDE CODE IS SLOW:
- Have screenshots ready of output examples
- Pre-generate a tweet to show as backup

IF TELEGRAM BOT DOESN'T RESPOND:
- Show a previous conversation in Telegram history
- Say "The bot runs on schedule -- let me show you what
  it sent this morning"

IF OBSIDIAN WON'T OPEN:
- Skip Beat 5, you've already made the point
- Go straight back to slides

---

## Key Lines to Memorize

These land well with agency audiences:

- "Four files. That's the entire instruction set."
- "Remove the human and you get volume. Amplify the human
   and you get a business."
- "The bot reads from the same reference files. Update once,
   everything changes."
- "38 decisions, all documented. Try asking your current process
   why you made a choice 6 weeks ago."
- "This isn't AI replacing a copywriter. This is AI making the
   founder's thinking the operating system."
