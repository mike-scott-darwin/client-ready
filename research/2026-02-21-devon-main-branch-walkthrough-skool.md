---
type: research
status: active
date: 2026-02-21
source: mining
linked_decisions: []
---

# Devon Main Branch Walkthrough: Daily Driver Workflow (Skool Video Transcript, Feb 21 2026)

## Source

Devon (Main Branch creator) recorded a 29-minute walkthrough of how he personally uses Main Branch day-to-day. Covers setup, daily workflow, think skill deep dive, and vision for automated outputs.

## Setup (What Devon Actually Uses)

- VS Code with Claude Code extension (tried Warp, Cursor, Claude's app -- keeps going back to VS Code)
- Opens from VIP folder first, then adds business repo via File > Add Folder to Workspace
- Saves workspace so both directories persist between sessions
- GitHub Desktop for syncing (watches green dots on changed files during conversation)

## Daily Workflow

**Start:** /start (alone, no extra intent after it). Lets the skill fully invoke and route.

**End:** /end every session. Crystallizes what happened, ties loose threads, gives final chance to codify before closing.

Devon's exact words: "Start every day with /start and end every day with /end."

## How Devon Feeds Context

**Screenshots over descriptions.** Drags in screenshots of Skool about pages, YouTube channels, classrooms, competitor funnels, pricing cards. Visual context is faster than typing descriptions.

**Voice dumps.** Uses speech-to-text (WhisperFlow or similar) to brain dump directly into Claude Code. Raw thinking captures more than typed summaries.

**Video/call recordings.** Drags video files into Claude Code to pull transcripts. Discovery calls, coaching calls, voice notes -- all become research material.

**Folder drops.** If there is a folder of downloaded data about the offer, drags the whole folder in and says "this is what this is."

## The Think Skill (Devon's Most Important Feature)

Devon calls /think "the most robust skill in the whole infrastructure" and says it deserves its own dedicated video.

**The loop:** Research > Decision > Codify > Output

**How decisions become content:** "These decisions that you reel with, that you try to figure out -- you're turning them into something that goes in your newsletter, something that goes on your Twitter, something you queue onto your Instagram, because this is the meat of why you're working. And that stuff, that behind the scenes, is great for social media content."

**Interest-led research:** Devon found a YouTube video, brought it into the tool, discussed it -- and it helped him understand his why more. "My interest I had in the video kind of leaks into the business."

## Context Window Management

- Watches the percentage indicator at the bottom of VS Code
- When context gets thin, re-invokes the skill to reload the full prompt
- Files are the safety net -- everything saved survives compaction
- Can ask the system to look at files and commits to rebuild context after compaction

Devon's advice: "If you start to kind of lose sight of what's going on, feel free to re-invoke it."

## The Vision

Devon's current state: type /ads to make ads, /organic to make content. Manual invocation.

Devon's future state: outputs automated based on preferences. Content queued to Twitter tailored to voice. Instagram carousels generated. Ads built for the ad account. All driven by enriched reference files.

"I'm obsessed with enriching this reference to automate the outputs."

## Key Principles

1. **Reference enrichment is the primary work.** Everything else (ads, content, sites) reads from reference. Better reference = better outputs.
2. **Decisions are content.** The behind-the-scenes thinking IS the content pipeline. Do not treat decisions as internal-only documents.
3. **Files survive context.** The context window is temporary. Files are permanent. Save everything that matters.
4. **Skills are flexible.** There is structure but also leniency. Break the rules when it makes sense. Modify, improve, intervene.
5. **soul.md is the anchor.** Devon emphasizes recording the why behind the work. "Having that why in there helps us stay connected to the offer, which gives us more energy and helps us execute more work with more interest."

## Lessons for Client Ready Workflow

**Use /end consistently.** Every session should close with crystallization. The machine concept decision, the OpenClaw research, the email updates -- all of today's work should get a final pass before session close.

**Mine decisions for content.** The funnel congruence audit, the machine concept decision, the brand metaphor decision -- these are not just internal docs. Each one is a potential X post, newsletter piece, or organic content seed.

**Re-invoke after compaction.** When context compacts, re-run /start or /think to reload the full skill prompt. Do not just keep chatting with degraded context.

**Voice input for brain dumps.** Faster than typing, captures raw thinking, feeds the system with unfiltered context.

**Screenshots of GHL workflows, Skool pages, funnel steps.** Visual context feeds the system faster than describing what things look like.

## Quote Bank

- "Start every day with /start and end every day with /end."
- "I'm obsessed with enriching this reference to automate the outputs."
- "These decisions that you reel with, that you try to figure out -- you're turning them into something that goes in your newsletter."
- "Instead of getting sucked into a rabbit hole, I brought the YouTube video into this tool and we talked about it and it actually helped me understand my why more."
- "All the project management tools have kind of faded into the background."
- "Don't be afraid to just kind of keep talking, keep re-invoking the same skill."
