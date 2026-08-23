# -*- coding: utf-8 -*-
"""Build FDA 2023 Novel Drug Approvals Dashboard HTML"""

DAF_BASE = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&varApplNo="
TOC_BASE = "https://www.accessdata.fda.gov/drugsatfda_docs/nda/{year}/{appno}Orig1s000TOC.html"

# Zurzuvae PPD approval was filed as Orig2s000
CUSTOM_TOC = {
    "Zurzuvae": "https://www.accessdata.fda.gov/drugsatfda_docs/nda/2023/217369Orig2s000TOC.html",
}

def daf_link(appno_num):
    return DAF_BASE + appno_num

def toc_link(appno_num, year=2023):
    return TOC_BASE.format(year=year, appno=appno_num)

# Data tuple:
# (no, name, ingredient, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note)
# note: use "Accelerated Approval" substring to trigger AA badge; "Resubmission" for resub badge

drugs = [
    (1,  "Leqembi",   "lecanemab-irmb",               "2023-01-06",
     "Treatment of adults with Alzheimer's disease (mild cognitive impairment or mild dementia stage) with confirmed amyloid pathology",
     "Neurology", "Eisai / Biogen", "Big Pharma", "BLA 761269", "761269", "Original", 2023,
     "Accelerated Approval – First disease-modifying therapy for Alzheimer's disease (Full Approval Jul 2023)"),

    (2,  "Brenzavvy", "bexagliflozin",                "2023-01-23",
     "Adjunct to diet and exercise to improve glycemic control in adults with type 2 diabetes mellitus",
     "Endocrinology", "TheracosBio", "Biotech", "NDA 214373", "214373", "Original", 2023, ""),

    (3,  "Orserdu",   "elacestrant",                  "2023-01-27",
     "Postmenopausal women or adult men with ER+/HER2- advanced or metastatic breast cancer with ESR1 mutation, after at least one prior line of endocrine therapy",
     "Oncology", "Menarini / Stemline", "Biotech", "NDA 217639", "217639", "Original", 2023, ""),

    (4,  "Jaypirca",  "pirtobrutinib",                "2023-01-27",
     "Adults with relapsed or refractory mantle cell lymphoma (MCL) after ≥2 prior lines of therapy including a BTK inhibitor",
     "Oncology", "Eli Lilly", "Big Pharma", "NDA 216059", "216059", "Original", 2023,
     "Accelerated Approval"),

    (5,  "Jesduvroq", "daprodustat",                  "2023-02-01",
     "Anemia due to chronic kidney disease in adults on dialysis for ≥4 months",
     "Nephrology", "GSK", "Big Pharma", "NDA 216951", "216951", "Original", 2023, ""),

    (6,  "Lamzede",   "velmanase alfa-tycv",           "2023-02-16",
     "Non-CNS manifestations of alpha-mannosidosis in adults and pediatric patients ≥4 years",
     "Rare Disease", "Chiesi", "Biotech", "BLA 761278", "761278", "Original", 2023, ""),

    (7,  "Filspari",  "sparsentan",                   "2023-02-17",
     "Adults with primary IgA nephropathy (IgAN) at risk of rapid disease progression",
     "Nephrology", "Travere Therapeutics", "Biotech", "NDA 216403", "216403", "Original", 2023,
     "Accelerated Approval – First non-immunosuppressive therapy for IgAN"),

    (8,  "Skyclarys", "omaveloxolone",                "2023-02-28",
     "Friedreich's ataxia in adults and adolescents ≥16 years",
     "Neurology", "Reata Pharmaceuticals", "Biotech", "NDA 216718", "216718", "Original", 2023,
     "First-ever treatment approved for Friedreich's ataxia"),

    (9,  "Zavzpret",  "zavegepant",                   "2023-03-09",
     "Acute treatment of migraine with or without aura in adults (nasal spray; first CGRP-antagonist nasal spray)",
     "Neurology", "Pfizer", "Big Pharma", "NDA 216386", "216386", "Original", 2023, ""),

    (10, "Daybue",    "trofinetide",                  "2023-03-10",
     "Rett syndrome in adults and pediatric patients ≥2 years",
     "Neurology", "Acadia Pharmaceuticals", "Biotech", "NDA 217026", "217026", "Original", 2023,
     "First and only FDA-approved treatment for Rett syndrome"),

    (11, "Rezzayo",   "rezafungin for injection",     "2023-03-22",
     "Candidemia and invasive candidiasis in adults with limited or no alternative treatment options (once-weekly echinocandin)",
     "Infectious Disease", "Cidara / Melinta", "Biotech", "NDA 217417", "217417", "Original", 2023, ""),

    (12, "Zynyz",     "retifanlimab-dlwr",            "2023-03-22",
     "Metastatic or recurrent locally advanced Merkel cell carcinoma (MCC) in adults",
     "Oncology", "Incyte", "Biotech", "BLA 761334", "761334", "Original", 2023,
     "Accelerated Approval"),

    (13, "Joenja",    "leniolisib",                   "2023-03-24",
     "Activated PI3K delta syndrome (APDS) in adults and pediatric patients ≥12 years",
     "Rare Disease", "Pharming Group", "Biotech", "NDA 217759", "217759", "Original", 2023, ""),

    (14, "Qalsody",   "tofersen",                     "2023-04-25",
     "SOD1-amyotrophic lateral sclerosis (SOD1-ALS) in adults (antisense oligonucleotide)",
     "Neurology", "Biogen", "Big Pharma", "NDA 215887", "215887", "Original", 2023,
     "Accelerated Approval – First treatment targeting SOD1-ALS"),

    (15, "Elfabrio",  "pegunigalsidase alfa-iwxj",    "2023-05-09",
     "Fabry disease in adults (PEGylated enzyme replacement therapy; every-2-week IV infusion)",
     "Rare Disease", "Chiesi / Protalix", "Biotech", "BLA 761161", "761161", "Original", 2023, ""),

    (16, "Veozah",    "fezolinetant",                 "2023-05-12",
     "Moderate to severe vasomotor symptoms (hot flashes) due to menopause",
     "Women's Health", "Astellas", "Big Pharma", "NDA 216578", "216578", "Original", 2023,
     "First non-hormonal NK3 receptor antagonist for menopausal vasomotor symptoms"),

    (17, "Miebo",     "perfluorohexyloctane",         "2023-05-18",
     "Signs and symptoms of dry eye disease (DED)",
     "Ophthalmology", "Bausch + Lomb / Novaliq", "Biotech", "NDA 216675", "216675", "Original", 2023, ""),

    (18, "Epkinly",   "epcoritamab-bysp",             "2023-05-19",
     "Adults with relapsed or refractory DLBCL (NOS) or large B-cell lymphoma from follicular lymphoma, after ≥2 prior lines of therapy",
     "Oncology", "AbbVie / Genmab", "Big Pharma", "BLA 761324", "761324", "Original", 2023,
     "Accelerated Approval"),

    (19, "Xacduro",   "sulbactam-durlobactam",        "2023-05-23",
     "Hospital-acquired or ventilator-associated bacterial pneumonia caused by susceptible Acinetobacter baumannii-calcoaceticus complex in adults",
     "Infectious Disease", "Innoviva / Entasis", "Biotech", "NDA 216974", "216974", "Original", 2023, ""),

    (20, "Posluma",   "flotufolastat F 18",           "2023-05-25",
     "PET imaging of PSMA-positive lesions in men with prostate cancer with biochemical recurrence or metastatic disease",
     "Oncology", "Blue Earth Diagnostics", "Biotech", "NDA 216023", "216023", "Original", 2023, ""),

    (21, "Paxlovid",  "nirmatrelvir + ritonavir",     "2023-05-25",
     "Mild-to-moderate COVID-19 in adults at high risk for progression to severe COVID-19",
     "Infectious Disease", "Pfizer", "Big Pharma", "NDA 217188", "217188", "Original", 2023,
     "Full NDA approval; previously under Emergency Use Authorization (EUA) since Dec 2021"),

    (22, "Inpefa",    "sotagliflozin",                "2023-05-26",
     "Reduce risk of cardiovascular death, hospitalization for HF, and urgent HF visit in adults with heart failure or type 2 diabetes with CKD and CV risk factors",
     "Cardiovascular", "Lexicon Pharmaceuticals", "Biotech", "NDA 216203", "216203", "Original", 2023, ""),

    (23, "Columvi",   "glofitamab-gxbm",              "2023-06-15",
     "Adults with relapsed or refractory DLBCL (NOS) or LBCL from follicular lymphoma, after ≥2 prior lines of therapy (fixed-duration bispecific CD20×CD3)",
     "Oncology", "Roche / Genentech", "Big Pharma", "BLA 761309", "761309", "Original", 2023,
     "Accelerated Approval"),

    (24, "Litfulo",   "ritlecitinib",                 "2023-06-23",
     "Severe alopecia areata in adults and adolescents ≥12 years (JAK3/TEC family inhibitor)",
     "Dermatology", "Pfizer", "Big Pharma", "NDA 215830", "215830", "Original", 2023, ""),

    (25, "Rystiggo",  "rozanolixizumab-noli",         "2023-06-26",
     "Adults with generalized myasthenia gravis (gMG) who are anti-AChR or anti-MuSK antibody positive (anti-FcRn antibody)",
     "Neurology", "UCB", "Biotech", "BLA 761286", "761286", "Original", 2023, ""),

    (26, "Ngenla",    "somatrogon-ghla",              "2023-06-27",
     "Growth failure due to inadequate growth hormone secretion in pediatric patients ≥3 years (once-weekly long-acting GH analog)",
     "Endocrinology", "Pfizer / OPKO", "Big Pharma", "BLA 761184", "761184", "Original", 2023, ""),

    (27, "Beyfortus", "nirsevimab-alip",              "2023-07-17",
     "Prevention of RSV lower respiratory tract disease in neonates, infants, and toddlers up to 24 months remaining vulnerable through their second RSV season",
     "Infectious Disease", "Sanofi / AstraZeneca", "Big Pharma", "BLA 761328", "761328", "Original", 2023,
     "First long-acting monoclonal antibody for RSV prevention in all infants"),

    (28, "Vanflyta",  "quizartinib",                  "2023-07-20",
     "Newly diagnosed FLT3-ITD positive AML in adults (in combination with standard induction/consolidation chemo, then maintenance monotherapy)",
     "Oncology", "Daiichi Sankyo", "Big Pharma", "NDA 216993", "216993", "Original", 2023, ""),

    (29, "Xdemvy",    "lotilaner ophthalmic solution", "2023-07-25",
     "Demodex blepharitis",
     "Ophthalmology", "Tarsus Pharmaceuticals", "Biotech", "NDA 217603", "217603", "Original", 2023,
     "First FDA-approved treatment for Demodex blepharitis"),

    (30, "Izervay",   "avacincaptad pegol",           "2023-08-04",
     "Geographic atrophy (GA) secondary to age-related macular degeneration (AMD) (complement C5 inhibitor; monthly intravitreal injection)",
     "Ophthalmology", "Iveric Bio (Astellas)", "Biotech", "NDA 217225", "217225", "Original", 2023, ""),

    (31, "Zurzuvae",  "zuranolone",                   "2023-08-04",
     "Postpartum depression (PPD) in adults (first oral neuroactive steroid; 14-day course)",
     "Psychiatry", "Biogen / Sage Therapeutics", "Big Pharma", "NDA 217369", "217369", "Original", 2023,
     "First oral neuroactive steroid for PPD; CRL issued for MDD indication on same day"),

    (32, "Talvey",    "talquetamab-tgvs",             "2023-08-09",
     "Adults with relapsed or refractory multiple myeloma who received ≥4 prior lines of therapy (first-in-class GPRC5D×CD3 bispecific)",
     "Oncology", "Janssen (J&J)", "Big Pharma", "BLA 761342", "761342", "Original", 2023,
     "Accelerated Approval"),

    (33, "Elrexfio",  "elranatamab-bcmm",             "2023-08-14",
     "Adults with relapsed or refractory multiple myeloma who received ≥4 prior lines of therapy (BCMA×CD3 bispecific)",
     "Oncology", "Pfizer", "Big Pharma", "BLA 761345", "761345", "Original", 2023,
     "Accelerated Approval"),

    (34, "Sohonos",   "palovarotene",                 "2023-08-16",
     "Reduction of new heterotopic ossification in adults and pediatric patients with fibrodysplasia ossificans progressiva (FOP)",
     "Rare Disease", "Ipsen", "Big Pharma", "NDA 215559", "215559", "Original", 2023,
     "First-ever treatment approved for FOP"),

    (35, "Veopoz",    "pozelimab-bbfg",               "2023-08-18",
     "CD55-deficient protein-losing enteropathy (CHAPLE disease) in adults and pediatric patients ≥1 year (anti-C5 monoclonal antibody)",
     "Rare Disease", "Regeneron", "Biotech", "BLA 761339", "761339", "Original", 2023,
     "First treatment for CHAPLE disease"),

    (36, "Aphexda",   "motixafortide",                "2023-09-08",
     "In combination with filgrastim (G-CSF) to mobilize hematopoietic stem cells for autologous transplantation in patients with multiple myeloma",
     "Hematology", "BioLineRx", "Biotech", "NDA 217159", "217159", "Original", 2023, ""),

    (37, "Ojjaara",   "momelotinib",                  "2023-09-15",
     "Intermediate or high-risk myelofibrosis with anemia in adults (JAK1/2 + ACVR1 inhibitor)",
     "Hematology", "GSK", "Big Pharma", "NDA 216873", "216873", "Original", 2023,
     "First treatment specifically approved for myelofibrosis with anemia"),

    (38, "Exxua",     "gepirone",                     "2023-09-22",
     "Major depressive disorder (MDD) in adults (selective 5-HT1A receptor agonist; extended-release tablet)",
     "Psychiatry", "Fabre-Kramer", "Biotech", "NDA 021164", "021164", "Resubmission", 2023,
     "Resubmission – NDA originally submitted in late 1990s; approved after 25+ years of FDA review"),

    (39, "Pombiliti", "cipaglucosidase alfa-atga",    "2023-09-28",
     "Late-onset Pompe disease in adults, in combination with the pharmacological chaperone miglustat",
     "Rare Disease", "Amicus Therapeutics", "Biotech", "BLA 761204", "761204", "Original", 2023, ""),

    (40, "Rivfloza",  "nedosiran",                    "2023-09-29",
     "Reduce urinary oxalate levels in children ≥9 years and adults with primary hyperoxaluria type 1 (PH1) and relatively preserved kidney function (RNAi therapy; monthly SC)",
     "Rare Disease", "Novo Nordisk", "Big Pharma", "NDA 215842", "215842", "Original", 2023, ""),

    (41, "Velsipity", "etrasimod",                    "2023-10-12",
     "Moderately to severely active ulcerative colitis in adults (selective S1P1/4/5 receptor modulator; once-daily oral)",
     "Gastroenterology", "Pfizer", "Big Pharma", "NDA 216956", "216956", "Original", 2023, ""),

    (42, "Bimzelx",   "bimekizumab-bkzx",             "2023-10-17",
     "Moderate to severe plaque psoriasis in adults who are candidates for systemic therapy or phototherapy (dual IL-17A/F inhibitor)",
     "Dermatology", "UCB", "Biotech", "BLA 761151", "761151", "Original", 2023, ""),

    (43, "Zilbrysq",  "zilucoplan",                   "2023-10-17",
     "Adults with generalized myasthenia gravis (gMG) who are anti-AChR antibody positive (complement C5 inhibitor; once-daily SC self-injection)",
     "Neurology", "UCB", "Biotech", "NDA 216834", "216834", "Original", 2023, ""),

    (44, "Omvoh",     "mirikizumab-mrkz",             "2023-10-26",
     "Moderately to severely active ulcerative colitis in adults (IL-23p19 antagonist; IV induction then SC maintenance)",
     "Gastroenterology", "Eli Lilly", "Big Pharma", "BLA 761279", "761279", "Original", 2023, ""),

    (45, "Agamree",   "vamorolone",                   "2023-10-26",
     "Duchenne muscular dystrophy in patients ≥2 years (dissociative steroidal anti-inflammatory; once-daily oral suspension)",
     "Rare Disease", "Catalyst / Santhera", "Biotech", "NDA 215239", "215239", "Original", 2023, ""),

    (46, "Loqtorzi",  "toripalimab-tpzi",             "2023-10-27",
     "Metastatic or recurrent locally advanced nasopharyngeal carcinoma (NPC): 1L with gemcitabine + cisplatin; ≥2L as monotherapy",
     "Oncology", "Coherus / Junshi", "Biotech", "BLA 761240", "761240", "Original", 2023,
     "First FDA-approved PD-1 inhibitor developed in China"),

    (47, "Fruzaqla",  "fruquintinib",                 "2023-11-08",
     "Previously treated metastatic colorectal cancer (CRC) in adults (VEGFR 1/2/3 inhibitor; 3rd-line+)",
     "Oncology", "Takeda / Hutchmed", "Big Pharma", "NDA 217564", "217564", "Original", 2023, ""),

    (48, "Defencath", "taurolidine + heparin",        "2023-11-15",
     "Reduce the incidence of catheter-related bloodstream infections in adults with kidney failure receiving hemodialysis through a central venous catheter (catheter lock solution)",
     "Infectious Disease", "CorMedix", "Biotech", "NDA 214520", "214520", "Original", 2023, ""),

    (49, "Augtyro",   "repotrectinib",                "2023-11-15",
     "Locally advanced or metastatic ROS1-positive non-small cell lung cancer (NSCLC) in adults (next-generation ROS1/NTRK inhibitor)",
     "Oncology", "Bristol-Myers Squibb", "Big Pharma", "NDA 218213", "218213", "Original", 2023, ""),

    (50, "Truqap",    "capivasertib",                 "2023-11-16",
     "HR-positive, HER2-negative locally advanced or metastatic breast cancer with PIK3CA/AKT1/PTEN-alterations in adults (in combination with fulvestrant)",
     "Oncology", "AstraZeneca", "Big Pharma", "NDA 218197", "218197", "Original", 2023, ""),

    (51, "Ryzneuta",  "efbemalenograstim alfa-vuxw",  "2023-11-16",
     "Decrease incidence of febrile neutropenia in adults with non-myeloid malignancies receiving myelosuppressive anti-cancer drugs (long-acting G-CSF; once-per-cycle SC)",
     "Hematology", "Evive / Acrotech", "Biotech", "BLA 761134", "761134", "Original", 2023, ""),

    (52, "Ogsiveo",   "nirogacestat",                 "2023-11-27",
     "Adults with progressing desmoid tumors requiring systemic treatment (gamma-secretase / Notch pathway inhibitor)",
     "Oncology", "SpringWorks Therapeutics", "Biotech", "NDA 217677", "217677", "Original", 2023, ""),

    (53, "Fabhalta",  "iptacopan",                    "2023-12-05",
     "Paroxysmal nocturnal hemoglobinuria (PNH) in adults (first oral factor B inhibitor; proximal complement inhibitor)",
     "Hematology", "Novartis", "Big Pharma", "NDA 218276", "218276", "Original", 2023,
     "First oral monotherapy for PNH"),

    (54, "Filsuvez",  "birch triterpenes",            "2023-12-18",
     "Wounds associated with dystrophic and junctional epidermolysis bullosa (EB) in adults and pediatric patients ≥6 months (topical gel)",
     "Rare Disease", "Chiesi / Amryt", "Biotech", "NDA 215064", "215064", "Original", 2024, ""),

    (55, "Wainua",    "eplontersen",                  "2023-12-21",
     "Polyneuropathy of hereditary transthyretin-mediated amyloidosis (hATTR-PN) in adults (GalNAc-conjugated antisense oligonucleotide; monthly SC self-injection)",
     "Rare Disease", "Ionis / AstraZeneca", "Big Pharma", "NDA 217388", "217388", "Original", 2024, ""),
]

