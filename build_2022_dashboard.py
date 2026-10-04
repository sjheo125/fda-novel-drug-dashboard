# -*- coding: utf-8 -*-
import os
"""Build FDA 2022 Novel Drug Approvals Dashboard HTML"""

DAF_BASE = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&varApplNo="
TOC_BASE = "https://www.accessdata.fda.gov/drugsatfda_docs/nda/{year}/{appno}Orig1s000TOC.html"

CUSTOM_TOC = {}

def daf_link(appno_num):
    return DAF_BASE + appno_num

def toc_link(appno_num, year=2022):
    return TOC_BASE.format(year=year, appno=appno_num)

# Data tuple:
# (no, name, ingredient, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note)

drugs = [
    (1,  "Quviviq",   "daridorexant",                   "2022-01-13",
     "Treatment of adults with insomnia (dual orexin receptor antagonist; nightly oral tablet)",
     "Neurology", "Idorsia Pharmaceuticals", "Biotech", "NDA 214985", "214985", "Original", 2022, ""),

    (2,  "Cibinqo",   "abrocitinib",                    "2022-01-14",
     "Moderate-to-severe atopic dermatitis in adults and adolescents ≥12 years (JAK1 inhibitor; oral)",
     "Dermatology", "Pfizer", "Big Pharma", "NDA 213871", "213871", "Original", 2022, ""),

    (3,  "Kimmtrak",  "tebentafusp-tebn",               "2022-01-25",
     "HLA-A*02:01-positive adults with unresectable or metastatic uveal melanoma (first-in-class ImmTAC bispecific)",
     "Oncology", "Immunocore", "Biotech", "BLA 761228", "761228", "Original", 2022,
     "First-in-class ImmTAC (Immune mobilizing monoclonal T-cell receptor Against Cancer) therapy; first bispecific approved for uveal melanoma"),

    (4,  "Vabysmo",   "faricimab-svoa",                 "2022-01-28",
     "Neovascular (wet) AMD and diabetic macular edema (DME) in adults (anti-VEGF-A + anti-Ang-2 bispecific; intravitreal injection)",
     "Ophthalmology", "Genentech / Roche", "Big Pharma", "BLA 761235", "761235", "Original", 2022,
     "First bispecific antibody approved for an ophthalmic indication; allows up to every-4-month dosing"),

    (5,  "Enjaymo",   "sutimlimab-jome",                "2022-02-15",
     "Decrease the need for red blood cell transfusion due to hemolysis in adults with cold agglutinin disease (CAD)",
     "Hematology", "Sanofi", "Big Pharma", "BLA 761164", "761164", "Original", 2022,
     "First treatment specifically approved for CAD; classical complement pathway (C1s) inhibitor"),

    (6,  "Pyrukynd",  "mitapivat",                      "2022-02-17",
     "Hemolytic anemia in adults with pyruvate kinase (PK) deficiency (first oral PK activator)",
     "Hematology", "Agios Pharmaceuticals", "Biotech", "NDA 216196", "216196", "Original", 2022,
     "First-ever FDA-approved treatment for pyruvate kinase deficiency"),

    (7,  "Vonjo",     "pacritinib",                     "2022-02-28",
     "Adults with intermediate or high-risk primary or secondary myelofibrosis with a platelet count <50×10⁹/L (JAK2/FLT3 inhibitor)",
     "Oncology", "CTI BioPharma", "Biotech", "NDA 208712", "208712", "Original", 2022,
     "Accelerated Approval – Only JAK inhibitor approved for severely thrombocytopenic myelofibrosis patients"),

    (8,  "Ztalmy",    "ganaxolone",                     "2022-03-18",
     "Seizures associated with CDKL5 deficiency disorder (CDD) in patients ≥2 years (neuroactive steroid GABA-A modulator; oral suspension)",
     "Neurology", "Marinus Pharmaceuticals", "Biotech", "NDA 215904", "215904", "Original", 2022,
     "First FDA-approved treatment for CDKL5 deficiency disorder (CDD)"),

    (9,  "Opdualag",  "nivolumab and relatlimab-rmbw",  "2022-03-18",
     "Unresectable or metastatic melanoma in adults and pediatric patients ≥12 years (fixed-dose combination of PD-1 + LAG-3 inhibitors)",
     "Oncology", "Bristol-Myers Squibb", "Big Pharma", "BLA 761234", "761234", "Original", 2022,
     "First FDA-approved LAG-3 blocking antibody combination; first new IO combo mechanism in melanoma in years"),

    (10, "Pluvicto",  "lutetium Lu 177 vipivotide tetraxetan", "2022-03-23",
     "PSMA-positive metastatic castration-resistant prostate cancer (mCRPC) in adults previously treated with ARPI and taxane-based chemotherapy",
     "Oncology", "Novartis", "Big Pharma", "NDA 215833", "215833", "Original", 2022,
     "First FDA-approved PSMA-targeted radioligand therapy (RLT) for prostate cancer"),

    (11, "Vivjoa",    "oteseconazole",                  "2022-04-22",
     "Recurrent vulvovaginal candidiasis (RVVC) in adult females who are not of reproductive potential (oral azole antifungal)",
     "Infectious Disease", "Mycovia Pharmaceuticals", "Biotech", "NDA 215888", "215888", "Original", 2022,
     "First-in-class highly selective CYP51 inhibitor (VCAN); designed to minimize off-target CYP enzyme effects"),

    (12, "Camzyos",   "mavacamten",                     "2022-04-28",
     "Symptomatic obstructive hypertrophic cardiomyopathy (HCM) in adults (NYHA class II–III) to improve functional capacity and symptoms",
     "Cardiovascular", "Bristol-Myers Squibb", "Big Pharma", "NDA 214998", "214998", "Original", 2022,
     "First-in-class cardiac myosin inhibitor; disease-modifying mechanism directly targeting HCM pathophysiology"),

    (13, "Voquezna",  "vonoprazan + amoxicillin (+ clarithromycin)", "2022-05-03",
     "Eradication of H. pylori infection in adults — Triple Pak (vonoprazan + amoxicillin + clarithromycin, NDA 215152) and Dual Pak (vonoprazan + amoxicillin, NDA 215153)",
     "Infectious Disease", "Phathom Pharmaceuticals", "Biotech", "NDA 215152", "215152", "Original", 2022,
     "First potassium-competitive acid blocker (PCAB) combination regimen approved in the US; superior to PPI-based triple therapy in CYP2C19 poor metabolizers"),

    (14, "Mounjaro",  "tirzepatide",                    "2022-05-13",
     "Adjunct to diet and exercise to improve glycemic control in adults with type 2 diabetes mellitus (weekly SC injection)",
     "Endocrinology", "Eli Lilly", "Big Pharma", "NDA 215866", "215866", "Original", 2022,
     "First-in-class dual GIP/GLP-1 receptor agonist; highest A1c reduction seen in a Phase 3 T2D program at time of approval"),

    (15, "Vtama",     "tapinarof",                      "2022-05-18",
     "Plaque psoriasis in adults (topical aryl hydrocarbon receptor modulating agent; once-daily cream)",
     "Dermatology", "Dermavant Sciences", "Biotech", "NDA 215272", "215272", "Original", 2022,
     "First-in-class therapeutic aryl hydrocarbon receptor (AhR) agonist for skin disease; non-steroidal topical"),

    (16, "Amvuttra",  "vutrisiran",                     "2022-06-13",
     "Polyneuropathy of hereditary transthyretin-mediated (hATTR) amyloidosis in adults (GalNAc-siRNA; quarterly SC injection)",
     "Rare Disease", "Alnylam Pharmaceuticals", "Biotech", "NDA 215515", "215515", "Original", 2022,
     "First quarterly-dosed RNAi therapy; enhanced GalNAc-conjugate enables SC self-injection without premedication"),

    (17, "Xenpozyme", "olipudase alfa-rpcp",            "2022-08-31",
     "Non-CNS manifestations of acid sphingomyelinase deficiency (ASMD) in adults and pediatric patients (enzyme replacement therapy; IV infusion)",
     "Rare Disease", "Sanofi / Genzyme", "Big Pharma", "BLA 761261", "761261", "Original", 2022,
     "First FDA-approved treatment for non-CNS manifestations of ASMD (Niemann-Pick disease type A/B)"),

    (18, "Spevigo",   "spesolimab-sbzo",                "2022-09-01",
     "Generalized pustular psoriasis (GPP) flares in adults (anti-IL-36 receptor monoclonal antibody; IV single-dose)",
     "Dermatology", "Boehringer Ingelheim", "Big Pharma", "BLA 761244", "761244", "Original", 2022,
     "First FDA-approved treatment for GPP flares; first anti-IL-36R antibody approved in the US"),

    (19, "Daxxify",   "daxibotulinum toxin A-lanm",     "2022-09-07",
     "Temporary improvement in the appearance of moderate to severe glabellar lines in adults (injectable neuromodulator)",
     "Dermatology", "Revance Therapeutics", "Biotech", "BLA 761127", "761127", "Original", 2022,
     "First and only peptide-formulated botulinum toxin; duration up to 6 months vs 3–4 months for conventional BoNT-A products"),

    (20, "Sotyktu",   "deucravacitinib",                "2022-09-09",
     "Moderate to severe plaque psoriasis in adults who are candidates for systemic therapy or phototherapy (oral TYK2 inhibitor)",
     "Dermatology", "Bristol-Myers Squibb", "Big Pharma", "NDA 214958", "214958", "Original", 2022,
     "First-in-class selective oral TYK2 inhibitor; allosteric mechanism differentiates from JAK inhibitors"),

    (21, "Rolvedon",  "eflapegrastim-xnst",             "2022-09-09",
     "Decrease the incidence of infection (febrile neutropenia) in adults with non-myeloid malignancies receiving myelosuppressive chemotherapy (once-per-cycle SC injection)",
     "Oncology", "Spectrum Pharmaceuticals", "Biotech", "BLA 761148", "761148", "Original", 2022, ""),

    (22, "Terlivaz",  "terlipressin",                   "2022-09-14",
     "Improve kidney function in adults with hepatorenal syndrome type 1 (HRS-1) (vasopressin analog; IV bolus)",
     "Gastroenterology", "Mallinckrodt", "Biotech", "NDA 022231", "022231", "Resubmission", 2022,
     "Resubmission – Only FDA-approved vasopressin analog for HRS-1 in the US; NDA first submitted ~2009 with multiple prior CRLs"),

    (23, "Elucirem",  "gadopiclenol",                   "2022-09-21",
     "MRI contrast enhancement of the brain, spine, and associated tissues, and whole-body (including cardiac) MRI in adults and pediatric patients ≥2 years",
     "Radiology", "Guerbet", "Biotech", "NDA 216986", "216986", "Original", 2022,
     "Macrocyclic GBCA with ~4× higher relaxivity than conventional GBCAs; allows half-dose imaging with equivalent or superior signal"),

    (24, "Omlonti",   "omidenepag isopropyl",           "2022-09-22",
     "Reduction of elevated intraocular pressure (IOP) in patients with open-angle glaucoma or ocular hypertension (once-daily ophthalmic solution)",
     "Ophthalmology", "Santen", "Biotech", "NDA 215092", "215092", "Original", 2022,
     "First-in-class selective EP2 prostanoid receptor agonist for glaucoma; novel MOA distinct from latanoprost and other FP-agonists"),

    (25, "Relyvrio",  "sodium phenylbutyrate and taurursodiol", "2022-09-29",
     "Amyotrophic lateral sclerosis (ALS) in adults (dual UPR/mitochondrial stress pathway inhibitor; oral)",
     "Neurology", "Amylyx Pharmaceuticals", "Biotech", "NDA 216660", "216660", "Original", 2022,
     "Withdrawn from US market April 2024 after Phase 3 PHOENIX trial failed to confirm benefit"),

    (26, "Lytgobi",   "futibatinib",                    "2022-09-30",
     "Previously treated, unresectable, locally advanced or metastatic intrahepatic cholangiocarcinoma harboring FGFR2 gene fusions or rearrangements",
     "Oncology", "Taiho Oncology", "Biotech", "NDA 214801", "214801", "Original", 2022,
     "Accelerated Approval – First irreversible (covalent) FGFR1-4 inhibitor; potent activity against acquired resistance mutations"),

    (27, "Imjudo",    "tremelimumab-actl",              "2022-10-21",
     "Unresectable hepatocellular carcinoma (HCC) in adults, in combination with durvalumab (STRIDE regimen: single priming dose + regular durvalumab)",
     "Oncology", "AstraZeneca", "Big Pharma", "BLA 761289", "761289", "Original", 2022,
     "First CTLA-4 inhibitor approved for HCC; single-dose priming strategy (STRIDE) showed OS benefit in HIMALAYA study"),

    (28, "Tecvayli",  "teclistamab-cqyv",               "2022-10-25",
     "Adults with relapsed or refractory multiple myeloma who have received ≥4 prior lines of therapy (BCMA×CD3 bispecific T-cell engager; weekly then biweekly SC)",
     "Oncology", "Janssen (J&J)", "Big Pharma", "BLA 761291", "761291", "Original", 2022,
     "Accelerated Approval – First FDA-approved BCMA×CD3 bispecific T-cell engager for multiple myeloma"),

    (29, "Elahere",   "mirvetuximab soravtansine-gynx", "2022-11-14",
     "Adults with FRα-positive, platinum-resistant epithelial ovarian, fallopian tube, or primary peritoneal cancer who received 1–3 prior systemic treatment regimens",
     "Oncology", "ImmunoGen", "Biotech", "BLA 761310", "761310", "Original", 2022,
     "Accelerated Approval – First ADC targeting folate receptor alpha (FRα) for ovarian cancer"),

    (30, "Tzield",    "teplizumab-mzwv",                "2022-11-17",
     "Delay the onset of Stage 3 type 1 diabetes (T1D) in adults and pediatric patients ≥8 years with Stage 2 T1D (anti-CD3 antibody; 14-day IV course)",
     "Endocrinology", "Provention Bio", "Biotech", "BLA 761183", "761183", "Original", 2023,
     "First-ever therapy approved to delay onset of clinical type 1 diabetes; first immunomodulatory treatment for T1D prevention"),

    (31, "Rezlidhia", "olutasidenib",                   "2022-12-01",
     "Relapsed or refractory acute myeloid leukemia (AML) with a susceptible IDH1 mutation in adults (oral IDH1 inhibitor)",
     "Oncology", "Forma Therapeutics / Rigel", "Biotech", "NDA 215814", "215814", "Original", 2023, ""),

    (32, "Krazati",   "adagrasib",                      "2022-12-12",
     "Locally advanced or metastatic KRAS G12C-mutated non-small cell lung cancer (NSCLC) in adults, after at least one prior systemic therapy",
     "Oncology", "Mirati Therapeutics", "Biotech", "NDA 216340", "216340", "Original", 2023,
     "Accelerated Approval – Second KRAS G12C inhibitor; demonstrated activity in NSCLC with CNS metastases"),

    (33, "Sunlenca",  "lenacapavir",                    "2022-12-22",
     "HIV-1 infection in heavily treatment-experienced adults with multidrug-resistant HIV-1 (in combination with other ARVs; twice-yearly SC injection + oral loading)",
     "Infectious Disease", "Gilead Sciences", "Big Pharma", "NDA 215973", "215973", "Original", 2023,
     "First-in-class HIV-1 capsid inhibitor; first long-acting injectable approved for treatment-experienced patients"),

    (34, "Lunsumio",  "mosunetuzumab-axgb",             "2022-12-22",
     "Adults with relapsed or refractory follicular lymphoma after ≥2 prior lines of systemic therapy (CD20×CD3 bispecific T-cell engager; fixed-duration IV)",
     "Oncology", "Genentech / Roche", "Big Pharma", "BLA 761263", "761263", "Original", 2023,
     "Accelerated Approval – First fixed-duration (8 cycles) CD20×CD3 bispecific T-cell engager for follicular lymphoma"),

    (35, "Xenoview",  "xenon Xe 129 hyperpolarized",    "2022-12-28",
     "Inhalation agent for use with MRI for evaluation of lung ventilation in adults and pediatric patients ≥12 years",
     "Pulmonology", "Polarean Imaging", "Biotech", "NDA 214375", "214375", "Original", 2023,
     "First and only inhaled hyperpolarized MRI contrast agent approved in the US; enables real-time functional lung ventilation imaging"),

    (36, "Briumvi",   "ublituximab-xiiy",               "2022-12-28",
     "Relapsing forms of multiple sclerosis (RMS) in adults, including CIS, RRMS, and active SPMS (anti-CD20 monoclonal antibody; short-duration IV infusion)",
     "Neurology", "TG Therapeutics", "Biotech", "BLA 761238", "761238", "Original", 2023,
     "Shortest infusion time (1 hr after first dose) among approved anti-CD20 therapies for MS"),

    (37, "NexoBrid",  "anacaulase-bcdb",                "2022-12-28",
     "Eschar removal (debridement) in adults and pediatric patients ≥28 days with deep partial- and/or full-thickness thermal burns (topical gel; enzymatic debridement)",
     "Dermatology", "MediWound / Vericel", "Biotech", "BLA 761192", "761192", "Original", 2023,
     "First enzymatic debridement agent approved in the US; non-surgical alternative to surgical eschar removal in burn care"),
]

