---
type: decision
status: active
date: 2026-07-04
trigger: Community launch — seed the room before charging full price
supersedes_price: 2026-03-07-dfy-upsell-community-first.md ($97/mo → $47/mo beta)
---

# Decision: Community launches at $47/mo (beta entry)

## Decision

The Client Ready Community launches at **$47/month — beta entry pricing.**
The **$97/mo** set in [2026-03-07-dfy-upsell-community-first.md](2026-03-07-dfy-upsell-community-first.md) becomes the **post-beta target**, not the launch price.

Everything else from the March decision holds: month-to-month, cancel anytime, 30-day trial bundled with DFY / DFY Lite, community is still the central engine.

## Why

- **Seed the room first.** An empty community at $97/mo is a hard sell. $47 lowers the barrier to get the first cohort in, generate activity, and build proof.
- **The $97/mo was planned but never went live.** `CLAUDE.md`'s gap list flagged community pricing as "⚠️ need to set $97/mo in GHL" — it was never actually configured. So $47 isn't a price cut from a live $97; it's the real launch price.
- **Beta framing is honest and gives room to raise.** Early members get founding/beta pricing; the price moves toward $97 once the room is seeded and delivering.

## Implications

- **Recurring revenue per member roughly halves** vs. the $97 model. Revenue projections in `outputs/dfy-upsell/funnel-restructure.md` and the 90-day value in `CLAUDE.md` were recomputed at $47 (e.g. ~10 members → ~$470/mo, not $970/mo).
- **Tight gap to the Monthly Playbook ($37/mo).** Community ($47) now sits only $10 above the newsletter ($37). Watch that the community's value (calls, DM access, curriculum) stays clearly differentiated, or the newsletter cannibalizes it. Revisit when raising toward $97.
- **Raise trigger:** once the room is active and delivering wins, move price toward $97/mo for new members (grandfather beta members or not — TBD).

## Scope of the repo update (this pass)

Swept community price `$97/mo → $47/mo` across all active files: `CLAUDE.md`, `README.md`, `offer.md`, product/page copy (incl. the community sales page `oto3-community-full-page-copy.md` and the DFY trial "then $X/mo" lines), funnel/membership/classroom reference docs, and the email sequences (`CR01`, `DB06`, recovery/broadcast source files).
Left intact: unrelated `$97` (DFY Lite one-time, Bump 3 Playbook, Funnel Snapshot), archived files, research, and the historical March decision doc (annotated with a forward pointer).

## Still to do (outside the repo)

- Set the community product to **$47/mo** in GHL (it was never set to $97 anyway).
- Repaste the corrected `$47` email templates (`CR01`, `DB06`) into GHL.
