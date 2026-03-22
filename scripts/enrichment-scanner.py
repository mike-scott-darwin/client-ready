#!/usr/bin/env python3
"""
Enrichment Scanner for Client Ready

Reads the last 7 days of journal/ entries, cross-references against
reference files, and outputs a connections report.

What it does (no LLM needed):
1. Lists recent journal entries and extracts key themes
2. Checks reference file staleness (days since last modified)
3. Finds recurring words/phrases across journal entries
4. Matches journal themes to content pillars
5. Lists open decisions that need resolution
6. Outputs a report to research/YYYY-MM-DD-enrichment-scan.md

Designed to run daily at 6am via launchd. The report is picked up
by /think or /start for smart analysis in Claude Code.
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).parent.parent
JOURNAL_DIR = REPO_ROOT / "journal"
REFERENCE_DIR = REPO_ROOT / "reference"
RESEARCH_DIR = REPO_ROOT / "research"
DECISIONS_DIR = REPO_ROOT / "decisions"
LOG_FILE = REPO_ROOT / "scripts" / "enrichment-scanner.log"

PILLARS = {
    "Offer Creation": [
        "offer", "validate", "validation", "pricing", "positioning",
        "zone of genius", "extract", "aligned", "alignment", "misaligned",
        "misalignment", "product", "sell", "selling", "monetize",
    ],
    "Funnel Strategy": [
        "funnel", "bump", "oto", "upsell", "email", "sequence",
        "landing page", "checkout", "conversion", "traffic", "paid",
        "ads", "retarget", "value ladder",
    ],
    "Anti-Guru": [
        "guru", "hustle", "grind", "content treadmill", "merry-go-round",
        "push through", "scale", "passive income", "six figure",
        "no-bs", "authentic", "honest", "contrarian", "real talk",
    ],
    "Behind the Scenes": [
        "struggle", "lesson", "mistake", "learned", "real numbers",
        "honest", "what happened", "building in public", "journey",
        "day in the life", "process", "behind",
    ],
}

REFERENCE_CONCEPTS = {
    "soul.md": [
        "can't grow into pain", "alignment", "dissociation", "association",
        "content merry-go-round", "paid traffic", "freedom", "pull or push",
        "identity", "north star", "burn down", "sustainable",
    ],
    "offer.md": [
        "confused to clear", "converting", "5 ai prompts", "one afternoon",
        "client ready offer", "low-ticket", "sprint", "blueprint",
        "accelerator", "community",
    ],
    "audience.md": [
        "year 2", "year 3", "9-to-5", "transition", "expertise",
        "courses", "tried content", "gurus lied", "not cut out",
        "skeptical", "burned", "coaches",
    ],
    "voice.md": [
        "anti-guru", "no emojis", "smart friend", "direct",
        "engineer", "practical", "no-bs", "specific not vague",
    ],
}

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "shall", "can", "need", "dare",
    "this", "that", "these", "those", "me", "my", "we", "our",
    "you", "your", "he", "him", "his", "she", "her", "it", "its",
    "they", "them", "their", "what", "which", "who", "whom", "how",
    "when", "where", "why", "not", "no", "nor", "so", "if", "then",
    "than", "too", "very", "just", "about", "above", "after", "again",
    "all", "also", "am", "as", "because", "before", "between", "both",
    "each", "few", "get", "got", "here", "into", "more", "most", "much",
    "must", "new", "now", "only", "other", "out", "own", "same", "some",
    "still", "such", "take", "through", "under", "up", "us", "way",
    "well", "while", "like", "even", "make", "one", "two", "first",
    "think", "know", "want", "see", "look", "going", "thing", "things",
    "really", "something", "people", "don't", "doesn't", "didn't",
    "won't", "wouldn't", "couldn't", "shouldn't", "it's", "that's",
    "there", "there's", "they're", "we're", "you're", "i'm", "i've",
    "i'll", "i'd", "let", "say", "said", "right", "over", "down",
    "back", "them", "time", "work", "day",
}


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def get_recent_journal_entries(days=7):
    entries = []
    cutoff = datetime.now() - timedelta(days=days)
    if not JOURNAL_DIR.exists():
        return entries
    for f in sorted(JOURNAL_DIR.iterdir()):
        if f.name.startswith("_") or f.name.startswith("."):
            continue
        if f.suffix != ".md":
            continue
        match = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        if match:
            try:
                entry_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                if entry_date >= cutoff:
                    content = f.read_text()
                    entries.append({"date": match.group(1), "filename": f.name, "content": content})
            except ValueError:
                continue
        else:
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if mtime >= cutoff:
                content = f.read_text()
                entries.append({"date": mtime.strftime("%Y-%m-%d"), "filename": f.name, "content": content})
    return entries


def check_reference_staleness():
    staleness = []
    core_dir = REFERENCE_DIR / "core"
    if core_dir.exists():
        for f in core_dir.iterdir():
            if f.suffix == ".md":
                mtime = datetime.fromtimestamp(f.stat().st_mtime)
                days_old = (datetime.now() - mtime).days
                staleness.append({"file": f.name, "last_modified": mtime.strftime("%Y-%m-%d"), "days_old": days_old})
    domain_dir = REFERENCE_DIR / "domain"
    if domain_dir.exists():
        for f in domain_dir.iterdir():
            if f.suffix == ".md":
                mtime = datetime.fromtimestamp(f.stat().st_mtime)
                days_old = (datetime.now() - mtime).days
                staleness.append({"file": f"domain/{f.name}", "last_modified": mtime.strftime("%Y-%m-%d"), "days_old": days_old})
    return sorted(staleness, key=lambda x: x["days_old"], reverse=True)


def find_recurring_themes(entries):
    if not entries:
        return []
    word_entry_count = Counter()
    for entry in entries:
        content_lower = entry["content"].lower()
        words = set(re.findall(r'\b[a-z]{4,}\b', content_lower))
        words -= STOP_WORDS
        for word in words:
            word_entry_count[word] += 1
    return [(word, count) for word, count in word_entry_count.most_common(30) if count >= 2]


def match_to_pillars(entries):
    pillar_matches = {pillar: [] for pillar in PILLARS}
    for entry in entries:
        content_lower = entry["content"].lower()
        for pillar, keywords in PILLARS.items():
            matched_keywords = [kw for kw in keywords if kw in content_lower]
            if matched_keywords:
                pillar_matches[pillar].append({"date": entry["date"], "keywords": matched_keywords})
    return pillar_matches


def find_reference_connections(entries):
    connections = []
    for entry in entries:
        content_lower = entry["content"].lower()
        for ref_file, concepts in REFERENCE_CONCEPTS.items():
            matched = [c for c in concepts if c in content_lower]
            if matched:
                connections.append({"date": entry["date"], "reference": ref_file, "concepts": matched})
    return connections


def get_open_decisions():
    open_decisions = []
    if not DECISIONS_DIR.exists():
        return open_decisions
    for f in sorted(DECISIONS_DIR.iterdir(), reverse=True):
        if f.suffix != ".md":
            continue
        content = f.read_text()
        if "status: draft" in content or "status: accepted" in content:
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else f.name
            status_match = re.search(r'status:\s*(\w+)', content)
            status = status_match.group(1) if status_match else "unknown"
            open_decisions.append({"file": f.name, "title": title, "status": status})
    return open_decisions


def generate_report(entries, staleness, recurring, pillar_matches, connections, open_decisions):
    today = datetime.now().strftime("%Y-%m-%d")
    lines = []
    lines.append("---")
    lines.append("type: research")
    lines.append(f"date: {today}")
    lines.append("source: enrichment-scanner")
    lines.append("status: complete")
    lines.append("---")
    lines.append("")
    lines.append("# Enrichment Scan")
    lines.append("")

    # Journal Activity
    lines.append("## Journal Activity (Last 7 Days)")
    lines.append("")
    if entries:
        lines.append(f"**{len(entries)} entries found.**")
        lines.append("")
        for entry in entries:
            word_count = len(entry["content"].split())
            lines.append(f"- {entry['date']}: {entry['filename']} ({word_count} words)")
        lines.append("")
    else:
        lines.append("No journal entries in the last 7 days.")
        lines.append("")
        lines.append("The flywheel starts with capture. Write a journal entry today -- even 3 sentences about what you are thinking about your offer, your audience, or your method.")
        lines.append("")

    # Reference Staleness
    lines.append("## Reference Staleness")
    lines.append("")
    stale_files = [s for s in staleness if s["days_old"] > 14]
    fresh_files = [s for s in staleness if s["days_old"] <= 14]
    if stale_files:
        lines.append("**Needs attention (14+ days untouched):**")
        lines.append("")
        for s in stale_files:
            lines.append(f"- **{s['file']}** -- {s['days_old']} days (last: {s['last_modified']})")
        lines.append("")
    if fresh_files:
        lines.append("**Recently updated:**")
        lines.append("")
        for s in fresh_files:
            lines.append(f"- {s['file']} -- {s['days_old']} days ago")
        lines.append("")

    # Recurring Themes
    lines.append("## Recurring Themes Across Entries")
    lines.append("")
    if recurring:
        lines.append("Words/concepts appearing in 2+ journal entries (signal vs noise):")
        lines.append("")
        for word, count in recurring[:15]:
            lines.append(f"- **{word}** (in {count} entries)")
        lines.append("")
        lines.append("Themes appearing 3+ times are graduation candidates -- consider turning them into content or reference updates via /think.")
        lines.append("")
    else:
        lines.append("Not enough journal entries to detect recurring themes yet. Write for 3-4 days and patterns will surface.")
        lines.append("")

    # Pillar Matches
    lines.append("## Content Pillar Connections")
    lines.append("")
    any_matches = False
    for pillar, matches in pillar_matches.items():
        if matches:
            any_matches = True
            lines.append(f"### {pillar}")
            for m in matches:
                lines.append(f"- {m['date']}: matched on {', '.join(m['keywords'])}")
            lines.append("")
    if not any_matches:
        lines.append("No pillar connections detected. Journal entries may be exploring new territory -- check if this signals a new pillar or just needs more entries.")
        lines.append("")

    # Reference Connections
    lines.append("## Reference File Connections")
    lines.append("")
    if connections:
        lines.append("Journal entries that touch existing reference concepts:")
        lines.append("")
        for c in connections:
            lines.append(f"- {c['date']} connects to **{c['reference']}**: {', '.join(c['concepts'])}")
        lines.append("")
        lines.append("These connections suggest the reference file could be enriched with the journal entry's perspective. Run /think codify to update.")
        lines.append("")
    else:
        lines.append("No direct connections to reference concepts detected. This could mean:")
        lines.append("1. Journal entries are exploring genuinely new territory (good -- potential new angles)")
        lines.append("2. The entries are too abstract to match keywords (try being more specific)")
        lines.append("")

    # Open Decisions
    lines.append("## Open Decisions")
    lines.append("")
    if open_decisions:
        lines.append(f"**{len(open_decisions)} decisions still open:**")
        lines.append("")
        for d in open_decisions:
            lines.append(f"- [{d['status']}] {d['title']} ({d['file']})")
        lines.append("")
        lines.append("Open decisions are thinking that hasn't become reference yet. Review and either codify or close.")
        lines.append("")
    else:
        lines.append("No open decisions. Clean slate.")
        lines.append("")

    # Suggested Actions
    lines.append("## Suggested Actions")
    lines.append("")
    suggestions = []
    if not entries:
        suggestions.append("Start journaling -- even 3 sentences per day feeds the flywheel")
    if stale_files:
        stalest = stale_files[0]
        suggestions.append(f"Enrich {stalest['file']} (untouched for {stalest['days_old']} days) -- run /think codify")
    graduation_candidates = [w for w, c in recurring if c >= 3]
    if graduation_candidates:
        suggestions.append(f"Graduate recurring themes to content or reference: {', '.join(graduation_candidates[:3])}")
    if open_decisions:
        suggestions.append(f"Resolve {len(open_decisions)} open decision(s) -- codify or close")
    if connections:
        ref_files_touched = set(c["reference"] for c in connections)
        suggestions.append(f"Journal connects to {', '.join(ref_files_touched)} -- consider enriching those files")
    if not suggestions:
        suggestions.append("Flywheel is spinning. Keep journaling and let patterns emerge.")
    for i, s in enumerate(suggestions, 1):
        lines.append(f"{i}. {s}")
    lines.append("")
    lines.append("---")
    lines.append(f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} by enrichment-scanner.py*")
    return "\n".join(lines)


def main():
    log("Starting enrichment scan...")
    entries = get_recent_journal_entries(days=7)
    staleness = check_reference_staleness()
    recurring = find_recurring_themes(entries)
    pillar_matches = match_to_pillars(entries)
    connections = find_reference_connections(entries)
    open_decisions = get_open_decisions()
    report = generate_report(entries, staleness, recurring, pillar_matches, connections, open_decisions)
    today = datetime.now().strftime("%Y-%m-%d")
    output_path = RESEARCH_DIR / f"{today}-enrichment-scan.md"
    output_path.write_text(report)
    log(f"Report saved to {output_path.name}")
    log(f"Journal entries: {len(entries)}, Stale refs: {len([s for s in staleness if s['days_old'] > 14])}, "
        f"Recurring themes: {len(recurring)}, Open decisions: {len(open_decisions)}")


if __name__ == "__main__":
    main()
