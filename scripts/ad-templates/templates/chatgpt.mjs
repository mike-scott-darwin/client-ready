// Fake ChatGPT screenshot — mirrors Miles's "ChatGPT answering the prospect's question" winner.
// Rides AI-tool familiarity. data: { model, question, answerHeading, answerBody: [para, ...] }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const model = data.model || "5.4";
  const body = (data.answerBody || [])
    .map((p) => `<p style="margin:0 0 30px;font:400 42px/1.42 ${brand.fontUI};color:#0D0D0D">${esc(p)}</p>`)
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#fff;position:relative;overflow:hidden;font-family:${brand.fontUI};color:#0D0D0D}
    .topbar{display:flex;align-items:center;justify-content:space-between;padding:40px 44px 20px}
    .brandmark{display:flex;align-items:center;gap:14px;font:700 46px ${brand.fontUI}}
    .brandmark .model{font-weight:400;color:#8E8E8E}
    .chev{color:#8E8E8E;font-size:30px;margin-left:2px}
    .topright{display:flex;align-items:center;gap:22px}
    .share{border:2px solid #E0E0E0;border-radius:26px;padding:12px 28px;font:500 32px ${brand.fontUI};color:#0D0D0D}
    .dots{width:60px;height:60px;border:2px solid #E0E0E0;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:40px;color:#0D0D0D;letter-spacing:2px}
    .body{padding:30px 48px}
    .qrow{display:flex;justify-content:flex-end;margin:24px 0 56px}
    .q{max-width:74%;background:#F4F4F4;border-radius:34px;padding:26px 34px;font:400 42px/1.35 ${brand.fontUI}}
    .ansHead{font:700 46px/1.3 ${brand.fontUI};margin:0 0 30px}
    .icons{display:flex;gap:34px;margin-top:14px}
    .icons svg{stroke:#8E8E8E;fill:none;stroke-width:2}
    .inputbar{position:absolute;bottom:38px;left:48px;right:48px;height:104px;border:2px solid #E4E4E4;border-radius:52px;display:flex;align-items:center;padding:0 34px;gap:24px}
    .plus{font-size:52px;color:#0D0D0D;font-weight:300}
    .ask{flex:1;font:400 40px ${brand.fontUI};color:#9B9B9B}
    .mic{width:66px;height:66px;border-radius:50%;background:#0D0D0D;display:flex;align-items:center;justify-content:center}
    .foot{position:absolute;bottom:8px;left:0;right:0;text-align:center;font:400 26px ${brand.fontUI};color:#B0B0B0}
  </style></head><body>
    <div class="ad">
      <div class="topbar">
        <div class="brandmark">ChatGPT <span class="model">${esc(model)}</span><span class="chev">▾</span></div>
        <div class="topright">
          <div class="share">Share</div>
          <div class="dots">···</div>
        </div>
      </div>
      <div class="body">
        <div class="qrow"><div class="q">${esc(data.question || "")}</div></div>
        <div class="ansHead">${esc(data.answerHeading || "")}</div>
        ${body}
        <div class="icons">
          <svg width="40" height="40" viewBox="0 0 24 24"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h8"/></svg>
          <svg width="40" height="40" viewBox="0 0 24 24"><path d="M7 11v9H4v-9zM7 11l4-8a2 2 0 0 1 3 2l-1 6h6a2 2 0 0 1 2 2l-2 7H7"/></svg>
          <svg width="40" height="40" viewBox="0 0 24 24"><path d="M17 13V4h3v9zM17 13l-4 8a2 2 0 0 1-3-2l1-6H5a2 2 0 0 1-2-2l2-7h12"/></svg>
          <svg width="40" height="40" viewBox="0 0 24 24"><path d="M4 9v6h4l6 5V4L8 9zM18 8a5 5 0 0 1 0 8"/></svg>
          <svg width="40" height="40" viewBox="0 0 24 24"><path d="M21 12a9 9 0 1 1-3-6.7M21 4v5h-5"/></svg>
        </div>
      </div>
      <div class="inputbar">
        <div class="plus">+</div>
        <div class="ask">Ask anything</div>
        <div class="mic"><svg width="34" height="34" viewBox="0 0 24 24" fill="#fff"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M6 11a6 6 0 0 0 12 0M12 17v4" stroke="#fff" stroke-width="2" fill="none"/></svg></div>
      </div>
      <div class="foot">ChatGPT can make mistakes. Check important info.</div>
    </div>
  </body></html>`;
}
