# -*- coding: utf-8 -*-
import os
"""Build FDA 2025 Novel Drug Approvals Analysis HTML"""

# Summary data from dashboard
ta_data = {
    "Oncology": 14,
    "Oncology / Hematology": 2,
    "Hematology": 2,
    "Hematology / Rare Disease": 1,
    "Immunology": 3,
    "Dermatology / Immunology": 1,
    "Infectious Disease": 3,
    "Cardiovascular": 2,
    "Cardiovascular / Metabolic": 1,
    "Pulmonology": 3,
    "Nephrology": 2,
    "Neurology / Immunology": 1,
    "Rare Disease / Metabolic": 1,
    "Rare Disease / Neurology": 1,
    "Rare Disease / Cardiology": 1,
    "Ophthalmology": 2,
    "Dermatology": 1,
    "Women's Health": 1,
    "Pain Management": 1,
    "Endocrinology": 1,
    "Neurology": 1,
}

# Consolidated TA for visualization
ta_consolidated = {
    "Oncology": 16,       # Oncology + Oncology/Hematology (pure oncology drugs)
    "Hematology": 3,      # Hematology + Hematology/Rare Disease
    "Immunology": 4,      # Immunology + Dermatology/Immunology
    "Infectious Disease": 3,
    "Cardiovascular / Metabolic": 3,
    "Pulmonology": 3,
    "Rare Disease": 3,    # Rare Disease/Metabolic + Rare Disease/Neurology + Rare Disease/Cardiology
    "Nephrology": 2,
    "Ophthalmology": 2,
    "Dermatology": 1,
    "Neurology": 2,       # Neurology + Neurology/Immunology
    "Women's Health": 1,
    "Pain Management": 1,
    "Endocrinology": 1,
}

total = 46
today = "2026-07-01"

max_ta = max(ta_consolidated.values())

# Sort by count descending
ta_sorted = sorted(ta_consolidated.items(), key=lambda x: x[1], reverse=True)

def bar(count, max_count, color):
    pct = count / max_count * 100
    return f'''<div class="bar-row">
      <div class="bar-label">{"{}"}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;background:{color}"></div></div>
      <div class="bar-count">{count}</div>
    </div>'''

colors_ta = ["#2657a8","#3473d0","#4a90e2","#6aa3e8","#88b8ef","#a0c8f5",
             "#e85d26","#f07a45","#c8303a","#3e8e6e","#56b38a","#73c9a2","#92dab8","#b0ebd0"]

ta_bars = ""
for i, (ta_name, cnt) in enumerate(ta_sorted):
    pct = cnt / max_ta * 100
    color = colors_ta[i % len(colors_ta)]
    ta_bars += f'''
    <div class="bar-row">
      <div class="bar-label">{ta_name}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;background:{color}"></div></div>
      <div class="bar-count">{cnt}</div>
    </div>'''

# Company data
companies_big = [
    ("Merck", 2), ("Novartis", 2), ("Boehringer Ingelheim", 2), ("Sanofi/Genzyme", 2),
    ("Bayer", 2), ("GlaxoSmithKline", 2),
    ("Daiichi Sankyo", 1), ("Alcon", 1), ("Johnson & Johnson", 1), ("AbbVie", 1),
    ("CSL Behring", 1), ("Regeneron", 1), ("Eli Lilly", 1), ("Otsuka", 1), ("UCB", 1),
]
companies_bio = [
    ("Vertex Pharmaceuticals", 1), ("medac GmbH", 1), ("SpringWorks Therapeutics", 1),
    ("Deciphera Pharmaceuticals", 1), ("Akeso / Chia Tai-Tianqing", 1), ("Verastem Oncology", 1),
    ("Nuvation Bio", 1), ("Dizal Pharmaceutical", 1), ("KalVista Pharmaceuticals", 1),
    ("LEO Pharma", 1), ("PTC Therapeutics", 1), ("LENZ Therapeutics", 1), ("Chimerix", 1),
    ("Insmed", 1), ("Ionis Pharmaceuticals", 1), ("Stealth BioTherapeutics", 1),
    ("Crinetics Pharmaceuticals", 1), ("Kura Oncology", 1), ("Arrowhead Pharmaceuticals", 1),
    ("LIB Therapeutics", 1), ("Innoviva Specialty Therapeutics", 1),
    ("Milestone Pharmaceuticals", 1), ("Cytokinetics", 1), ("Omeros", 1), ("Vanda Pharmaceuticals", 1),
]

n_big = 21
n_bio = 25
pct_big = n_big / total * 100
pct_bio = n_bio / total * 100

# TA oncology breakdown (what types of cancer)
oncology_cancers = [
    ("Breast Cancer", 3), ("NSCLC", 6), ("AML / Leukemia", 3), ("Multiple Myeloma", 1),
    ("Ovarian Cancer", 1), ("Nasopharyngeal Carcinoma", 1), ("Glioma (Brain)", 1), ("TGCT / NF1", 2),
]
onc_bars = ""
for name, cnt in sorted(oncology_cancers, key=lambda x: x[1], reverse=True):
    pct = cnt / max(v for _, v in oncology_cancers) * 100
    onc_bars += f'''
    <div class="bar-row">
      <div class="bar-label">{name}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%;background:#c8303a"></div></div>
      <div class="bar-count">{cnt}</div>
    </div>'''

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2025 Novel Drugs – TA & Company Analysis</title>
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

