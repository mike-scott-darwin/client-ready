#!/usr/bin/env python3
"""
X Auto-Poster for Client Ready

Reads today's tweet drafts from content/drafts/tweets/ (one tweet per file),
posts the next unposted tweet, and tracks what's been posted in a state file.

Designed to run via launchd at scheduled intervals (e.g., 8am, 10:30am, 1pm, 4pm, 7pm).
Each invocation posts one tweet. Five invocations = five tweets spaced across the day.
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
DRAFTS_DIR = REPO_ROOT / "content" / "drafts" / "tweets"
PUBLISHED_DIR = REPO_ROOT / "content" / "published" / "tweets"
STATE_FILE = REPO_ROOT / ".x-poster-state.json"
LOG_FILE = REPO_ROOT / "scripts" / "x-poster.log"


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_env():
    """Load credentials from .env file."""
    if not ENV_FILE.exists():
        log(f"ERROR: .env file not found at {ENV_FILE}")
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
    """Load posting state (which tweets have been posted today)."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    """Save posting state."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def find_today_tweets():
    """Find all tweet files for today, sorted by filename."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not DRAFTS_DIR.exists():
        return [], today
    tweets = sorted([
        f for f in DRAFTS_DIR.iterdir()
        if f.name.startswith(today) and f.suffix == ".md"
    ])
    return tweets, today


def parse_tweet_file(filepath):
    """Read a single tweet file, strip frontmatter, return text."""
    content = filepath.read_text()
    parts = content.split("---")
    if len(parts) >= 3:
        body = "---".join(parts[2:]).strip()
    else:
        body = content.strip()
    return body


def post_tweet(client, text):
    """Post a single tweet. Returns tweet ID or None."""
    try:
        response = client.create_tweet(text=text)
        return response.data["id"]
    except Exception as e:
        log(f"ERROR posting tweet: {e}")
        return None


def move_to_published(filepath, tweet_id):
    """Move individual tweet file to published/tweets/ with metadata in frontmatter."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name
    content = filepath.read_text()
    content = content.replace('status: draft', 'status: published')
    # Extract the date portion from the filename (e.g., 2026-03-08 from 2026-03-08-1.md)
    scheduled_date = filepath.stem.rsplit("-", 1)[0]
    content = content.replace(
        f'scheduled_date: {scheduled_date}',
        f'scheduled_date: {scheduled_date}\npublished_date: {datetime.now().isoformat()}\ntweet_id: "{tweet_id}"\nurl: https://x.com/mikescot/status/{tweet_id}'
    )
    dest.write_text(content)
    filepath.unlink()
    log(f"Moved {filepath.name} -> content/published/tweets/")


def main():
    # Load credentials
    env = load_env()
    required = ["X_CONSUMER_KEY", "X_CONSUMER_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    for key in required:
        if key not in env:
            log(f"ERROR: Missing {key} in .env")
            sys.exit(1)

    # Find today's tweet files
    tweet_files, today = find_today_tweets()
    if not tweet_files:
        log(f"No tweet drafts found for {today}. Skipping.")
        sys.exit(0)

    # Load state
    state = load_state()
    posted_today = state.get(today, [])

    # Find next unposted tweet
    next_index = len(posted_today)
    if next_index >= len(tweet_files):
        log(f"All {len(tweet_files)} tweets for {today} already posted. Skipping.")
        sys.exit(0)

    tweet_file = tweet_files[next_index]
    tweet_text = parse_tweet_file(tweet_file)

    if not tweet_text:
        log(f"Empty tweet in {tweet_file.name}. Skipping.")
        sys.exit(0)

    # Post it
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

    log(f"Posting tweet {next_index + 1}/{len(tweet_files)} for {today} ({tweet_file.name})...")
    tweet_id = post_tweet(client, tweet_text)

    if tweet_id:
        posted_today.append({
            "index": next_index,
            "tweet_id": str(tweet_id),
            "url": f"https://x.com/mikescot/status/{tweet_id}",
            "posted_at": datetime.now().isoformat(),
            "source_file": tweet_file.name,
            "text_preview": tweet_text[:60],
        })
        state[today] = posted_today
        save_state(state)
        log(f"Tweet {next_index + 1} posted: https://x.com/mikescot/status/{tweet_id}")

        # Move individual tweet file to published
        move_to_published(tweet_file, tweet_id)
    else:
        log(f"Failed to post tweet {next_index + 1}.")
        sys.exit(1)


if __name__ == "__main__":
    main()
