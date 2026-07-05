# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

### Ad creative — fal.ai (Flux)

Generate ad images from the terminal, like Devon's BookedOutRoofers setup.

- Key: `FAL_KEY` in `.env` (get one at https://fal.ai/dashboard/keys)
- Script: `scripts/fal-image.py`
- Output: `outputs/ad-creative/` (image + sidecar `.json` with prompt/seed)

```bash
# 1:1 feed ad (default: flux dev)
python3 scripts/fal-image.py --prompt "..."

# story/reels, cheap+fast model, 3 variants
python3 scripts/fal-image.py --prompt "..." --model schnell --size story --num 3

# preview the request without spending (no key needed)
python3 scripts/fal-image.py --prompt "..." --dry-run
```

Models: `schnell` (cheapest) · `dev` (default) · `pro` · `pro-ultra`.
Sizes: `feed`/`1:1`, `story`/`9:16`, `landscape`, or raw `1080x1350`.

**On-message angles** (grounded in `reference/proof/angles/main-angles.md`,
defined in `scripts/ad-prompts.json` — edit prompts there):

```bash
python3 scripts/fal-image.py --list-angles              # see all keys
python3 scripts/fal-image.py --angle 9-to-5 --num 4     # one angle, 4 variants
python3 scripts/fal-image.py --angle all --model schnell  # whole set, cheap
python3 scripts/fal-image.py --angle ladder --extra "woman in her 40s"
```

Angle keys: `9-to-5`, `one-afternoon`, `ladder`, `alignment`, `ai-90`,
`overwhelm`, `objection-sales-calls`. Each leaves headline space up top for a
copy overlay (Flux won't render clean text — add it after). For text-heavy
"ugly static" ads use the `notes` template below, not fal.

### Ad creative — HTML→PNG templates (text-exact, mirrors Miles's winners)

For the native screenshot / value-stack formats fal.ai CAN'T render (crisp UI
text + exact numbers). Renders via installed Chrome (playwright-core). See
`research/2026-07-05-miles-creative-oldest-winners.md`.

- Templates + copy: `scripts/ad-templates/` (edit `content.json` for copy,
  `brand.mjs` for colors/fonts)
- Output: `outputs/ad-creative/` (PNG + sidecar `.json`)

```bash
node scripts/ad-templates/render.mjs --list
node scripts/ad-templates/render.mjs --template imessage --preset all
node scripts/ad-templates/render.mjs --template order-summary --preset front-end-27
# ad-hoc copy without editing content.json:
node scripts/ad-templates/render.mjs --template imessage \
  --data '{"contact":"Pat","messages":[{"from":"them","text":"..."},{"from":"me","text":"..."}]}'
```

Templates (all 7 of Miles's proven formats):
- `imessage` (his #1 winner) — one-afternoon, no-calls, 9-to-5
- `order-summary` (value stack) — front-end-27
- `chatgpt` (AI answer screenshot) — offer-clarity, no-calls
- `typo` (bold text card; accent a word with `*asterisks*`) — not-you,
  grow-into-pain, one-afternoon
- `gmail` (inbox — clarity moments, NOT fake income) — validated-offer
- `tabloid` ("Breaking News" red banner) — one-afternoon, no-calls
- `handwritten` (paper note, cursive) — grow-into-pain
- `notes` (iOS Notes screenshot — the ugly-static format, copy baked in) —
  read-first, dont-buy, 9-to-5

⚠️ The order-summary line-item prices are illustrative — confirm they map to
real front-end deliverables before running. Never use fabricated income claims
(FTC + our own `main-angles.md` rules).

---

Add whatever helps you do your job. This is your cheat sheet.
