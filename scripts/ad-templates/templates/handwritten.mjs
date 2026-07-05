// Handwritten note mockup — mirrors Miles's intimate personal-story winner.
// Legible handwriting via macOS cursive fonts on a warm paper card (crisp + reproducible,
// unlike Flux which garbles handwritten text). data: { lines:[...], signature }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const hand = "'Bradley Hand','Snell Roundhand','Segoe Print',cursive";
  const lines = (data.lines || [])
    .map((l) => (l.trim() === "" ? `<div style="height:26px"></div>` : `<p style="margin:0 0 18px">${esc(l)}</p>`))
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:#C9BFA8;
      display:flex;align-items:center;justify-content:center;font-family:${hand}}
    .paper{width:${W - 170}px;background:#F5EEDC;
      box-shadow:0 30px 70px rgba(0,0,0,.35);padding:82px 88px;
      background-image:repeating-linear-gradient(0deg,transparent,transparent 74px,rgba(0,0,0,.04) 75px);
      transform:rotate(-1.1deg)}
    .body{font:400 54px/1.32 ${hand};color:#1E2A32}
    .sig{font:400 70px ${hand};color:#1E2A32;margin-top:26px;border-bottom:4px solid #1E2A32;display:inline-block;padding-bottom:6px}
  </style></head><body>
    <div class="ad">
      <div class="paper">
        <div class="body">${lines}</div>
        ${data.signature ? `<div class="sig">${esc(data.signature)}</div>` : ""}
      </div>
    </div>
  </body></html>`;
}
