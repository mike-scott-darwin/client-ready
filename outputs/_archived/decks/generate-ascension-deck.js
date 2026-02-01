const pptxgen = require('pptxgenjs');

// Sensible defaults - professional dark theme
const COLORS = {
  bgPrimary: "0f172a",     // Dark navy
  bgSecondary: "1e293b",   // Lighter navy
  textPrimary: "f8fafc",   // Off-white
  textMuted: "94a3b8",     // Muted gray
  accent1: "22c55e",       // Green (money/success)
  accent2: "3b82f6",       // Blue
  accent3: "f59e0b",       // Amber
  accent4: "ef4444",       // Red
  white: "ffffff"
};

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_16x9';
pptx.title = 'Client Ready Offer System - Ascension Model';
pptx.author = 'Michael';

// Helper to add consistent footer
function addFooter(slide, pageNum, total) {
  slide.addText(`${pageNum}/${total}`, {
    x: 9.3, y: 5.2, w: 0.5, h: 0.3,
    fontSize: 10, color: COLORS.textMuted, align: 'right'
  });
}

// ============ SLIDE 1: TITLE ============
const slide1 = pptx.addSlide();
slide1.background = { color: COLORS.bgPrimary };
slide1.addText('Client Ready Offer System', {
  x: 0.5, y: 1.8, w: 9, h: 1,
  fontSize: 48, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});
slide1.addText('The Ascension Model', {
  x: 0.5, y: 2.8, w: 9, h: 0.6,
  fontSize: 28, color: COLORS.accent1,
  fontFace: 'Arial'
});
slide1.addText('From $27 Low-Ticket to $5K+ High-Ticket', {
  x: 0.5, y: 3.6, w: 9, h: 0.5,
  fontSize: 18, color: COLORS.textMuted,
  fontFace: 'Arial'
});
addFooter(slide1, 1, 10);

// ============ SLIDE 2: THE PROBLEM ============
const slide2 = pptx.addSlide();
slide2.background = { color: COLORS.bgPrimary };
slide2.addText('The Problem', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});
slide2.addText([
  { text: 'Coaches are stuck:', options: { bold: true, color: COLORS.accent3 } },
  { text: '\n\n' },
  { text: '"I help everyone with everything"', options: { color: COLORS.textMuted, italic: true } },
  { text: '\n\n' },
  { text: 'No validated offer', options: { bullet: true, color: COLORS.textPrimary } },
  { text: '\n' },
  { text: 'No clear pricing', options: { bullet: true, color: COLORS.textPrimary } },
  { text: '\n' },
  { text: 'No path to high-ticket clients', options: { bullet: true, color: COLORS.textPrimary } },
  { text: '\n' },
  { text: 'Wondering: "Will anyone pay for this?"', options: { bullet: true, color: COLORS.textPrimary } }
], {
  x: 0.5, y: 1.3, w: 8.5, h: 3.5,
  fontSize: 20, color: COLORS.textPrimary,
  fontFace: 'Arial', valign: 'top'
});
addFooter(slide2, 2, 10);

