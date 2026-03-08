#!/usr/bin/env python3
"""
Beehiiv Newsletter Poster for Client Ready

Posts the next unposted newsletter from content/drafts/newsletter/.
Converts markdown to HTML and creates as draft on Beehiiv so you
can review formatting before sending.

Usage:
    python3 beehiiv-poster.py              # Post next unposted newsletter as draft
    python3 beehiiv-poster.py --all        # Post all unposted newsletters as drafts
    python3 beehiiv-poster.py --publish    # Publish immediately (sends to subscribers)
    python3 beehiiv-poster.py --schedule   # Schedule using dates from frontmatter

Requires:
    pip3 install markdown

Environment variables (.env):
    BEEHIIV_API_KEY  - API key from Beehiiv dashboard
    BEEHIIV_PUB_ID   - Publication ID (starts with "pub_")

Note: Beehiiv Create Post API requires Scale plan or higher.
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
DRAFTS_DIR = REPO_ROOT / "content" / "drafts" / "newsletter"
PUBLISHED_DIR = REPO_ROOT / "content" / "published" / "newsletter"
STATE_FILE = REPO_ROOT / ".beehiiv-poster-state.json"
LOG_FILE = REPO_ROOT / "scripts" / "beehiiv-poster.log"


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


def find_next_draft():
    """Find the next unposted newsletter draft with scheduled_date <= today."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not DRAFTS_DIR.exists():
        return None

    state = load_state()
    posted_files = set(state.get("posted_files", []))

    drafts = sorted([
        f for f in DRAFTS_DIR.iterdir()
        if f.suffix == ".md" and f.name not in posted_files
    ])

    for draft in drafts:
        date_part = "-".join(draft.stem.split("-")[:3])
        if date_part <= today:
            return draft

    return None


def find_all_ready_drafts():
    """Find all unposted newsletter drafts with scheduled_date <= today."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not DRAFTS_DIR.exists():
        return []

    state = load_state()
    posted_files = set(state.get("posted_files", []))

    drafts = sorted([
        f for f in DRAFTS_DIR.iterdir()
        if f.suffix == ".md" and f.name not in posted_files
    ])

    return [d for d in drafts if "-".join(d.stem.split("-")[:3]) <= today]


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


def parse_newsletter(filepath):
    """Parse newsletter draft into title, subject, preview, and body."""
    with open(filepath) as f:
        content = f.read()

    fm, body = parse_frontmatter(content)

    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem

    # Extract subject line
    subject_match = re.search(r'\*\*Subject line:\*\*\s*(.+)', body)
    subject = subject_match.group(1).strip() if subject_match else title

    # Extract preview text
    preview_match = re.search(r'\*\*Preview text:\*\*\s*(.+)', body)
    preview = preview_match.group(1).strip() if preview_match else ""

    # Get body content (everything after the metadata block)
    body = re.sub(r'^#\s+.+\n+', '', body)
    body = re.sub(r'\*\*Subject line:\*\*\s*.+\n+', '', body)
    body = re.sub(r'\*\*Preview text:\*\*\s*.+\n+', '', body)
    body = re.sub(r'^---\s*\n+', '', body.strip())

    return {
        "title": title,
        "subject": subject,
        "preview": preview,
        "body_md": body.strip(),
        "frontmatter": fm,
    }


def markdown_to_html(md_text):
    """Convert markdown to HTML."""
    try:
        import markdown
    except ImportError:
        log("ERROR: markdown not installed. Run: pip3 install markdown")
        sys.exit(1)

    html = markdown.markdown(md_text, extensions=["extra"])
    html = re.sub(r'<p>---</p>', '<hr>', html)
    return html


def post_to_beehiiv(api_key, pub_id, newsletter, status="draft", schedule_at=None):
    """Post newsletter to Beehiiv via API."""
    ctx = ssl.create_default_context()

    body_html = markdown_to_html(newsletter["body_md"])

    payload = {
        "title": newsletter["title"],
        "subtitle": newsletter["preview"],
        "body_content": body_html,
        "status": status,
        "email_settings": {
            "email_subject_line": newsletter["subject"],
            "display_title_in_email": True,
            "display_subtitle_in_email": True,
        },
    }

    if schedule_at and status == "confirmed":
        payload["scheduled_at"] = schedule_at

    post_data = json.dumps(payload).encode()

    req = urllib.request.Request(
        f"https://api.beehiiv.com/v2/publications/{pub_id}/posts",
        data=post_data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        resp = urllib.request.urlopen(req, context=ctx)
        result = json.loads(resp.read().decode())
        return result.get("data", {}).get("id", "unknown")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"ERROR posting ({e.code}): {body}")
        if e.code == 401:
            log("HINT: API key is invalid. Regenerate at https://app.beehiiv.com/settings/integrations")
        if e.code == 403:
            log("HINT: Beehiiv Create Post API requires Scale plan ($49/mo).")
            log("HINT: Check your plan at https://app.beehiiv.com/settings/billing")
        return None


def move_to_published(filepath):
    """Move draft to published/newsletter/ and update frontmatter status."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name

    content = filepath.read_text()
    content = re.sub(r'status:\s*draft', 'status: published', content)
    content = re.sub(r'published_date:\s*null',
                     f'published_date: {datetime.now().strftime("%Y-%m-%d")}',
                     content)
    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} -> content/published/newsletter/")


def main():
    post_all = "--all" in sys.argv
    publish = "--publish" in sys.argv
    schedule = "--schedule" in sys.argv

    status = "confirmed" if (publish or schedule) else "draft"

    # Load credentials — accept both env var names
    env = load_env()
    api_key = env.get("BEEHIIV_API_KEY")
    pub_id = env.get("BEEHIIV_PUB_ID") or env.get("BEEHIIV_PUBLICATION_ID")

    if not api_key:
        log("ERROR: Missing BEEHIIV_API_KEY in .env")
        sys.exit(1)
    if not pub_id:
        log("ERROR: Missing BEEHIIV_PUB_ID in .env")
        sys.exit(1)

    # Find drafts
    if post_all:
        to_post = find_all_ready_drafts()
    else:
        draft = find_next_draft()
        to_post = [draft] if draft else []

    if not to_post:
        log("No newsletter drafts ready. Skipping.")
        sys.exit(0)

    log(f"Posting {len(to_post)} newsletter(s) as {status}...")

    state = load_state()
    posted_files = set(state.get("posted_files", []))
    success_count = 0

    for draft_path in to_post:
        newsletter = parse_newsletter(draft_path)

        schedule_at = None
        if schedule:
            fm = newsletter["frontmatter"]
            sched_date = fm.get("scheduled_date")
            if sched_date:
                schedule_at = f"{sched_date}T10:00:00Z"

        log(f"Posting: {newsletter['title']} ({draft_path.name}) as {status}...")

        post_id = post_to_beehiiv(api_key, pub_id, newsletter, status, schedule_at)

        if post_id:
            posted_files.add(draft_path.name)
            state.setdefault("posts", {})[draft_path.name] = {
                "post_id": post_id,
                "posted_at": datetime.now().isoformat(),
                "status": status,
                "title": newsletter["title"],
                "subject": newsletter["subject"],
            }
            state["posted_files"] = list(posted_files)
            save_state(state)
            log(f"  -> {status}: {post_id}")
            move_to_published(draft_path)
            success_count += 1
        else:
            log(f"  -> FAILED: {draft_path.name}")

    log(f"Done. {success_count}/{len(to_post)} posted successfully.")

    if success_count < len(to_post):
        sys.exit(1)


if __name__ == "__main__":
    main()
