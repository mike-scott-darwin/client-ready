# Email Backend

All email sequences for the Client Ready funnel, organized by audience segment.

---

## Sequence Overview

```
Visitor → [1] Non-Buyer Sequence (30 days)
              ↓ (if buys)
          [2] Welcome Sequence (10 days, 8 AM)
              │   Day 3: consumption branch (opened vs not opened)
              │   Days 5,7,9: soft ascension P.S.
              ↓ (parallel)
          [3] Recovery Sequences (Days 2-8, 2 PM)
              ↓ (after Day 10)
          [4] Daily Broadcast (ongoing)

Sprint/Blueprint buyers also get:
          [7] Accountability DM (manual, within 48 hours)
```

---

## Files

| # | File | Audience | Trigger | Duration |
|---|------|----------|---------|----------|
| 1 | [1-non-buyers-30-day.md](1-non-buyers-30-day.md) | Leads who didn't buy | Visited sales page | 30 days |
| 2 | [2-buyers-welcome-10-day.md](2-buyers-welcome-10-day.md) | New buyers | Purchased $27 | Days 1-10 |
| 3a | [3-buyers-recovery-bumps.md](3-buyers-recovery-bumps.md) | Buyers who missed bumps | No bump purchase | Days 2,4,6 |
| 3b | [3-buyers-recovery-otos.md](3-buyers-recovery-otos.md) | Buyers who missed OTOs | No Sprint/DFY | Days 3,5,7 |
| 3c | [3-buyers-recovery-community.md](3-buyers-recovery-community.md) | Buyers who said no to all | No Sprint/DFY | Day 8 |
| 4 | [4-buyers-daily-broadcast.md](4-buyers-daily-broadcast.md) | All buyers (long-term) | Day 11+ | Ongoing |

---

## Email Timing (Avoids Stacking)

| Time | Sequence Type |
|------|---------------|
| 8:00 AM | Welcome (relationship) |
| 2:00 PM | Recovery (upsells) |

**Max 2 emails per day.** Morning = value. Afternoon = offer.

---

## Journey by Segment

### Non-Buyers (Leads)
1. Visit sales page, don't buy
2. Enter **1-non-buyers-30-day** sequence
3. Goal: Convert to $27 purchase
4. If buy → exit, enter buyer sequences

### New Buyers (Days 1-10)
1. Purchase $27
2. Enter **2-buyers-welcome-10-day** (8 AM, relationship + iron strike ascension)
   - Day 3 branches based on product consumption (Advanced Tips vs Quick Start)
   - Days 5, 7, 9 include soft ascension P.S. sections
3. Simultaneously enter recovery sequences (2 PM, upsells):
   - **3-buyers-recovery-bumps** if missed bumps
   - **3-buyers-recovery-otos** if missed Sprint/DFY
   - **3-buyers-recovery-community** on Day 8 if still no upsell
4. Sprint/Blueprint buyers get manual accountability DM within 48 hours (Workflow 7)
5. After Day 10 → join daily broadcast

### Long-Term Buyers (Day 11+)
1. Exit welcome sequence
2. Join **4-buyers-daily-broadcast**
3. Receive daily story + rotating offer
4. Backend ($5K) seeded through Friday emails

---

## Strategy Reference

See [reference/domain/email-rhythm.md](../../reference/domain/email-rhythm.md) for:
- Why daily emails work
- Writing process (15-20 min)
- Story sources
- Metrics to track

---

## Archived

Old/superseded files in `_archived/`:
- `2026-01-25-email-sequence-buyers-v1.md` — Original 30-day buyer sequence (merged into welcome + recovery)
