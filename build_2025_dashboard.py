# -*- coding: utf-8 -*-
import os
"""Build FDA 2025 Novel Drug Approvals Dashboard HTML"""

DAF_BASE = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&varApplNo="
DAF_SEARCH = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm"
TOC_BASE = "https://www.accessdata.fda.gov/drugsatfda_docs/nda/{year}/{appno}Orig1s000TOC.html"

def daf_link(appno_num):
    return DAF_BASE + appno_num

def toc_link(appno_num, year=2025):
    return TOC_BASE.format(year=year, appno=appno_num)

# Data tuple: (no, name, ingredient, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note)
# toc_year: 2025 or 2026 (based on where review docs are located)
# note: "" or "Accelerated Approval" or "Resubmission"

drugs = [
    # no, name, ingredient, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note
    (1, "Datroway", "datopotamab deruxtecan-dlnk", "2025-01-17",
     "Unresectable or metastatic HR-positive, HER2-negative breast cancer with prior endocrine-based therapy and chemotherapy",
     "Oncology", "Daiichi Sankyo", "Big Pharma", "BLA 761394", "761394", "Original", 2025, ""),

    (2, "Grafapex", "treosulfan", "2025-01-21",
     "Preparative regimen for allogeneic HSCT in adult and pediatric patients ≥1 year with AML or MDS (with fludarabine)",
     "Oncology / Hematology", "medac GmbH", "Biotech", "NDA 214759", "214759", "Original", 2025, ""),

    (3, "Journavx", "suzetrigine", "2025-01-30",
     "Moderate-to-severe acute pain in adults",
     "Pain Management", "Vertex Pharmaceuticals", "Biotech", "NDA 219209", "219209", "Original", 2025, ""),

    (4, "Gomekli", "mirdametinib", "2025-02-11",
     "Adults and pediatric patients ≥2 years with neurofibromatosis type 1 (NF1) with symptomatic plexiform neurofibromas not amenable to complete resection",
     "Oncology", "SpringWorks Therapeutics", "Biotech", "NDA 219389", "219389", "Original", 2025, ""),

    (5, "Romvimza", "vimseltinib", "2025-02-14",
     "Symptomatic tenosynovial giant cell tumor (TGCT) for which surgical resection will potentially cause worsening functional limitation or severe morbidity",
     "Oncology", "Deciphera Pharmaceuticals", "Biotech", "NDA 219304", "219304", "Original", 2025, ""),

    (6, "Blujepa", "gepotidacin", "2025-03-25",
     "Uncomplicated urinary tract infections (uUTI) in female adult and pediatric patients ≥12 years weighing ≥40 kg",
     "Infectious Disease", "GlaxoSmithKline", "Big Pharma", "NDA 218230", "218230", "Original", 2025, ""),

    (7, "Qfitlia", "fitusiran", "2025-03-28",
     "Prophylaxis to prevent or reduce bleeding episodes in adults and pediatric patients ≥12 years with hemophilia A or B with or without inhibitors",
     "Hematology", "Sanofi/Genzyme", "Big Pharma", "NDA 219019", "219019", "Original", 2025, ""),

    (8, "Vanrafia", "atrasentan", "2025-04-02",
     "Reduction of proteinuria in adults with primary IgA nephropathy (IgAN) at risk of rapid disease progression",
     "Nephrology", "Novartis", "Big Pharma", "NDA 219208", "219208", "Original", 2025, "Accelerated Approval"),

    (9, "Penpulimab-kcqx", "penpulimab-kcqx", "2025-04-23",
     "In combination with chemotherapy for first-line treatment of adults with recurrent or metastatic non-keratinizing nasopharyngeal carcinoma; or monotherapy for platinum-resistant/refractory disease",
     "Oncology", "Akeso / Chia Tai-Tianqing", "Biotech", "BLA 761258", "761258", "Original", 2025, ""),

    (10, "Imaavy", "nipocalimab-aahu", "2025-04-29",
     "Generalized myasthenia gravis in adults who are anti-AChR antibody positive",
     "Neurology / Immunology", "Johnson & Johnson", "Big Pharma", "BLA 761430", "761430", "Original", 2025, ""),

    (11, "Avmapki Fakzynja", "avutometinib + defactinib", "2025-05-08",
     "Adults with KRAS-mutated recurrent low-grade serous ovarian cancer (LGSOC) who have received prior systemic therapy",
     "Oncology", "Verastem Oncology", "Biotech", "NDA 219616", "219616", "Original", 2025, "Accelerated Approval"),

    (12, "Emrelis", "telisotuzumab vedotin-tllv", "2025-05-14",
     "Adults with locally advanced or metastatic non-squamous NSCLC with high c-Met protein overexpression who received prior systemic therapy",
     "Oncology", "AbbVie", "Big Pharma", "BLA 761384", "761384", "Original", 2025, "Accelerated Approval"),

    (13, "Tryptyr", "acoltremon", "2025-05-28",
     "Signs and symptoms of dry eye disease (DED) in adults",
     "Ophthalmology", "Alcon", "Big Pharma", "NDA 217370", "217370", "Original", 2025, ""),

    (14, "Enflonsia", "clesrovimab-cfor", "2025-06-09",
     "Prevention of RSV lower respiratory tract disease in neonates and infants born during or entering their first RSV season",
     "Infectious Disease", "Merck", "Big Pharma", "BLA 761432", "761432", "Original", 2025, ""),

    (15, "Ibtrozi", "taletrectinib", "2025-06-11",
     "Adults with locally advanced or metastatic ROS1-positive NSCLC",
     "Oncology", "Nuvation Bio", "Biotech", "NDA 219713", "219713", "Original", 2025, ""),

    (16, "Andembry", "garadacimab-gxii", "2025-06-16",
     "Prophylaxis to prevent attacks of hereditary angioedema (HAE) in adults and pediatric patients ≥12 years",
     "Immunology", "CSL Behring", "Big Pharma", "BLA 761367", "761367", "Resubmission", 2025, ""),

    (17, "Lynozyfic", "linvoseltamab-gcpt", "2025-07-02",
     "Adults with relapsed or refractory multiple myeloma who have received ≥4 prior lines of therapy",
     "Oncology", "Regeneron", "Big Pharma", "BLA 761400", "761400", "Original", 2025, "Accelerated Approval"),

    (18, "Zegfrovy", "sunvozertinib", "2025-07-02",
     "Adults with locally advanced or metastatic non-squamous NSCLC with EGFR exon 20 insertion mutations, progressed on/after platinum-based chemotherapy",
     "Oncology", "Dizal (Jiangsu) Pharmaceutical", "Biotech", "NDA 219839", "219839", "Original", 2025, "Accelerated Approval"),

    (19, "Ekterly", "sebetralstat", "2025-07-03",
     "Acute attacks of hereditary angioedema (HAE) in adults and pediatric patients ≥12 years",
     "Immunology", "KalVista Pharmaceuticals", "Biotech", "NDA 219301", "219301", "Original", 2025, ""),

    (20, "Anzupgo", "delgocitinib", "2025-07-23",
     "Moderate to severe chronic hand eczema (CHE) in adults with inadequate response to topical corticosteroids",
     "Dermatology", "LEO Pharma", "Biotech", "NDA 219155", "219155", "Original", 2025, ""),

    (21, "Sephience", "sepiapterin", "2025-07-28",
     "Hyperphenylalaninemia (HPA) in adults and pediatric patients ≥1 month with sepiapterin-responsive phenylketonuria (PKU)",
     "Rare Disease / Metabolic", "PTC Therapeutics", "Biotech", "NDA 219666", "219666", "Original", 2025, ""),

    (22, "Vizz", "aceclidine", "2025-07-31",
     "Presbyopia in adults",
     "Ophthalmology", "LENZ Therapeutics", "Biotech", "NDA 218585", "218585", "Original", 2025, ""),

    (23, "Modeyso", "dordaviprone", "2025-08-06",
     "Adults and pediatric patients ≥1 year with diffuse midline glioma harboring an H3 K27M mutation with progressive disease following prior therapy",
     "Oncology", "Chimerix", "Biotech", "NDA 219876", "219876", "Original", 2025, "Accelerated Approval"),

    (24, "Hernexeos", "zongertinib", "2025-08-08",
     "Adults with unresectable or metastatic non-squamous NSCLC with HER2 TKD activating mutations who have received prior systemic therapy",
     "Oncology", "Boehringer Ingelheim", "Big Pharma", "NDA 219042", "219042", "Original", 2025, "Accelerated Approval"),

    (25, "Brinsupri", "brensocatib", "2025-08-12",
     "Non-cystic fibrosis bronchiectasis (NCFB) in adults and pediatric patients ≥12 years",
     "Pulmonology", "Insmed", "Biotech", "NDA 217673", "217673", "Original", 2025, ""),

    (26, "Dawnzera", "donidalorsen", "2025-08-21",
     "Prophylaxis to prevent attacks of hereditary angioedema (HAE) in adults and pediatric patients ≥12 years",
     "Immunology", "Ionis Pharmaceuticals", "Biotech", "NDA 219407", "219407", "Original", 2025, ""),

    (27, "Wayrilz", "rilzabrutinib", "2025-08-29",
     "Adults with persistent or chronic immune thrombocytopenia (ITP) who have had an insufficient response to a previous treatment",
     "Hematology", "Sanofi/Genzyme", "Big Pharma", "NDA 219685", "219685", "Original", 2025, ""),

    (28, "Keytruda Qlex", "pembrolizumab + berahyaluronidase alfa-pmph", "2025-09-19",
     "Adults and pediatric patients ≥12 years: solid tumor indications approved for IV pembrolizumab (subcutaneous formulation)",
     "Oncology", "Merck", "Big Pharma", "BLA 761467", "761467", "Original", 2025, ""),

    (29, "Forzinity", "elamipretide", "2025-09-19",
     "Adults and pediatric patients with Barth syndrome weighing ≥30 kg to improve muscle strength",
     "Rare Disease / Cardiology", "Stealth BioTherapeutics", "Biotech", "NDA 215244", "215244", "Original", 2025, "Accelerated Approval"),

    (30, "Inluriyo", "imlunestrant", "2025-09-25",
     "Adults with ER-positive, HER2-negative, ESR1-mutated advanced or metastatic breast cancer with disease progression following ≥1 line of endocrine therapy",
     "Oncology", "Eli Lilly", "Big Pharma", "NDA 218881", "218881", "Original", 2025, ""),

    (31, "Palsonify", "paltusotine", "2025-09-25",
     "Adults with acromegaly who had an inadequate response to surgery and/or for whom surgery is not an option",
     "Endocrinology", "Crinetics Pharmaceuticals", "Biotech", "NDA 219070", "219070", "Original", 2025, ""),

    (32, "Rhapsido", "remibrutinib", "2025-09-30",
     "Adults with chronic spontaneous urticaria (CSU) who remain symptomatic despite H1 antihistamine treatment",
     "Dermatology / Immunology", "Novartis", "Big Pharma", "NDA 218436", "218436", "Original", 2025, ""),

    (33, "Jascayd", "nerandomilast", "2025-10-07",
     "Adults with idiopathic pulmonary fibrosis (IPF)",
     "Pulmonology", "Boehringer Ingelheim", "Big Pharma", "NDA 218764", "218764", "Original", 2025, ""),

    (34, "Lynkuet", "elinzanetant", "2025-10-24",
     "Moderate to severe vasomotor symptoms (hot flashes) due to menopause",
     "Women's Health", "Bayer", "Big Pharma", "NDA 219469", "219469", "Original", 2025, ""),

    (35, "Kygevvi", "doxecitine + doxribtimine", "2025-11-03",
     "Adults and pediatric patients with thymidine kinase 2 deficiency (TK2d)",
     "Rare Disease / Neurology", "UCB", "Big Pharma", "NDA 219792", "219792", "Original", 2025, ""),

    (36, "Komzifti", "ziftomenib", "2025-11-13",
     "Adults with relapsed or refractory acute myeloid leukemia (AML) with a susceptible NPM1 mutation",
     "Oncology / Hematology", "Kura Oncology", "Biotech", "NDA 220305", "220305", "Original", 2025, ""),

    (37, "Redemplo", "plozasiran", "2025-11-18",
     "Adjunct to diet to reduce triglycerides in adults with familial chylomicronemia syndrome (FCS)",
     "Cardiovascular / Metabolic", "Arrowhead Pharmaceuticals", "Biotech", "NDA 219947", "219947", "Original", 2025, ""),

    (38, "Hyrnuo", "sevabertinib", "2025-11-19",
     "Adults with locally advanced or metastatic non-squamous NSCLC with HER2 TKD activating mutations who have received prior systemic therapy",
     "Oncology", "Bayer", "Big Pharma", "NDA 219972", "219972", "Original", 2025, "Accelerated Approval"),

    (39, "Voyxact", "sibeprenlimab-szsi", "2025-11-25",
     "Reduction of proteinuria in adults with primary IgA nephropathy (IgAN) at risk for disease progression",
     "Nephrology", "Otsuka Pharmaceutical", "Big Pharma", "BLA 761434", "761434", "Original", 2025, "Accelerated Approval"),

    (40, "Lerochol", "lerodalcibep-liga", "2025-12-12",
     "Adjunct to diet and exercise to reduce LDL-C in adults with hypercholesterolemia, including heterozygous familial hypercholesterolemia (HeFH)",
     "Cardiovascular", "LIB Therapeutics", "Biotech", "BLA 761427", "761427", "Original", 2026, ""),

    (41, "Nuzolvence", "zoliflodacin", "2025-12-12",
     "Uncomplicated urogenital gonorrhea in adults and adolescents",
     "Infectious Disease", "Innoviva Specialty Therapeutics", "Biotech", "NDA 219491", "219491", "Original", 2026, ""),

    (42, "Cardamyst", "etripamil", "2025-12-12",
     "Conversion of acute symptomatic episodes of paroxysmal supraventricular tachycardia (PSVT) to sinus rhythm in adults",
     "Cardiovascular", "Milestone Pharmaceuticals", "Biotech", "NDA 218571", "218571", "Resubmission", 2026, ""),

    (43, "Myqorzo", "aficamten", "2025-12-19",
     "Adults with symptomatic obstructive hypertrophic cardiomyopathy (oHCM) to improve functional capacity and symptoms",
     "Cardiovascular", "Cytokinetics", "Biotech", "NDA 219083", "219083", "Original", 2026, ""),

    (44, "Exdensur", "depemokimab-ulaa", "2025-12-16",
     "Add-on maintenance treatment for severe asthma with eosinophilic phenotype in adults and pediatric patients ≥12 years",
     "Pulmonology", "GlaxoSmithKline", "Big Pharma", "BLA 761458", "761458", "Original", 2026, ""),

    (45, "Yartemlea", "narsoplimab-wuug", "2025-12-23",
     "Adults and pediatric patients ≥2 years with hematopoietic stem cell transplant-associated thrombotic microangiopathy (TA-TMA)",
     "Hematology / Rare Disease", "Omeros", "Biotech", "BLA 761152", "761152", "Resubmission", 2026, ""),

    (46, "Nereus", "tradipitant", "2025-12-30",
     "Prevention of vomiting induced by motion in adults",
     "Neurology", "Vanda Pharmaceuticals", "Biotech", "NDA 220152", "220152", "Original", 2026, ""),
]

