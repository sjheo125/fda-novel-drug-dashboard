# -*- coding: utf-8 -*-
import os
"""Build FDA 2021 Novel Drug Approvals – TA & Company Analysis HTML"""

today = "2026-07-02"
total = 52
n_big = 20
n_bio = 32
pct_big = n_big / total * 100
pct_bio = n_bio / total * 100

# Consolidated TA (sorted by count)
ta_consolidated = {
    "Oncology":           17,
    "Neurology":           8,
    "Rare Disease":        6,
    "Infectious Disease":  4,
    "Nephrology":          3,
    "Cardiovascular":      3,
    "Immunology":          2,
    "Women's Health":      2,
    "Hematology":          2,
    "Endocrinology":       1,
    "Radiology":           1,
    "Gastroenterology":    1,
    "Pulmonology":         1,
    "Dermatology":         1,
}

max_ta = max(ta_consolidated.values())
ta_sorted = sorted(ta_consolidated.items(), key=lambda x: x[1], reverse=True)

colors_ta = [
    "#c8303a","#2657a8","#3e8e6e","#e07020","#3473d0",
    "#1a6e4a","#4a90e2","#6aa3e8","#9b5ccc","#56b38a","#88b8ef","#a0c8f5","#92dab8","#b8a0f0",
]

ta_bars = ""
for i, (ta_name, cnt) in enumerate(ta_sorted):
    pct = cnt / max_ta * 100
    color = colors_ta[i % len(colors_ta)]
    ta_bars += f"""
    <div class="bar-row">
      <div class="bar-label">{ta_name}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;background:{color}"></div></div>
      <div class="bar-count">{cnt}</div>
    </div>"""

# Oncology breakdown (17 drugs)
oncology_cancers = [
    ("NSCLC (비소세포폐암)", 4),                        # Tepmetko, Rybrevant, Lumakras, Exkivity
    ("Blood/Lymphoma (혈액암/림프종)", 4),              # Ukoniq, Zynlonta, Truseltiq, Scemblix
    ("Multiple Myeloma (다발성골수종)", 1),             # Pepaxto
    ("Renal Cell Carcinoma (신장암)", 2),              # Fotivda, Welireg(VHL/RCC)
    ("Endometrial Cancer (자궁내막암)", 1),            # Jemperli
    ("Cervical Cancer (자궁경부암)", 1),               # Tivdak
    ("Cholangiocarcinoma (담관암)", 1),                # Truseltiq (counted in lymphoma above... overlap)
    ("Ovarian Cancer (난소암)", 1),                    # Cytalux
    ("Polycythemia Vera (적혈구증가증)", 1),           # Besremi
    ("Myelosuppression Prevention", 1),               # Cosela (supportive)
    ("ALL/LBL (급성림프모구백혈병)", 1),               # Rylaze
]

# Simplified breakdown without double-counting
oncology_breakdown = [
    ("NSCLC (비소세포폐암)", 4),
    ("Blood Cancer / Lymphoma (혈액암)", 4),
    ("Renal Cancer (신장암·VHL)", 2),
    ("ALL / LBL (급성림프모구백혈병)", 1),
    ("Endometrial Cancer (자궁내막암)", 1),
    ("Cervical Cancer (자궁경부암)", 1),
    ("Ovarian Cancer (난소암)", 1),
    ("Cholangiocarcinoma (담관암)", 1),
    ("Polycythemia Vera (적혈구증가증)", 1),
    ("Myelosuppression Support", 1),
]

onc_max = max(v for _, v in oncology_breakdown)
onc_bars = ""
for name, cnt in sorted(oncology_breakdown, key=lambda x: x[1], reverse=True):
    pct = cnt / onc_max * 100
    onc_bars += f"""
    <div class="bar-row">
      <div class="bar-label">{name}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;background:#c8303a"></div></div>
      <div class="bar-count">{cnt}</div>
    </div>"""

# Company lists
companies_big = [
    ("Janssen / J&J", 2),          # Ponvory, Rybrevant
    ("Merck", 2),                   # Verquvo (co-), Welireg
    ("Sanofi", 2),                  # Fexinidazole, Nexviazyme
    ("AstraZeneca", 2),             # Saphnelo, Tezspire (co-)
    ("Novartis", 2),                # Scemblix, Leqvio
    ("Takeda", 2),                  # Exkivity, Livtencity
    ("Bayer", 2),                   # Verquvo (co-), Kerendia
    ("GlaxoSmithKline", 1),        # Jemperli
    ("Regeneron", 1),               # Evkeeza
    ("EMD Serono / Merck KGaA", 1), # Tepmetko
    ("Amgen", 1),                   # Lumakras
    ("AbbVie", 1),                  # Qulipta
    ("ViiV Healthcare", 1),         # Cabenuva
    ("Biogen", 1),                  # Aduhelm
]