// ============ SLIDE 3: VALUE LADDER OVERVIEW ============
const slide3 = pptx.addSlide();
slide3.background = { color: COLORS.bgPrimary };
slide3.addText('The Value Ladder', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

// Visual ladder boxes
const tiers = [
  { label: '$5K+', name: '1:1 Build', y: 1.2, color: COLORS.accent1 },
  { label: '$397', name: 'Done-For-You', y: 2.0, color: COLORS.accent2 },
  { label: '$97-297', name: 'Sprint', y: 2.8, color: COLORS.accent3 },
  { label: '$27+bumps', name: 'Front-End', y: 3.6, color: COLORS.accent4 }
];

tiers.forEach((tier, i) => {
  const width = 3 + (i * 0.8);
  slide3.addShape(pptx.shapes.RECTANGLE, {
    x: 0.5, y: tier.y, w: width, h: 0.65,
    fill: { color: tier.color }, line: { color: tier.color }
  });
  slide3.addText(`${tier.label}  ${tier.name}`, {
    x: 0.6, y: tier.y + 0.12, w: width - 0.2, h: 0.4,
    fontSize: 16, bold: true, color: COLORS.white,
    fontFace: 'Arial'
  });
});

slide3.addText('Low commitment entry\nHigh value ascension', {
  x: 6, y: 2.2, w: 3.5, h: 1.5,
  fontSize: 18, color: COLORS.textMuted, align: 'center',
  fontFace: 'Arial'
});
addFooter(slide3, 3, 10);

// ============ SLIDE 4: TIER 1 - FRONT END ============
const slide4 = pptx.addSlide();
slide4.background = { color: COLORS.bgPrimary };
slide4.addText('Tier 1: Front-End Entry', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

slide4.addShape(pptx.shapes.RECTANGLE, {
  x: 0.5, y: 1.2, w: 4.2, h: 2.2,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent1, pt: 2 }
});
slide4.addText('$27 - Client Ready Offer System', {
  x: 0.6, y: 1.3, w: 4, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.accent1, fontFace: 'Arial'
});
slide4.addText([
  { text: 'PDF guide + 5 AI prompts', options: { bullet: true } },
  { text: '\n' },
  { text: 'Offer document template', options: { bullet: true } },
  { text: '\n' },
  { text: 'Validate offer in one afternoon', options: { bullet: true } }
], {
  x: 0.6, y: 1.8, w: 4, h: 1.5,
  fontSize: 14, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide4.addShape(pptx.shapes.RECTANGLE, {
  x: 5, y: 1.2, w: 4.5, h: 2.2,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent3, pt: 2 }
});
slide4.addText('Order Bumps', {
  x: 5.1, y: 1.3, w: 4.3, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.accent3, fontFace: 'Arial'
});
slide4.addText([
  { text: '$47 - 24-Hour Launch Kit', options: { bullet: true } },
  { text: '\n' },
  { text: '$37 - Plug & Play Funnel Pack', options: { bullet: true } },
  { text: '\n\n' },
  { text: 'Target: 30% bump rate', options: { color: COLORS.textMuted } }
], {
  x: 5.1, y: 1.8, w: 4.3, h: 1.5,
  fontSize: 14, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide4.addText('Max front-end cart: $111', {
  x: 0.5, y: 3.6, w: 9, h: 0.4,
  fontSize: 18, color: COLORS.textMuted, fontFace: 'Arial'
});
addFooter(slide4, 4, 10);

// ============ SLIDE 5: OTO 1 - SPRINT ============
const slide5 = pptx.addSlide();
slide5.background = { color: COLORS.bgPrimary };
slide5.addText('OTO 1: The Client Ready Sprint', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

// Two columns for options
slide5.addShape(pptx.shapes.RECTANGLE, {
  x: 0.5, y: 1.2, w: 4.2, h: 3.2,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent2, pt: 2 }
});
slide5.addText('Self-Paced: $97', {
  x: 0.6, y: 1.3, w: 4, h: 0.4,
  fontSize: 18, bold: true, color: COLORS.accent2, fontFace: 'Arial'
});
slide5.addText([
  { text: 'Complete funnel system', options: { bullet: true } },
  { text: '\n' },
  { text: 'Unfair Advantage Framework', options: { bullet: true } },
  { text: '\n' },
  { text: 'AI Landing Page Generator', options: { bullet: true } },
  { text: '\n' },
  { text: 'Traffic Playbook', options: { bullet: true } },
  { text: '\n' },
  { text: 'Skool Community Access', options: { bullet: true } }
], {
  x: 0.6, y: 1.8, w: 4, h: 2.5,
  fontSize: 13, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide5.addShape(pptx.shapes.RECTANGLE, {
  x: 5, y: 1.2, w: 4.5, h: 3.2,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent1, pt: 2 }
});
slide5.addText('4-Week Sprint: $297', {
  x: 5.1, y: 1.3, w: 4.3, h: 0.4,
  fontSize: 18, bold: true, color: COLORS.accent1, fontFace: 'Arial'
});
slide5.addText([
  { text: 'Everything in Self-Paced PLUS:', options: { bullet: true, bold: true } },
  { text: '\n' },
  { text: 'Weekly group calls (4 sessions)', options: { bullet: true } },
  { text: '\n' },
  { text: 'Direct chat access', options: { bullet: true } },
  { text: '\n' },
  { text: 'Accountability check-ins', options: { bullet: true } },
  { text: '\n' },
  { text: 'Hot seat feedback', options: { bullet: true } },
  { text: '\n\n' },
  { text: 'Launch in 30 days or keep working', options: { color: COLORS.accent1, italic: true } }
], {
  x: 5.1, y: 1.8, w: 4.3, h: 2.5,
  fontSize: 13, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide5.addText('Target: 10-15% conversion', {
  x: 0.5, y: 4.5, w: 9, h: 0.4,
  fontSize: 16, color: COLORS.textMuted, fontFace: 'Arial'
});
addFooter(slide5, 5, 10);

// ============ SLIDE 6: OTO 2 - DFY ============
const slide6 = pptx.addSlide();
slide6.background = { color: COLORS.bgPrimary };
slide6.addText('OTO 2: Done-For-You Funnel', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

slide6.addText('$397 one-time', {
  x: 0.5, y: 1.1, w: 4, h: 0.5,
  fontSize: 28, bold: true, color: COLORS.accent1, fontFace: 'Arial'
});
slide6.addText('10 spots/month (real scarcity)', {
  x: 4.5, y: 1.15, w: 5, h: 0.4,
  fontSize: 16, color: COLORS.accent4, fontFace: 'Arial'
});

slide6.addText([
  { text: 'Complete Client Funnel Blueprint', options: { bullet: true } },
  { text: '\n' },
  { text: '1-on-1 Integration Call', options: { bullet: true } },
  { text: '\n' },
  { text: 'Complete Copy Pack (Ads, Emails, Sales Pages)', options: { bullet: true } },
  { text: '\n' },
  { text: 'Market Research & ICP Analysis', options: { bullet: true } },
  { text: '\n' },
  { text: '100+ page custom bundle', options: { bullet: true } }
], {
  x: 0.5, y: 1.7, w: 5, h: 2.2,
  fontSize: 16, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide6.addShape(pptx.shapes.RECTANGLE, {
  x: 5.5, y: 1.7, w: 4, h: 2.5,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent1, pt: 2 }
});
slide6.addText('Timeline', {
  x: 5.6, y: 1.8, w: 3.8, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.accent1, fontFace: 'Arial'
});
slide6.addText([
  { text: 'Day 1-3: Onboarding', options: { bullet: true } },
  { text: '\n' },
  { text: 'Week 1-2: Build', options: { bullet: true } },
  { text: '\n' },
  { text: 'Week 3: Delivery', options: { bullet: true } },
  { text: '\n' },
  { text: 'Week 4: Integration + Launch', options: { bullet: true } }
], {
  x: 5.6, y: 2.3, w: 3.8, h: 1.8,
  fontSize: 14, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide6.addText('Guarantee: 100 customers or I keep working with you', {
  x: 0.5, y: 4.3, w: 9, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.accent3, fontFace: 'Arial'
});
addFooter(slide6, 6, 10);

// ============ SLIDE 7: BACKEND HIGH-TICKET ============
const slide7 = pptx.addSlide();
slide7.background = { color: COLORS.bgPrimary };
slide7.addText('Backend: 1:1 Funnel Build', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

slide7.addText('$5,000+', {
  x: 0.5, y: 1.2, w: 4, h: 0.7,
  fontSize: 48, bold: true, color: COLORS.accent1, fontFace: 'Arial'
});

slide7.addText([
  { text: 'For buyers who want maximum support:', options: { bold: true, color: COLORS.accent2 } },
  { text: '\n\n' },
  { text: 'Complete funnel built by Michael', options: { bullet: true } },
  { text: '\n' },
  { text: 'Offer extraction and refinement', options: { bullet: true } },
  { text: '\n' },
  { text: 'Funnel installation', options: { bullet: true } },
  { text: '\n' },
  { text: 'Traffic and scaling strategy', options: { bullet: true } }
], {
  x: 0.5, y: 2.0, w: 5, h: 2.5,
  fontSize: 18, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide7.addShape(pptx.shapes.RECTANGLE, {
  x: 5.5, y: 2.0, w: 4, h: 2.0,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent3, pt: 2 }
});
slide7.addText('Qualification', {
  x: 5.6, y: 2.1, w: 3.8, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.accent3, fontFace: 'Arial'
});
slide7.addText([
  { text: 'Application required', options: { bullet: true } },
  { text: '\n' },
  { text: 'Call to assess fit', options: { bullet: true } },
  { text: '\n' },
  { text: 'Validated offer (or close)', options: { bullet: true } },
  { text: '\n' },
  { text: 'Ready to invest', options: { bullet: true } }
], {
  x: 5.6, y: 2.6, w: 3.8, h: 1.4,
  fontSize: 14, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});

slide7.addText('Primary high-ticket revenue driver', {
  x: 0.5, y: 4.5, w: 9, h: 0.4,
  fontSize: 16, color: COLORS.textMuted, fontFace: 'Arial'
});
addFooter(slide7, 7, 10);

// ============ SLIDE 8: FUNNEL FLOW ============
const slide8 = pptx.addSlide();
slide8.background = { color: COLORS.bgPrimary };
slide8.addText('The Funnel Flow', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

// Flow boxes
const flowSteps = [
  { label: 'Awareness', sub: 'Ads / Content', x: 0.3, color: COLORS.textMuted },
  { label: '$27', sub: 'Front-End', x: 1.7, color: COLORS.accent4 },
  { label: '+$84', sub: 'Bumps', x: 3.1, color: COLORS.accent3 },
  { label: '$97-297', sub: 'Sprint', x: 4.5, color: COLORS.accent2 },
  { label: '$397', sub: 'DFY', x: 5.9, color: COLORS.accent2 },
  { label: 'Community', sub: 'Engagement', x: 7.3, color: COLORS.textMuted },
  { label: '$5K+', sub: '1:1', x: 8.7, color: COLORS.accent1 }
];

flowSteps.forEach((step) => {
  slide8.addShape(pptx.shapes.RECTANGLE, {
    x: step.x, y: 1.5, w: 1.2, h: 0.9,
    fill: { color: COLORS.bgSecondary }, line: { color: step.color, pt: 2 }
  });
  slide8.addText(step.label, {
    x: step.x, y: 1.55, w: 1.2, h: 0.45,
    fontSize: 12, bold: true, color: step.color, align: 'center', fontFace: 'Arial'
  });
  slide8.addText(step.sub, {
    x: step.x, y: 1.95, w: 1.2, h: 0.35,
    fontSize: 9, color: COLORS.textMuted, align: 'center', fontFace: 'Arial'
  });
});

// Arrows between boxes
for (let i = 0; i < flowSteps.length - 1; i++) {
  slide8.addShape(pptx.shapes.RIGHT_ARROW, {
    x: flowSteps[i].x + 1.2, y: 1.8, w: 0.35, h: 0.3,
    fill: { color: COLORS.textMuted }
  });
}

slide8.addText('Engagement builds trust. Trust enables high-ticket.', {
  x: 0.5, y: 2.7, w: 9, h: 0.5,
  fontSize: 18, color: COLORS.textMuted, italic: true, fontFace: 'Arial'
});

// Key metrics below
slide8.addText('Target Metrics:', {
  x: 0.5, y: 3.4, w: 2, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.textPrimary, fontFace: 'Arial'
});
slide8.addText([
  { text: 'Bump rate: 30%', options: { bullet: true } },
  { text: '     ' },
  { text: 'OTO 1: 10-15%', options: { bullet: true } },
  { text: '     ' },
  { text: 'OTO 2: 5-10%', options: { bullet: true } },
  { text: '     ' },
  { text: 'HT close: 20-30%', options: { bullet: true } }
], {
  x: 0.5, y: 3.8, w: 9, h: 0.8,
  fontSize: 14, color: COLORS.textPrimary, fontFace: 'Arial'
});
addFooter(slide8, 8, 10);

// ============ SLIDE 9: ECONOMICS ============
const slide9 = pptx.addSlide();
slide9.background = { color: COLORS.bgPrimary };
slide9.addText('Funnel Economics', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

// Table data
const tableData = [
  ['Step', 'Price', 'Type'],
  ['Front-end', '$27', 'One-time'],
  ['Bump 1', '$47', 'One-time'],
  ['Bump 2', '$37', 'One-time'],
  ['OTO 1 (Self)', '$97', 'One-time'],
  ['OTO 1 (Sprint)', '$297', 'One-time'],
  ['OTO 2', '$397', 'One-time'],
  ['Backend', '$5K+', 'High-ticket']
];

slide9.addTable(tableData, {
  x: 0.5, y: 1.1, w: 5.5,
  fontFace: 'Arial',
  fontSize: 14,
  color: COLORS.textPrimary,
  border: { pt: 1, color: COLORS.bgSecondary },
  fill: { color: COLORS.bgSecondary },
  colW: [2, 1.5, 2],
  rowH: 0.4,
  align: 'left',
  valign: 'middle'
});

slide9.addShape(pptx.shapes.RECTANGLE, {
  x: 6.3, y: 1.1, w: 3.2, h: 2.8,
  fill: { color: COLORS.bgSecondary }, line: { color: COLORS.accent1, pt: 2 }
});
slide9.addText('Key Numbers', {
  x: 6.4, y: 1.2, w: 3, h: 0.4,
  fontSize: 16, bold: true, color: COLORS.accent1, fontFace: 'Arial'
});
slide9.addText([
  { text: 'Max cart: $805', options: { bullet: true } },
  { text: '\n' },
  { text: 'Target AOV: $100-180', options: { bullet: true } },
  { text: '\n' },
  { text: 'CAC < AOV goal', options: { bullet: true } },
  { text: '\n' },
  { text: 'No subscriptions', options: { bullet: true } }
], {
  x: 6.4, y: 1.7, w: 3, h: 2,
  fontSize: 14, color: COLORS.textPrimary, fontFace: 'Arial', valign: 'top'
});
addFooter(slide9, 9, 10);

// ============ SLIDE 10: SUMMARY ============
const slide10 = pptx.addSlide();
slide10.background = { color: COLORS.bgPrimary };
slide10.addText('The Client Ready Method', {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontSize: 36, bold: true, color: COLORS.textPrimary,
  fontFace: 'Arial'
});

const steps = [
  { num: '1', title: 'EXTRACT', desc: 'Pull out your unfair advantage' },
  { num: '2', title: 'VALIDATE', desc: 'Test with real buyers first' },
  { num: '3', title: 'BUILD', desc: 'Install the 24-hour funnel' },
  { num: '4', title: 'SCALE', desc: 'Traffic playbook to $5K+ clients' }
];

steps.forEach((step, i) => {
  const yPos = 1.2 + (i * 0.85);
  slide10.addShape(pptx.shapes.OVAL, {
    x: 0.5, y: yPos, w: 0.5, h: 0.5,
    fill: { color: COLORS.accent1 }
  });
  slide10.addText(step.num, {
    x: 0.5, y: yPos + 0.08, w: 0.5, h: 0.35,
    fontSize: 18, bold: true, color: COLORS.white, align: 'center', fontFace: 'Arial'
  });
  slide10.addText(step.title, {
    x: 1.2, y: yPos + 0.05, w: 2, h: 0.4,
    fontSize: 18, bold: true, color: COLORS.accent1, fontFace: 'Arial'
  });
  slide10.addText(step.desc, {
    x: 3.2, y: yPos + 0.08, w: 6, h: 0.4,
    fontSize: 16, color: COLORS.textPrimary, fontFace: 'Arial'
  });
});

slide10.addText('"You can\'t grow into pain" — Offer must align with what you actually do well', {
  x: 0.5, y: 4.7, w: 9, h: 0.4,
  fontSize: 14, color: COLORS.textMuted, italic: true, fontFace: 'Arial'
});
addFooter(slide10, 10, 10);

// Generate the file
pptx.writeFile({ fileName: 'client-ready-ascension-model.pptx' })
  .then(() => console.log('Created: client-ready-ascension-model.pptx'))
  .catch(err => console.error(err));
