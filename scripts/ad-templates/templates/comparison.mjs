// Comparison table — "what you need / old way / our way" with NO/YES pills.
// data: { title, colOld, colNew, rows: [{need, old:bool, new:bool}] }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const pill = (v) => v
    ? `<span style="display:inline-flex;align-items:center;justify-content:center;background:#17B26A;color:#fff;font:800 30px ${brand.fontUI};border-radius:34px;padding:12px 30px">YES</span>`
    : `<span style="display:inline-flex;align-items:center;justify-content:center;background:#E14B4B;color:#fff;font:800 30px ${brand.fontUI};border-radius:34px;padding:12px 30px">NO</span>`;

  const rows = (data.rows || [])
    .map((r) => `
      <tr>
        <td style="text-align:left;font:600 38px ${brand.fontUI};color:${brand.ink};padding:26px 24px;border-top:2px solid ${brand.line}">${esc(r.need)}</td>
        <td style="text-align:center;padding:26px 10px;border-top:2px solid ${brand.line}">${pill(r.old)}</td>
        <td style="text-align:center;padding:26px 10px;border-top:2px solid ${brand.line};background:rgba(217,144,43,.10)">${pill(r.new)}</td>
      </tr>`)
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:${brand.bg};font-family:${brand.fontUI};color:${brand.ink};padding:76px 64px;display:flex;flex-direction:column;justify-content:center}
    .title{text-align:center;font:800 68px/1.15 ${brand.fontDisplay};letter-spacing:-1px;margin-bottom:48px}
    table{width:100%;border-collapse:collapse}
    thead td{font:800 32px ${brand.fontUI};padding:0 10px 22px}
    .hneed{text-align:left;color:${brand.inkSoft}}
    .hold{text-align:center;color:${brand.inkSoft}}
    .hnew{text-align:center;color:${brand.accent}}
  </style></head><body>
    <div class="ad">
      <div class="title">${esc(data.title || "")}</div>
      <table>
        <thead><tr>
          <td class="hneed">WHAT YOU NEED</td>
          <td class="hold">${esc(data.colOld || "OLD WAY")}</td>
          <td class="hnew">${esc(data.colNew || "CLIENT READY")}</td>
        </tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
  </body></html>`;
}
