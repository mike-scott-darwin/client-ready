# DFY Offer Build — Generation Pipeline (Step 3)

This is the middleware for **Step 3** of the DFY Offer Build process
(`outputs/products/internal/dfy-offer-build-process.md`): buyer intake → Claude
→ six deliverables. Everything upstream (purchase trigger, questionnaire) and
downstream (review, delivery) is GHL + Michael.

The engine reads the canonical system prompt **live** from
`outputs/dfy-upsell/system-prompt.md`, so the code can't drift from the doc —
edit the prompt there, and every generation picks it up.

## Files

| File | What it is |
|------|-----------|
| `dfy_generate.py` | Generation core. CLI + importable `generate(intake, lite, model)`. |
| `webhook_server.py` | Reference GHL webhook handler (thin wrapper around the core). |
| `sample-intake.json` | Example 11-field intake for testing. |

## Setup

```bash
pip3 install anthropic
export ANTHROPIC_API_KEY=...        # or run `ant auth login` once
```

## The three ways to run it (in the order you should adopt them)

### 1. Manual, per order — start here
No infrastructure. Validate prompt quality on the first 5–10 real orders before
building any pipeline (this is the "test, validate, build" move).

```bash
python3 dfy_generate.py --in sample-intake.json --out build.md      # full DFY ($197)
python3 dfy_generate.py --in sample-intake.json --out lite.md --lite # DFY Lite ($97)
```

Paste each buyer's 11 answers into a JSON file shaped like `sample-intake.json`,
run it, review, deliver. When the output is consistently good, automate.

### 2. Webhook (reference) — when volume justifies it
Runs the same core behind an HTTP endpoint GHL can POST to.

```bash
python3 webhook_server.py --port 8787
# GHL: add a "Custom Webhook" action on form submit → http://<host>:8787/dfy
```

It accepts the POST, returns `202` immediately (so GHL doesn't time out),
generates in the background, and writes to `outputs/dfy-runs/<contact>.md`
(gitignored — contains client intake). **Delivery is not wired** — fill in
`on_complete()` with your Google Doc / email step.

### 3. Make.com / n8n / serverless — production
For real volume, prefer a managed queue over a long-lived Python process. The
core (`dfy_generate.generate`) ports directly into a Cloudflare Worker / Vercel
function, or you rebuild the one API call inside a Make.com/n8n scenario using
`system-prompt.md` + the user-message template in `dfy-offer-build-process.md`.

## API specifics (already handled in the code — don't regress these)

- **Model:** `claude-sonnet-5` (best quality/cost here). `DFY_MODEL=claude-opus-4-8`
  for max quality at ~3x cost.
- **No `temperature`/`top_p`/`top_k`** — Sonnet 5 / Opus 4.8 reject non-default
  sampling params with a 400. Tone is steered by the system prompt.
- **Streaming** with `get_final_message()` — avoids the SDK's HTTP-timeout guard
  at `max_tokens=16000`.
- **Thinking disabled** for predictable per-order cost (~$0.20–0.50). Flip to
  `{"type": "adaptive"}` in `dfy_generate.py` for higher-quality copy at higher
  token cost.
- **`stop_reason == "refusal"`** is handled (raises rather than returning empty).

## Before this goes live — two blockers outside the code

1. **GHL account.** The GHL MCP in this workspace is authed to the **Codify**
   sub-account, but the 202 buyers live in `AKRQpXEUDgloSAbxzDmh`. Build the
   form + webhook against the buyer account, not Codify.
2. **Delivery path.** Decide Google Doc vs. emailed markdown/PDF and wire it
   into `on_complete()`. The core produces markdown; packaging is downstream.