# ── Stats ────────────────────────────────────────────────────────────────────
total       = len(drugs)
n_bigpharma = sum(1 for d in drugs if d[7] == "Big Pharma")
n_biotech   = total - n_bigpharma
n_accel     = sum(1 for d in drugs if "Accelerated Approval" in d[12])
n_resub     = sum(1 for d in drugs if d[10] == "Resubmission")
n_oncology  = sum(1 for d in drugs if d[5] == "Oncology")

today = "2026-07-02"

# ── Build rows ───────────────────────────────────────────────────────────────
rows_html = ""
for (no, name, ing, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note) in drugs:
    daf_url = daf_link(appno_num)
    if name in CUSTOM_TOC:
        toc_url = CUSTOM_TOC[name]
    else:
        toc_url = toc_link(appno_num, toc_year)

    daf_cell = f'<a href="{daf_url}" target="_blank">Drugs@FDA</a>'
    toc_cell = f'<a href="{toc_url}" target="_blank">TOC</a>'

    note_parts = []
    if "Accelerated Approval" in note:
        note_parts.append("Accelerated Approval")
    if submission == "Resubmission":
        note_parts.append("Resubmission")
    note_cell = " / ".join(note_parts)

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

# ── HTML ─────────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2022 Novel Drug Approvals Dashboard</title>
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
    <h1>FDA 2022 Novel Drug Approvals Dashboard</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Source: FDA Novel Drug Approvals 2022 (CDER NMEs and new therapeutic biologics) &nbsp;|&nbsp; Total: {total} novel drug approvals</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card"><div class="val">{total}</div><div class="lbl">Total Novel Approvals</div></div>
    <div class="stat-card"><div class="val">{n_bigpharma}</div><div class="lbl">Big Pharma</div></div>
    <div class="stat-card"><div class="val">{n_biotech}</div><div class="lbl">Biotech</div></div>
    <div class="stat-card"><div class="val">{n_accel}</div><div class="lbl">Accelerated Approval</div></div>
    <div class="stat-card"><div class="val">{n_resub}</div><div class="lbl">Resubmission</div></div>
    <div class="stat-card"><div class="val">{n_oncology}</div><div class="lbl">Oncology Drugs</div></div>
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
    Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2022" target="_blank">FDA Novel Drug Approvals for 2022</a>
    &nbsp;|&nbsp; TOC links: accessdata.fda.gov &nbsp;|&nbsp; Built: {today}
  </div>

</div>
</body>
</html>"""

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FDA Novel Drug Approvals 2022 Dashboard.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Dashboard saved to: {output_path}")
print(f"Total: {total} | Big Pharma: {n_bigpharma} | Biotech: {n_biotech}")
print(f"Accelerated Approval: {n_accel} | Resubmission: {n_resub} | Oncology: {n_oncology}")
