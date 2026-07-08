// Before / After split card.
// data: { title, before: {lines:[...]}, after: {lines:[...]}, footer }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const col = (label, lines, opts) => `
    <div style="flex:1;padding:70px 52px;background:${opts.bg};color:${opts.fg};display:flex;flex-direction:column">
      <div style="font:800 40px ${brand.fontUI};letter-spacing:3px;color:${opts.label};margin-bottom:34px">${esc(label)}</div>
      ${(lines || []).map((l) => `<p style="margin:0 0 24px;font:500 44px/1.34 ${brand.fontUI}">${esc(l)}</p>`).join("")}
    </div>`;

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;font-family:${brand.fontUI};display:flex;flex-direction:column}
    .title{text-align:center;font:800 62px/1.15 ${brand.fontDisplay};color:${brand.ink};background:${brand.bg};padding:56px 60px 40px}
    .cols{flex:1;display:flex}
    .footer{text-align:center;font:700 42px ${brand.fontUI};color:${brand.accent};background:${brand.ink};padding:44px}
  </style></head><body>
    <div class="ad">
      ${data.title ? `<div class="title">${esc(data.title)}</div>` : ""}
      <div class="cols">
        ${col("BEFORE", (data.before || {}).lines, { bg: "#E7E3DA", fg: "#4A4A46", label: "#9A948A" })}
        ${col("AFTER", (data.after || {}).lines, { bg: brand.ink, fg: "#EDEBE6", label: brand.accent })}
      </div>
      ${data.footer ? `<div class="footer">${esc(data.footer)}</div>` : ""}
    </div>
  </body></html>`;
}
