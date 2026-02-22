---
type: research
date: 2026-02-22
source: mining
topics: [competitor-analysis, ad-copy, meta-ads, miles-stutz, creative-strategy]
linked_decisions: []
status: complete
---

# Miles Stutz Ad Library Mining — Feb 22 2026

**Source:** Apify Meta Ad Library scrape (194 ads, Feb 22 2026)
**Prior research:** `2026-02-11-miles-stutz-apify-scrape-synthesis.md` (23 ads), `2026-02-10-miles-stutz-ad-library-mining.md` (manual)
**Raw data:** `2026-02-22-miles-stutz-meta-ads-apify.json`
**One-sentence summary:** Miles nuked his entire ad account and relaunched 194 fresh ads in one week, killed the digitalsnacks.co domain entirely, replaced it with a new $17 "Rapid Ascension" funnel at freeclientsystem.com, and shifted from 61% video to 70% static image — a complete creative and product reset.

---

## 1. Volume & Scale

| Metric | Feb 11 | Feb 22 | Change |
|--------|--------|--------|--------|
| Total active ads | 23 | 194 | +743% (8.4x) |
| Unique body texts | ~20 | 49 | ~2.5x |
| Unique collation groups | ~18 | 172 | ~9.5x |
| Products/domains | 2 (digitalsnacks.co + phonefreesales.co) | 2 (rapidascension.freeclientsystem.com + phonefreesales.co) | Domain swap |

**Why the 8x increase:** This is not gradual scaling. Every single ad started between Feb 15-20, 2026. The earliest active ad is 7 days old. Miles killed his entire previous library (including the Sep 2025 "Content Slave" winner that ran for 5+ months) and relaunched everything from zero. This is a full creative reset — new product, new domain, new copy, new creatives.

**So what:** This signals a major strategic pivot. When someone with Miles' experience and spend level wipes the slate, they've either found something that works dramatically better, or something broke. The $17 Rapid Ascension product at 120 ads (62% of total) is the bet.

---

## 2. Format Distribution

| Format | Feb 11 | Feb 22 | Change |
|--------|--------|--------|--------|
| Video | 14 (61%) | 49 (25%) | -36 pts |
| Image | 9 (39%) | 136 (70%) | +31 pts |
| Carousel | 0 (0%) | 9 (5%) | New |
| DCO (Dynamic Creative) | 0 | 9 (5%) | New |

### By Product

| Product | Video | Image | Carousel | Total |
|---------|-------|-------|----------|-------|
| Rapid Ascension ($17) | 0 (0%) | 114 (95%) | 6 (5%) | 120 |
| No-Phone Offer ($9) | 34 (58%) | 22 (37%) | 3 (5%) | 59 |
| No-URL (comment/DM) | 15 (100%) | 0 (0%) | 0 (0%) | 15 |

**So what:** The Feb 10 manual mining was right all along — static image is the workhorse. The Feb 11 Apify scrape caught a moment of heavy video testing. Now with 194 ads, the picture is clear: Miles runs static for his primary front-end (Rapid Ascension) and video for his secondary product (No-Phone Offers) and comment-to-DM funnels. Static at volume is the proven path for direct-response low-ticket.

**New format — Carousel:** 9 carousel ads appear for the first time. All use 2-card formats with copy pulled from the same body texts. A/B testing format, not angle.

**New format — DCO:** 9 ads use Meta's Dynamic Creative Optimization (body shows `{{product.brand}}`, `{{product.name}}`, `{{product.description}}`). These let Meta auto-assemble combinations of headline, image, body, and CTA. Miles is using Meta's AI to test creative variations automatically.

---

## 3. Product Distribution — The Big Pivot

| Product | Domain | Ads | % | Price | Status |
|---------|--------|-----|---|-------|--------|
| **Rapid Ascension System** | rapidascension.freeclientsystem.com | 120 | 62% | $17 | **NEW** |
| No-Phone Offer Method | phonefreesales.co/no-phone-offer-method | 49 | 25% | $9 | Continuing |
| No-Phone (home) | phonefreesales.co/ | 10 | 5% | $9 | Continuing |
| Comment-to-DM (no URL) | n/a | 15 | 8% | $17 (via DM) | Continuing |
| **Digital Snacks** | digitalsnacks.co | 0 | 0% | $7-$97 | **KILLED** |

### What Changed

**digitalsnacks.co is dead.** Zero ads. Zero presence. The domain that was 57% of his Feb 11 library is completely gone.

