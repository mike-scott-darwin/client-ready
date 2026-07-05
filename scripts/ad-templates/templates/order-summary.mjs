// Value-stack "Order Summary" checkout mockup — mirrors Miles's workhorse value-stack winner.
// Renders our real stack in the Client Ready design system (teal ink + amber accent).
// data: { brand, system, items:[{label, price}], totalOriginal, totalToday, cta }

import { brand } from "../brand.mjs";

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export function render(data, W, H) {
  const title = data.system || "The Client Ready Offer System";
  const rows = (data.items || [])
    .map((it) => {
      const included = /^incl/i.test(String(it.price));
      const priceHtml = included
        ? `<span style="font-weight:700;color:${brand.ink};letter-spacing:1px">INCLUDED</span>`
        : `<span style="font-weight:800;color:${brand.ink}">${esc(it.price)}</span>`;
      return `
      <div style="display:flex;align-items:center;gap:24px;padding:17px 0;border-bottom:1px solid ${brand.line}">
        <div style="flex:none;width:58px;height:58px;border-radius:50%;background:${brand.accent};
          color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:800">✓</div>
        <div style="flex:1;font:600 40px ${brand.fontUI};color:${brand.ink}">${esc(it.label)}</div>
        <div style="flex:none;font:800 40px ${brand.fontUI}">${priceHtml}</div>
      </div>`;
    })
    .join("");

  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{margin:0;padding:0;box-sizing:border-box}
    .ad{width:${W}px;height:${H}px;background:${brand.bg};padding:58px 72px 60px;
      font-family:${brand.fontUI};color:${brand.ink};display:flex;flex-direction:column}
    .brandrow{display:flex;align-items:center;justify-content:center;gap:22px;margin-bottom:20px}
    .logo{width:62px;height:62px;position:relative}
    .logo span{position:absolute;left:0;width:62px;height:22px;border-radius:6px;
      background:linear-gradient(135deg,${brand.accent},#B9761C)}
    .brandname{font:800 50px ${brand.fontDisplay};letter-spacing:-1px}
    .title{text-align:center;font:800 92px/1 ${brand.fontDisplay};letter-spacing:-3px;margin-top:4px}
    .subtitle{text-align:center;font:500 38px ${brand.fontUI};color:${brand.inkSoft};margin:12px 0 14px}
    .items{flex:1}
    .totalrow{display:flex;align-items:baseline;justify-content:space-between;padding-top:26px;margin-top:4px}
    .totallabel{font:800 58px ${brand.fontDisplay};letter-spacing:-1px}
    .totalval{font:800 58px ${brand.fontDisplay}}
    .strike{color:${brand.inkSoft};text-decoration:line-through;margin-right:16px;font-weight:600}
    .today{color:${brand.accent}}
    .cta{margin-top:30px;height:116px;border-radius:58px;background:${brand.accent};
      display:flex;align-items:center;justify-content:center;
      font:800 56px ${brand.fontDisplay};color:#fff;box-shadow:0 12px 30px rgba(217,144,43,.35)}
  </style></head><body>
    <div class="ad">
      <div class="brandrow">
        <div class="logo"><span style="top:0"></span><span style="top:22px;opacity:.85"></span><span style="top:44px;opacity:.7"></span></div>
        <div class="brandname">${esc(data.brand || brand.name)}</div>
      </div>
      <div class="title">ORDER SUMMARY</div>
      <div class="subtitle">${esc(title)}</div>
      <div class="items">${rows}</div>
      <div class="totalrow">
        <div class="totallabel">TOTAL VALUE</div>
        <div class="totalval"><span class="strike">${esc(data.totalOriginal || "")}</span><span class="today">${esc(data.totalToday || "")} TODAY</span></div>
      </div>
      <div class="cta">${esc(data.cta || "Start for $27")}</div>
    </div>
  </body></html>`;
}