# ── Stats ───────────────────────────────────────────────────────────────────
total         = len(drugs)
n_bigpharma   = sum(1 for d in drugs if d[7] == "Big Pharma")
n_biotech     = total - n_bigpharma
n_accel       = sum(1 for d in drugs if "Accelerated Approval" in d[12])
n_resub       = sum(1 for d in drugs if d[10] == "Resubmission")
n_oncology    = sum(1 for d in drugs if d[5] == "Oncology")

today = "2026-07-01"

# ── Build rows ───────────────────────────────────────────────────────────────
rows_html = ""
for (no, name, ing, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note) in drugs:
    daf_url  = daf_link(appno_num)
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

# ── HTML ────────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FDA 2023 Novel Drug Approvals Dashboard</title>
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
    <h1>FDA 2023 Novel Drug Approvals Dashboard</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Source: FDA Novel Drug Approvals 2023 (CDER NMEs and new therapeutic biologics) &nbsp;|&nbsp; Total: {total} novel drug approvals</p>
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
    Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2023" target="_blank">FDA Novel Drug Approvals for 2023</a>
    &nbsp;|&nbsp; TOC links: accessdata.fda.gov &nbsp;|&nbsp; Built: {today}
  </div>

</div>
</body>
</html>"""

output_path = r"C:\0_MBA\Healthcare\FDA New Drug Approval Dashboard\FDA Novel Drug Approvals 2023 Dashboard.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Dashboard saved to: {output_path}")
print(f"Total: {total} | Big Pharma: {n_bigpharma} | Biotech: {n_biotech}")
print(f"Accelerated Approval: {n_accel} | Resubmission: {n_resub} | Oncology: {n_oncology}")