**rapidascension.freeclientsystem.com is the replacement.** Same underlying concept (Digital Snacks), but repackaged as the "Rapid Ascension System" at $17 (up from $7), on a completely new domain under the "Free Client System" brand umbrella. The link description across 113 ads is identical: "AI-powered system. 1,090+ students. Build your first Digital Snack in 60 minutes. $17 today."

**The $17 price point now dominates.** 118 ads mention $17 in the copy. Only 47 mention $9. The Feb 11 "$17 hidden third product" is now the primary product. The $9 No-Phone Offer is now the secondary funnel.

**So what:** Miles consolidated from three front-end funnels (Digital Snacks $7, No-Phone $9, Comment-to-DM $17) into two clean funnels (Rapid Ascension $17, No-Phone $9). He raised his front-end price and rebranded. This aligns with the Cat Howell data in Client Ready's own research: cheap front-ends ($7) kill AOV. $17 is the new floor.

---

## 4. Copy & Body Analysis

### 4.1 Unique Copy Blocks

49 unique body texts across 194 ads. Most copy is heavily duplicated across multiple image creatives:

| Copy Block (Hook) | Repetitions | Product | Angle |
|-------------------|-------------|---------|-------|
| "I don't chase high-ticket clients..." | 54x | Rapid Ascension | Low-Ticket Ascension |
| "The 3-step system for turning $17 buyers..." | 16x | Rapid Ascension | Speed/Mechanism |
| "Every expert is optimizing for sales calls..." | 16x | Rapid Ascension | No-Sales-Calls |
| "Diego had no audience, no email list..." | 16x | Rapid Ascension | Case Study |
| "If you're an expert already making $10K..." | 11x | Rapid Ascension | Scale/Revenue |
| "I removed sales calls 6 months ago..." | 9x | No-Phone | No-Sales-Calls |

**Key insight:** His most-repeated copy block (54 instances) runs on 54 different image creatives with the same body text. This is radical creative variance applied to images, not copy. He tests the visual, not the words.

### 4.2 Top Hooks

**Rapid Ascension (Top 5 hooks by frequency):**

1. "I don't chase high-ticket clients, haven't in over a year now and I still made $750,000 last year. What I do instead sounds a little backwards..." (54x)
2. "The 3-step system for turning $17 buyers into $5,000+ clients automatically in 3 hours without trying to go viral..." (16x)
3. "Every expert is optimizing for getting sales calls booked. I deleted mine completely and I made more than ever." (16x)
4. "Diego had no audience, no email list, and no idea how to sell anything online. 6 months later he's making $14K/month teaching chess." (16x)
5. "If you're an expert already making $10K, $20K, maybe $30K/month...what got you here won't get you to $100K/month." (11x)

**No-Phone Offer (Top 5 hooks by frequency):**

1. "I removed sales calls from my business 6 months ago -- my close rate more than doubled." (9x)
2. "My Coaching business was growing. Leads were coming in. But I was drowning in sales calls." (2x)
3. "I took over 2000 Sales Calls -- and I'm not even a High-Ticket Closer!" (2x)
4. "For 8 years, I thought I needed to prove my value on every single call." (2x)
5. "I closed a $15,000 client this morning." (2x)

### 4.3 New Hook Patterns (Not in Feb 11)

| Pattern | Example | Frequency |
|---------|---------|-----------|
| Anti-chasing reversal | "I don't chase high-ticket clients" — positions chasing as the problem | Dominant (54x) |
| Backwards/counterintuitive | "What I do instead sounds a little backwards" — curiosity trigger | High |
| Chess case study | "Diego... making $14K/month teaching chess" — niche credibility | 16x |
| Scaling ceiling | "What got you here won't get you to $100K/month" — problem-aware trigger | 11x |
| 3-step system claim | "3 hours. That's it." — speed mechanism | 16x |
| Close rate doubling | "My close rate more than doubled" — counter-expectation | 9x |

### 4.4 Angle Distribution (Revised)

| Angle | Ads | % | vs Feb 11 |
|-------|-----|---|-----------|
| Low-Ticket Ascension (sell $17 → $5K) | 71 | 37% | **NEW dominant angle** |
| No-Sales-Calls / Calendar Trap | 53 | 27% | Was 30% — still strong |
| Anti-Proof / Offer Clarity | 17 | 9% | Was 9% — stable |
| Case Study (Diego, named) | 16 | 8% | Was 4% — doubled |
| Scale / Revenue Without Burnout | 18 | 9% | Was 17% — halved |
| Anti-Organic / Content Treadmill | 5 | 3% | Was 35% — **collapsed** |
| Pro-Ads / Belief-Shift | 3 | 2% | Was 13% — reduced |
| Anti-Customization / Systemization | 2 | 1% | **NEW** |
| DCO/Template | 9 | 5% | **NEW** |

