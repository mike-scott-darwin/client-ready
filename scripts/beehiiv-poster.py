#!/usr/bin/env python3
"""
Beehiiv Newsletter Poster for Client Ready

Posts the next unposted newsletter from content/drafts/newsletter/.
Converts markdown to HTML. Attempts API posting first; if plan doesn't
support it, generates an HTML file and opens Beehiiv for manual paste.

Usage:
    python3 beehiiv-poster.py              # Post next newsletter (API or HTML fallback)
    python3 beehiiv-poster.py --all        # Process all ready newsletters
    python3 beehiiv-poster.py --publish    # Publish immediately via API
    python3 beehiiv-poster.py --schedule   # Schedule via API using frontmatter dates
    python3 beehiiv-poster.py --html-only  # Skip API, just generate HTML for paste

Requires:
    pip3 install markdown

Environment variables (.env):
    BEEHIIV_API_KEY  - API key from Beehiiv dashboard
    BEEHIIV_PUB_ID   - Publication ID (starts with "pub_")

Note: Beehiiv Create Post API requires Enterprise plan.
On lower plans, the script generates HTML + opens Beehiiv for manual paste.
"""

import os
import sys
import json
import re
import subprocess
import urllib.request
import urllib.error
import ssl
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = REPO_ROOT / ".env"
DRAFTS_DIR = REPO_ROOT / "content" / "drafts" / "newsletter"
PUBLISHED_DIR = REPO_ROOT / "content" / "published" / "newsletter"
HTML_DIR = REPO_ROOT / "scripts" / "newsletter-html"
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

    title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem

    subject_match = re.search(r'\*\*Subject line:\*\*\s*(.+)', body)
    subject = subject_match.group(1).strip() if subject_match else title

    preview_match = re.search(r'\*\*Preview text:\*\*\s*(.+)', body)
    preview = preview_match.group(1).strip() if preview_match else ""

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


def generate_html_file(newsletter, draft_name):
    """Generate a styled HTML file for manual paste into Beehiiv."""
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    html_path = HTML_DIR / f"{Path(draft_name).stem}.html"

    body_html = markdown_to_html(newsletter["body_md"])

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{newsletter['subject']}</title>
<style>
body {{ font-family: -apple-system, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; line-height: 1.6; color: #1a1a1a; }}
h1, h2, h3 {{ line-height: 1.3; }}
hr {{ border: none; border-top: 1px solid #ddd; margin: 24px 0; }}
blockquote {{ border-left: 3px solid #333; margin-left: 0; padding-left: 16px; color: #555; }}
</style>
</head>
<body>
<h1>{newsletter['title']}</h1>
{body_html}
</body>
</html>"""

    html_path.write_text(full_html)
    return html_path


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
        log(f"API error ({e.code}): {body[:200]}")
        if e.code == 401:
            log("HINT: API key is invalid. Regenerate at https://app.beehiiv.com/settings/integrations")
        if e.code == 403:
            log("API posting requires Enterprise plan. Falling back to HTML generation.")
        return None


def move_to_published(filepath, post_id=None):
    """Move draft to published/newsletter/ and update frontmatter status."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name

    content = filepath.read_text()
    content = re.sub(r'status:\s*draft', 'status: published', content)
    content = re.sub(r'published_date:\s*null',
                     f'published_date: {datetime.now().strftime("%Y-%m-%d")}',
                     content)
    if post_id:
        parts = content.split("---")
        if len(parts) >= 3:
            parts[1] = parts[1].rstrip() + f'\npost_id: "{post_id}"\n'
            content = "---".join(parts)
    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} -> content/published/newsletter/")


def main():
    post_all = "--all" in sys.argv
    publish = "--publish" in sys.argv
    schedule = "--schedule" in sys.argv
    html_only = "--html-only" in sys.argv

    status = "confirmed" if (publish or schedule) else "draft"

    # Load credentials
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

    log(f"Processing {len(to_post)} newsletter(s)...")

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

        log(f"Processing: {newsletter['title']} ({draft_path.name})...")

        post_id = None
        if not html_only:
            post_id = post_to_beehiiv(api_key, pub_id, newsletter, status, schedule_at)

        if post_id:
            log(f"  -> API {status}: {post_id}")
        else:
            # Fallback: generate HTML for manual paste
            html_path = generate_html_file(newsletter, draft_path.name)
            log(f"  -> HTML generated: {html_path}")
            log(f"  -> Subject: {newsletter['subject']}")
            log(f"  -> Preview: {newsletter['preview']}")
            # Open the HTML file and Beehiiv new post page
            try:
                subprocess.run(["open", str(html_path)], check=False)
                subprocess.run(["open", f"https://app.beehiiv.com/posts/new"], check=False)
            except Exception:
                pass

        posted_files.add(draft_path.name)
        state.setdefault("posts", {})[draft_path.name] = {
            "post_id": post_id or "manual",
            "posted_at": datetime.now().isoformat(),
            "status": status if post_id else "html-generated",
            "title": newsletter["title"],
            "subject": newsletter["subject"],
        }
        state["posted_files"] = list(posted_files)
        save_state(state)
        move_to_published(draft_path, post_id)
        success_count += 1

    log(f"Done. {success_count}/{len(to_post)} processed.")


if __name__ == "__main__":
    main()
