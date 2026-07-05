// iOS Notes screenshot — the real "ugly static" format (Miles runs these).
// Copy is baked IN as legible text (fal.ai couldn't render this, hence the blank card).
// data: { title, time, lines: [...] }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const NOTES_YELLOW = "#E5A50A";

export function render(data, W, H) {
  const body = (data.lines || [])
    .map((l) => (l.trim() === ""
      ? `<div style="height:28px"></div>`
      : `<p style="margin:0 0 14px;font:400 52px/1.35 ${brand.fontUI};color:#1C1C1E">${esc(l)}</p>`))
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#fff;font-family:${brand.fontUI};color:#1C1C1E;overflow:hidden}
    .statusbar{display:flex;justify-content:space-between;align-items:center;padding:26px 44px 6px;font:600 34px ${brand.fontUI}}
    .statusbar .icons{display:flex;align-items:center;gap:12px}
    .nav{display:flex;align-items:center;justify-content:space-between;padding:14px 34px 22px}
    .back{display:flex;align-items:center;gap:6px;color:${NOTES_YELLOW};font:400 40px ${brand.fontUI}}
    .back .chev{font-size:52px;font-weight:300;line-height:1}
    .navicons{display:flex;align-items:center;gap:34px;color:${NOTES_YELLOW}}
    .navicons svg{fill:${NOTES_YELLOW}}
    .note{padding:14px 48px}
    .title{font:800 64px/1.18 ${brand.fontUI};margin-bottom:10px}
    .stamp{font:400 30px ${brand.fontUI};color:#8E8E93;margin-bottom:34px}
    .stamp b{color:#8E8E93;font-weight:400}
  </style></head><body>
    <div class="ad">
      <div class="statusbar">
        <div>9:41</div>
        <div class="icons">
          <svg width="42" height="30" viewBox="0 0 42 30"><g fill="#000">
            <rect x="0" y="20" width="7" height="9" rx="2"/><rect x="10" y="14" width="7" height="15" rx="2"/>
            <rect x="20" y="8" width="7" height="21" rx="2"/><rect x="30" y="2" width="7" height="27" rx="2"/></g></svg>
          <svg width="40" height="30" viewBox="0 0 40 30" fill="#000"><path d="M20 6c7 0 13 3 17 7l-4 4c-3-3-8-5-13-5s-10 2-13 5L3 13c4-4 10-7 17-7z"/><path d="M20 15c4 0 7 1 9 3l-9 9-9-9c2-2 5-3 9-3z"/></svg>
          <svg width="58" height="30" viewBox="0 0 58 30"><rect x="1" y="5" width="46" height="20" rx="6" fill="none" stroke="#000" stroke-width="3"/><rect x="5" y="9" width="38" height="12" rx="3" fill="#000"/><rect x="50" y="11" width="4" height="8" rx="2" fill="#000"/></svg>
        </div>
      </div>
      <div class="nav">
        <div class="back"><span class="chev">‹</span> Notes</div>
        <div class="navicons">
          <svg width="40" height="46" viewBox="0 0 24 28"><path d="M12 2l5 5h-3v8h-4V7H7l5-5z"/><rect x="4" y="15" width="16" height="11" rx="2" fill="none" stroke="${NOTES_YELLOW}" stroke-width="2"/></svg>
          <svg width="44" height="44" viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.8 9.94l-3.75-3.75L3 17.25zM20.7 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
        </div>
      </div>
      <div class="note">
        <div class="title">${esc(data.title || "")}</div>
        <div class="stamp">${esc(data.time || "Today at 9:41 AM")}</div>
        ${body}
      </div>
    </div>
  </body></html>`;
}
