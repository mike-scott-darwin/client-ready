// Gmail inbox mockup — mirrors Miles's "stacked notifications" winner, but FTC-safe:
// clarity/validation moments (new buyer, community join, a DM), NOT fabricated income totals.
// data: { messages: [{sender, initial, color, subject, preview, time}] }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const rows = (data.messages || [])
    .map((m) => {
      const initial = esc((m.initial || m.sender || "•").trim()[0] || "•").toUpperCase();
      return `
      <div style="display:flex;align-items:flex-start;gap:26px;padding:26px 4px;border-bottom:1px solid #F0F0F0">
        <div style="flex:none;width:78px;height:78px;border-radius:50%;background:${m.color || "#5B6B66"};
          color:#fff;display:flex;align-items:center;justify-content:center;font:600 40px ${brand.fontUI}">${initial}</div>
        <div style="flex:1;min-width:0">
          <div style="display:flex;justify-content:space-between;align-items:baseline">
            <div style="font:700 40px ${brand.fontUI};color:#1F1F1F">${esc(m.sender || "")}</div>
            <div style="font:400 30px ${brand.fontUI};color:#5F6368;flex:none;margin-left:16px">${esc(m.time || "")}</div>
          </div>
          <div style="font:700 38px ${brand.fontUI};color:#1F1F1F;margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${esc(m.subject || "")}</div>
          <div style="font:400 36px ${brand.fontUI};color:#5F6368;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${esc(m.preview || "")}</div>
        </div>
        <div style="flex:none;color:#DADCE0;font-size:44px;margin-top:6px">☆</div>
      </div>`;
    })
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#fff;font-family:${brand.fontUI};color:#1F1F1F;overflow:hidden}
    .statusbar{display:flex;justify-content:space-between;align-items:center;padding:22px 40px 8px;font:600 30px ${brand.fontUI};color:#000}
    .search{margin:16px 34px 8px;height:96px;background:#F1F3F4;border-radius:48px;display:flex;align-items:center;padding:0 34px;gap:26px}
    .hamb{font-size:40px;color:#5F6368}
    .searchtxt{flex:1;font:400 38px ${brand.fontUI};color:#5F6368}
    .gemini{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#4285F4,#9B72CB,#D96570);opacity:.9}
    .avatar{width:60px;height:60px;border-radius:50%;background:${brand.accent};color:#fff;display:flex;align-items:center;justify-content:center;font:600 32px ${brand.fontUI}}
    .inbox{padding:18px 40px 6px;font:600 34px ${brand.fontUI};color:#5F6368}
    .list{padding:0 36px}
  </style></head><body>
    <div class="ad">
      <div class="statusbar"><div>9:41</div><div>▾ 🔋</div></div>
      <div class="search">
        <div class="hamb">≡</div>
        <div class="searchtxt">Search in mail</div>
        <div class="gemini"></div>
        <div class="avatar">M</div>
      </div>
      <div class="inbox">Inbox</div>
      <div class="list">${rows}</div>
    </div>
  </body></html>`;
}
