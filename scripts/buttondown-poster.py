#!/usr/bin/env python3
"""
Buttondown Poster for The Monthly Playbook ($37/mo — OTO2)

Sends the next unposted Monthly Playbook issue from
content/drafts/monthly-playbook/ to Buttondown, targeting the paid tag.

Unlike Beehiiv (whose Create-Post API is Enterprise-only), Buttondown's
email API works on the Standard ($29/mo) plan, and it takes MARKDOWN
directly — so there's no HTML conversion and no copy-paste.

Usage:
    python3 buttondown-poster.py               # Create next issue as a DRAFT in Buttondown (review, then send in UI)
    python3 buttondown-poster.py --send        # Create AND send immediately to the paid tag
    python3 buttondown-poster.py --schedule    # Schedule via API using frontmatter scheduled_date
    python3 buttondown-poster.py --all         # Process all ready drafts

Requires:
    A Buttondown Standard plan or above (API + paid features).

Environment variables (.env):
    BUTTONDOWN_API_KEY  - API key from Buttondown → Settings → Programming
    BUTTONDOWN_TAG      - (optional) paid-list tag name; defaults to "monthly-playbook"

TAG TARGETING: Buttondown targets tags by ID (e.g. 'sub_tag_...'), not by name —
verified against the live API 2026-07-11. This script resolves BUTTONDOWN_TAG
(a human name) to its ID at runtime via GET /v1/tags, so you set the readable
name in .env and the script handles the ID.

PLAN REQUIREMENT: tags need Basic; API send + paid subscriptions need Standard
($29/mo). On Free, tag creation returns 403 and sends won't work.
Always do a --send test to yourself (tag a test subscriber) first.
Docs: https://docs.buttondown.com/api-emails-create
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
import ssl
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = REPO_ROOT / ".env"
DRAFTS_DIR = REPO_ROOT / "content" / "drafts" / "monthly-playbook"
PUBLISHED_DIR = REPO_ROOT / "content" / "published" / "monthly-playbook"
STATE_FILE = REPO_ROOT / ".buttondown-poster-state.json"
LOG_FILE = REPO_ROOT / "scripts" / "buttondown-poster.log"

API_BASE = "https://api.buttondown.com/v1"
DEFAULT_TAG = "monthly-playbook"


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_env():
    if not ENV_FILE.exists():
        log(f"ERROR: .env not found at {ENV_FILE}")
        sys.exit(1)
    env = {}
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def parse_frontmatter(content):
    """Extract YAML frontmatter as a dict."""
    parts = content.split("---")
    if len(parts) < 3:
        return {}, content
    fm_text = parts[1]
    body = "---".join(parts[2:]).strip()
    fm = {}
    for line in fm_text.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            value = value.strip()
            if value == "null":
                value = None
            fm[key.strip()] = value
    return fm, body


def parse_issue(filepath):
    """Parse a Monthly Playbook draft into title, subject, preview, and markdown body."""
    with open(filepath) as f:
        content = f.read()

    fm, body = parse_frontmatter(content)

    title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem

    subject_match = re.search(r'\*\*Subject line:\*\*\s*(.+)', body)
    subject = subject_match.group(1).strip() if subject_match else title

    preview_match = re.search(r'\*\*Preview text:\*\*\s*(.+)', body)
    preview = preview_match.group(1).strip() if preview_match else ""

    # Strip the H1 title + subject/preview meta lines from the body Buttondown sends.
    body = re.sub(r'^#\s+.+\n+', '', body)
    body = re.sub(r'\*\*Subject line:\*\*\s*.+\n+', '', body)
    body = re.sub(r'\*\*Preview text:\*\*\s*.+\n+', '', body)
    body = re.sub(r'^---\s*\n+', '', body.strip())

    return {
        "title": title,
        "subject": subject,
        "preview": preview,
        "body_md": body.strip(),   # Buttondown accepts markdown directly — no HTML conversion.
        "frontmatter": fm,
    }


def find_ready_drafts(all_ready=False):
    """Find unposted drafts with scheduled_date (or filename date) <= today."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not DRAFTS_DIR.exists():
        return []
    state = load_state()
    posted = set(state.get("posted_files", []))
    drafts = sorted(f for f in DRAFTS_DIR.iterdir() if f.suffix == ".md" and f.name not in posted)

    ready = []
    for d in drafts:
        fm, _ = parse_frontmatter(d.read_text())
        sched = fm.get("scheduled_date") or "-".join(d.stem.split("-")[:2])
        if sched and str(sched) <= today:
            ready.append(d)
    if all_ready:
        return ready
    return ready[:1]


def resolve_tag_id(api_key, tag_name):
    """
    Buttondown targets tags by ID (e.g. 'sub_tag_...'), NOT by name — verified against
    the live API. Look up the ID for a human-readable tag name. Returns None if not found
    (e.g. the tag doesn't exist yet, or the plan is below Basic so tags are disabled).
    """
    ctx = ssl.create_default_context()
    url = f"{API_BASE}/tags"   # paginate — accounts can have 100+ tags across pages
    try:
        while url:
            req = urllib.request.Request(
                url, headers={"Authorization": f"Token {api_key}"}, method="GET",
            )
            resp = urllib.request.urlopen(req, context=ctx)
            data = json.loads(resp.read().decode())
            for t in data.get("results", []):
                if t.get("name") == tag_name:
                    return t.get("id")
            url = data.get("next")   # DRF-style cursor; None on last page
    except urllib.error.HTTPError as e:
        log(f"Tag lookup failed ({e.code}): {e.read().decode()[:200]}")
    return None


