// "Breaking News" tabloid mockup — mirrors Miles's red-banner winner, FTC-safe:
// validation/clarity claims, never income claims.
// data: { banner, headline, bullets:[...], sub, cta }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const bullets = (data.bullets || [])
    .map((b) => `<div style="display:flex;align-items:flex-start;gap:20px;margin:14px 0">
        <span style="color:#1DB954;font-size:56px;line-height:1;flex:none">✅</span>
        <span style="font:800 62px/1.12 ${brand.fontDisplay};color:#0B0B0B">${esc(b)}</span></div>`)
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#0C1A2B;font-family:${brand.fontDisplay};position:relative;overflow:hidden;display:flex;flex-direction:column}
    .banner{background:#E01E2B;margin:40px 40px 0;border-radius:14px;padding:34px 40px;text-align:center}
    .banner .kick{color:#fff;font:800 44px ${brand.fontDisplay};letter-spacing:2px;opacity:.9}
    .banner .head{color:#fff;font:800 82px/1.06 ${brand.fontDisplay};letter-spacing:-2px;margin-top:8px;text-shadow:3px 3px 0 rgba(0,0,0,.25)}
    .whiteband{background:#fff;margin:26px 40px 0;border-radius:14px;padding:44px 46px}
    .sub{color:#fff;text-align:center;font:800 60px/1.15 ${brand.fontDisplay};padding:36px 60px 0}
    .ctawrap{margin-top:auto;padding:40px}
    .cta{background:#FFE24A;border-radius:16px;padding:38px;text-align:center;font:800 66px ${brand.fontDisplay};color:#0B0B0B}
    .adv{position:absolute;bottom:16px;right:34px;color:#8A97A6;font:600 26px ${brand.fontUI};letter-spacing:2px}
  </style></head><body>
    <div class="ad">
      <div class="banner">
        <div class="kick">${esc(data.banner || "NEW")}</div>
        <div class="head">${esc(data.headline || "")}</div>
      </div>
      <div class="whiteband">${bullets}</div>
      ${data.sub ? `<div class="sub">${esc(data.sub)}</div>` : ""}
      <div class="ctawrap"><div class="cta">${esc(data.cta || "See how →")}</div></div>
      <div class="adv">ADVERTISEMENT</div>
    </div>
  </body></html>`;
}
