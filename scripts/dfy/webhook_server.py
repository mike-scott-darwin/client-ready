#!/usr/bin/env python3
"""
DFY webhook handler — reference implementation of Step 3's middleware.

Receives the GHL "Your Offer Builder — Quick Intake" form submission as a JSON
POST, maps the fields onto the generation core, runs the build in a background
thread (so the webhook returns immediately and GHL doesn't time out), and
writes the deliverables to outputs/dfy-runs/<contact>.md.

This is a STARTING POINT, not production. It intentionally does not deliver the
result (Google Doc / email) — wire that into `on_complete()` once the GHL
account + delivery path are settled (see README.md). For real volume, prefer a
managed queue (Make.com / n8n / a serverless function) over a long-lived
process; this exists to validate the pipeline end-to-end with real payloads.

Usage:
    export ANTHROPIC_API_KEY=...          # or an `ant auth login` profile
    python3 webhook_server.py --port 8787
    # then point a GHL "Custom Webhook" action at http://<host>:8787/dfy

Requires:
    pip3 install anthropic     # (stdlib http.server handles the web side)
"""

import argparse
import json
import re
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import dfy_generate

RUNS_DIR = dfy_generate.REPO_ROOT / "outputs" / "dfy-runs"

# GHL sometimes nests custom fields or prefixes them. Map any incoming keys we
# recognize onto our canonical field names.
FIELD_KEYS = {key for key, _ in dfy_generate.FIELDS}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")
    return slug or "buyer"


def extract_intake(payload: dict) -> tuple[dict, str, bool]:
    """Pull the 11 answers, a contact label, and the lite flag from GHL's POST."""
    # Flatten one level of nesting (GHL may wrap answers under customData/customFields).
    flat = dict(payload)
    for container in ("customData", "customFields", "custom_data", "data"):
        nested = payload.get(container)
        if isinstance(nested, dict):
            flat.update(nested)

    intake = {key: flat.get(key, "") for key in FIELD_KEYS}
    contact = flat.get("email") or flat.get("full_name") or flat.get("name") or "buyer"
    # DFY Lite if the payload says so (tag, product name, or explicit flag).
    blob = json.dumps(payload).lower()
    lite = bool(flat.get("lite")) or "dfy-lite" in blob or "dfy lite" in blob
    return intake, contact, lite


def on_complete(contact: str, out_path: Path, lite: bool) -> None:
    """Hook for delivery. Replace the print with your Google Doc / email step."""
    print(f"[done] {'DFY Lite' if lite else 'DFY'} build for {contact} -> {out_path}")


def run_build(payload: dict) -> None:
    intake, contact, lite = extract_intake(payload)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out_path = RUNS_DIR / f"{stamp}-{slugify(contact)}.md"
    try:
        result = dfy_generate.generate(intake, lite=lite)
        out_path.write_text(result, encoding="utf-8")
        on_complete(contact, out_path, lite)
    except Exception as e:  # noqa: BLE001 — log and move on; one bad order shouldn't kill the server
        print(f"[error] build failed for {contact}: {e}")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):  # noqa: N802 — http.server API
        if self.path.rstrip("/") != "/dfy":
            self.send_error(404, "Not found")
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw or "{}")
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        # Kick off the build and acknowledge immediately.
        threading.Thread(target=run_build, args=(payload,), daemon=True).start()
        body = json.dumps({"status": "accepted"}).encode()
        self.send_response(202)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):  # quieter default logging
        print(f"[web] {self.address_string()} {fmt % args}")


def main() -> None:
    parser = argparse.ArgumentParser(description="DFY intake webhook (reference).")
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"DFY webhook listening on http://{args.host}:{args.port}/dfy")
    server.serve_forever()


if __name__ == "__main__":
    main()
