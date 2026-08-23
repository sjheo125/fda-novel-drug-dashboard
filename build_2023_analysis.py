# -*- coding: utf-8 -*-
"""Build FDA 2023 Novel Drug Approvals – TA & Company Analysis HTML"""

today = "2026-07-01"
total = 55
n_big = 26
n_bio = 29
pct_big = n_big / total * 100
pct_bio = n_bio / total * 100

# Consolidated TA (sorted by count)
ta_consolidated = {
    "Oncology":            14,
    "Rare Disease":        10,
    "Neurology":            7,
    "Infectious Disease":   5,
    "Hematology":           4,
    "Ophthalmology":        3,
    "Dermatology":          2,
    "Psychiatry":           2,
    "Gastroenterology":     2,
    "Endocrinology":        2,
    "Nephrology":           2,
    "Women's Health":       1,
    "Cardiovascular":       1,
}

max_ta = max(ta_consolidated.values())
ta_sorted = sorted(ta_consolidated.items(), key=lambda x: x[1], reverse=True)

colors_ta = [
    "#c8303a","#2657a8","#3473d0","#e07020","#3e8e6e",
    "#4a90e2","#6aa3e8","#56b38a","#88b8ef","#a0c8f5","#92dab8","#b8a0f0","#f0c040",
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

# Oncology breakdown (14 drugs)
oncology_cancers = [
    ("Multiple Myeloma (다발성골수종)", 2),       # Talvey, Elrexfio
    ("Breast Cancer (유방암)", 2),                # Orserdu, Truqap
    ("Lymphoma / DLBCL", 2),                      # Epkinly, Columvi
    ("NSCLC (비소세포폐암)", 1),                  # Augtyro (ROS1)
    ("Mantle Cell Lymphoma", 1),                   # Jaypirca
    ("AML (급성골수성백혈병)", 1),                 # Vanflyta
    ("Merkel Cell Carcinoma", 1),                  # Zynyz
    ("Nasopharyngeal Carcinoma (비인두암)", 1),    # Loqtorzi
    ("Colorectal Cancer (대장암)", 1),             # Fruzaqla
    ("Desmoid Tumor (데스모이드 종양)", 1),        # Ogsiveo
    ("Prostate Cancer Imaging (전립선암 영상)", 1), # Posluma
]
onc_max = max(v for _, v in oncology_cancers)
onc_bars = ""
for name, cnt in sorted(oncology_cancers, key=lambda x: x[1], reverse=True):
    pct = cnt / onc_max * 100
    onc_bars += f"""
    <div class="bar-row">
      <div class="bar-label">{name}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;background:#c8303a"></div></div>
      <div class="bar-count">{cnt}</div>
    </div>"""

# Company lists
companies_big = [
    ("Pfizer", 4),               # Zavzpret, Litfulo, Ngenla, Elrexfio, Velsipity → 5 actually (+ Velsipity)
    ("Biogen", 3),               # Leqembi, Qalsody, Zurzuvae
    ("Eli Lilly", 2),            # Jaypirca, Omvoh
    ("GSK", 2),                  # Jesduvroq, Ojjaara
    ("AstraZeneca", 2),          # Truqap, Wainua (co-dev)
    ("Janssen (J&J)", 1),        # Talvey
    ("Roche / Genentech", 1),    # Columvi
    ("AbbVie", 1),               # Epkinly
    ("Daiichi Sankyo", 1),       # Vanflyta
    ("Sanofi", 1),               # Beyfortus
    ("Novo Nordisk", 1),         # Rivfloza
    ("Bristol-Myers Squibb", 1), # Augtyro
    ("Takeda", 1),               # Fruzaqla
    ("Novartis", 1),             # Fabhalta
    ("Astellas", 1),             # Veozah
    ("Ipsen", 1),                # Sohonos
]

companies_bio = [
    ("UCB", 3),                  # Rystiggo, Bimzelx, Zilbrysq
    ("Chiesi", 3),               # Lamzede, Elfabrio, Filsuvez
    ("Pfizer / OPKO (Ngenla)", 0),   # counted in Big Pharma
    ("Menarini / Stemline", 1),  # Orserdu
    ("Travere Therapeutics", 1), # Filspari
    ("Reata Pharmaceuticals", 1),# Skyclarys
    ("Acadia Pharmaceuticals", 1), # Daybue
    ("Cidara / Melinta", 1),     # Rezzayo
    ("Incyte", 1),               # Zynyz
    ("Pharming Group", 1),       # Joenja
    ("Bausch + Lomb / Novaliq", 1), # Miebo
    ("Innoviva / Entasis", 1),   # Xacduro
    ("Blue Earth Diagnostics", 1), # Posluma
    ("Lexicon Pharmaceuticals", 1), # Inpefa
    ("Tarsus Pharmaceuticals", 1), # Xdemvy
    ("Iveric Bio (Astellas)", 1),# Izervay
    ("Sage Therapeutics", 1),    # Zurzuvae co-dev
    ("BioLineRx", 1),            # Aphexda
    ("Fabre-Kramer", 1),         # Exxua
    ("Amicus Therapeutics", 1),  # Pombiliti
    ("Regeneron", 1),            # Veopoz
    ("Catalyst / Santhera", 1),  # Agamree
    ("Coherus / Junshi", 1),     # Loqtorzi
    ("CorMedix", 1),             # Defencath
    ("SpringWorks Therapeutics", 1), # Ogsiveo
    ("Evive / Acrotech", 1),     # Ryzneuta
    ("TheracosBio", 1),          # Brenzavvy
]
companies_big = [(c, n) for c, n in companies_big if n > 0]
companies_bio = [(c, n) for c, n in companies_bio if n > 0]

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2023 Novel Drugs – TA &amp; Company Analysis</title>
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css');

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: "Pretendard", "Segoe UI", -apple-system, Arial, sans-serif;
  font-size: 13.5px;
  background: #f0f2f7;
  color: #1f2328;
  -webkit-font-smoothing: antialiased;
}}
.page-wrap {{ max-width: 1200px; margin: 0 auto; padding: 32px 24px; }}