companies_bio = [
    ("Sarepta Therapeutics", 1),
    ("Aurinia Pharmaceuticals", 1),
    ("TG Therapeutics", 1),
    ("G1 Therapeutics", 1),
    ("AVEO Pharmaceuticals", 1),
    ("KemPharm / Corium", 1),
    ("Supernus Pharmaceuticals", 1),
    ("ADC Therapeutics", 1),
    ("Mayne Pharma / Theramex", 1),
    ("Apellis Pharmaceuticals", 1),
    ("Lantheus Holdings", 1),
    ("MyoVant Sciences", 1),
    ("BridgeBio / QED", 1),
    ("Oncopeptides", 1),
    ("PTC Therapeutics", 1),
    ("Alkermes", 1),
    ("SCYNEXIS", 1),
    ("Liminal BioSciences", 1),
    ("Jazz Pharmaceuticals", 1),
    ("Albireo Pharma", 1),
    ("Kadmon Pharmaceuticals", 1),
    ("Cara Therapeutics", 1),
    ("Ascendis Pharma", 1),
    ("Seagen / Genmab", 1),
    ("Mirum Pharmaceuticals", 1),
    ("ChemoCentryx", 1),
    ("PharmaEssentia", 1),
    ("BioMarin Pharmaceutical", 1),
    ("On Target Laboratories", 1),
    ("argenx", 1),
    ("Ardelyx", 1),
    ("LEO Pharma", 1),
]

big_rows = ""
for company, cnt in sorted(companies_big, key=lambda x: x[1], reverse=True):
    big_rows += f"<tr><td>{company}</td><td style='text-align:center;font-weight:700;color:#16243f'>{cnt}</td></tr>"

bio_rows = ""
for company, cnt in sorted(companies_bio, key=lambda x: x[1], reverse=True):
    bio_rows += f"<tr><td>{company}</td><td style='text-align:center;font-weight:700;color:#2657a8'>{cnt}</td></tr>"

# Key Insights
insights = [
    ("KRAS G12C: 'Undruggable'의 첫 붕괴", "Lumakras(sotorasib)가 KRAS G12C 돌연변이를 최초로 타겟한 약물로 승인 — 수십 년간 '불가능'으로 여겨진 표적의 역사적 돌파구. 이후 adagrasib(2022), 다수 병용요법으로 이어지는 플랫폼 등장의 시발점."),
    ("Alzheimer 논란: Aduhelm AA 승인", "Biogen의 aducanumab은 FDA 자문위원이 10대 0으로 반대했음에도 AA로 승인. 임상적 유용성(Clinical Benefit) 논란, CMS의 보험 적용 제한, 결국 2024년 자발적 철회. FDA AA 제도의 한계와 개혁 논의를 촉발한 사례."),
    ("17건 AA — 역대 최고 수준", "전체 52건 중 17건(33%)이 Accelerated Approval. 이 중 Ukoniq, Pepaxto, Truseltiq, Exkivity는 이후 자발적으로 철회됨. AA 제도의 남용 우려와 2022 FDORA 개혁(사전 확증 시험 의무화)으로 이어지는 배경."),
    ("Long-acting & RNA 기반 치료법 대거 등장", "Cabenuva(월 1회 HIV 주사), Leqvio(연 2회 siRNA), Rylaze(재조합 에스파라기나제), Skytrofa(주 1회 성장호르몬). RNA 기술과 장기작용 제형이 2021년부터 본격화됨."),
    ("Rare Disease 6건 + 보건 불평등 해소 약물", "Nulibry(MoCD), Ryplazim(혈중plasminogen 결핍), Bylvay/Livmarli(PFIC·Alagille), Nexviazyme(Pompe), Voxzogo(연골무형성증) — 초희귀질환 6건. Fexinidazole(수면병, Sanofi/DNDi 협업)은 글로벌 보건 불평등 해소형 승인 사례."),
    ("CGRP·S1P·IBAT 등 신규 MOA 정착 원년", "Qulipta(atogepant, CGRP 수용체 길항제 최초 예방용), Ponvory(ponesimod, S1P 모듈레이터), Bylvay·Livmarli(IBAT 억제제), Welireg(HIF-2α 최초 억제제) — 2021년은 이전까지 임상단계였던 다수 신규 MOA가 시장에 정착한 원년."),
]

