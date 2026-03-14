---
type: research
status: active
date: 2026-03-08
source: gemini
enhances:
  - reference/core/offer.md
linked_decisions: []
---

# Meta Ads Research: Low-Ticket Coach Offers (March 2026)

## Summary
Meta advertising for low-ticket coaching products ($47-97) has evolved significantly post-Andromeda update. Creative variance has replaced traditional targeting as the primary success factor, with broad targeting and Advantage+ placements becoming the new standard. Data from Miles Stutz and Cat Howell shows successful low-ticket funnels achieving $80-120 CPAs with AOVs of $100-120 through strategic bump offers and OTO structure. Landing pages have shifted from video-only to hybrid formats combining VSL with long-form copy and visual evidence.

## Key Insights
- Creative IS targeting: Meta's algorithm now operates at account level, with ad copy and visuals serving as primary audience signals
- "Ugly" static creatives (Notes app screenshots, tweet formats) are outperforming polished assets, driving 60-70% of conversions
- Silent review videos (product demos without speaking) are emerging as high-trust formats for cold traffic
- Traditional interest targeting and micro-budget ad sets ($5/day) no longer perform effectively
- Hybrid VSL pages (video + long-form copy + visual evidence) outperform video-only landing pages
- Broad targeting with creative variance outperforms traditional interest/lookalike targeting
- Early winners reveal themselves after ~$20 spend per creative concept for low-ticket offers

## Data Points
- Target AOV: $100-120 (front-end + bumps)
- Combined bump rate benchmark: 50%+ (Cat Howell data)
- OTO conversion rates:
  - DFY Offer Build ($197): 15%
  - DFY Lite downsell ($97): 10% of remaining
  - Newsletter ($37/mo): 8%
- CPAs under $80 qualify for 20% budget increase every 48 hours
- Kill threshold: $150-200 CPA for $100-120 AOV funnel
- Mobile traffic: 80%+ of landing page visitors
- Checkout conversion rate target: 30%

## Contrarian Findings
1. Traditional targeting optimization (interest stacking, detailed targeting) now hurts performance by restricting the algorithm
2. "Feed Only" placements limit reach and increase costs - Advantage+ Placements finds cheaper inventory
3. Minor creative testing (button colors, copy tweaks) is ineffective - radical concept variance required
4. Lookalike audiences as primary targeting underperform broad targeting with strong creatives
5. Video-only landing pages are losing effectiveness despite being considered "best practice"

## Suggested Reference Updates

### offer.md Updates
1. Add section on creative format hierarchy:
   ```markdown
   ### Creative Format Rankings (2026)
   1. "Ugly" static text-on-background
   2. Silent Review demos
   3. B-roll with text overlay
   4. Founder face-to-camera
   5. AI UGC
   6. Human UGC
   ```

2. Update targeting section:
   ```markdown
   ### Post-Andromeda Targeting
   - Broad is default
   - Creative IS targeting
   - No interest stacking
   - Advantage+ Placements enabled
   ```

3. Add low-ticket testing rule:
   ```markdown
   ### The $20 Rule
   For $47-97 products, winners reveal themselves after ~$20 spend per concept. Kill concepts without positive signals at this threshold.
   ```

### campaign-structure.md Updates
1. Three-stage pipeline:
   - ABO Testing ($50/day per concept)
   - CBO Winners ($100/day start)
   - ASC Scaling (mature pixel only)

2. Budget split:
   - 70% scaling
   - 20% testing
   - 10% retargeting
   
   Flip to 70% testing / 30% scaling during launch phase.

## Sources
- Miles Stutz research (Feb 2026)
- Cat Howell benchmarks (Feb 2026)
- Andromeda algorithm analysis
- Internal offer.md documentation