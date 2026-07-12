---
type: output
subtype: review-log
date: 2026-07-04
batch: clarity-sells-angles (absolution, offer-closes-itself, tool-fatigue)
lenses: [ftc-compliance, meta-policy, copy-quality, voice-authenticity]
files_reviewed:
  - outputs/ads/absolution.md
  - outputs/ads/offer-closes-itself.md
  - outputs/ads/tool-fatigue.md
origin: decisions/2026-07-04-clarity-sells-angle-territory.md
final_status: CLEAR (P1 + P2 fixes applied; standing typicality data gap noted)
---

# Review Log — Clarity-Sells Angles (Jul 4 2026)

## Review Pipeline

4 parallel review agents ran fresh against the three draft ad files (lens files absent in this repo, so each agent's checklist was embedded in its prompt): **FTC/Substantiation, Meta Policy, Copy Quality, Voice Authenticity.** Findings deduplicated and prioritized below. All P1 and P2 findings were fixed in-place; the files' `review_status` was updated to CLEAR.

**Headline result:** The only launch-blocking (P1) findings were **Meta Personal Attributes** violations — second-person accusation about the reader's failure/status ("you're not bad at this," "you've bought everything and launched nothing," "you still can't put your offer in front of a real person"). `offer-closes-itself.md` was already clean (first-person model). Fixed by converting accusations to first-person confession ("I") or third-person diagnosis ("most coaches").

---

## P1 — Blocking (Meta Personal Attributes) — ALL FIXED

### P1-1: `absolution.md` — second-person accusation throughout P1 + short-form
**Lens:** Meta Policy
Lines "You're not bad at this," "some quiet part of you has started to wonder if you're just not cut out for this," "You were never the problem," and the short-form "You're not bad at this / You've been trying to grow into an offer that was never yours" assert the reader's negative self-state as fact.
**Fix:** Converted the entire P1 to first-person confession ("For years, I thought I was bad at this… I'd been carrying an offer that was never aligned to who I actually am"). Payoff line → "The problem was never the person. It was the offer." Short-form → "It was never about being bad at this. / It was an offer that was never mine to begin with." Kept "you can't grow into pain" (generalized maxim, safe) and second-person only where it's instruction/benefit ("what you actually do well," "You find out if it lands").

### P1-2: `tool-fatigue.md` P2 body — "your hard drive is a graveyard… you still can't put your offer in front of a real person"
**Lens:** Meta Policy
Asserts the reader's hard drive, history, and failure as fact (multiple implied personal attributes).
**Fix:** First-person — "My hard drive was a graveyard… I still couldn't put my offer in front of a real person — because it didn't exist yet."

### P1-3: `tool-fatigue.md` P3 hook — "The reason you've bought everything and launched nothing…" (worst offender) + H4 headline
**Lens:** Meta Policy
Flat assertion of reader failure/status; the exact pattern Meta cites.
**Fix:** Third-person — "The reason so many coaches buy everything and launch nothing isn't discipline…" Headline H4 → "Why 'One More Course' Never Ships an Offer."

### P1-4: `tool-fatigue.md` P1 short-form — "Still can't say what you sell in one sentence"
**Lens:** Meta Policy, FTC
Long-form is first-person; the compressed version silently flipped to second-person accusation.
**Fix:** "And I still couldn't say what I sell in one sentence."

---

## P2 — Fix Before Launch — ALL FIXED

### P2-1: Missing self-guided disclaimer on secondary pitch primaries (all 3 files)
**Lens:** FTC / Substantiation
Every file had the disclaimer on P1 but omitted it on P2 (and offer-closes-itself P3). "Self-guided" alone (offer-closes-itself P3) is insufficient.
**Fix:** Added "Self-guided — results depend on your effort and your market" (or the compact "Self-guided — your effort, your market" on short pattern-interrupt primaries) to every pitch primary. Pure belief-shift ads (no CTA) correctly remain exempt.

### P2-2: Systematic missing CTA on P2 pitch primaries (all 3 files)
**Lens:** Copy Quality
All three P2 primaries ended on a value statement with no click directive.
**Fix:** Added "→ Link below." to each P2 primary and its short-form.

### P2-3: `offer-closes-itself.md` P2 — implied buyer income outcome
**Lens:** FTC
"the $5K clients show up already understanding the offer" implies the buyer will get $5K clients as a result.
**Fix:** Reframed to "a clear offer does the convincing a sales call used to." Removed the causal buyer-outcome from both long and short-form; kept "$5K/$47" only as descriptive contrast of Michael's own model.

### P2-4: `offer-closes-itself.md` P2 — hook/body verbatim echo (template seam)
**Lens:** Voice Authenticity
Hook and first body line were near-identical.
**Fix:** Body now opens "I don't sell $5K coaching packages. I sell a $47 system. Sounds backwards. It isn't. Here's the mechanic."

### P2-5: `offer-closes-itself.md` P1 — soft hook + redundant middle
**Lens:** Copy Quality
Weakest hook of the pitch primaries (abstract belief, not concrete); the clarity-holds/collapses idea stated three times.
**Fix:** Hook now leads with concrete cost ("Discovery calls that ate my afternoon. 'Let me think about it.' The 45-minute pitch to someone who was never going to buy"). Trimmed the redundant "It reads clean because it IS clean" sentence (also resolves the caps-emphasis overuse noted by voice).

### P2-6: `absolution.md` P2 + headline — "Stop blaming your discipline" / "you have a [X] problem"
**Lens:** Meta Policy
Imperative + repeated second-person diagnosis imply the reader's self-state.
**Fix:** Neutralized to "It's not a discipline problem. It's an offer problem." / "It's not a consistency problem. It's not a 'mindset' problem." Headline H3 updated to match. "Confused → Clear → Converting. Most coaches force step 3 while stuck on step 1."

### P2-7: `tool-fatigue.md` — "You don't need a 13th prompt pack" (P2 + short-form + H1) and P3 "you already know enough… You never did"
**Lens:** Meta Policy
Prescriptive/diagnostic second-person implying the reader's purchases and knowledge state.
**Fix:** "The fix was never a 13th prompt pack. It was one offer that actually exists." Short-form and H1 matched. P3 → "most coaches already know enough… It was never a knowledge problem. It never is." H2 → first-person "Still Couldn't Say What I Sell."

---

## P3 — Applied (low-cost polish)

- **Typicality caveat** added to every "testimonials only with the coaching disclaimer" proof rule (all 3 files): the disclaimer alone does not cure the typicality gap — coaching results are not representative of $47-buyer outcomes.
- **`absolution.md`** — reconciled testimonial wording: "clarity in 90 minutes" → "clarity in one session," with a note to match `testimonials.md` (~1.5 hours) and not invent a specific time.
- **Voice:** added a signature "Wrong." to `absolution.md` P3 ("They question themselves… Wrong.").
- **Awareness labels:** the `UNAWARE` tags on the P3 belief-shift ads relabeled to "EARLIER-AWARENESS (belief-shift, runs one level below file)" to prevent media-buyer confusion.

---

## Standing Items (NOT fixed here — require data / buyer action)

- **Typicality data gap (carried from `_archived/.../review-log.md` P1-1):** No `reference/proof/typicality.md` exists. The three ad *copy* files do not deploy testimonials in the copy itself, so copy is clear — but any **creative** that uses a named testimonial (Renee, etc.) or a count carries FTC risk until average-buyer outcome data is collected. Proof rules in all three files now flag this.
- **Unverified social proof:** "150+ students" / "4.7/5" remain unverified (flagged in `testimonials.md` itself). The "no counts" guardrail in all three files must hold until verified against Stripe/GHL.
- **Hook truncation (P3, buyer action):** Verify the P1/P3 hooks land their payoff before the ~125-char mobile "…more" fold in Ads Manager preview before spend.

---

## Final Status

| File | Status | Notes |
|------|--------|-------|
| `absolution.md` | **CLEAR** | Was highest-risk (Meta P1 ×2); converted to first-person confession. Now launch-ready on all four lenses. |
| `offer-closes-itself.md` | **CLEAR** | No P1; the clean first-person model. P2 hook/redundancy/implied-outcome fixes applied. |
| `tool-fatigue.md` | **CLEAR** | Was highest-risk on P3 hook (Meta P1); fixed to third-person. Strongest voice + specificity of the three. |

No P1 remains. Ship-ready at test budget. Do not scale, and do not deploy testimonial/count creatives, until the typicality + verification gaps above are closed.
