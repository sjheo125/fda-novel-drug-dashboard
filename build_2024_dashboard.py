# -*- coding: utf-8 -*-
"""Build FDA 2024 Novel Drug Approvals Dashboard HTML"""

DAF_BASE = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&varApplNo="
TOC_BASE = "https://www.accessdata.fda.gov/drugsatfda_docs/nda/{year}/{appno}Orig1s000TOC.html"

CBER_PAGES = {
    "Amtagvi":  ("https://www.fda.gov/vaccines-blood-biologics/tissue-cellular-gene-therapies/amtagvi",
                 "https://www.fda.gov/vaccines-blood-biologics/tissue-cellular-gene-therapies/amtagvi"),
    "Aucatzyl": ("https://www.fda.gov/vaccines-blood-biologics/aucatzyl",
                 "https://www.fda.gov/vaccines-blood-biologics/aucatzyl"),
    "Ryoncil":  ("https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/ryoncil",
                 "https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/ryoncil"),
}

def daf_link(appno_num):
    return DAF_BASE + appno_num

def toc_link(appno_num, year=2024):
    return TOC_BASE.format(year=year, appno=appno_num)

# Data tuple:
# (no, name, ingredient, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note)
# toc_year: year where review docs are found on accessdata.fda.gov
# note: "" | "Accelerated Approval" | "Accelerated Approval / Resubmission" | "Resubmission" | "CBER Product"

