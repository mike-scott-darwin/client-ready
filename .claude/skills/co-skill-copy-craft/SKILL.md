---
name: co-skill-copy-craft
description: "Composable sub-skill. A direct-response craft layer the generation skills apply ON TOP OF the client's voice — awareness/sophistication staging, lead & hook selection, headline shapes, readability momentum, offer logic, proof discipline. Returns the applicable craft moves + a craft checklist for an output kind. Voice files always win on conflict. Called by /co-skill-brief-draft and /co-skill-review (and directly by /co-write, /co-ad, /co-email, /co-content, /co-landing, /co-organic). Not a standalone operator skill."
---

# /co-skill-copy-craft — The Craft Layer

Composable sub-skill. Other Codify skills call this to apply **direct-response craft** — the universal *structure* of copy that converts — to copy that is already in the client's voice.

**This is craft, not voice.** The craft is universal (how a great ad is shaped). The voice is the client's (extracted in `.codify/voice.md`). This layer makes the client's substrate hit harder. It never replaces it.

> We don't install a famous copywriter's voice. We apply the craft — to the client's.

**Not a standalone operator skill.** Invoked by the generation skills and the brief/review sub-skills.

---

## The Non-Negotiable Contract

1. **Voice wins on every conflict.** `.codify/voice.md` governs tone, vocabulary, and the "never say" list. This layer governs *structure*. If a craft move ("add urgency", "agitate the pain") collides with the voice (anti-hype, no fear), **the voice wins, silently.** Craft bends to voice, never the reverse.
2. **Amplifier, not avatar.** Craft amplifies the client's real expertise by structuring it well. It never fabricates a claim, invents proof, or impersonates an authority the client hasn't earned. No craft move justifies a fact that isn't true.
3. **The masters stay internal.** This reference exists for the operator/agent. **No source name (or "direct-response", "copywriting formula", etc.) ever appears in client-facing copy or deliverables.** The craft is invisible scaffolding.
4. **Specificity over technique.** Every move below loses to one concrete, true detail from the client's substrate. Craft is the frame; the client's real numbers, names, and outcomes are the picture.

---

## Inputs

The caller passes:

- **Output kind** — `cold-email | ad | email-sequence | content | landing | sales-page | vsl | organic`
- **Dial** — `convert | story | brand` (defaults: convert for ad/email/landing/sales; story for vsl; brand for organic/content)
- **Draft or brief** — optional. If passed, return *applied* notes against it; if absent, return the craft moves to generate against.
- **Voice digest** — the caller's read of `.codify/voice.md` (tone + "never say" list), so conflicts resolve toward voice.

## Outputs

A single structured report to the caller:

```json
{
  "awareness": "unaware|problem|solution|product|most-aware",
  "sophistication": "1-5",
  "recommended_lead": "promise|problem|story|proclamation|secret|offer",
  "moves": ["ordered craft moves for this output kind"],
  "craft_checklist": ["pass/fail items the draft must clear"],
  "voice_conflicts_resolved": ["any craft move suppressed because voice.md overrides"]
}
```

---

## 1. Stage the reader (decides everything downstream)

Before any line, locate the reader on two axes — they set the lead and the length.

**Awareness** (how much the reader already knows):
| Level | The reader… | Lead with |
|---|---|---|
| Unaware | doesn't know they have the problem | a story or a startling truth |
| Problem-aware | feels the pain, not the fix | the problem, named precisely |
| Solution-aware | knows fixes exist, not yours | the mechanism / how yours differs |
| Product-aware | knows you, not convinced | proof, specifics, risk reversal |
| Most-aware | ready, needs a reason now | the offer + the CTA |

**Sophistication** (how many claims the market has already heard): stage 1 = state the claim plainly; stages 3-5 = the claim is exhausted, so lead with a **new mechanism** or a fresh frame, not a louder promise. The more sophisticated the market, the more you win on *specificity and mechanism*, not adjectives.

## 2. Pick the lead / hook

Match the lead to awareness. Default menu (pick one, never stack):
- **Promise lead** — the specific result, made concrete (product/most-aware).
- **Problem lead** — name the reader's exact friction in their words (problem-aware).
- **Story lead** — one real moment, in motion (unaware; `story` dial).
- **Proclamation / contrarian** — a defensible against-the-grain claim (solution-aware).
- **Secret/mechanism lead** — "here's why X actually happens" (solution/product-aware, high sophistication).
- **Offer lead** — straight to the thing + the reason to act now (most-aware).

The hook's only job is to earn the next line. Test: would the reader keep reading if the rest were blank?

## 3. Headline / subject shapes

Proven shapes, in priority order — specificity beats cleverness every time:
1. **Direct benefit** — the result, stated plainly.
2. **How-to** — "how [audience] get [result] without [objection]".
3. **News** — what changed, what's new, what they don't know yet.
4. **Question** — only if the honest answer is "yes, that's me".
5. **Testimonial-as-headline** — the customer's own words.

Rules: lead with the concrete noun/number, not the clever turn. A headline a competitor could run unchanged is a failed headline. Lowercase, conversational subjects for cold email (see the cold-email canon).

## 4. Momentum (the slippery slope)

Every sentence exists to make the next one read. Enforce:
- First sentence short. Then keep them short until trust is earned.
- One idea per sentence; one job per paragraph.
- Cut every word the meaning survives without. Read it aloud — where you stumble, the reader leaves.
- Transitions carry the reader downhill: "Here's why." "But there's a catch." "Which means—".
- Friction kills momentum: jargon, throat-clearing, hedging, "in today's world".

## 5. Offer logic (for anything asking for action)

- **One ask.** One CTA, repeated, never competing asks.
- **Reason-why.** Why this, why now, why them — stated, not assumed.
- **Risk reversal.** Lower the cost of saying yes (guarantee, "reply to book", "cancel anytime", "files you own").
- **Concrete next step.** Name the literal action and what happens after it.

## 6. Proof & specificity discipline

- Numbers over adjectives. "511 runs in one week" beats "incredibly productive".
- Named, checkable outcomes over vibes.
- Delete empty intensifiers: robust, world-class, cutting-edge, seamless, game-changing.
- Every claim traces to something true in `.codify/` or the client's real results. If it can't, cut it.

## 7. Dial adjustments

- **`convert`** — tightest. Lead → proof → offer → one CTA. Momentum is everything.
- **`story`** — earn the turn slowly; one real moment, then the lesson, then the ask. Longer leads allowed.
- **`brand`** — no hard ask; the "CTA" is a thought or a question. Craft serves resonance, not click.

---

## How callers use this

- `co-skill-brief-draft` calls this to set `awareness`, `sophistication`, and the recommended lead **into the brief**, so generation starts from the right frame.
- `co-skill-review` calls this to run the **craft_checklist** as an extra gate (alongside the Seven Sweeps) — flagging weak leads, stacked CTAs, empty adjectives, momentum stalls.
- Generation skills (`/co-write`, `/co-ad`, etc.) read the returned `moves` to shape the draft — then `voice.md` and the exemplars in `.codify/exemplars/<kind>/` govern *how it sounds*.

**Order of authority, always:** client substrate (voice, offer, audience, exemplars) → craft layer (this) → generic model defaults. Never the reverse.