**Critical shift:** Anti-Organic was his #1 angle in Feb 11 (35%). It's now 3%. Low-Ticket Ascension (the "sell a $17 product, ascend to high-ticket" narrative) replaced it entirely. The primary selling message is no longer "stop posting content" — it's "sell a $17 product that turns buyers into $5K clients automatically."

**New angle — Anti-Customization:** "I used to customize my offer for every single High-Ticket prospect" → "Stop Customizing. Start Scaling." Positions one-size-fits-all offers as the solution to the customization trap.

### 4.5 Copy Template (Rapid Ascension Style)

The dominant Rapid Ascension copy follows a new skeleton, different from the Feb 11 No-Phone template:

1. Counterintuitive income claim: "I don't chase high-ticket clients... still made $750K"
2. The backwards reveal: "I sell a $17 product"
3. Mechanism explanation: "$17 buyers upgrade to $5K-$10K in 7 days"
4. Psychology bridge: "When someone pays $17 and gets a quick win, something shifts"
5. Trust reframe: "There's trust with a receipt attached"
6. Product naming: "I call these Digital Snacks"
7. AI + simplicity: "An hour packaging it using AI prompts and plug-and-play templates"
8. Tiny action: "Then you run $20/day in Facebook ads"
9. Speed claim: "Within hours, people start buying"
10. Automated ascension: "The built-in upgrade sequence handles the rest"
11. Social proof: "1,090+ students" / "Over 250+ launched"
12. Price: "$17 today" (anchored against $147)
13. Guarantee: 30-day money-back
14. Urgency: None (clean, no fake scarcity)

### 4.6 Price Mentions

| Price Point | Mentions | Context |
|-------------|----------|---------|
| $17 | 495 (across 118 ads) | Primary front-end price |
| $9 | 95 (across 47 ads) | No-Phone Offer price |
| $97 | 47 | Anchor: "normally $97" (No-Phone) |
| $147 | 54 | Anchor: "normally $147" (Rapid Ascension) |
| $5K-$15K | ~170 | Income claims (client values) |
| $750K | 54 | Annual income claim |
| $1.4M | ~18 | Monthly revenue claim |
| $14K/month | 86 | Diego case study |

**So what:** The $17 → $147 anchor (88% discount) is the new primary framing, replacing the $9 → $97 anchor (91% discount). Slightly less aggressive discount percentage but higher absolute price point. Both price anchors are aggressive but standard for this market.

---

## 5. CTA Patterns

| CTA Type | Count | % |
|----------|-------|---|
| Learn more | 179 | 92% |
| No button (comment-to-DM) | 4 | 2% |
| Send message | 2 | 1% |
| (none/blank) | 9 | 5% |

**Comment-to-DM triggers in copy:**
- "Comment 'Snacks' below" — still active (4 ads with explicit CTA text, ~11 more in no-URL video format)
- The $17 step-by-step course via DM remains the third funnel path

**So what:** "Learn more" dominates at 92%. No significant CTA experimentation. The selling happens in the copy, not the button.

---

## 6. Date Analysis

| Date | Ads Launched |
|------|-------------|
| Feb 15 | 68 |
| Feb 16 | 57 |
| Feb 17 | 12 |
| Feb 18 | 12 |
| Feb 19 | 24 |
| Feb 20 | 21 |

- **Oldest active ad:** Feb 15, 2026 (7 days old)
- **No ads from before Feb 15.** Every ad from the Feb 11 scrape (including the Sep 2025 "Content Slave" winner) has been turned off.
- **Launch pattern:** 125 ads (64%) launched on Feb 15-16 (the initial wave), then 69 ads (36%) launched over the next 4 days (iterative additions).
- **End dates:** 119 ads show Feb 21 as end date, meaning many are already stopped or being rotated.

**So what:** This is a coordinated relaunch, not gradual scaling. Miles launched ~125 ads in 2 days, then added ~70 more over the next 4 days. He's testing at massive volume and killing fast — matching his own teaching: "Fire quick. Let them run. Over CPA? Turn it off."

---

## 7. Country/Targeting

| Targeting | Count |
|-----------|-------|
| Global (empty/no targeting) | 194 (100%) |