drugs = [
    (1,  "Zelsuvmi",       "berdazimer gel",                       "2024-01-19",
     "Molluscum contagiosum in patients ≥1 year",
     "Dermatology",         "Botanix Pharma",              "Biotech",    "NDA 217424", "217424", "Original",     2024, ""),

    (2,  "Amtagvi",        "lifileucel",                           "2024-02-16",
     "Unresectable or metastatic melanoma previously treated with a PD-1/PD-L1 blocking antibody and, if BRAF V600-mutant, a BRAF inhibitor",
     "Oncology",            "Iovance Biotherapeutics",     "Biotech",    "BLA STN 125773", "", "Original",      2024, "CBER Product"),

    (3,  "Exblifep",       "cefepime + enmetazobactam",            "2024-02-22",
     "Complicated urinary tract infections including pyelonephritis in adults caused by susceptible gram-negative organisms",
     "Infectious Disease",  "Allecra Therapeutics",        "Biotech",    "NDA 216165", "216165", "Original",    2024, ""),

    (4,  "Letybo",         "letibotulinumtoxinA-wlbg",             "2024-02-29",
     "Temporary improvement in appearance of moderate-to-severe glabellar lines in adults",
     "Dermatology",         "Hugel",                       "Biotech",    "BLA 761225", "761225", "Resubmission", 2024, ""),

    (5,  "Tevimbra",       "tislelizumab-jsgr",                    "2024-03-13",
     "Unresectable or metastatic esophageal squamous cell carcinoma after prior systemic chemotherapy",
     "Oncology",            "BeiGene",                     "Big Pharma", "BLA 761232", "761232", "Original",    2024, ""),

    (6,  "Rezdiffra",      "resmetirom",                           "2024-03-14",
     "Non-cirrhotic MASH with moderate-to-advanced liver fibrosis (F2–F3) as adjunct to diet and exercise",
     "Hepatology",          "Madrigal Pharmaceuticals",    "Biotech",    "NDA 217785", "217785", "Original",    2024, ""),

    (7,  "Tryvio",         "aprocitentan",                         "2024-03-19",
     "Adults with hypertension not adequately controlled on other antihypertensives (combination or add-on)",
     "Cardiovascular",      "Janssen (J&J)",                "Big Pharma", "NDA 217686", "217686", "Original",   2024, ""),

    (8,  "Duvyzat",        "givinostat",                           "2024-03-21",
     "Duchenne muscular dystrophy in patients ≥6 years",
     "Rare Disease",        "ITF Therapeutics / Italfarmaco","Biotech",  "NDA 217865", "217865", "Original",    2024, ""),

    (9,  "Winrevair",      "sotatercept-csrk",                     "2024-03-26",
     "Adults with pulmonary arterial hypertension (PAH, WHO Group I) as add-on to background PAH therapy",
     "Cardiovascular",      "Merck",                       "Big Pharma", "BLA 761363", "761363", "Original",    2024, ""),

    (10, "Vafseo",         "vadadustat",                           "2024-03-27",
     "Anemia due to chronic kidney disease in adults on dialysis",
     "Nephrology",          "Akebia Therapeutics",          "Biotech",   "NDA 215192", "215192", "Resubmission", 2024, ""),

    (11, "Voydeya",        "danicopan",                            "2024-04-02",
     "Extravascular hemolysis as add-on to ravulizumab or eculizumab in adults with PNH",
     "Hematology",          "Alexion / AstraZeneca",        "Big Pharma","NDA 218037", "218037", "Original",    2024, ""),

    (12, "Zevtera",        "ceftobiprole medocaril sodium",        "2024-04-03",
     "Hospital-acquired bacterial pneumonia, community-acquired bacterial pneumonia, and acute bacterial skin and skin structure infections in adults",
     "Infectious Disease",  "Basilea Pharmaceutica",        "Biotech",   "NDA 218275", "218275", "Original",    2024, ""),

    (13, "Lumisight",      "pegulicianine",                        "2024-04-17",
     "Optical imaging agent for intraoperative detection of residual cancerous tissue in the lumpectomy cavity",
     "Oncology",            "Lumicell",                     "Biotech",   "NDA 214511", "214511", "Original",    2024, ""),

    (14, "Anktiva",        "nogapendekin alfa inbakicept-pmln",    "2024-04-22",
     "BCG-unresponsive non-muscle invasive bladder cancer with CIS with or without papillary tumors (with BCG)",
     "Oncology",            "ImmunGene",                    "Biotech",   "BLA 761336", "761336", "Original",    2024, ""),

    (15, "Ojemda",         "tovorafenib",                          "2024-04-23",
     "Relapsed or refractory pediatric low-grade glioma harboring a BRAF fusion or rearrangement, or BRAF V600 mutation (≥6 months)",
     "Oncology",            "Day One Biopharmaceuticals",   "Biotech",   "NDA 218033", "218033", "Original",    2024, "Accelerated Approval"),

    (16, "Imdelltra",      "tarlatamab-dlle",                      "2024-05-16",
     "Extensive-stage small cell lung cancer with disease progression on or after platinum-based chemotherapy",
     "Oncology",            "Amgen",                        "Big Pharma","BLA 761344", "761344", "Original",    2024, "Accelerated Approval"),

    (17, "Rytelo",         "imetelstat",                           "2024-06-06",
     "Low- to intermediate-1 risk MDS with transfusion-dependent anemia requiring ≥4 RBC units/8 weeks, not responsive to ESAs",
     "Hematology",          "Geron Corporation",            "Biotech",   "NDA 217779", "217779", "Original",    2024, ""),

    (18, "Iqirvo",         "elafibranor",                          "2024-06-10",
     "Primary biliary cholangitis with inadequate response to UDCA (with UDCA) or unable to tolerate UDCA (monotherapy)",
     "Hepatology",          "Ipsen",                        "Big Pharma","NDA 218860", "218860", "Original",    2024, "Accelerated Approval"),

    (19, "Sofdra",         "sofpironium bromide",                  "2024-06-18",
     "Primary axillary hyperhidrosis in adults and pediatric patients ≥9 years",
     "Dermatology",         "Botanix Pharma",               "Biotech",   "NDA 217347", "217347", "Original",   2024, ""),

    (20, "Piasky",         "crovalimab-akkz",                      "2024-06-20",
     "Paroxysmal nocturnal hemoglobinuria in adults and pediatric patients ≥13 years weighing ≥40 kg",
     "Hematology",          "Genentech / Roche",            "Big Pharma","BLA 761388", "761388", "Original",   2024, ""),

    (21, "Xolremdi",       "mavorixafor",                          "2024-06-20",
     "WHIM syndrome in adults and pediatric patients ≥12 years",
     "Rare Disease",        "X4 Pharmaceuticals",           "Biotech",   "NDA 218709", "218709", "Original",   2024, ""),

    (22, "Ohtuvayre",      "ensifentrine",                         "2024-06-26",
     "Maintenance treatment of chronic obstructive pulmonary disease (COPD) in adults",
     "Pulmonology",         "Verona Pharma",                "Biotech",   "NDA 217389", "217389", "Original",   2024, ""),

    (23, "Kisunla",        "donanemab-azbt",                       "2024-07-02",
     "Early symptomatic Alzheimer's disease (mild cognitive impairment or mild dementia) in adults",
     "Neurology",           "Eli Lilly",                    "Big Pharma","BLA 761248", "761248", "Original",   2024, ""),

    (24, "Leqselvi",       "deuruxolitinib",                       "2024-07-25",
     "Alopecia areata in adults and pediatric patients ≥12 years",
     "Dermatology",         "Sun Pharma",                   "Big Pharma","NDA 217900", "217900", "Original",   2024, ""),

    (25, "Voranigo",       "vorasidenib",                          "2024-08-06",
     "Adults and pediatric patients ≥12 years with residual or recurrent grade 2 astrocytoma or oligodendroglioma with a susceptible IDH1 or IDH2 mutation",
     "Oncology",            "Servier Pharmaceuticals",      "Big Pharma","NDA 218784", "218784", "Original",   2024, ""),

    (26, "Yorvipath",      "palopegteriparatide",                  "2024-08-09",
     "Hypoparathyroidism in adults",
     "Endocrinology",       "Ascendis Pharma",              "Biotech",   "NDA 216490", "216490", "Original",   2024, ""),

    (27, "Nemluvio",       "nemolizumab-ilto",                     "2024-08-12",
     "Prurigo nodularis in adults",
     "Dermatology",         "Galderma",                     "Big Pharma","BLA 761390", "761390", "Original",   2024, "Accelerated Approval"),

    (28, "Livdelzi",       "seladelpar",                           "2024-08-14",
     "Primary biliary cholangitis with inadequate response to UDCA (with UDCA) or unable to tolerate UDCA (monotherapy)",
     "Hepatology",          "CymaBay / Gilead",             "Biotech",   "NDA 217899", "217899", "Original",   2024, "Accelerated Approval"),

    (29, "Niktimvo",       "axatilimab-csfr",                      "2024-08-14",
     "Chronic graft-versus-host disease after failure of ≥2 prior lines of systemic therapy (adults and pediatric patients ≥40 kg)",
     "Oncology / Immunology","Syndax Pharmaceuticals",      "Biotech",   "BLA 761411", "761411", "Original",  2024, "Accelerated Approval"),

    (30, "Lazcluze",       "lazertinib",                           "2024-08-19",
     "EGFR exon 19 deletions or exon 21 L858R-mutated locally advanced or metastatic NSCLC (first-line, with amivantamab-vmjw)",
     "Oncology",            "Janssen (J&J)",                "Big Pharma","NDA 219008", "219008", "Original",   2024, ""),

    (31, "Ebglyss",        "lebrikizumab-lbkz",                    "2024-09-13",
     "Moderate-to-severe atopic dermatitis in adults and pediatric patients ≥12 years not adequately controlled with topical therapies",
     "Dermatology",         "Eli Lilly",                    "Big Pharma","BLA 761306", "761306", "Resubmission",2024, ""),

    (32, "Miplyffa",       "arimoclomol",                          "2024-09-20",
     "Neurological manifestations of Niemann-Pick disease type C (NPC) in adults and patients ≥2 years (with miglustat)",
     "Rare Disease",        "Zevra Therapeutics",           "Biotech",   "NDA 214927", "214927", "Original",   2024, ""),

    (33, "Aqneursa",       "levacetylleucine",                     "2024-09-24",
     "Neurological manifestations of Niemann-Pick disease type C in adults and patients weighing ≥15 kg",
     "Rare Disease",        "IntraBio",                     "Biotech",   "NDA 219132", "219132", "Original",   2024, ""),

    (34, "Cobenfy",        "xanomeline + trospium chloride",       "2024-09-26",
     "Schizophrenia in adults",
     "Psychiatry",          "Bristol-Myers Squibb",         "Big Pharma","NDA 216158", "216158", "Original",   2024, ""),

    (35, "Flyrcado",       "flurpiridaz F 18",                     "2024-09-27",
     "PET myocardial perfusion imaging (MPI) under rest or stress in adults with known or suspected coronary artery disease",
     "Cardiovascular",      "GE HealthCare",                "Big Pharma","NDA 215168", "215168", "Original",   2024, ""),

    (36, "Itovebi",        "inavolisib",                           "2024-10-09",
     "PIK3CA-mutated HR-positive, HER2-negative locally advanced or metastatic breast cancer with disease progression on/after endocrine therapy (with palbociclib + fulvestrant)",
     "Oncology",            "Genentech / Roche",            "Big Pharma","NDA 219249", "219249", "Original",   2024, "Accelerated Approval"),

    (37, "Hympavzi",       "marstacimab-hncq",                     "2024-10-11",
     "Routine prophylaxis to prevent or reduce bleeding in adults and patients ≥12 years with hemophilia A without FVIII inhibitors or hemophilia B without FIX inhibitors",
     "Hematology",          "Pfizer",                       "Big Pharma","BLA 761369", "761369", "Original",   2024, ""),

    (38, "Vyloy",          "zolbetuximab-clzb",                    "2024-10-18",
     "CLDN18.2-positive, HER2-negative locally advanced unresectable or metastatic gastric or GEJ adenocarcinoma (first-line, with fluoropyrimidine- and platinum-based chemotherapy)",
     "Oncology",            "Astellas",                     "Big Pharma","BLA 761365", "761365", "Resubmission",2024, ""),

    (39, "Orlynvah",       "sulopenem etzadroxil + probenecid",    "2024-10-24",
     "Uncomplicated urinary tract infections caused by susceptible microorganisms in adult women",
     "Infectious Disease",  "Iterum Therapeutics",          "Biotech",   "NDA 213972", "213972", "Original",   2024, ""),

    (40, "Ziihera",        "zanidatamab-hrii",                     "2024-11-06",
     "Previously treated, unresectable or metastatic HER2-positive (IHC 3+) biliary tract cancer",
     "Oncology",            "Jazz Pharmaceuticals",         "Big Pharma","BLA 761416", "761416", "Original",   2024, "Accelerated Approval"),

    (41, "Aucatzyl",       "obecabtagene autoleucel",              "2024-11-08",
     "Relapsed or refractory B-cell precursor acute lymphoblastic leukemia in adults",
     "Oncology",            "Autolus Therapeutics",         "Biotech",   "BLA STN 125813","",  "Original",    2024, "CBER Product"),

    (42, "Revuforj",       "revumenib",                            "2024-11-15",
     "Relapsed or refractory acute leukemia with a KMT2A translocation in adults and patients ≥1 year",
     "Oncology",            "Syndax Pharmaceuticals",       "Biotech",   "NDA 218944", "218944", "Original",   2024, "Accelerated Approval"),

    (43, "Bizengri",       "zenocutuzumab-zbco",                   "2024-11-21",
     "NRG1 gene fusion-positive locally advanced or metastatic non-small cell lung cancer or pancreatic adenocarcinoma in adults after prior systemic therapy",
     "Oncology",            "Merus",                        "Biotech",   "BLA 761352", "761352", "Original",   2024, "Accelerated Approval"),

    (44, "Attruby",        "acoramidis",                           "2024-11-22",
     "Cardiomyopathy of wild-type or variant transthyretin-mediated amyloidosis (ATTR-CM) to reduce cardiovascular death and cardiovascular-related hospitalization",
     "Cardiovascular",      "BridgeBio Pharma",             "Biotech",   "NDA 216540", "216540", "Original",   2024, ""),

    (45, "Unloxcyt",       "cosibelimab-ipdl",                     "2024-12-13",
     "Metastatic cutaneous squamous cell carcinoma or locally advanced CSCC not eligible for curative surgery or radiation",
     "Oncology",            "Checkpoint Therapeutics",      "Biotech",   "BLA 761297", "761297", "Original",   2025, ""),

    (46, "Ensacove",       "ensartinib",                           "2024-12-13",
     "Adults with ALK-positive locally advanced or metastatic NSCLC who have not previously received an ALK inhibitor",
     "Oncology",            "Xcovery Holdings",             "Biotech",   "NDA 218171", "218171", "Original",   2025, ""),

    (47, "Ryoncil",        "remestemcel-L-rknd",                   "2024-12-18",
     "Steroid-refractory acute graft-versus-host disease in pediatric patients ≥2 months",
     "Oncology / Immunology","Mesoblast",                   "Biotech",   "BLA STN 125706","",  "Original",    2024, "CBER Product"),

    (48, "Alyftrek",       "vanzacaftor / tezacaftor / deutivacaftor","2024-12-20",
     "Cystic fibrosis in patients ≥6 years with at least one F508del mutation or another responsive mutation in the CFTR gene",
     "Pulmonology",         "Vertex Pharmaceuticals",       "Biotech",   "NDA 218730", "218730", "Original",   2025, ""),

    (49, "Alhemo",         "concizumab-mtci",                      "2024-12-20",
     "Routine prophylaxis to prevent or reduce bleeding in adults and patients ≥12 years with hemophilia A or B with inhibitors",
     "Hematology",          "Novo Nordisk",                 "Big Pharma","BLA 761315", "761315", "Original",   2025, ""),

    (50, "Opdivo Qvantig", "nivolumab + hyaluronidase-nvhy",        "2024-12-27",
     "Subcutaneous formulation for all approved IV nivolumab indications in adults and pediatric patients ≥12 years",
     "Oncology",            "Bristol-Myers Squibb",         "Big Pharma","BLA 761381", "761381", "Original",   2025, ""),
]

