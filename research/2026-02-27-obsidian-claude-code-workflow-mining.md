---
type: research
status: active
date: 2026-02-27
source: mining
linked_decisions: []
---

# Obsidian + Claude Code Workflow — YouTube Mining

## Sources

Two YouTube videos on using Obsidian as a context layer for Claude Code and AI agents.

Video 1: Greg Isenberg and Vin (internetvin) on "Context Architecture" and the thinking partner workflow.

Video 2: Paperless Movement (Tom) on AI-native local PKM with Claude Code and the Cowork interface.

## Core Thesis (Both Videos)

AI agents are only as good as the context you give them. Most people use AI inefficiently by re-explaining themselves in temporary chat windows. The fix: store structured knowledge in local Markdown files (Obsidian), let Claude Code read the vault directly, and use the AI as a thinking partner rather than a task executor.

## Key Frameworks

**Context Architecture (Video 1):**

- Capture: Dump raw thoughts into Obsidian Daily Notes
- Contextualize: Maintain "Context Files" (readmes for your life and projects) defining values, state, goals
- Synthesize: Claude Code scans the vault, finds patterns and connections you missed
- Feedback Loop: AI acts as a "mirror" for cognition, not just an automation tool

**Specific Commands (Video 1):**

- /context: Loads core readme files so AI immediately knows who you are
- /trace [topic]: Look through daily note history and trace how an idea evolved
- /connect [A] [B]: Find novel connections between two disparate topics
- /ghost [question]: AI answers as you based only on vault content -- tests positioning clarity
- /drift: Compares stated intentions vs actual behavior over 30 days
- /graduate: Weekly scan of daily notes, identifies recurring themes, promotes to full content
- /challenge: Pressure tests beliefs by finding contradictions in your notes

**ICOR Framework (Video 2):**

- Input, Control, Output, Refine
- Separation of Outer World (noise: email, Slack) vs Inner World (signal: Obsidian)
- AI agent acts as triage between outer and inner worlds
- Action management (tasks in ClickUp/Todoist) decoupled from knowledge management (notes in Obsidian)

## Technical Setup

- Obsidian stores everything as local Markdown files -- Claude Code reads them directly via filesystem
- Obsidian CLI bridges Claude Code to vault metadata (orphan notes, link density, backlinks)
- "Cowork" is Anthropic's GUI wrapper for Claude Code -- shows what AI is reading/changing visually
- Bidirectional wiki links create a graph that AI can traverse for connections
- Frontmatter (YAML) enables structured queries via Dataview plugin

## Mapping to Client Ready

What the reference system already provides (no change needed):

- Identity context: soul.md
- Offer context: offer.md
- Audience context: audience.md
- Style context: voice.md
- Decision history: decisions/ folder
- Project state: content-strategy.md

What is missing (the gap Obsidian fills):

- Raw thinking inbox: no daily notes or journal layer for unprocessed ideas
- Pattern discovery: no mechanism to find recurring themes across sessions
- Idea graduation: no pipeline from "half-thought" to "content or reference update"
- Phone capture: no way to send a quick thought from phone into the system

## Implications for OpenClaw

The journal layer turns the phone from an approval device into a capture device. Voice memos and quick thoughts land in journal/ via messaging, get triaged by the agent, and graduate to content or reference updates. The morning brief gains a "thinking patterns" section. Content recycling feeds from raw ideas, not just published performance.
