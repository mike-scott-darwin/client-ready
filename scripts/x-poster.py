#!/usr/bin/env python3
"""
X Thread Poster for Client Ready

Posts a daily thread (5 connected tweets) from content/drafts/tweets/.
Each invocation posts one complete thread, then moves all 5 files to published/.

Designed to run via launchd once per day (e.g., 8:30am).
Each thread is 5 tweets posted as a reply chain.

Posts any thread with scheduled_date <= today (catches up on missed days).
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

# Max threads per day (safety limit)
MAX_THREADS_PER_DAY = 1


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
    """Load posting state."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    """Save posting state."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def find_next_thread():
    """Find the next unposted thread (group of tweets for a date) with scheduled_date <= today."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not DRAFTS_DIR.exists():
        return [], today

    drafts = sorted([
        f for f in DRAFTS_DIR.iterdir()
        if f.suffix == ".md"
    ])

    # Group by date
    dates_seen = {}
    for draft in drafts:
        date_part = "-".join(draft.stem.split("-")[:3])
        if date_part <= today:
            dates_seen.setdefault(date_part, []).append(draft)

    if not dates_seen:
        return [], today

    # Return the oldest date's files (sorted by post number)
    oldest_date = min(dates_seen.keys())
    thread_files = sorted(dates_seen[oldest_date])
    return thread_files, today


def parse_tweet_file(filepath):
    """Read a single tweet file, strip frontmatter, return text."""
    content = filepath.read_text()
    parts = content.split("---")
    if len(parts) >= 3:
        body = "---".join(parts[2:]).strip()
    else:
        body = content.strip()
    return body


def post_thread(client, tweets):
    """Post a thread (reply chain). Returns list of (file, tweet_id) tuples."""
    results = []
    previous_id = None

    for filepath, text in tweets:
        try:
            kwargs = {"text": text}
            if previous_id:
                kwargs["in_reply_to_tweet_id"] = previous_id
            response = client.create_tweet(**kwargs)
            tweet_id = response.data["id"]
            results.append((filepath, str(tweet_id)))
            previous_id = tweet_id
            log(f"  Posted tweet {len(results)}/{len(tweets)}: {text[:50]}...")
        except Exception as e:
            log(f"  ERROR posting tweet {len(results)+1}: {e}")
            results.append((filepath, None))
            # If the first tweet fails, abort the thread
            if previous_id is None:
                break

    return results


def move_to_published(filepath, tweet_id, thread_id=None):
    """Move individual tweet file to published/tweets/ with metadata in frontmatter."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PUBLISHED_DIR / filepath.name
    content = filepath.read_text()
    content = content.replace('status: draft', 'status: published')

    # Add metadata
    parts = content.split("---")
    if len(parts) >= 3:
        fm = parts[1].rstrip()
        fm += f'\npublished_date: {datetime.now().isoformat()}'
        if tweet_id:
            fm += f'\ntweet_id: "{tweet_id}"'
            fm += f'\nurl: https://x.com/mikescot/status/{tweet_id}'
        if thread_id:
            fm += f'\nthread_id: "{thread_id}"'
        fm += '\n'
        parts[1] = fm
        content = "---".join(parts)

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

    # Check daily limit
    today = datetime.now().strftime("%Y-%m-%d")
    state = load_state()
    posted_today = state.get(today, [])
    if len(posted_today) >= MAX_THREADS_PER_DAY:
        log(f"Daily limit reached ({MAX_THREADS_PER_DAY} thread(s)). Skipping.")
        sys.exit(0)

    # Find next thread to post
    thread_files, _ = find_next_thread()
    if not thread_files:
        log(f"No tweet drafts ready (scheduled_date <= {today}). Skipping.")
        sys.exit(0)

    # Parse all tweets in the thread
    tweets = []
    for f in thread_files:
        text = parse_tweet_file(f)
        if text:
            tweets.append((f, text))

    if not tweets:
        log("All tweet files empty. Skipping.")
        sys.exit(0)

    # Post the thread
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

    date_part = "-".join(thread_files[0].stem.split("-")[:3])
    log(f"Posting thread for {date_part} ({len(tweets)} tweets)...")
    results = post_thread(client, tweets)

    # The first tweet's ID is the thread ID
    thread_id = results[0][1] if results else None
    success_count = sum(1 for _, tid in results if tid)

    if thread_id:
        posted_today.append({
            "thread_id": thread_id,
            "url": f"https://x.com/mikescot/status/{thread_id}",
            "posted_at": datetime.now().isoformat(),
            "date": date_part,
            "tweet_count": success_count,
            "source_files": [f.name for f in thread_files],
        })
        state[today] = posted_today
        save_state(state)
        log(f"Thread posted: https://x.com/mikescot/status/{thread_id} ({success_count}/{len(tweets)} tweets)")

        # Move all files to published
        for filepath, tweet_id in results:
            move_to_published(filepath, tweet_id, thread_id)
    else:
        log("Failed to post thread (first tweet failed).")
        sys.exit(1)


if __name__ == "__main__":
    main()