# --- HTML Generation ---
today = "2026-07-01"

rows_html = ""
for (no, name, ing, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note) in drugs:
    # Handle CBER products (no standard CDER Drugs@FDA link)
    if name in CBER_PAGES:
        daf_url, toc_url = CBER_PAGES[name]
        daf_cell = f'<a href="{daf_url}" target="_blank">FDA CBER</a>'
        toc_cell = f'<a href="{toc_url}" target="_blank">CBER Page</a>'
    else:
        daf_url = daf_link(appno_num)
        toc_url = toc_link(appno_num, toc_year)
        daf_cell = f'<a href="{daf_url}" target="_blank">Drugs@FDA</a>'
        toc_cell = f'<a href="{toc_url}" target="_blank">TOC</a>'

    # Note badge
    note_parts = []
    if "Accelerated Approval" in note:
        note_parts.append("Accelerated Approval")
    if submission == "Resubmission":
        note_parts.append("Resubmission")
    if "CBER" in note:
        note_parts.append("CBER")
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
      <td>{daf_cell}</td>
      <td>{toc_cell}</td>
      <td class="note-cell">{note_cell}</td>
    </tr>"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2024 Novel Drug Approvals Dashboard</title>
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
    <h1>FDA 2024 Novel Drug Approvals Dashboard</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Source: FDA Novel Drug Approvals 2024 &nbsp;|&nbsp; Total: 50 novel drug approvals</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card"><div class="val">50</div><div class="lbl">Total Novel Approvals</div></div>
    <div class="stat-card"><div class="val">21</div><div class="lbl">Big Pharma</div></div>
    <div class="stat-card"><div class="val">29</div><div class="lbl">Biotech</div></div>
    <div class="stat-card"><div class="val">10</div><div class="lbl">Accelerated Approval</div></div>
    <div class="stat-card"><div class="val">4</div><div class="lbl">Resubmission</div></div>
    <div class="stat-card"><div class="val">19</div><div class="lbl">Oncology Drugs</div></div>
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
    Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2024" target="_blank">FDA Novel Drug Approvals for 2024</a>
    &nbsp;|&nbsp; TOC links: accessdata.fda.gov &nbsp;|&nbsp; CBER products: fda.gov/vaccines-blood-biologics &nbsp;|&nbsp; Built: {today}
  </div>

</div>
</body>
</html>"""

output_path = r"C:\0_MBA\Healthcare\FDA New Drug Approval Dashboard\FDA Novel Drug Approvals 2024 Dashboard.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Dashboard saved to: {output_path}")
print(f"Total drugs: {len(drugs)}")
big_pharma = sum(1 for d in drugs if d[7] == "Big Pharma")
accel = sum(1 for d in drugs if "Accelerated" in d[12])
resub = sum(1 for d in drugs if d[10] == "Resubmission")
cber = sum(1 for d in drugs if "CBER" in d[12])
print(f"Big Pharma: {big_pharma}, Biotech: {len(drugs)-big_pharma}")
print(f"Accelerated Approval: {accel}, Resubmission: {resub}, CBER: {cber}")
