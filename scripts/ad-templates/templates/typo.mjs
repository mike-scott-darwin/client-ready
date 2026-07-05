// Bold typographic card — mirrors Miles's "You're not bad at sales..." winner.
// Mass-produces from one-liners. Accent segments wrapped in *asterisks*.
// data: { headline: "You can't *grow into pain.*", subline, accentColor }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

// Split on * pairs; odd-index segments render in the accent color.
function markup(str, accent) {
  return String(str)
    .split("*")
    .map((seg, i) => (i % 2 ? `<span style="color:${accent}">${esc(seg)}</span>` : esc(seg)))
    .join("");
}

export function render(data, W, H) {
  const accent = data.accentColor || brand.accent;
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:${brand.bg};font-family:${brand.fontDisplay};
      display:flex;flex-direction:column;align-items:center;justify-content:center;
      text-align:center;padding:110px 90px}
    .headline{font:800 128px/1.12 ${brand.fontDisplay};letter-spacing:-3px;color:${brand.ink}}
    .rule{width:120px;height:5px;background:${brand.ink};opacity:.25;margin:56px 0 40px;border-radius:3px}
    .subline{font:700 46px ${brand.fontUI};color:${brand.ink}}
  </style></head><body>
    <div class="ad">
      <div class="headline">${markup(data.headline || "", accent)}</div>
      ${data.subline ? `<div class="rule"></div><div class="subline">${esc(data.subline)}</div>` : ""}
    </div>
  </body></html>`;
}
