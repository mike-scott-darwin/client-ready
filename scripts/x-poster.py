#!/usr/bin/env python3
"""
X Auto-Poster for Client Ready

Reads today's tweet draft from content/drafts/, posts the next unposted tweet,
and tracks what's been posted in a state file.

Designed to run via launchd at scheduled intervals (e.g., 8am, 10:30am, 1pm, 4pm, 7pm).
Each invocation posts one tweet. Five invocations = five tweets spaced across the day.
"""

import os
import sys
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
ENV_FILE = REPO_ROOT / ".env"
DRAFTS_DIR = REPO_ROOT / "content" / "drafts"
PUBLISHED_DIR = REPO_ROOT / "content" / "published"
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


def find_today_draft():
    """Find today's tweet draft file."""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-x-tweets-daily.md"
    filepath = DRAFTS_DIR / filename

    if filepath.exists():
        return filepath, today
    return None, today


def parse_tweets(filepath):
    """Parse individual tweets from a draft file."""
    with open(filepath) as f:
        content = f.read()

    # Split on tweet headers (e.g., **Tweet 1 (...)**)
    tweet_blocks = re.split(r'\*\*Tweet \d+[^*]*\*\*\s*\n', content)

    tweets = []
    for block in tweet_blocks:
        # Clean up: remove frontmatter, headers, and separators
        block = block.strip()
        if not block or block.startswith("---") or block.startswith("#"):
            continue

        # Remove trailing --- separators
        block = re.sub(r'\n---\s*$', '', block).strip()

        # Skip if it looks like frontmatter
        if "platform:" in block or "type:" in block:
            continue

        if block:
            tweets.append(block)

    return tweets


def post_tweet(client, text):
    """Post a single tweet. Returns tweet ID or None."""
    try:
        response = client.create_tweet(text=text)
        return response.data["id"]
    except Exception as e:
        log(f"ERROR posting tweet: {e}")
        return None


def main():
    # Load credentials
    env = load_env()
    required = ["X_CONSUMER_KEY", "X_CONSUMER_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    for key in required:
        if key not in env:
            log(f"ERROR: Missing {key} in .env")
            sys.exit(1)

    # Find today's draft
    draft_path, today = find_today_draft()
    if not draft_path:
        log(f"No draft found for {today}. Skipping.")
        sys.exit(0)

    # Parse tweets
    tweets = parse_tweets(draft_path)
    if not tweets:
        log(f"No tweets parsed from {draft_path.name}. Skipping.")
        sys.exit(0)

    # Load state
    state = load_state()
    posted_today = state.get(today, [])

    # Find next unposted tweet
    next_index = len(posted_today)
    if next_index >= len(tweets):
        log(f"All {len(tweets)} tweets for {today} already posted. Skipping.")
        sys.exit(0)

    tweet_text = tweets[next_index]

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

    log(f"Posting tweet {next_index + 1}/{len(tweets)} for {today}...")
    tweet_id = post_tweet(client, tweet_text)

    if tweet_id:
        posted_today.append({
            "index": next_index,
            "tweet_id": str(tweet_id),
            "url": f"https://x.com/mikescot/status/{tweet_id}",
            "posted_at": datetime.now().isoformat(),
            "text_preview": tweet_text[:60],
        })
        state[today] = posted_today
        save_state(state)
        log(f"Tweet {next_index + 1} posted: https://x.com/mikescot/status/{tweet_id}")

        # Move to published/ after all tweets for the day are posted
        if next_index + 1 >= len(tweets):
            move_to_published(draft_path)
    else:
        log(f"Failed to post tweet {next_index + 1}.")
        sys.exit(1)


def move_to_published(filepath):
    """Move draft to published/ and update frontmatter status."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name

    # Update frontmatter before moving
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