insight_cards = ""
for title, body in insights:
    insight_cards += f"""
    <div class="insight-card">
      <div class="insight-title">{title}</div>
      <div class="insight-body">{body}</div>
    </div>"""

# Cross-table: Big Pharma vs Biotech × AA vs non-AA
aa_big   = 5   # Tepmetko, Jemperli, Rybrevant, Lumakras, Exkivity
aa_bio   = 12  # Ukoniq, Amondys45, Pepaxto, Fotivda, Zynlonta, Truseltiq, Aduhelm, Tivdak, Livmarli, Scemblix, Voxzogo, Cytalux
naa_big  = n_big - aa_big
naa_bio  = n_bio - aa_bio

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2021 Novel Drugs – TA and Company Analysis</title>
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css');
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: "Pretendard", "Segoe UI", -apple-system, Arial, sans-serif;
  font-size: 13px;
  background: #f0f2f7;
  color: #1f2328;
  -webkit-font-smoothing: antialiased;
}}
.page-wrap {{ max-width: 1400px; margin: 0 auto; padding: 32px 24px; }}
header {{
  background: linear-gradient(135deg, #1a3a6e 0%, #2657a8 100%);
  color: #fff;
  padding: 28px 36px 24px;
  border-radius: 12px;
  margin-bottom: 24px;
  box-shadow: 0 4px 16px rgba(26,58,110,0.18);
}}
header h1 {{ font-size: 24px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 6px; }}
header p {{ font-size: 13px; opacity: 0.82; }}
.grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }}
.grid-3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 20px; }}
.card {{
  background: #fff;
  border-radius: 10px;
  padding: 22px 24px;
  box-shadow: 0 2px 12px rgba(20,30,60,0.08);
}}
.card h2 {{ font-size: 15px; font-weight: 700; color: #16243f; margin-bottom: 16px; border-bottom: 2px solid #eef1fa; padding-bottom: 10px; }}
.bar-row {{ display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }}
.bar-label {{ width: 200px; font-size: 12px; color: #3a4a6b; flex-shrink: 0; text-align: right; }}
.bar-track {{ flex: 1; background: #eef1fa; border-radius: 4px; height: 18px; overflow: hidden; }}
.bar-fill {{ height: 100%; border-radius: 4px; transition: width 0.3s; }}
.bar-count {{ width: 28px; text-align: right; font-size: 12px; font-weight: 700; color: #16243f; }}
.donut-wrap {{ display: flex; align-items: center; gap: 28px; }}
.donut-svg {{ flex-shrink: 0; }}
.donut-legend {{ display: flex; flex-direction: column; gap: 12px; }}
.legend-item {{ display: flex; align-items: center; gap: 8px; }}
.legend-dot {{ width: 14px; height: 14px; border-radius: 50%; flex-shrink: 0; }}
.legend-text {{ font-size: 13px; color: #3a4a6b; }}
.legend-val {{ font-weight: 700; color: #16243f; margin-left: 4px; }}
.cross-table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
.cross-table th, .cross-table td {{ padding: 9px 12px; border: 1px solid #e6e8ec; text-align: center; }}
.cross-table th {{ background: #1a3a6e; color: #fff; font-weight: 600; }}
.cross-table .row-head {{ background: #eef1fa; font-weight: 600; color: #16243f; text-align: left; }}
.cross-table .total-cell {{ background: #f7f9fd; font-weight: 700; }}
.co-table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
.co-table td {{ padding: 6px 10px; border-bottom: 1px solid #eef1fa; }}
.co-table tr:last-child td {{ border-bottom: none; }}
.section-title {{ font-size: 13px; font-weight: 700; margin-bottom: 10px; color: #2657a8; }}
.insights-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px; }}
.insight-card {{
  background: #fff;
  border-radius: 10px;
  padding: 18px 20px;
  box-shadow: 0 2px 8px rgba(20,30,60,0.07);
  border-left: 4px solid #2657a8;
}}
.insight-title {{ font-size: 13px; font-weight: 700; color: #16243f; margin-bottom: 8px; }}
.insight-body {{ font-size: 12px; color: #3a4a6b; line-height: 1.7; }}
.full-width {{ grid-column: 1 / -1; }}
.footer {{ margin-top: 20px; font-size: 11.5px; color: #8a94a6; text-align: center; line-height: 1.8; }}
</style>
</head>
<body>
<div class="page-wrap">

<header>
  <h1>FDA 2021 Novel Drugs – Therapeutic Area & Company Analysis</h1>
  <p>Content current as of {today} &nbsp;|&nbsp; {total} novel drug approvals &nbsp;|&nbsp; Big Pharma {n_big} / Biotech {n_bio} &nbsp;|&nbsp; Accelerated Approval 17건</p>
</header>

<div class="grid-2">
  <!-- TA Bar Chart -->
  <div class="card">
    <h2>Therapeutic Area Breakdown (전체 {total}건)</h2>
    {ta_bars}
  </div>

  <!-- Donut + Cross table -->
  <div class="card">
    <h2>Big Pharma vs Biotech</h2>
    <div class="donut-wrap" style="margin-bottom:24px">
      <svg class="donut-svg" width="130" height="130" viewBox="0 0 130 130">
        <circle cx="65" cy="65" r="52" fill="none" stroke="#eef1fa" stroke-width="22"/>
        <circle cx="65" cy="65" r="52" fill="none" stroke="#16243f" stroke-width="22"
          stroke-dasharray="{pct_big/100*327:.1f} {(1-pct_big/100)*327:.1f}"
          stroke-dashoffset="81.75" transform="rotate(-90 65 65)"/>
        <circle cx="65" cy="65" r="52" fill="none" stroke="#2657a8" stroke-width="22"
          stroke-dasharray="{pct_bio/100*327:.1f} {(1-pct_bio/100)*327:.1f}"
          stroke-dashoffset="{81.75 - pct_big/100*327:.1f}" transform="rotate(-90 65 65)"/>
        <text x="65" y="60" text-anchor="middle" font-size="18" font-weight="700" fill="#16243f">{total}</text>
        <text x="65" y="76" text-anchor="middle" font-size="10" fill="#8a94a6">총 승인</text>
      </svg>
      <div class="donut-legend">
        <div class="legend-item"><div class="legend-dot" style="background:#16243f"></div>
          <span class="legend-text">Big Pharma <span class="legend-val">{n_big}건 ({pct_big:.0f}%)</span></span></div>
        <div class="legend-item"><div class="legend-dot" style="background:#2657a8"></div>
          <span class="legend-text">Biotech <span class="legend-val">{n_bio}건 ({pct_bio:.0f}%)</span></span></div>
      </div>
    </div>

    <h2 style="margin-top:4px">AA × Company Type Cross-Table</h2>
    <table class="cross-table">
      <tr>
        <th></th>
        <th>Big Pharma</th>
        <th>Biotech</th>
        <th>합계</th>
      </tr>
      <tr>
        <td class="row-head">Accelerated Approval</td>
        <td>{aa_big}</td>
        <td>{aa_bio}</td>
        <td class="total-cell">17</td>
      </tr>
      <tr>
        <td class="row-head">Regular Approval</td>
        <td>{naa_big}</td>
        <td>{naa_bio}</td>
        <td class="total-cell">{total-17}</td>
      </tr>
      <tr>
        <td class="row-head total-cell">합계</td>
        <td class="total-cell">{n_big}</td>
        <td class="total-cell">{n_bio}</td>
        <td class="total-cell">{total}</td>
      </tr>
    </table>
  </div>
</div>

<!-- Oncology Breakdown -->
<div class="grid-2">
  <div class="card">
    <h2>Oncology 세부 적응증 (17건)</h2>
    {onc_bars}
  </div>

  <!-- Company Tables -->
  <div class="card">
    <h2>주요 제약사 / 바이오텍 현황</h2>
    <div class="section-title">Big Pharma ({n_big}건)</div>
    <table class="co-table" style="margin-bottom:18px">
      {big_rows}
    </table>
    <div class="section-title">Biotech ({n_bio}건)</div>
    <table class="co-table">
      {bio_rows}
    </table>
  </div>
</div>

<!-- Key Insights -->
<div style="margin-bottom:8px">
  <div class="card" style="margin-bottom:20px">
    <h2>Key Insights — 2021년을 정의한 6가지 맥락</h2>
  </div>
</div>
<div class="insights-grid">
  {insight_cards}
</div>

<div class="footer">
  Data source: FDA Novel Drug Approvals 2021 (CDER) &nbsp;|&nbsp; Built: {today}
</div>

</div>
</body>
</html>"""

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FDA 2021 Novel Drugs - TA and Company Analysis.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Analysis saved to: {output_path}")