/* Bar chart */
.bar-row {{
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  gap: 10px;
}}
.bar-label {{
  width: 220px;
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

/* Company donut-style */
.company-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}}
.company-block h3 {{
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 12px;
  color: #16243f;
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

/* Insight cards */
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
    <h1>FDA 2025 Novel Drug Approvals – Therapeutic Area &amp; Company Analysis</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Total 46 novel approvals &nbsp;|&nbsp;
       Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2025" style="color:#fff;text-decoration:underline;" target="_blank">FDA Novel Drug Approvals for 2025</a></p>
  </header>

  <!-- TA Analysis -->
  <div class="section">
    <h2>📊 Therapeutic Area별 승인 현황 (Consolidated)</h2>
    {ta_bars}
  </div>

  <!-- Oncology breakdown -->
  <div class="section">
    <h2>🎗 Oncology 세부 분류 ({sum(v for _,v in oncology_cancers)}개 항암제)</h2>
    {onc_bars}
    <p style="font-size:12px;color:#5b6472;margin-top:12px;">
      * NSCLC(비소세포폐암) 6개: Emrelis(c-Met), Ibtrozi(ROS1), Zegfrovy(EGFR exon20), Hernexeos(HER2), Hyrnuo(HER2), Keytruda Qlex(PD-1 SC formulation)<br>
      * AML/Leukemia 3개: Grafapex(전처치), Komzifti(NPM1+), Lynozyfic(MM포함 혈액암)
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
          {"".join(f"<li>{co} ({cnt})</li>" for co,cnt in companies_big)}
        </ul>
      </div>
      <div class="company-block bio">
        <h3>🔬 Biotech ({n_bio}개)</h3>
        <ul class="co-list">
          {"".join(f"<li>{co} ({cnt})</li>" for co,cnt in companies_bio)}
        </ul>
      </div>
    </div>
  </div>

  <!-- Cross-table -->
  <div class="section cross-table">
    <h2>📋 TA × Company Type 교차 분석 (주요 TA)</h2>
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
        <tr><td>Oncology (모든 암종)</td><td>7</td><td>9</td><td>16</td></tr>
        <tr><td>Hematology</td><td>2</td><td>1</td><td>3</td></tr>
        <tr><td>Immunology (HAE/CSU/MG 포함)</td><td>2</td><td>2</td><td>4</td></tr>
        <tr><td>Infectious Disease</td><td>2</td><td>1</td><td>3</td></tr>
        <tr><td>Cardiovascular / Metabolic</td><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>Pulmonology</td><td>2</td><td>1</td><td>3</td></tr>
        <tr><td>Rare Disease</td><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>Nephrology</td><td>2</td><td>0</td><td>2</td></tr>
        <tr><td>Ophthalmology</td><td>1</td><td>1</td><td>2</td></tr>
        <tr><td>기타 (Women's/Neuro/Endo/Pain/Derm)</td><td>1</td><td>6</td><td>7</td></tr>
        <tr style="font-weight:700;background:#f4f7fd;"><td>합계</td><td>21</td><td>25</td><td>46</td></tr>
      </tbody>
    </table>
  </div>

  <!-- Insights -->
  <div class="section">
    <h2>💡 Key Insights</h2>
    <div class="insights-grid">
      <div class="insight-card">
        <strong>① 항암제 최다 (16/46, 35%)</strong>
        2025년도 2026년과 마찬가지로 항암제가 압도적. 특히 NSCLC 6개 (Emrelis, Ibtrozi, Zegfrovy, Hernexeos, Hyrnuo, Keytruda Qlex) — 바이오마커 기반 정밀의학의 심화 반영.
      </div>
      <div class="insight-card">
        <strong>② Accelerated Approval 22% (10/46)</strong>
        10개 신약이 가속승인. 주로 희귀암·희귀질환 대상. Vanrafia(신장), Forzinity(Barth증후군), Lynozyfic(다발성골수종) 등 unmet need 높은 영역에 집중.
      </div>
      <div class="insight-card">
        <strong>③ Biotech 우세 (25 vs 21)</strong>
        바이오텍이 54%로 빅파마를 앞섰으나 격차는 크지 않음. 빅파마는 Oncology·Nephrology에 집중, 바이오텍은 Rare Disease·Cardiovascular 등 틈새 영역을 공략.
      </div>
      <div class="insight-card">
        <strong>④ HAE (유전성혈관부종) 3종 한해 승인</strong>
        Andembry(예방), Dawnzera(예방), Ekterly(급성발작) — 모두 다른 기전. HAE 치료 패러다임이 다양화되고 경쟁 심화 중. 이미 Haegarda, Takhzyro, Orladeyo 등이 시장에 존재.
      </div>
      <div class="insight-card">
        <strong>⑤ siRNA·ASO 플랫폼 약진</strong>
        Redemplo(plozasiran, siRNA for FCS), Dawnzera(donidalorsen, ASO for HAE). Arrowhead·Ionis 등 핵산의약 플랫폼 기업이 최초 승인 획득하며 상업화 단계 진입.
      </div>
      <div class="insight-card">
        <strong>⑥ 통증치료 새 패러다임 (Journavx)</strong>
        Journavx(suzetrigine)는 25년 만의 새 진통제 기전(Nav1.8 차단)이자 최초 비오피오이드 급성통증치료제. Vertex의 항목에 주목. 만성통증 확장 임상 진행 중.
      </div>
    </div>
  </div>

  <div class="footer">
    FDA 2025 Novel Drug Approvals Analysis &nbsp;|&nbsp; Content as of {today}<br>
    <a href="FDA Novel Drug Approvals 2025 Dashboard.html">← 대시보드로 돌아가기</a>
  </div>

</div>
</body>
</html>"""

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FDA 2025 Novel Drugs - TA and Company Analysis.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Analysis saved to: {output_path}")
