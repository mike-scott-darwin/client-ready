---
type: reference
status: active
updated: 2026-03-07
---

# DFY Offer Build — Intake Questionnaire

**Purpose:** Canonical 11-question intake for DFY Offer Build ($197) and DFY Lite ($97) clients.

**Form:** GHL form titled "Your Offer Builder — Quick Intake"
**Submission URL:** https://forms.gle/vtX5Pvc5cSNzcA34A *(needs updating to GHL form)*
**Time to complete:** 10-15 minutes

---

## The 11 Questions

Each question maps directly to the 6 deliverables (ICP, Offer Doc, Google Offer Doc, Sales Page, Email Sequence, Ad Hooks).

### 1. What do you do?
**Label:** `what_you_do`
**Type:** Long text
**Prompt:** "Describe what you help people with — like you're telling a friend at dinner. Don't use jargon. 2-4 sentences."
**Maps to:** All deliverables — establishes the core offer

### 2. Who's your best client ever?
**Label:** `best_client`
**Type:** Long text
**Prompt:** "Describe one real person you've helped (or want to help). What were they struggling with? What did they do for work? What was their life like before and after? If you haven't had clients yet, describe the person you'd most love to work with."
**Maps to:** ICP (primary source), Google Offer Doc (who's it for section)

### 3. What result do you deliver?
**Label:** `result`
**Type:** Long text
**Prompt:** "What's different about someone's life or business 90 days after working with you? Be specific. 'They feel better' isn't enough. 'They have 3 paying clients and stopped second-guessing their offer' is."
**Maps to:** Offer Doc (transformation), Google Offer Doc (headline + proof), Ad Hooks

### 4. What's your process?
**Label:** `process`
**Type:** Long text
**Prompt:** "Walk me through the steps you take someone through. What do you do first, second, third? Even if it's informal — describe how you actually help people, start to finish."
**Maps to:** Offer Doc (mechanism), Google Offer Doc (tease + mechanism section)

### 5. What makes you different?
**Label:** `differentiator`
**Type:** Long text
**Prompt:** "What do you do that other people in your space don't? This could be your background, your approach, a specific framework, or just how you think about the problem differently."
**Maps to:** ICP (zone of genius), Ad Hooks (contrarian + curiosity hooks)

### 6. What's your story?
**Label:** `story`
**Type:** Long text
**Prompt:** "Why do you do this? What happened that led you here? The messy version is better than the polished version."
**Maps to:** Google Offer Doc (backstory section), Ad Hooks (story hook)

### 7. What do you charge now (and want to charge)?
**Label:** `pricing`
**Type:** Short text
**Prompt:** "Current price and desired price. Example: 'Currently $500/session, want to sell a $3K package' or 'Haven't charged yet, thinking $2K-5K.'"
**Maps to:** Offer Doc (pricing recommendation, price anchoring), Google Offer Doc (price reveal)

### 8. What's stopping you from getting more clients right now?
**Label:** `stuck_point`
**Type:** Long text
**Prompt:** "Be honest. Is it your offer? Your confidence? No funnel? No traffic? Don't know where to find people? This helps us prioritize what to build first."
**Maps to:** Google Offer Doc (push section), Ad Hooks (pain agitation hook), Offer Doc (objection handling)

### 9. How do your clients describe their problem in their own words?
**Label:** `client_language`
**Type:** Long text
**Prompt:** "Copy-paste a real DM, email, or comment if you have one. If not, write what they typically say when they first reach out. Their exact words are gold for your copy."
**Maps to:** Google Offer Doc (headline, benefits, future pacing), Ad Hooks (all hooks), ICP (psychographics)

### 10. What have your clients tried before that didn't work?
**Label:** `failed_solutions`
**Type:** Long text
**Prompt:** "Courses, other coaches, DIY, free YouTube content, templates — what did they try and why did it fail? This helps us position your offer against the alternatives."
**Maps to:** Google Offer Doc (counterintuitive tease), Ad Hooks (problem aware + contrarian), Offer Doc (problem section)

### 11. What objections do people have before buying from you?
**Label:** `objections`
**Type:** Long text
**Prompt:** "Price, time, skepticism, 'I've tried this before,' 'I'm not ready' — what do people say before they decide? Include the ones you hear most, even if they feel awkward."
**Maps to:** Google Offer Doc (push / not for section), Offer Doc (objection handling), Ad Hooks (solution aware hook)

### Optional: Best-performing content
**Label:** `content_links`
**Type:** Long text
**Prompt:** "Share links to 2-3 posts, emails, or videos that got the best response from your audience. This helps us match your voice and tone in the deliverables."
**Maps to:** Voice matching across all deliverables

---

## Guidelines for Clients

Include these on the form:

- Takes 10-15 minutes
- Be specific — first instinct is usually right
- NO wrong answers — honesty beats perfection
- Include examples where possible
- The more detail you give, the better your deliverables

**For new businesses:**
- Make educated guesses based on research/intuition
- Share hypotheses about who you want to serve
- Describe your vision, even if not fully formed

---

## Question → Deliverable Map

| Question | ICP | Offer Doc | Google Offer Doc | Ad Hooks |
|----------|-----|-----------|-----------------|----------|
| 1. What you do | x | x | x | x |
| 2. Best client | **PRIMARY** | | who's it for | |
| 3. Result | | x | headline + proof | x |
| 4. Process | | **PRIMARY** | tease + mechanism | |
| 5. Differentiator | x | | | **PRIMARY** |
| 6. Story | | | **backstory** | x |
| 7. Pricing | | **PRIMARY** | price reveal | |
| 8. Stuck point | | x | push section | x |
| 9. Client language | x | | **benefits + future pacing** | **PRIMARY** |
| 10. Failed solutions | | x | **counterintuitive tease** | x |
| 11. Objections | | **PRIMARY** | push / not for | x |
| Optional: Content | voice | voice | voice | voice |

**Two more deliverables draw from the same answers** (map above covers the original four):

- **Sales Page (cold landing):** same inputs as the Google Offer Doc — Q8/Q9 for the problem, Q10 for "why the usual fixes fail," Q4 for the mechanism, Q5/Q6 for the About section, Q11 for the FAQ. More trust-building and proof than the warm doc.
- **Email Sequence (5 emails):** Q6 (story), Q10 (common mistake), Q3 (social proof), Q11 (objection handling in the pitch email), Q9 (client language throughout).

---

## Automation

- Form is sent immediately after DFY purchase (GHL automation)
- Submission triggers webhook → Claude API → raw output
- Michael reviews within 48 hours
- See `outputs/dfy-upsell/system-prompt.md` for API spec and generation prompt
- See `outputs/products/internal/dfy-offer-build-process.md` for full end-to-end workflow
