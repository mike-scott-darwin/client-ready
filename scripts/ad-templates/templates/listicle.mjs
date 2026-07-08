// Numbered listicle card — "5 signs..." format.
// data: { title, subtitle, items: [...], closer }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
// Accent segments wrapped in *asterisks*.
const markup = (str) => String(str)
  .split("*")
  .map((seg, i) => (i % 2 ? `<b style="color:${brand.accent}">${esc(seg)}</b>` : esc(seg)))
  .join("");

export function render(data, W, H) {
  const items = (data.items || [])
    .map((it, i) => `
      <div style="display:flex;align-items:flex-start;gap:28px;padding:22px 0;border-bottom:1px solid ${brand.line}">
        <div style="flex:none;width:66px;height:66px;border-radius:50%;background:${brand.accent};color:#fff;
          display:flex;align-items:center;justify-content:center;font:800 38px ${brand.fontUI}">${i + 1}</div>
        <div style="flex:1;font:600 42px/1.3 ${brand.fontUI};color:${brand.ink};padding-top:6px">${esc(it)}</div>
      </div>`)
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:${brand.bg};font-family:${brand.fontUI};color:${brand.ink};padding:70px 66px;display:flex;flex-direction:column;justify-content:center}
    .title{font:800 72px/1.12 ${brand.fontDisplay};letter-spacing:-1px}
    .subtitle{font:500 40px ${brand.fontUI};color:${brand.inkSoft};margin:14px 0 30px}
    .closer{font:800 46px/1.25 ${brand.fontDisplay};color:${brand.ink};margin-top:34px}
    .closer b{color:${brand.accent}}
  </style></head><body>
    <div class="ad">
      <div class="title">${esc(data.title || "")}</div>
      ${data.subtitle ? `<div class="subtitle">${esc(data.subtitle)}</div>` : ""}
      <div>${items}</div>
      ${data.closer ? `<div class="closer">${markup(data.closer)}</div>` : ""}
    </div>
  </body></html>`;
}