**Publisher platforms:** All 194 ads run across Facebook, Instagram, Messenger, and Threads simultaneously.

**So what:** Confirms the post-Andromeda principle in Client Ready's own ad strategy: broad targeting is default. Miles runs everything worldwide with no geographic restrictions. Creative IS targeting.

---

## 8. Creative Patterns

### 8.1 Collation (Creative Versions)

| Collation Count | Ads | Meaning |
|-----------------|-----|---------|
| 1 (single version) | 149 | One creative per ad |
| 2 (dual version) | 42 | Two creatives per ad (A/B) |
| Null | 3 | Unknown |

**172 unique collation groups** across 194 ads. Most are single-version, meaning Miles is testing individual creatives rather than paired short/long copy on the same image (which he did in Feb 11).

### 8.2 Image-Heavy Strategy for Rapid Ascension

120 Rapid Ascension ads: 114 are static image, 6 are carousel, 0 are video. This product is being tested purely with static images + long-form copy. The copy does all the selling; the image is the scroll-stopper.

54 of those 120 ads use the exact same body text on different images — radical creative variance on the visual, not the copy.

### 8.3 AAA Eligibility (Advantage+ Creative)

35 out of 194 ads (18%) are eligible for Advantage+ Auto-Application (Meta's AI-powered creative optimization). This means Meta can automatically adjust aspect ratios, add music, enhance visuals, etc.

### 8.4 AI-Generated Media Flag

0 out of 194 ads are flagged as containing "digitally created media." Either Miles is not using AI-generated images, or he's using them in ways Meta's detection doesn't flag.

---

## 9. Spend & Reach

| Data Point | Available? |
|------------|------------|
| Spend data | No (0/194) |
| Reach estimates | No (0/194) |
| Impressions text | No (all null) |
| Impressions index | 115 ads at index 0, 79 at index -1 |

**So what:** Meta Ad Library does not expose spend, reach, or impression data for non-political ads. The impressions index (0 vs -1) likely indicates whether the ad has accumulated enough impressions to register, but provides no absolute numbers. No performance data can be extracted from this scrape.

---

## 10. Delta from Feb 11 — What Changed

### Killed
- **digitalsnacks.co domain** — completely dead, 0 ads
- **Sep 2025 "Content Slave" copy** — the 5-month winner is gone
- **Anti-Organic as lead angle** — collapsed from 35% to 3%
- **All pre-Feb-15 ads** — entire library wiped and relaunched
- **Ultra-short animated video (5-9s)** — not visible in this scrape

### Added
- **rapidascension.freeclientsystem.com** — new domain, new product, 120 ads (62%)
- **$17 as primary price** (was hidden $17 third product; now the main front-end)
- **"Free Client System" brand umbrella** — freeclientsystem.com as the parent domain
- **Carousel format** — 9 ads, never seen before
- **DCO (Dynamic Creative Optimization)** — 9 ads with template variables
- **Low-Ticket Ascension as dominant angle** — 37%, new narrative framework
- **Diego chess case study** — 16 ads, concrete niche proof
- **Anti-Customization angle** — "Stop Customizing. Start Scaling."

### Unchanged
- **phonefreesales.co** — still running, 59 ads (down from 43% to 30% of total)
- **$9 No-Phone Offer** — same product, same price, same core angles
- **Comment-to-DM with "Snacks"** — still active, 15 no-URL ads
- **"1,090+ students" social proof** — unchanged number, appears in 97 ads
- **"Learn more" as dominant CTA** — 92%, same as before
- **Global targeting, all platforms** — unchanged
- **Long-form narrative copy** — still the dominant format

### Shifted
- **Format ratio flipped:** Video 61% → 25%; Image 39% → 70%
- **Primary product:** Digital Snacks ($7) → Rapid Ascension ($17)
- **Primary angle:** Anti-Organic (35%) → Low-Ticket Ascension (37%)
- **Testing approach:** Paired short/long per image → Same copy, different images (radical visual variance)
- **Price anchor:** $9 (normally $97) → $17 (normally $147)

---

## 11. Patterns

### Pattern 1: The Complete Reset
Miles didn't iterate. He wiped and relaunched. This suggests the old account had either exhausted creative, hit frequency caps, or the new Rapid Ascension product tested so well in a small test that it warranted a full rebuild. The fact that he killed a 5-month proven winner ("Content Slave") tells you the new system is significantly outperforming.

### Pattern 2: $17 Is the New $9
The hidden $17 comment-to-DM product from Feb 11 is now the primary front-end. Cat Howell's research (in Client Ready's own files) showed that $17 front-ends killed AOV, but Miles apparently found a way to make it work — likely through aggressive upsell/ascension mechanics ("Rapid Ascension System"). The name itself signals the strategy: rapid ascension from $17 to high-ticket.

