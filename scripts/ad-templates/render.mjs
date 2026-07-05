#!/usr/bin/env node
/**
 * Ad-template renderer for Client Ready.
 *
 * Renders text-exact ad creative (HTML/CSS -> PNG via the installed Chrome) that
 * fal.ai/Flux cannot produce — the native screenshot & value-stack formats that
 * are Miles Stutz's oldest / highest-impression winners.
 * See research/2026-07-05-miles-creative-oldest-winners.md.
 *
 * Usage:
 *   node scripts/ad-templates/render.mjs --list
 *   node scripts/ad-templates/render.mjs --template imessage --preset one-afternoon
 *   node scripts/ad-templates/render.mjs --template order-summary --preset front-end-27
 *   node scripts/ad-templates/render.mjs --template imessage --preset all
 *   node scripts/ad-templates/render.mjs --template imessage --data '{"contact":"Pat","messages":[...]}'
 *
 * Options:
 *   --template  imessage | order-summary   (required)
 *   --preset    preset key from content.json, or "all"
 *   --data      inline JSON, merged over the preset
 *   --size      WxH (default 1080x1350, the 4:5 Meta feed size)
 *   --out       output dir (default outputs/ad-creative)
 */

import { chromium } from "playwright-core";
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(HERE, "..", "..");
const CONTENT = JSON.parse(readFileSync(join(HERE, "content.json"), "utf8"));

function parseArgs(argv) {
  const a = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) {
      const k = argv[i].slice(2);
      const v = argv[i + 1] && !argv[i + 1].startsWith("--") ? argv[++i] : true;
      a[k] = v;
    }
  }
  return a;
}

function stamp() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}${p(d.getSeconds())}`;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.list || !args.template) {
    console.log("Templates & presets (scripts/ad-templates/content.json):\n");
    for (const [tpl, presets] of Object.entries(CONTENT)) {
      if (tpl.startsWith("_")) continue;
      console.log(`  ${tpl}`);
      for (const k of Object.keys(presets)) if (!k.startsWith("_")) console.log(`      - ${k}`);
    }
    if (!args.template) process.exit(args.list ? 0 : 1);
    return;
  }

  const tpl = args.template;
  const mod = await import(join(HERE, "templates", `${tpl}.mjs`));
  const [W, H] = String(args.size || "1080x1350").split("x").map(Number);
  const outDir = args.out ? String(args.out) : join(REPO_ROOT, "outputs", "ad-creative");
  mkdirSync(outDir, { recursive: true });

  // Build the job list.
  const presets = CONTENT[tpl] || {};
  let jobs = [];
  if (args.data) {
    jobs.push({ key: args.preset || "custom", data: JSON.parse(args.data) });
  } else if (args.preset === "all") {
    jobs = Object.keys(presets).filter((k) => !k.startsWith("_")).map((k) => ({ key: k, data: presets[k] }));
  } else if (args.preset && presets[args.preset]) {
    jobs.push({ key: args.preset, data: presets[args.preset] });
  } else {
    console.error(`Unknown preset '${args.preset}' for '${tpl}'. Try --list.`);
    process.exit(1);
  }

  const browser = await chromium.launch({ channel: "chrome" });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });

  const s = stamp();
  const saved = [];
  for (const job of jobs) {
    const html = mod.render(job.data, W, H);
    await page.setContent(html, { waitUntil: "networkidle" });
    const el = await page.$(".ad");
    const dest = join(outDir, `${s}-${tpl}-${job.key}.png`);
    await el.screenshot({ path: dest });
    const rel = dest.replace(REPO_ROOT + "/", "");
    saved.push(rel);
    console.log(`  saved ${rel}`);

    writeFileSync(dest.replace(/\.png$/, ".json"), JSON.stringify({
      template: tpl, preset: job.key, size: `${W}x${H}`,
      data: job.data, generated_at: s,
    }, null, 2));
  }
  await browser.close();
  console.log(`Done. ${saved.length} image(s) in outputs/ad-creative/`);
}

main().catch((e) => { console.error(e); process.exit(1); });
