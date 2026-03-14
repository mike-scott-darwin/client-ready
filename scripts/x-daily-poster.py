#!/usr/bin/env python3
"""
X Daily Tweet Poster for Client Ready

Posts standalone daily tweets from content/drafts/tweets/daily/.
Each invocation posts one tweet, then moves the file to published/.

Designed to run via launchd once per day (e.g., 9:30am).
Posts any tweet with scheduled_date <= today (catches up on missed days).
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = REPO_ROOT / ".env"
DRAFTS_DIR = REPO_ROOT / "content" / "drafts" / "tweets" / "daily"
PUBLISHED_DIR = REPO_ROOT / "content" / "published" / "tweets" / "daily"
STATE_FILE = REPO_ROOT / ".x-daily-poster-state.json"
LOG_FILE = REPO_ROOT / "scripts" / "x-daily-poster.log"

# Max tweets per day (safety limit)
MAX_TWEETS_PER_DAY = 1


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
    """Find the next unposted daily tweet with scheduled_date <= today."""
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


def parse_tweet_file(filepath):
    """Read a single tweet file, strip frontmatter, return text."""
    content = filepath.read_text()
    parts = content.split("---")
    if len(parts) >= 3:
        body = "---".join(parts[2:]).strip()
    else:
        body = content.strip()
    # Remove markdown title if present
    body = re.sub(r'^#\s+.*\n+', '', body).strip()
    return body


def move_to_published(filepath, tweet_id):
    """Move tweet file to published/tweets/daily/ with metadata."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name
    content = filepath.read_text()
    content = content.replace('status: draft', 'status: published')

    parts = content.split("---")
    if len(parts) >= 3:
        fm = parts[1].rstrip()
        fm += f'\npublished_date: {datetime.now().isoformat()}'
        if tweet_id:
            fm += f'\ntweet_id: "{tweet_id}"'
            fm += f'\nurl: https://x.com/mikescot/status/{tweet_id}'
        fm += '\n'
        parts[1] = fm
        content = "---".join(parts)

    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} -> content/published/tweets/daily/")


def main():
    env = load_env()
    required = ["X_CONSUMER_KEY", "X_CONSUMER_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    for key in required:
        if key not in env:
            log(f"ERROR: Missing {key} in .env")
            sys.exit(1)

    # Check daily limit
    today = datetime.now().strftime("%Y-%m-%d")
    state = load_state()
    posted_today = state.get(today, [])
    if len(posted_today) >= MAX_TWEETS_PER_DAY:
        log(f"Daily limit reached ({MAX_TWEETS_PER_DAY} tweet(s)). Skipping.")
        sys.exit(0)

    # Find next draft
    draft_path, _ = find_next_draft()
    if not draft_path:
        log(f"No daily tweet drafts ready (scheduled_date <= {today}). Skipping.")
        sys.exit(0)

    text = parse_tweet_file(draft_path)
    if not text:
        log(f"No content parsed from {draft_path.name}. Skipping.")
        sys.exit(0)

    # Post the tweet
    try:
        import tweepy
    except ImportError:
        log("ERROR: tweepy not installed. Run: pip3 install tweepy")
        sys.exit(1)

    client = tweepy.Client(
        consumer_key=env["X_CONSUMER_KEY"],
        consumer_secret=env["X_CONSUMER_SECRET"],
        access_token=env["X_ACCESS_TOKEN"],
        access_token_secret=env["X_ACCESS_TOKEN_SECRET"],
    )

    log(f"Posting daily tweet from {draft_path.name}...")
    try:
        response = client.create_tweet(text=text)
        tweet_id = str(response.data["id"])
        posted_today.append({
            "tweet_id": tweet_id,
            "url": f"https://x.com/mikescot/status/{tweet_id}",
            "posted_at": datetime.now().isoformat(),
            "source_file": draft_path.name,
            "text_preview": text[:80],
        })
        state[today] = posted_today
        save_state(state)
        log(f"Tweet posted: https://x.com/mikescot/status/{tweet_id}")
        move_to_published(draft_path, tweet_id)
    except Exception as e:
        log(f"ERROR posting tweet: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
