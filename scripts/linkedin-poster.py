#!/usr/bin/env python3
"""
LinkedIn Auto-Poster for Client Ready

Reads today's LinkedIn post draft from content/drafts/, posts it.
Designed to run via launchd once daily (e.g., 9:00 AM).
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
STATE_FILE = REPO_ROOT / ".linkedin-poster-state.json"
LOG_FILE = REPO_ROOT / "scripts" / "linkedin-poster.log"


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


def find_today_draft():
    today = datetime.now().strftime("%Y-%m-%d")
    # Look for any LinkedIn post draft for today
    for f in DRAFTS_DIR.iterdir():
        if f.name.startswith(today) and "linkedin" in f.name and f.suffix == ".md":
            return f, today
    return None, today


def parse_linkedin_post(filepath):
    """Extract post text from LinkedIn draft markdown file."""
    with open(filepath) as f:
        content = f.read()

    # Remove frontmatter
    parts = content.split("---")
    if len(parts) >= 3:
        body = "---".join(parts[2:]).strip()
    else:
        body = content.strip()

    # Remove the markdown title (# LinkedIn: ...)
    body = re.sub(r'^#\s+.*\n+', '', body).strip()

    return body


def post_to_linkedin(access_token, person_sub, text):
    ctx = ssl.create_default_context()
    post_data = json.dumps({
        "author": f"urn:li:person:{person_sub}",
        "commentary": text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }).encode()

    req = urllib.request.Request(
        "https://api.linkedin.com/rest/posts",
        data=post_data,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "LinkedIn-Version": "202602",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        method="POST"
    )

    try:
        resp = urllib.request.urlopen(req, context=ctx)
        post_id = resp.headers.get("x-restli-id", "unknown")
        return post_id
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"ERROR posting ({e.code}): {body}")
        return None


def main():
    env = load_env()
    required = ["LINKEDIN_ACCESS_TOKEN", "LINKEDIN_PERSON_SUB"]
    for key in required:
        if key not in env:
            log(f"ERROR: Missing {key} in .env")
            sys.exit(1)

    draft_path, today = find_today_draft()
    if not draft_path:
        log(f"No LinkedIn draft found for {today}. Skipping.")
        sys.exit(0)

    state = load_state()
    if today in state:
        log(f"LinkedIn post for {today} already published. Skipping.")
        sys.exit(0)

    post_text = parse_linkedin_post(draft_path)
    if not post_text:
        log(f"No content parsed from {draft_path.name}. Skipping.")
        sys.exit(0)

    log(f"Posting LinkedIn content from {draft_path.name}...")
    post_id = post_to_linkedin(
        env["LINKEDIN_ACCESS_TOKEN"],
        env["LINKEDIN_PERSON_SUB"],
        post_text
    )

    if post_id:
        state[today] = {
            "post_id": post_id,
            "posted_at": datetime.now().isoformat(),
            "source_file": draft_path.name,
            "text_preview": post_text[:80],
        }
        save_state(state)
        log(f"LinkedIn post published: {post_id}")
        move_to_published(draft_path)
    else:
        log("Failed to publish LinkedIn post.")
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
