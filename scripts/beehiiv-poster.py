#!/usr/bin/env python3
"""
Beehiiv Newsletter Poster for Client Ready

Reads newsletter drafts from content/drafts/, converts to HTML,
and posts to Beehiiv via API. Creates as drafts by default so you
can review formatting before sending.

Usage:
    python3 beehiiv-poster.py              # Post next unposted newsletter as draft
    python3 beehiiv-poster.py --all        # Post all unposted newsletters as drafts
    python3 beehiiv-poster.py --publish    # Publish immediately (sends to subscribers)
    python3 beehiiv-poster.py --schedule   # Schedule using dates from frontmatter

Requires:
    pip3 install markdown

Environment variables (.env):
    BEEHIIV_API_KEY        - API key from Beehiiv dashboard
    BEEHIIV_PUBLICATION_ID - Publication ID (starts with "pub_")

Note: Beehiiv Create Post API requires Enterprise plan.
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
DRAFTS_DIR = REPO_ROOT / "content" / "drafts"
PUBLISHED_DIR = REPO_ROOT / "content" / "published"
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


def find_newsletter_drafts():
    """Find all newsletter draft files, sorted by date."""
    drafts = []
    for f in sorted(DRAFTS_DIR.iterdir()):
        if "newsletter" in f.name and f.suffix == ".md":
            drafts.append(f)
    return drafts


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
    # Remove title line and subject/preview lines
    body = re.sub(r'^#\s+.+\n+', '', body)
    body = re.sub(r'\*\*Subject line:\*\*\s*.+\n+', '', body)
    body = re.sub(r'\*\*Preview text:\*\*\s*.+\n+', '', body)
    # Remove leading separator
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

    # Convert --- horizontal rules that markdown might miss
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
        if e.code == 403:
            log("HINT: Beehiiv Create Post API requires Enterprise plan.")
            log("HINT: Check your plan at https://app.beehiiv.com/settings/billing")
        return None


def main():
    # Parse args
    post_all = "--all" in sys.argv
    publish = "--publish" in sys.argv
    schedule = "--schedule" in sys.argv

    status = "confirmed" if (publish or schedule) else "draft"

    # Load credentials
    env = load_env()
    required = ["BEEHIIV_API_KEY", "BEEHIIV_PUBLICATION_ID"]
    for key in required:
        if key not in env:
            log(f"ERROR: Missing {key} in .env")
            log("Add to .env:")
            log("  BEEHIIV_API_KEY=your_api_key_here")
            log("  BEEHIIV_PUBLICATION_ID=pub_your_id_here")
            sys.exit(1)

    api_key = env["BEEHIIV_API_KEY"]
    pub_id = env["BEEHIIV_PUBLICATION_ID"]

    # Find drafts
    drafts = find_newsletter_drafts()
    if not drafts:
        log("No newsletter drafts found in content/drafts/. Skipping.")
        sys.exit(0)

    # Load state
    state = load_state()
    posted_files = set(state.get("posted_files", []))

    # Filter to unposted
    unposted = [d for d in drafts if d.name not in posted_files]
    if not unposted:
        log("All newsletter drafts already posted. Skipping.")
        sys.exit(0)

    # Select what to post
    to_post = unposted if post_all else [unposted[0]]

    log(f"Found {len(unposted)} unposted newsletter(s). Posting {len(to_post)}...")

    success_count = 0
    for draft_path in to_post:
        newsletter = parse_newsletter(draft_path)

        # Determine schedule time
        schedule_at = None
        if schedule:
            fm = newsletter["frontmatter"]
            sched_date = fm.get("scheduled_date")
            if sched_date:
                # Schedule for 10:00 AM UTC on the scheduled date
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


def move_to_published(filepath):
    """Move draft to published/ and update frontmatter status."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name

    content = filepath.read_text()
    content = re.sub(r'status:\s*draft', 'status: published', content)
    content = re.sub(r'published_date:\s*null',
                     f'published_date: {datetime.now().strftime("%Y-%m-%d")}',
                     content)
    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} → content/published/")



if __name__ == "__main__":
    main()