### Pattern 3: Static Image at Massive Volume
120 Rapid Ascension ads are 95% static image. The same copy block runs on 54 different images. This is the purest expression of "creative IS targeting" — same message, different visual triggers, let Meta's algorithm find which scroll-stopper works for which audience segment.

### Pattern 4: Product Consolidation
Three front-ends (Digital Snacks $7, No-Phone $9, Comment-to-DM $17) consolidated into two clean funnels with separate domains. Each product has its own domain, its own creative strategy (static vs video), and its own angle set. Clean separation.

### Pattern 5: Angle Migration
Anti-Organic (content treadmill attacks) were the #1 angle. Now they barely exist. The new dominant angle is positive-mechanism: "Here's what works (sell a $17 product)" rather than "Here's what doesn't work (posting content)." This is a maturation from problem-aware messaging to solution-aware messaging. Miles may have found that negative angles attract tire-kickers while positive-mechanism angles attract buyers.

### Pattern 6: Case Study as Scale Strategy
Diego (chess teacher, $14K/month) appears in 16 ads. This is a named case study from a non-obvious niche, proving the method works outside typical coaching. The specificity ("20-page guide," "The Opening Trap Guide," "$30/day in ads") makes it believable. This is the kind of case study Client Ready needs but doesn't have yet.

---

## 12. vs Client Ready Comparison

| Dimension | Miles Stutz (Feb 22) | Client Ready | Gap / Opportunity |
|-----------|---------------------|--------------|-------------------|
| Active ads | 194 | 0 (pre-launch) | Volume gap (expected) |
| Front-end price | $17 | $47 | CR is higher — better AOV if bumps convert |
| Price anchor | $147 | $197 | Similar strategy |
| Primary format | 95% static image | Planned static + video | Validates static-first approach |
| Primary angle | Low-Ticket Ascension (37%) | Offer Clarity / Before-the-Funnel | Different mechanism story — not a direct conflict |
| Case studies | Diego (chess, $14K/mo), named | None yet | Critical gap for CR |
| Domains | 2 (separate products) | 1 (clientreadyoffer.com) | CR has single funnel focus — right for launch |
| Copy length | Long-form dominant | Long-form planned | Aligned |
| Targeting | Global, broad | Planned broad | Aligned |
| CTA | "Learn more" (92%) | Planned "Learn more" | Aligned |
| Comment-to-DM | Active (15 ads) | Not planned | Watch, not copy |
| DCO / carousel | Testing (18 ads) | Not planned | Future test after baseline |
| Social proof | "1,090+ students" | None yet | Critical gap — solve with early buyers |
| Guarantee | 30-day money-back | 30-day money-back | Aligned |
| AI mention | "AI-powered system," "AI prompts" | AI prompts in product | Both use AI — CR should feature this in copy |
| Revenue claims | $750K, $1.4M, $14K/mo, $15K clients | None (FTC-compliant) | CR's advantage — sustainable positioning |
| Profanity | Reduced from Feb 11 | None | Non-issue |

### Where Client Ready Has Advantage

1. **FTC compliance.** Miles makes income claims ($750K, $1.4M) without disclaimers. Client Ready's clean positioning is a long-term advantage. When enforcement tightens, Miles has to rewrite everything.

2. **Higher front-end price.** $47 vs $17. If Client Ready's bumps convert at target rates (50%+ take rate), AOV will be significantly higher. Miles needs massive volume to compensate for lower front-end.

3. **"Before the funnel" positioning.** Miles assumes you know what to sell. Client Ready solves the step he skips: "What IS my offer?" This targets an earlier-stage buyer with less competition.

4. **Anti-fake-urgency.** Miles doesn't use fake scarcity (an improvement from other competitors), but Client Ready's "Link's in the bio. Or don't." is still more distinctive.

### Where Miles Has Advantage

1. **Proven case studies.** Diego (chess, $14K/mo) with specific product details. Client Ready has zero proof. This is the #1 gap.

2. **Volume and velocity.** 194 ads launched in 7 days. The testing velocity alone generates more data than Client Ready can access.

3. **Clear mechanism name.** "Digital Snacks" and "Rapid Ascension" are memorable, concrete product names. "Client Ready Offer System" is functional but not as sticky.

