// Reddit post mockup — native "someone figured this out" format.
// data: { subreddit, time, upvotes, comments, title, body: [para,...] }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const body = (data.body || [])
    .map((p) => `<p style="margin:0 0 26px;font:400 42px/1.4 ${brand.fontUI};color:#1A1A1B">${esc(p)}</p>`)
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#DAE0E6;font-family:${brand.fontUI};display:flex;align-items:center;justify-content:center;padding:56px}
    .card{width:100%;background:#fff;border-radius:20px;padding:52px 54px;box-shadow:0 6px 24px rgba(0,0,0,.10)}
    .head{display:flex;align-items:center;gap:18px;margin-bottom:26px}
    .sub-ic{width:64px;height:64px;border-radius:50%;background:#FF4500;color:#fff;display:flex;align-items:center;justify-content:center;font:800 34px ${brand.fontUI}}
    .sub{font:700 34px ${brand.fontUI};color:#1A1A1B}
    .meta{font:400 30px ${brand.fontUI};color:#7C7C7C}
    .title{font:800 58px/1.22 ${brand.fontUI};color:#1A1A1B;margin-bottom:28px}
    .foot{display:flex;align-items:center;gap:44px;margin-top:38px;color:#878A8C;font:700 34px ${brand.fontUI}}
    .pill{display:flex;align-items:center;gap:14px;background:#F6F7F8;border-radius:40px;padding:14px 26px}
  </style></head><body>
    <div class="ad"><div class="card">
      <div class="head">
        <div class="sub-ic">r/</div>
        <div>
          <div class="sub">r/${esc(data.subreddit || "coaching")}</div>
          <div class="meta">Posted by u/offer_engineer · ${esc(data.time || "6h")}</div>
        </div>
      </div>
      <div class="title">${esc(data.title || "")}</div>
      ${body}
      <div class="foot">
        <div class="pill">▲ &nbsp;${esc(String(data.upvotes ?? "3.4k"))}&nbsp; ▼</div>
        <div>💬 ${esc(String(data.comments ?? "212"))}</div>
        <div>↗ Share</div>
      </div>
    </div></div>
  </body></html>`;
}
