## INTERNAL: DFY Offer Build — End-to-End Process

**For Michael's use only — not shared with clients**

---

### Overview

Client purchases OTO1 ($197) → answers 11 questions → Claude API generates 6 deliverables → Michael spot-checks → client receives package within 48 hours.

**DFY Lite ($97):** Same intake, reduced scope — only Deliverables 1 and 2 (ICP + Offer Doc).

---

### Step 1: Purchase Trigger

**When:** Client buys DFY Offer Build ($197) or DFY Lite ($97) on OTO page

**GHL automation fires (all instant, in parallel):**
- Tag applied: `dfy-purchased` or `dfy-lite-purchased`
- 30-day community trial activated (tag: `community-trial`)
- Questionnaire email sent immediately (GHL template)
- Community access granted immediately + auto-welcome pointing to the pinned "Start Here" intake post
- Internal Slack/email notification to Michael

**Principle: never gate the questionnaire behind the community.** The 48-hour clock starts at purchase. The questionnaire is the raw material for the paid deliverable; the community trial is the ascension bonus. They run in parallel — one never waits on the other. The same questionnaire link lives in three places (email, community pinned post, Michael's DM) so completion doesn't depend on any single channel landing.

**If purchased during OTO flow:**
- Redirect to next OTO page as normal
- Questionnaire email arrives in their inbox by the time they finish checkout

**If purchased from recovery email (Days 3/5/7):**
- Remove from OTO recovery sequence
- Send questionnaire email immediately

---

### Step 2: Questionnaire Intake

**Form:** GHL form — "Your Offer Builder — Quick Intake"
**Time for client:** 10-15 minutes
**Questions:** See `reference/domain/delivery/dfy-intake-questionnaire.md`

**Multi-channel intake — the same link, three ways:**

| Channel | When | Automated? | Role |
|---------|------|-----------|------|
| Questionnaire email | Instantly on purchase | ✅ GHL | The spine — protects the 48h clock, works even if they never open the community |
| Community "Start Here" post | On community access | ✅ GHL (pinned) | Reinforcement — they see it the moment they log in |
| Michael's personal DM in Skool | Within a few hours | 🟡 Manual (now) | The human touch — "Saw you grabbed the DFY build. Here's your questionnaire: [link]. Fill it out and I'll have your package back in 48h." |

The DM is the *cherry on top*, not the only path. Personal outreach lifts completion, but the automated email is what guarantees the intake never stalls on Michael's availability. At low volume the manual DM is worth doing on every order (great for learning real intake); wire it as an automation candidate once volume shows up — it's a "works at 5 buyers, breaks at 50" step.

The 11 questions:

| # | Question | GHL Field |
|---|----------|-----------|
| 1 | What do you do? | `what_you_do` |
| 2 | Who's your best client ever? | `best_client` |
| 3 | What result do you deliver? | `result` |
| 4 | What's your process? | `process` |
| 5 | What makes you different? | `differentiator` |
| 6 | What's your story? | `story` |
| 7 | What do you charge now (and want to charge)? | `pricing` |
| 8 | What's stopping you from getting more clients? | `stuck_point` |
| 9 | How do your clients describe their problem? | `client_language` |
| 10 | What have they tried before that didn't work? | `failed_solutions` |
| 11 | What objections do people have before buying? | `objections` |
| Opt | Best-performing content links | `content_links` |

**Non-response nudges** (the early DM already went out in Step 1 as reinforcement, not a last resort):
- **24 hours, no submission:** GHL sends automated reminder email
- **48 hours, no submission:** Michael follow-up DM in Skool — "Still want me to build this? Just need your 11 answers: [link]. Two minutes and the clock starts."

---

### Step 3: AI Generation

**Trigger:** Form submission → GHL webhook

**Pipeline:** GHL form → webhook → Make.com scenario → Claude API → output stored

**API configuration:**

| Setting | Value |
|---------|-------|
| Model | `claude-sonnet-5` (or `claude-opus-4-8` for max quality, ~3x cost) |
| Max tokens | 16,000 (stream the request at this size) |
| Sampling params | none — `temperature`/`top_p`/`top_k` 400 on Sonnet 5 / Opus 4.8 |
| Cost per call | ~$0.20-0.50 |
| Generation time | 30-60 seconds |

**System prompt:** See `outputs/dfy-upsell/system-prompt.md`

**User message format:**
```
Build the six deliverables for this person based on their questionnaire answers.

## Their Answers

**What they do:**
{{what_you_do}}

**Their best client:**
{{best_client}}

**The result they deliver:**
{{result}}

**Their process:**
{{process}}

**What makes them different:**
{{differentiator}}

**Their story:**
{{story}}

**Current and desired pricing:**
{{pricing}}

**What's stopping them:**
{{stuck_point}}

**How their clients describe the problem (in their own words):**
{{client_language}}

**What their clients tried before that didn't work:**
{{failed_solutions}}

**Objections people have before buying:**
{{objections}}

**Links to best-performing content (optional):**
{{content_links}}
```

**Output:** 6 deliverables, ~8,000-12,000 tokens total

**DFY Lite:** Same API call, but add to user message: "This is a DFY Lite order. Generate only Deliverable 1 (ICP) and Deliverable 2 (Offer Document). Skip deliverables 3-6 (Google Offer Doc, Sales Page, Email Sequence, Ad Hooks)."

---

### Step 4: Review & Refine

**Time:** 30-45 minutes (DFY) / 15-20 minutes (DFY Lite)
**Who:** Michael — every deliverable reviewed personally before sending

**Checklist:**

- [ ] **ICP** feels like a real person, not a generic avatar
- [ ] **Offer name** is specific to their niche (not "The Success System")
- [ ] **Mechanism** has a clear name and 3-4 steps that make sense
- [ ] **Google Offer Doc** sounds like THEM — mirrors their language, written in short punchy lines not paragraphs
- [ ] **Sales Page** reads for COLD traffic — leads with their problem, builds trust, more proof than the warm doc, paste-ready for GHL
- [ ] **Email sequence** has 5 emails, each with subject + preview + body, escalating from welcome to pitch
- [ ] **No invented testimonials** — only placeholders where proof is needed
- [ ] **No income claims** or revenue promises
- [ ] **Price recommendation** makes sense for their market
- [ ] **Ad hooks** cover all awareness levels (not just "aware")
- [ ] **The bridge** to their higher-ticket service is clear and natural
- [ ] **Consistency** across all 6 deliverables — same offer name, mechanism, language, positioning
- [ ] Would I send this to a $5K Accelerator client? If not, what's missing?

**Common fixes:**
- Mechanism name too generic → rename using their actual language
- ICP too broad → narrow to the one person from Q2
- Google Offer Doc sounds like Michael, not them → rewrite key sections in their voice
- Google Offer Doc too formal/long-form → shorten lines, add more line breaks, make it punchy
- Ad hooks too similar → ensure different awareness levels are actually different
- Client language (Q9) not used in headlines → swap in their exact words
- Failed solutions (Q10) not referenced in "here's why" section → add contrast
- Objections (Q11) missing from FAQ → add the ones they listed

---

### Step 5: Package & Deliver

**Format:** Google Doc (shared via link, "Can comment" access)

**Document structure:**
```
[Client Name] — DFY Offer Build
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Section 1: Ideal Client Profile (Dream Client Blueprint)
Section 2: Offer Document (Your Validated Offer)
Section 3: Google Offer Doc — Ready to Send (One-Page Sales Weapon, DFY only)
Section 4: Sales Page — Paste into GHL (Plug-and-Play Sales Page, DFY only)
Section 5: Email Sequence — 5 Emails (Buyer-to-Client Email Machine, DFY only)
Section 6: Ad Hooks — 5 Variations (DFY only)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next Steps (bottom of doc)
```

**Next Steps section (include at bottom):**
```
## What to Do With This

1. Read through everything. Highlight anything that doesn't sound like you.
2. Reply with any changes — I'll revise once (included).
3. Copy your Google Offer Doc into a Google Doc and send it to your warm audience TODAY.
4. Paste your Sales Page into GHL when you're ready to point cold traffic at a landing page.
5. Load your 5-email sequence into GHL to nurture new leads toward the offer.
6. Drop your ad hooks into Meta Ads Manager when you're ready to run cold traffic.

Questions? DM me in Skool or reply to this email.

P.S. Your 30-day community trial is active. Join the next weekly call
and I'll help you implement: [SKOOL LINK]
```

**Delivery method:**
- Email with Google Doc link
- Personal Loom video (2-3 min) walking through the deliverables and highlighting key decisions
- DM in Skool: "Your offer build is in your inbox. Watch the walkthrough video first."

---

### Step 6: Revision Round

**Included:** 1 revision round (within 7 days of delivery)

**Process:**
1. Client comments on Google Doc or replies to email
2. Michael makes revisions (typically 15-30 min)
3. Updated doc sent back within 24 hours
4. Done

**Scope of revisions:**
- Tone/voice adjustments — always yes
- Changing target audience — yes, but flag that it cascades to all deliverables
- Complete rewrite — not included, offer paid revision ($50) or suggest Accelerator
- "Can you also build my funnel?" — no, that's the Accelerator ($5K)

---

### Step 7: Follow-Up & Ascension

**48 hours after delivery:**
- Accountability DM in Skool: "Did you get a chance to review your offer build? Any questions?"

**7 days after delivery:**
- Check-in email: "Have you put your landing page live yet? Reply if you're stuck."

**14 days after delivery:**
- Community trial reminder: "Your 30-day trial is halfway through. Here's what's coming up this week: [WEEKLY CALL TOPIC]"

**25 days after delivery:**
- Trial ending soon: "Your community trial ends in 5 days. Here's what members are working on this month: [HIGHLIGHTS]. Stay for $47/mo or cancel — no hard feelings."

**Accelerator seed (if engaged):**
- If client is active in community + has implemented the DFY build
- Personal DM: "You've got the offer built. Want help building the complete funnel and running traffic? That's what the Accelerator is for."
- Only pitch if they've shown signals (attending calls, asking about traffic, posting wins)

---

### Time & Economics

| Step | DFY ($197) | DFY Lite ($97) |
|------|-----------|---------------|
| Questionnaire intake | — | — |
| API generation | 2 min | 2 min |
| Review & refine | 30-45 min | 15-20 min |
| Package & deliver | 15 min | 10 min |
| Loom walkthrough | 5 min | 3 min |
| Revision round | 15-30 min | 10-15 min |
| **Total (with revision)** | **~1-1.5 hours** | **~30-50 min** |

**Effective hourly rate:**
- DFY at $197: ~$130-200/hour
- DFY Lite at $97: ~$115-195/hour
- API cost: ~$0.10-0.30 per generation (negligible)

---

### Automation Checklist (GHL Setup)

- [ ] GHL form created with 11 questions + 1 optional + field labels
- [ ] Purchase trigger → questionnaire email automation (instant)
- [ ] Purchase trigger → community access granted + auto-welcome (instant, parallel)
- [ ] Community "Start Here" post pinned with the questionnaire link
- [ ] Michael early-DM reminder (manual now; automation candidate at volume)
- [ ] Form submission → Make.com webhook
- [ ] Make.com → Claude API scenario built
- [ ] API output → stored in GHL custom field or sent to email
- [ ] 24-hour questionnaire reminder automation
- [ ] 48-hour no-response DM reminder
- [ ] Delivery email template (with Google Doc link placeholder)
- [ ] 7-day check-in email automation
- [ ] Community trial 14-day and 25-day reminder automations
- [ ] Tag: `dfy-delivered` applied after sending
- [ ] Tag: `dfy-revision-requested` if revision comes in
- [ ] Tag: `dfy-complete` after revision delivered or 7 days with no revision request
