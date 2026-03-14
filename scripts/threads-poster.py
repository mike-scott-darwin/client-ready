#!/usr/bin/env python3
"""
Threads Auto-Poster for Client Ready

Posts one daily standalone post from content/drafts/threads/.
Designed to run via launchd once daily (e.g., 10:30am).

Posts any draft with scheduled_date <= today (catches up on missed days).
Uses Threads API two-step publish: create container → publish.
"""

import os
import sys
import json
import re
import time
import urllib.request
import urllib.parse
import urllib.error
import ssl
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = REPO_ROOT / ".env"
DRAFTS_DIR = REPO_ROOT / "content" / "drafts" / "threads"
PUBLISHED_DIR = REPO_ROOT / "content" / "published" / "threads"
STATE_FILE = REPO_ROOT / ".threads-poster-state.json"
LOG_FILE = REPO_ROOT / "scripts" / "threads-poster.log"

MAX_POSTS_PER_DAY = 1


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
    today = datetime.now().strftime("%Y-%m-%d")
    if not DRAFTS_DIR.exists():
        return None, today

    drafts = sorted([
        f for f in DRAFTS_DIR.iterdir()
        if f.suffix == ".md"
    ])

    for draft in drafts:
        date_part = "-".join(draft.stem.split("-")[:3])
        if date_part <= today:
            return draft, today

    return None, today


def parse_post_file(filepath):
    content = filepath.read_text()
    parts = content.split("---")
    if len(parts) >= 3:
        body = "---".join(parts[2:]).strip()
    else:
        body = content.strip()
    body = re.sub(r'^#\s+.*\n+', '', body).strip()
    return body


def post_to_threads(access_token, user_id, text):
    ctx = ssl.create_default_context()

    # Step 1: Create media container
    params = urllib.parse.urlencode({
        'media_type': 'TEXT',
        'text': text,
        'access_token': access_token,
    })
    url = f"https://graph.threads.net/v1.0/{user_id}/threads?{params}"
    req = urllib.request.Request(url, method='POST', data=b'')

    try:
        resp = urllib.request.urlopen(req, context=ctx)
        result = json.loads(resp.read())
        container_id = result['id']
        log(f"  Container created: {container_id}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"  ERROR creating container ({e.code}): {body}")
        return None

    # Step 2: Wait for processing
    time.sleep(5)

    # Step 3: Publish
    params2 = urllib.parse.urlencode({
        'creation_id': container_id,
        'access_token': access_token,
    })
    url2 = f"https://graph.threads.net/v1.0/{user_id}/threads_publish?{params2}"
    req2 = urllib.request.Request(url2, method='POST', data=b'')

    try:
        resp2 = urllib.request.urlopen(req2, context=ctx)
        result2 = json.loads(resp2.read())
        post_id = result2['id']
        log(f"  Published: {post_id}")
        return post_id
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"  ERROR publishing ({e.code}): {body}")
        return None


def move_to_published(filepath, post_id):
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name
    content = filepath.read_text()
    content = content.replace('status: draft', 'status: published')

    parts = content.split("---")
    if len(parts) >= 3:
        fm = parts[1].rstrip()
        fm += f'\npublished_date: {datetime.now().isoformat()}'
        if post_id:
            fm += f'\nthreads_id: "{post_id}"'
        fm += '\n'
        parts[1] = fm
        content = "---".join(parts)

    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} -> content/published/threads/")


def main():
    env = load_env()
    required = ["THREADS_ACCESS_TOKEN", "THREADS_USER_ID"]
    for key in required:
        if key not in env:
            log(f"ERROR: Missing {key} in .env")
            sys.exit(1)

    today = datetime.now().strftime("%Y-%m-%d")
    state = load_state()
    if today in state:
        log(f"Already posted to Threads today ({today}). Skipping.")
        sys.exit(0)

    draft_path, _ = find_next_draft()
    if not draft_path:
        log(f"No Threads drafts ready (scheduled_date <= {today}). Skipping.")
        sys.exit(0)

    text = parse_post_file(draft_path)
    if not text:
        log(f"No content parsed from {draft_path.name}. Skipping.")
        sys.exit(0)

    # Threads has a 500 char limit
    if len(text) > 500:
        log(f"WARNING: Post is {len(text)} chars, truncating to 500")
        text = text[:497] + "..."

    log(f"Posting to Threads from {draft_path.name}...")
    post_id = post_to_threads(
        env["THREADS_ACCESS_TOKEN"],
        env["THREADS_USER_ID"],
        text
    )

    if post_id:
        state[today] = {
            "post_id": post_id,
            "posted_at": datetime.now().isoformat(),
            "source_file": draft_path.name,
            "text_preview": text[:80],
        }
        save_state(state)
        log(f"Threads post published: {post_id}")
        move_to_published(draft_path, post_id)
    else:
        log("Failed to publish Threads post.")
        sys.exit(1)


if __name__ == "__main__":
    main()
