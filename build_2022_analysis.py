# -*- coding: utf-8 -*-
import os
"""Build FDA 2022 Novel Drug Approvals – TA & Company Analysis HTML"""

today = "2026-07-02"
total = 37
n_big = 14
n_bio = 23
pct_big = n_big / total * 100
pct_bio = n_bio / total * 100

# Consolidated TA (sorted by count)
ta_consolidated = {
    "Oncology":           12,
    "Dermatology":         6,
    "Neurology":           4,
    "Infectious Disease":  3,
    "Hematology":          2,
    "Rare Disease":        2,
    "Endocrinology":       2,
    "Ophthalmology":       2,
    "Cardiovascular":      1,
    "Gastroenterology":    1,
    "Radiology":           1,
    "Pulmonology":         1,
}

max_ta = max(ta_consolidated.values())
ta_sorted = sorted(ta_consolidated.items(), key=lambda x: x[1], reverse=True)

colors_ta = [
    "#c8303a","#2657a8","#3473d0","#e07020","#3e8e6e",
    "#4a90e2","#6aa3e8","#56b38a","#88b8ef","#a0c8f5","#92dab8","#b8a0f0",
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

# Oncology breakdown (12 drugs)
oncology_cancers = [
    ("Melanoma (흑색종)", 2),                      # Kimmtrak(uveal), Opdualag(cutaneous)
    ("Myelofibrosis (골수섬유증)", 1),              # Vonjo — AA
    ("Prostate Cancer (전립선암)", 1),              # Pluvicto
    ("Cholangiocarcinoma (담관암)", 1),             # Lytgobi — AA
    ("HCC (간세포암)", 1),                          # Imjudo
    ("Multiple Myeloma (다발성골수종)", 1),         # Tecvayli — AA
    ("Ovarian Cancer (난소암)", 1),                 # Elahere — AA
    ("AML (급성골수성백혈병)", 1),                  # Rezlidhia
    ("NSCLC (비소세포폐암)", 1),                    # Krazati — AA
    ("Follicular Lymphoma (여포성림프종)", 1),      # Lunsumio — AA
    ("Febrile Neutropenia (발열성 호중구감소증)", 1), # Rolvedon (oncology supportive)
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
    ("Bristol-Myers Squibb", 3),   # Opdualag, Camzyos, Sotyktu
    ("Genentech / Roche", 2),      # Vabysmo, Lunsumio
    ("Sanofi", 2),                 # Enjaymo, Xenpozyme
    ("Pfizer", 1),                 # Cibinqo
    ("Novartis", 1),               # Pluvicto
    ("Eli Lilly", 1),              # Mounjaro
    ("Boehringer Ingelheim", 1),   # Spevigo
    ("AstraZeneca", 1),            # Imjudo
    ("Janssen (J&J)", 1),          # Tecvayli
    ("Gilead Sciences", 1),        # Sunlenca
]

companies_bio = [
    ("Idorsia Pharmaceuticals", 1),    # Quviviq
    ("Immunocore", 1),                 # Kimmtrak
    ("Agios Pharmaceuticals", 1),      # Pyrukynd
    ("CTI BioPharma", 1),              # Vonjo
    ("Marinus Pharmaceuticals", 1),    # Ztalmy
    ("Mycovia Pharmaceuticals", 1),    # Vivjoa
    ("Phathom Pharmaceuticals", 1),    # Voquezna
    ("Dermavant Sciences", 1),         # Vtama
    ("Alnylam Pharmaceuticals", 1),    # Amvuttra
    ("Spectrum Pharmaceuticals", 1),   # Rolvedon
    ("Mallinckrodt", 1),               # Terlivaz
    ("Guerbet", 1),                    # Elucirem
    ("Santen", 1),                     # Omlonti
    ("Amylyx Pharmaceuticals", 1),     # Relyvrio
    ("Taiho Oncology", 1),             # Lytgobi
    ("Revance Therapeutics", 1),       # Daxxify
    ("ImmunoGen", 1),                  # Elahere
    ("Provention Bio", 1),             # Tzield
    ("Forma Therapeutics / Rigel", 1), # Rezlidhia
    ("Mirati Therapeutics", 1),        # Krazati
    ("Polarean Imaging", 1),           # Xenoview
    ("TG Therapeutics", 1),            # Briumvi
    ("MediWound / Vericel", 1),        # NexoBrid
]

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2022 Novel Drugs – TA &amp; Company Analysis</title>
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
  width: 280px;
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
  margin-bottom: 20px;
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
    <h1>FDA 2022 Novel Drug Approvals – Therapeutic Area &amp; Company Analysis</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Total {total} novel approvals &nbsp;|&nbsp;
       Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2022" style="color:#fff;text-decoration:underline;" target="_blank">FDA Novel Drug Approvals for 2022</a></p>
  </header>

  <!-- TA Analysis -->
  <div class="section">
    <h2>📊 Therapeutic Area별 승인 현황 (Consolidated)</h2>
    {ta_bars}
  </div>

  <!-- Oncology breakdown -->
  <div class="section">
    <h2>🎗 Oncology 세부 분류 (12개 항암제)</h2>
    {onc_bars}
    <p style="font-size:12px;color:#5b6472;margin-top:14px;">
      * Melanoma 2개: Kimmtrak(tebentafusp, ImmTAC 최초 — uveal melanoma), Opdualag(nivolumab+relatlimab, LAG-3 최초 병용 — cutaneous melanoma)<br>
      * 6개 Accelerated Approval: Vonjo(myelofibrosis), Lytgobi(cholangiocarcinoma), Tecvayli(myeloma), Elahere(ovarian), Krazati(NSCLC), Lunsumio(follicular lymphoma)<br>
      * Pluvicto는 방사성리간드치료(RLT) 최초 PSMA 표적 승인 — theranostics 분야 이정표
    </p>
  </div>

  <!-- Company Analysis -->
  <div class="section">
    <h2>🏢 Company Type – Big Pharma vs Biotech</h2>

    <div class="pct-bar">
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
        <tr><td>Oncology (모든 암종)</td><td>5</td><td>7</td><td>12</td></tr>
        <tr><td>Dermatology</td><td>3</td><td>3</td><td>6</td></tr>
        <tr><td>Neurology</td><td>0</td><td>4</td><td>4</td></tr>
        <tr><td>Infectious Disease</td><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>Hematology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Rare Disease</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Endocrinology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Ophthalmology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>Cardiovascular</td><td>1</td><td>0</td><td>1</td></tr>
        <tr><td>Gastroenterology</td><td>0</td><td>1</td><td>1</td></tr>
        <tr><td>Radiology</td><td>0</td><td>1</td><td>1</td></tr>
        <tr><td>Pulmonology</td><td>0</td><td>1</td><td>1</td></tr>
        <tr class="total-row"><td>합계</td><td>14</td><td>23</td><td>37</td></tr>
      </tbody>
    </table>
  </div>

  <!-- Insights -->
  <div class="section">
    <h2>💡 Key Insights – 2022 FDA Novel Drugs</h2>
    <div class="insights-grid">
      <div class="insight-card">
        <strong>① First-in-class 메커니즘의 해</strong>
        Sotyktu(TYK2 최초 allosteric 억제제), Krazati(KRAS G12C 2번째 — CNS 침투 확인), Camzyos(cardiac myosin 억제제 최초), Opdualag(LAG-3 최초 병용), Mounjaro(이중 GIP/GLP-1 최초) 등 — 여러 분야에서 동시에 새로운 MOA가 개막된 해.
      </div>
      <div class="insight-card">
        <strong>② Pluvicto — 방사성리간드치료(RLT) 원년</strong>
        Lu-177-PSMA(lutetium vipivotide tetraxetan)는 PSMA 발현 전립선암에서 최초 RLT 승인. 핵의학과 종양학의 통합(theranostics) 패러다임 신호 — 이후 RLT 파이프라인 폭증의 출발점.
      </div>
      <div class="insight-card">
        <strong>③ Dermatology 르네상스 — 한 해 6종</strong>
        Cibinqo(JAK1, 아토피), Vtama(AhR 최초, 건선), Spevigo(IL-36R 최초, GPP), Daxxify(peptide BoNT 최초), Sotyktu(TYK2, 건선), NexoBrid(효소 debridement 최초) — 피부과 영역에서 다양한 MOA가 동시에 검증된 예외적인 해.
      </div>
      <div class="insight-card">
        <strong>④ Mounjaro — GLP-1 시대를 여는 티핑포인트</strong>
        tirzepatide(이중 GIP/GLP-1 RA)는 T2D로 2022년 승인 → 이후 비만(Zepbound) 및 심부전 등으로 적응증 확대. 2022년 승인 당시부터 A1c 감소폭이 기존 GLP-1 RA를 크게 상회, 대사질환 치료의 패러다임 전환 예고.
      </div>
      <div class="insight-card">
        <strong>⑤ Bispecific 시대 개막 — 3가지 형식</strong>
        Vabysmo(VEGF×Ang-2 안과 bispecific 최초), Opdualag(PD-1+LAG-3 ICI 병용 최초), Tecvayli(BCMA×CD3 T-cell engager 최초) — 같은 해 서로 다른 형식의 bispecific 3종이 각각 다른 치료 영역에서 동시 승인.
      </div>
      <div class="insight-card">
        <strong>⑥ 가속승인 6개 — 모두 항암제</strong>
        Vonjo(myelofibrosis+혈소판감소증), Lytgobi(FGFR2 담관암), Tecvayli(BCMA 골수종), Elahere(FRα 난소암), Krazati(KRAS G12C 폐암), Lunsumio(CD20 여포림프종) — 2022년 AA는 100% 종양학. Elahere는 이후 MIRASOL 데이터로 2024년 정규승인 전환.
      </div>
    </div>
  </div>

  <div class="footer">
    FDA 2022 Novel Drug Approvals Analysis &nbsp;|&nbsp; Content as of {today}<br>
    <a href="FDA Novel Drug Approvals 2022 Dashboard.html">← 2022 대시보드로 돌아가기</a>
  </div>

</div>
</body>
</html>"""

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FDA 2022 Novel Drugs - TA and Company Analysis.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Analysis saved to: {output_path}")