# --- HTML Generation ---
today = "2026-07-01"

rows_html = ""
for (no, name, ing, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note) in drugs:
    daf_url = daf_link(appno_num)
    toc_url = toc_link(appno_num, toc_year)

    # Note badge
    note_parts = []
    if note:
        note_parts.append(note)
    if submission == "Resubmission":
        note_parts.append("Resubmission")

    note_cell = ""
    if note_parts:
        note_cell = " / ".join(note_parts)

    # Company type badge
    co_badge_class = "badge-bigpharma" if co_type == "Big Pharma" else "badge-biotech"
    co_badge = f'<span class="co-badge {co_badge_class}">{co_type}</span>'

    rows_html += f"""
    <tr>
      <td class="num">{no}</td>
      <td class="drug-name">{name}</td>
      <td>{ing}</td>
      <td class="date">{date}</td>
      <td class="use-cell">{use}</td>
      <td><span class="ta-tag">{ta}</span></td>
      <td>{company}<br>{co_badge}</td>
      <td class="appno">{appno_disp}</td>
      <td class="submission {'sub-original' if submission == 'Original' else 'sub-resub'}">{submission}</td>
      <td><a href="{daf_url}" target="_blank">Drugs@FDA</a></td>
      <td><a href="{toc_url}" target="_blank">TOC</a></td>
      <td class="note-cell">{note_cell}</td>
    </tr>"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2025 Novel Drug Approvals Dashboard</title>
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css');

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: "Pretendard", "Segoe UI", -apple-system, "Apple SD Gothic Neo", Arial, sans-serif;
  font-size: 13px;
  background: #f0f2f7;
  color: #1f2328;
  -webkit-font-smoothing: antialiased;
}}

.page-wrap {{
  max-width: 1600px;
  margin: 0 auto;
  padding: 32px 24px;
}}

header {{
  background: linear-gradient(135deg, #1a3a6e 0%, #2657a8 100%);
  color: #fff;
  padding: 28px 36px 24px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 4px 16px rgba(26,58,110,0.18);
}}

header h1 {{
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.03em;
  margin-bottom: 6px;
}}

header p {{
  font-size: 13px;
  opacity: 0.82;
  line-height: 1.6;
}}

.stats-bar {{
  display: flex;
  gap: 14px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}}

.stat-card {{
  background: #fff;
  border-radius: 10px;
  padding: 14px 20px;
  box-shadow: 0 2px 8px rgba(20,30,60,0.07);
  flex: 1;
  min-width: 140px;
  text-align: center;
}}

.stat-card .val {{
  font-size: 28px;
  font-weight: 700;
  color: #2657a8;
  line-height: 1;
}}

.stat-card .lbl {{
  font-size: 11px;
  color: #5b6472;
  margin-top: 5px;
}}

.table-wrap {{
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(20,30,60,0.08);
  overflow-x: auto;
}}

table {{
  width: 100%;
  border-collapse: collapse;
}}

thead th {{
  background: #1a3a6e;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  padding: 11px 10px;
  text-align: left;
  white-space: nowrap;
  letter-spacing: 0.01em;
  position: sticky;
  top: 0;
  z-index: 2;
}}

thead th:first-child {{ border-radius: 10px 0 0 0; }}
thead th:last-child {{ border-radius: 0 10px 0 0; }}

tbody tr {{
  border-bottom: 1px solid #e6e8ec;
  transition: background 0.12s;
}}

tbody tr:hover {{ background: #f4f7fd; }}
tbody tr:last-child {{ border-bottom: none; }}

td {{
  padding: 9px 10px;
  vertical-align: top;
  line-height: 1.5;
  letter-spacing: -0.01em;
  color: #1f2328;
}}

td.num {{ color: #8a94a6; font-size: 11px; text-align: center; width: 36px; }}
td.drug-name {{ font-weight: 700; color: #16243f; font-size: 13.5px; white-space: nowrap; }}
td.date {{ white-space: nowrap; font-size: 12px; color: #3a4a6b; }}
td.appno {{ font-family: monospace; font-size: 12px; white-space: nowrap; color: #2657a8; }}
td.use-cell {{ font-size: 12px; color: #3a4a6b; max-width: 280px; }}
td.note-cell {{ font-size: 11px; color: #e07020; font-weight: 600; white-space: nowrap; }}

td.submission {{ font-size: 11px; font-weight: 600; white-space: nowrap; }}
td.sub-original {{ color: #1e7e34; }}
td.sub-resub {{ color: #b85c00; }}

.ta-tag {{
  display: inline-block;
  padding: 3px 8px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  background: #eef1fa;
  color: #2657a8;
  white-space: nowrap;
}}

.co-badge {{
  display: inline-block;
  padding: 2px 7px;
  border-radius: 20px;
  font-size: 10px;
  font-weight: 700;
  margin-top: 3px;
  letter-spacing: 0.02em;
}}

.badge-bigpharma {{ background: #16243f; color: #fff; }}
.badge-biotech {{ background: #2657a8; color: #fff; }}

a {{
  color: #2657a8;
  text-decoration: none;
  font-weight: 500;
  font-size: 12px;
}}

a:hover {{ text-decoration: underline; color: #1a3a6e; }}

.footer {{
  margin-top: 20px;
  font-size: 11.5px;
  color: #8a94a6;
  text-align: center;
  line-height: 1.8;
}}
</style>
</head>
<body>
<div class="page-wrap">

  <header>
    <h1>FDA 2025 Novel Drug Approvals Dashboard</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Source: FDA Novel Drug Approvals 2025 &nbsp;|&nbsp; Total: 46 novel drug approvals</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card"><div class="val">46</div><div class="lbl">Total Novel Approvals</div></div>
    <div class="stat-card"><div class="val">21</div><div class="lbl">Big Pharma</div></div>
    <div class="stat-card"><div class="val">25</div><div class="lbl">Biotech</div></div>
    <div class="stat-card"><div class="val">10</div><div class="lbl">Accelerated Approval</div></div>
    <div class="stat-card"><div class="val">3</div><div class="lbl">Resubmission</div></div>
    <div class="stat-card"><div class="val">14</div><div class="lbl">Oncology Drugs</div></div>
  </div>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>No.</th>
          <th>Drug Name</th>
          <th>Active Ingredient</th>
          <th>Approval Date</th>
          <th>FDA-Approved Use</th>
          <th>Therapeutic Area</th>
          <th>Company</th>
          <th>Application No.</th>
          <th>Submission</th>
          <th>Drugs@FDA</th>
          <th>FDA Review (TOC)</th>
          <th>Note</th>
        </tr>
      </thead>
      <tbody>{rows_html}
      </tbody>
    </table>
  </div>

  <div class="footer">
    Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2025" target="_blank">FDA Novel Drug Approvals for 2025</a>
    &nbsp;|&nbsp; TOC links: accessdata.fda.gov &nbsp;|&nbsp; Built: {today}
  </div>

</div>
</body>
</html>"""

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FDA Novel Drug Approvals 2025 Dashboard.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Dashboard saved to: {output_path}")
print(f"Total drugs: {len(drugs)}")
big_pharma = sum(1 for d in drugs if d[7] == "Big Pharma")
accel = sum(1 for d in drugs if "Accelerated" in d[12])
resub = sum(1 for d in drugs if d[10] == "Resubmission")
print(f"Big Pharma: {big_pharma}, Biotech: {len(drugs)-big_pharma}")
print(f"Accelerated Approval: {accel}, Resubmission: {resub}")