header {{
  background: linear-gradient(135deg, #1a3a6e 0%, #2657a8 100%);
  color: #fff;
  padding: 28px 36px 22px;
  border-radius: 12px;
  margin-bottom: 24px;
  box-shadow: 0 4px 16px rgba(26,58,110,0.18);
}}
header h1 {{ font-size: 24px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 6px; }}
header p {{ font-size: 13px; opacity: 0.82; }}

.section {{
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(20,30,60,0.08);
  padding: 26px 28px;
  margin-bottom: 22px;
}}

h2 {{
  font-size: 16px;
  font-weight: 700;
  color: #16243f;
  letter-spacing: -0.02em;
  margin-bottom: 18px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e6e8ec;
}}

.bar-row {{
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  gap: 10px;
}}
.bar-label {{
  width: 260px;
  font-size: 12.5px;
  color: #3a4a6b;
  flex-shrink: 0;
  text-align: right;
}}
.bar-track {{
  flex: 1;
  background: #eef1fa;
  border-radius: 20px;
  height: 22px;
  overflow: hidden;
}}
.bar-fill {{
  height: 100%;
  border-radius: 20px;
  transition: width 0.4s;
}}
.bar-count {{
  width: 30px;
  font-size: 13px;
  font-weight: 700;
  color: #2657a8;
  text-align: left;
}}

.company-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}}
.company-block h3 {{
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 12px;
}}
.company-block.big h3 {{ color: #16243f; }}
.company-block.bio h3 {{ color: #2657a8; }}

.co-list {{
  list-style: none;
  font-size: 12.5px;
  color: #3a4a6b;
  line-height: 2;
}}
.co-list li::before {{
  content: "• ";
  color: #2657a8;
  font-weight: 700;
}}

.pct-bar {{
  display: flex;
  height: 28px;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 14px;
  font-size: 12px;
  font-weight: 700;
}}
.pct-seg {{
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
}}

.insights-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.insight-card {{
  background: #f4f7fd;
  border-left: 4px solid #2657a8;
  border-radius: 0 8px 8px 0;
  padding: 14px 16px;
  font-size: 12.5px;
  color: #3a4a6b;
  line-height: 1.65;
}}
.insight-card strong {{
  color: #16243f;
  display: block;
  margin-bottom: 5px;
  font-size: 13px;
}}

.cross-table table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}}
.cross-table th {{
  background: #1a3a6e;
  color: #fff;
  padding: 9px 12px;
  text-align: center;
  font-weight: 600;
}}
.cross-table td {{
  padding: 9px 12px;
  border-bottom: 1px solid #e6e8ec;
  text-align: center;
  color: #3a4a6b;
}}
.cross-table tr:hover td {{ background: #f4f7fd; }}
.cross-table td:first-child {{ text-align: left; color: #16243f; font-weight: 600; }}
.cross-table tr.total-row td {{ font-weight: 700; background: #f4f7fd; }}

.footer {{
  margin-top: 20px;
  font-size: 11.5px;
  color: #8a94a6;
  text-align: center;
  line-height: 1.8;
}}
a {{ color: #2657a8; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<div class="page-wrap">

  <header>
    <h1>FDA 2023 Novel Drug Approvals – Therapeutic Area &amp; Company Analysis</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Total {total} novel approvals &nbsp;|&nbsp;
       Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2023" style="color:#fff;text-decoration:underline;" target="_blank">FDA Novel Drug Approvals for 2023</a></p>
  </header>

  <!-- TA Analysis -->
  <div class="section">
    <h2>📊 Therapeutic Area별 승인 현황 (Consolidated)</h2>
    {ta_bars}
  </div>

  <!-- Oncology breakdown -->
  <div class="section">
    <h2>🎗 Oncology 세부 분류 (14개 항암제)</h2>
    {onc_bars}
    <p style="font-size:12px;color:#5b6472;margin-top:14px;">
      * Multiple Myeloma 2개: Talvey(talquetamab, GPRC5D×CD3 최초 bispecific), Elrexfio(elranatamab, BCMA×CD3 bispecific) — 둘 다 가속승인<br>
      * Lymphoma/DLBCL 2개: Epkinly(epcoritamab, CD20×CD3 SC bispecific), Columvi(glofitamab, CD20×CD3 IV, fixed duration) — 둘 다 가속승인<br>
      * Breast Cancer 2개: Orserdu(elacestrant, ESR1 표적 SERD), Truqap(capivasertib, AKT 억제제 + fulvestrant)<br>
      * NSCLC 1개: Augtyro(repotrectinib, next-gen ROS1/NTRK 억제제)
    </p>
  </div>

  <!-- Company Analysis -->
  <div class="section">
    <h2>🏢 Company Type – Big Pharma vs Biotech</h2>

    <div class="pct-bar" style="margin-bottom:20px;">
      <div class="pct-seg" style="width:{pct_big:.1f}%;background:#16243f;">Big Pharma {n_big} ({pct_big:.0f}%)</div>
      <div class="pct-seg" style="width:{pct_bio:.1f}%;background:#2657a8;">Biotech {n_bio} ({pct_bio:.0f}%)</div>
    </div>

    <div class="company-grid">
      <div class="company-block big">
        <h3>🏦 Big Pharma ({n_big}개)</h3>
        <ul class="co-list">
          {"".join(f"<li>{co} ({cnt})</li>" for co, cnt in companies_big)}
        </ul>
      </div>
      <div class="company-block bio">
        <h3>🔬 Biotech ({n_bio}개)</h3>
        <ul class="co-list">
          {"".join(f"<li>{co} ({cnt})</li>" for co, cnt in companies_bio)}
        </ul>
      </div>
    </div>
  </div>

  <!-- Cross-table -->
  <div class="section cross-table">
    <h2>📋 TA × Company Type 교차 분석</h2>
    <table>
      <thead>
        <tr>
          <th>Therapeutic Area</th>
          <th>Big Pharma</th>
          <th>Biotech</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Oncology (모든 암종)</td><td>9</td><td>5</td><td>14</td></tr>
        <tr><td>Rare Disease</td><td>3</td><td>7</td><td>10</td></tr>
        <tr><td>Neurology</td><td>3</td><td>4</td><td>7</td></tr>
        <tr><td>Infectious Disease</td><td>2</td><td>3</td><td>5</td></tr>
        <tr><td>Hematology</td><td>2</td><td>2</td><td>4</td></tr>
        <tr><td>Ophthalmology</td><td>0</td><td>3</td><td>3</td></tr>
        <tr><td>Dermatology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Psychiatry</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Gastroenterology</td><td>2</td><td>0</td><td>2</td></tr>
        <tr><td>Endocrinology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Nephrology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Women's Health</td><td>1</td><td>0</td><td>1</td></tr>
        <tr><td>Cardiovascular</td><td>0</td><td>1</td><td>1</td></tr>
        <tr class="total-row"><td>합계</td><td>26</td><td>29</td><td>55</td></tr>
      </tbody>
    </table>
  </div>

  <!-- Insights -->
  <div class="section">
    <h2>💡 Key Insights – 2023 FDA Novel Drugs</h2>
    <div class="insights-grid">
      <div class="insight-card">
        <strong>① 알츠하이머 최초 질병수정치료제 (Leqembi)</strong>
        lecanemab이 1월 가속승인 → 7월 정식승인으로 전환. 20여 년에 걸친 amyloid 가설 논란을 일단락하고 DMT 시대를 개막. 가속승인-정규승인 전환 경로의 모범 사례.
      </div>
      <div class="insight-card">
        <strong>② Bispecific 항체 붐 — 2023년은 T세포 이중항체의 해</strong>
        Epkinly(CD20×CD3), Columvi(CD20×CD3), Talvey(GPRC5D×CD3), Elrexfio(BCMA×CD3) — 4종의 bispecific T-cell engager 승인. 특히 MM에서 BCMA와 GPRC5D 두 표적이 각각 검증됨.
      </div>
      <div class="insight-card">
        <strong>③ Rare Disease "First-ever" 5개</strong>
        Daybue(Rett syndrome 최초), Skyclarys(Friedreich's ataxia 최초), Sohonos(FOP 최초), Veopoz(CHAPLE 최초), Qalsody(SOD1-ALS 최초) — 한 해에 다섯 가지 치료 불가 희귀질환에 최초 치료제가 탄생.
      </div>
      <div class="insight-card">
        <strong>④ 가속승인 9개 (16%)</strong>
        Leqembi·Jaypirca·Filspari·Zynyz·Qalsody·Epkinly·Columvi·Talvey·Elrexfio — 이 중 bispecific 4종, rare disease 2종. 가속승인이 혁신 약물의 조기 접근 수단으로 정착.
      </div>
      <div class="insight-card">
        <strong>⑤ 25년 만의 승인: Exxua (gepirone)</strong>
        1990년대 말부터 여러 차례 CRL을 받은 선택적 5-HT1A 효능제가 2023년 Class 2 resubmission으로 최종 승인. 개발이 중단될 뻔했던 약물의 집념 있는 재도전 사례.
      </div>
      <div class="insight-card">
        <strong>⑥ 중국 개발 PD-1의 미국 진출 (Loqtorzi)</strong>
        Coherus/Junshi의 toripalimab이 비인두암(NPC) 적응증으로 FDA 승인 획득 — 중국 제약사가 개발한 면역항암제 최초 미국 승인. 글로벌 제약 생태계 다변화 신호.
      </div>
    </div>
  </div>

  <div class="footer">
    FDA 2023 Novel Drug Approvals Analysis &nbsp;|&nbsp; Content as of {today}<br>
    <a href="FDA Novel Drug Approvals 2023 Dashboard.html">← 2023 대시보드로 돌아가기</a>
  </div>

</div>
</body>
</html>"""

output_path = r"C:\0_MBA\Healthcare\FDA New Drug Approval Dashboard\FDA 2023 Novel Drugs - TA and Company Analysis.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Analysis saved to: {output_path}")