4. **AI-powered positioning.** "Build your first Digital Snack in 60 minutes using AI" is specific and modern. Client Ready has AI prompts but doesn't lead with this in ad copy.

---

## 13. What to Steal (Actionable)

### Act On (High Signal)

1. **Static image at volume with same copy.** Miles' #1 play is 54 different images with the same body text. Client Ready should test 5-10 different image creatives per copy block, not 1-2. Let Meta find the winning visual.

2. **$17 validates higher front-ends.** Miles moved FROM $7 TO $17, supporting Client Ready's $47 price point. If Miles can't make $7 work, $47 with strong bumps is the right bet. Don't lower price.

3. **Case study angle at 8%.** Diego's chess story runs on 16 ads. Client Ready needs ONE early client win story — any niche, any result — to unlock this angle. Prioritize getting the first 5-10 sales and collecting a story.

4. **Anti-Customization angle.** "Stop Customizing. Start Scaling." is directly applicable to Client Ready's offer (one-size-fits-all templates vs custom work). Test this as an ad angle.

5. **AI prominently in copy.** Miles puts "AI-powered" in his link descriptions. Client Ready's 5 AI prompts should be featured prominently in ad copy, not buried in product details.

6. **Counterintuitive hook pattern.** "I don't chase high-ticket clients... I sell a $17 product" — the backwards reveal creates massive curiosity. Client Ready equivalent: "I don't sell $5K coaching packages... I sell a $47 system that makes the $5K offer sell itself."

### Watch (Interesting, Not Urgent)

7. **DCO (Dynamic Creative Optimization).** Miles is testing 9 ads with template variables. Worth exploring after Client Ready has baseline data.

8. **Carousel format.** 9 carousel ads, all 2-card. New format test. Monitor if this appears in future scrapes.

9. **freeclientsystem.com as brand umbrella.** Miles now has a parent domain housing sub-products. Client Ready doesn't need this at launch but may want it for multi-product phase.

10. **"Rapid Ascension" naming.** The product name communicates the transformation (rapid) and the mechanism (ascension from low to high ticket). Client Ready's "Offer System" is functional — consider if a more aspirational name would perform better in ads.

### Don't Copy

- **Revenue claims.** $750K, $1.4M — these are unsubstantiated and FTC-risky.
- **Complete ad account reset.** Miles can afford to nuke and rebuild. Client Ready should build incrementally.
- **$17 front-end price.** Miles is testing whether $17 works. Client Ready's own research (Cat Howell) says $17 kills AOV. Stick with $47.
- **54 versions of same copy.** This works with spend to test at scale. Client Ready should start with 3-5 image variants per copy, not 54.

---

## 14. Open Questions

1. **Why did Miles kill digitalsnacks.co?** Was it a branding problem (too cute), a conversion problem (domain didn't convert), or a strategic consolidation? The answer matters — if "Digital Snacks" as a name was confusing, naming matters more than we think.

2. **Is the Rapid Ascension system the same product as Digital Snacks, repackaged?** The copy still says "Digital Snacks" in the body text. The brand confusion between "Rapid Ascension" (domain) and "Digital Snacks" (copy) suggests this was a fast pivot, not a clean rebrand.

3. **Why 95% static for Rapid Ascension but 58% video for No-Phone?** Is this a format preference by product type, or did Miles test video for Rapid Ascension and kill it before this scrape?

4. **Will the Feb 11 "Content Slave" copy return?** It ran for 5+ months and was his most proven winner. Killing it is bold. If it comes back in a future scrape, that tells us the reset didn't outperform the original.

5. **Should Client Ready build a "Low-Ticket Ascension" angle?** Miles' dominant message is now "sell a $17 product → ascend to high-ticket." Client Ready's equivalent: "validate your offer for $47 → ascend to Sprint/Blueprint/Accelerator." Is this angle worth testing?

6. **"1,090+ students" hasn't changed since Feb 11.** Is this number frozen (social proof placeholder) or is enrollment actually stalled? If frozen, it's a manufactured number. Client Ready should track and update its own proof numbers honestly.

---

## Appendix: Raw Statistics

- Total ads scraped: 194
- All ads active: Yes (194/194)
- Date range: Feb 15-20, 2026 (all < 8 days old)
- Unique ad archive IDs: 194
- Unique collation IDs: 172
- Unique body texts: 49
- Global targeting: 100%
- Platforms: Facebook + Instagram + Messenger + Threads (100%)
- Spend/reach data: None available
- AI-generated media flag: 0/194
