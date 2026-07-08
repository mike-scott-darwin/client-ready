// Quote card — big pull-quote with attribution.
// data: { quote, author, role }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:${brand.ink};font-family:${brand.fontDisplay};
      display:flex;flex-direction:column;justify-content:center;padding:110px 92px;color:#EDEBE6}
    .mark{font:800 200px/0.7 Georgia,serif;color:${brand.accent};margin-bottom:24px}
    .quote{font:800 76px/1.22 ${brand.fontDisplay};letter-spacing:-1px}
    .rule{width:110px;height:5px;background:${brand.accent};margin:52px 0 32px;border-radius:3px}
    .author{font:800 46px ${brand.fontUI};color:#fff}
    .role{font:500 38px ${brand.fontUI};color:#A7AFA9;margin-top:6px}
  </style></head><body>
    <div class="ad">
      <div class="mark">&ldquo;</div>
      <div class="quote">${esc(data.quote || "")}</div>
      <div class="rule"></div>
      <div class="author">${esc(data.author || "")}</div>
      ${data.role ? `<div class="role">${esc(data.role)}</div>` : ""}
    </div>
  </body></html>`;
}
