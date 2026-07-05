// iMessage conversation mockup — mirrors Miles Stutz's #1 (oldest, highest-impression) winner.
// Native "text from a friend" format. Renders our copy with pixel-exact iOS chrome.
// data: { time, contact, messages: [{from:'them'|'me', text}] }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const time = data.time || "9:41";
  const contact = data.contact || "Alex";
  const initial = esc(contact.trim()[0] || "•").toUpperCase();
  const bubbles = (data.messages || [])
    .map((m) => {
      const me = m.from === "me";
      const bg = me ? brand.imessageBlue : brand.imessageGray;
      const color = me ? "#fff" : "#000";
      const align = me ? "flex-end" : "flex-start";
      const radius = me
        ? "26px 26px 8px 26px"
        : "26px 26px 26px 8px";
      return `
        <div style="display:flex;justify-content:${align};margin:10px 0;">
          <div style="max-width:74%;background:${bg};color:${color};
            font:400 40px/1.28 ${brand.fontUI};padding:20px 28px;border-radius:${radius};
            box-shadow:0 1px 1px rgba(0,0,0,.05);">${esc(m.text)}</div>
        </div>`;
    })
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#fff;position:relative;overflow:hidden;font-family:${brand.fontUI}}
    .statusbar{display:flex;justify-content:space-between;align-items:center;padding:26px 44px 6px;font:600 34px ${brand.fontUI}}
    .statusbar .icons{display:flex;align-items:center;gap:12px}
    .header{display:flex;flex-direction:column;align-items:center;padding:6px 0 20px;border-bottom:1px solid #ECECEC;position:relative}
    .chev{position:absolute;left:34px;top:14px;color:${brand.imessageBlue};font-size:56px;font-weight:300}
    .avatar{width:118px;height:118px;border-radius:50%;background:#C7C7CC;color:#fff;
      display:flex;align-items:center;justify-content:center;font:600 56px ${brand.fontUI};margin-bottom:10px}
    .name{font:600 32px ${brand.fontUI};color:#000}
    .thread{padding:26px 34px}
    .inputbar{position:absolute;bottom:0;left:0;right:0;display:flex;align-items:center;gap:22px;
      padding:22px 34px 40px;border-top:1px solid #ECECEC;background:#fff}
    .plus{width:56px;height:56px;border-radius:50%;background:#E9E9EB;color:#8E8E93;
      display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:300}
    .field{flex:1;height:64px;border:2px solid #D1D1D6;border-radius:32px;
      display:flex;align-items:center;padding:0 26px;color:#B0B0B5;font:400 34px ${brand.fontUI}}
  </style></head><body>
    <div class="ad">
      <div class="statusbar">
        <div>${esc(time)}</div>
        <div class="icons">
          <svg width="42" height="30" viewBox="0 0 42 30"><g fill="#000">
            <rect x="0" y="20" width="7" height="9" rx="2"/><rect x="10" y="14" width="7" height="15" rx="2"/>
            <rect x="20" y="8" width="7" height="21" rx="2"/><rect x="30" y="2" width="7" height="27" rx="2"/></g></svg>
          <svg width="40" height="30" viewBox="0 0 40 30" fill="#000"><path d="M20 6c7 0 13 3 17 7l-4 4c-3-3-8-5-13-5s-10 2-13 5L3 13c4-4 10-7 17-7z"/><path d="M20 15c4 0 7 1 9 3l-9 9-9-9c2-2 5-3 9-3z"/></svg>
          <svg width="58" height="30" viewBox="0 0 58 30"><rect x="1" y="5" width="46" height="20" rx="6" fill="none" stroke="#000" stroke-width="3"/><rect x="5" y="9" width="38" height="12" rx="3" fill="#000"/><rect x="50" y="11" width="4" height="8" rx="2" fill="#000"/></svg>
        </div>
      </div>
      <div class="header">
        <div class="chev">‹</div>
        <div class="avatar">${initial}</div>
        <div class="name">${esc(contact)}</div>
      </div>
      <div class="thread">${bubbles}</div>
      <div class="inputbar">
        <div class="plus">+</div>
        <div class="field">iMessage</div>
      </div>
    </div>
  </body></html>`;
}