def post_to_buttondown(api_key, tag_id, issue, status="draft", schedule_at=None):
    """
    Create (and optionally send/schedule) an email in Buttondown, targeting subscribers
    who hold `tag_id`.

    Buttondown email statuses:
        "draft"          - saved, not sent (review + send in the UI)
        "about_to_send"  - sends immediately to the filtered audience
        "scheduled"      - sends at publish_date
    """
    ctx = ssl.create_default_context()

    payload = {
        "subject": issue["subject"],
        "body": issue["body_md"],          # markdown, sent as-is
        "status": status,
        # Tag targeting — sends ONLY to subscribers holding the paid tag.
        # Shape verified against the live API 2026-07-11: field 'subscriber.tags',
        # operator 'contains', value = tag ID (sub_tag_...).
        "filters": {
            "filters": [
                {"field": "subscriber.tags", "operator": "contains", "value": tag_id}
            ],
            "groups": [],
            "predicate": "and",
        },
    }
    if issue.get("preview"):
        payload["description"] = issue["preview"]   # preview/preheader text
    if schedule_at and status == "scheduled":
        payload["publish_date"] = schedule_at

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{API_BASE}/emails",
        data=data,
        headers={
            "Authorization": f"Token {api_key}",   # Buttondown uses the "Token" scheme, not "Bearer"
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        resp = urllib.request.urlopen(req, context=ctx)
        result = json.loads(resp.read().decode())
        return result.get("id", "unknown")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"API error ({e.code}): {body[:300]}")
        if e.code == 401:
            log("HINT: API key invalid. Regenerate at Buttondown → Settings → Programming.")
        if e.code == 403:
            log("HINT: paid/API features need the Standard plan or above (https://buttondown.com/pricing).")
        if e.code == 400:
            log("HINT: likely the tag-targeting field. Check https://docs.buttondown.com/api-emails-create")
        return None


def move_to_published(filepath, email_id=None):
    """Move draft to published/ and stamp frontmatter."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name
    content = filepath.read_text()
    content = re.sub(r'status:\s*draft', 'status: published', content)
    content = re.sub(r'published_date:\s*null',
                     f'published_date: {datetime.now().strftime("%Y-%m-%d")}', content)
    if email_id:
        parts = content.split("---")
        if len(parts) >= 3:
            parts[1] = parts[1].rstrip() + f'\nbuttondown_id: "{email_id}"\n'
            content = "---".join(parts)
    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} -> content/published/monthly-playbook/")


def main():
    post_all = "--all" in sys.argv
    send = "--send" in sys.argv
    schedule = "--schedule" in sys.argv

    if send:
        status = "about_to_send"
    elif schedule:
        status = "scheduled"
    else:
        status = "draft"

    env = load_env()
    api_key = env.get("BUTTONDOWN_API_KEY")
    tag_name = env.get("BUTTONDOWN_TAG") or DEFAULT_TAG
    if not api_key:
        log("ERROR: Missing BUTTONDOWN_API_KEY in .env")
        sys.exit(1)

    # Buttondown targets tags by ID, not name — resolve it once up front.
    tag_id = resolve_tag_id(api_key, tag_name)
    if not tag_id:
        log(f"ERROR: tag '{tag_name}' not found in Buttondown. Create it first "
            f"(needs Basic plan or higher), then retry. See buttondown-poster.log.")
        sys.exit(1)

    to_post = find_ready_drafts(all_ready=post_all)
    if not to_post:
        log("No Monthly Playbook drafts ready. Skipping.")
        sys.exit(0)

    log(f"Processing {len(to_post)} issue(s) → tag '{tag_name}' ({tag_id}), status '{status}'...")
    state = load_state()
    posted = set(state.get("posted_files", []))
    ok = 0

    for draft_path in to_post:
        issue = parse_issue(draft_path)

        schedule_at = None
        if schedule:
            sched = issue["frontmatter"].get("scheduled_date")
            if sched:
                schedule_at = f"{sched}T08:00:00Z"

        log(f"Processing: {issue['title']} ({draft_path.name})...")
        email_id = post_to_buttondown(api_key, tag_id, issue, status, schedule_at)

        if not email_id:
            log("  -> FAILED (see error above). Draft left in place for retry.")
            continue

        log(f"  -> Buttondown {status}: {email_id}")
        log(f"  -> Subject: {issue['subject']}")
        posted.add(draft_path.name)
        state.setdefault("posts", {})[draft_path.name] = {
            "buttondown_id": email_id,
            "posted_at": datetime.now().isoformat(),
            "status": status,
            "subject": issue["subject"],
        }
        state["posted_files"] = list(posted)
        save_state(state)
        # Only archive locally once it's actually sent/scheduled (not a bare draft you may edit).
        if status in ("about_to_send", "scheduled"):
            move_to_published(draft_path, email_id)
        ok += 1

    log(f"Done. {ok}/{len(to_post)} processed.")


if __name__ == "__main__":
    main()
