---
type: reference
status: active
date: 2026-03-06
---

# Deep Research Pipeline — Bot Instructions

These instructions govern the overnight deep research pipeline.
The OpenClaw bot reads this file during research cron jobs.

## Overview

Every night at 2:00 AM, you research one topic from the rotation in
research-topics.yaml. Every morning at 5:30 AM, you compile findings
and send a summary to Telegram.

## Nightly Research Job (2:00 AM)

### Step 1 — Determine today's topic

Read /Users/michaelscott/Documents/GitHub/client-ready/scripts/research-topics.yaml.
Match the current day of week to the rotation entry.

### Step 2 — Read current reference state

Read the reference file(s) listed in the "enhances" field for today's topic.
Understand what's already documented so research adds NEW insights, not
duplicates of what's already in the file.

### Step 3 — Run Gemini deep research

Use the Gemini deep research tool with today's research prompt.
Let the research run fully — don't cut it short.

### Step 4 — Save findings

Save to: /Users/michaelscott/Documents/GitHub/client-ready/research/YYYY-MM-DD-SLUG-gemini.md

Use this frontmatter:

```yaml
---
type: research
status: active
date: YYYY-MM-DD
source: gemini
enhances:
  - reference/core/FILENAME.md
linked_decisions: []
---
```

Structure the research file:

1. **Summary** — 3-5 sentence overview of key findings
2. **Key Insights** — Bulleted list of actionable findings (aim for 5-10)
3. **Data Points** — Specific numbers, benchmarks, case studies found
4. **Contrarian Findings** — Anything that challenges current assumptions
5. **Suggested Reference Updates** — Specific quotes/sections to add to
   reference files, with exact file paths and suggested placement
6. **Sources** — Where findings came from (URLs, studies, case studies)

### Step 5 — Commit locally

Stage and commit with message: [add] Deep research: TOPIC TITLE

Do NOT push to GitHub. Mike pushes manually from terminal.

## Morning Summary Job (5:30 AM)

### Step 1 — Find overnight research

Check /Users/michaelscott/Documents/GitHub/client-ready/research/ for files
created in the last 24 hours matching the pattern *-gemini.md.

### Step 2 — Read and analyze

For each new research file:
- Read the full file
- Read the reference file(s) it enhances
- Identify the 3-5 most actionable findings
- Draft specific suggestions for reference file updates

### Step 3 — Send Telegram summary

Send a single Telegram message with this structure:

OVERNIGHT RESEARCH COMPLETE

Topic: [title]
File: research/[filename]

TOP FINDINGS:
1. [Most important finding — one sentence]
2. [Second finding]
3. [Third finding]

SUGGESTED REFERENCE UPDATES:
- [which file]: [what to add/change and why]
- [which file]: [what to add/change and why]

Reply "approve" to apply these suggestions.
Reply "skip" to ignore.
Reply with specific feedback to adjust.

### Step 4 — Handle response

If Mike replies "approve":
- Apply the suggested changes to reference files
- Commit with message: [update] FILENAME — enhanced from DATE research
- Do NOT push — local commit only

If Mike replies "skip":
- Do nothing. Move on.

If Mike gives specific feedback:
- Adjust suggestions based on feedback
- Present revised changes for approval

## Rules

1. NEVER auto-edit reference files without explicit approval
2. NEVER push to GitHub — local commits only
3. NEVER duplicate insights already in reference files
4. Focus on DATA over opinions — numbers, benchmarks, case studies
5. Prioritize CONTRARIAN insights that challenge assumptions
6. Keep research files under 2000 words — dense and actionable, not padded
7. Skip generic advice that any coach could find on Google
8. When in doubt, flag it for human review rather than assuming
