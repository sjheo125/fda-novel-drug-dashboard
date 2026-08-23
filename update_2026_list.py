# -*- coding: utf-8 -*-
"""
2026 Novel Drug Approvals 리스트를 2026-08-22 기준으로 업데이트.
- 기존 23건(Zycubo~Lumvoa) 그대로 유지, 단 Cypsedo/Ambelvist/Lumvoa의 신청번호 새로 확인되어 보정
- 신규 10건(Trutakna~Pasatru) 추가 (FDA 공식 Novel Drug Approvals for 2026 페이지, content current as of 08/19/2026 기준)
- 산출물: FDA_2026_Novel_Drugs_Dashboard.xlsx, FDA Novel Drug Approvals 2026 Dashboard.html
"""
import re
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from pathlib import Path

BASE_DIR = Path(__file__).parent
XLSX_PATH = BASE_DIR / "FDA_2026_Novel_Drugs_Dashboard.xlsx"
HTML_PATH = BASE_DIR / "FDA Novel Drug Approvals 2026 Dashboard.html"

TOC = "https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/{}TOC.html"
DAF = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&varApplNo={}"

# (no, drug, ingredient, date, use, ta, company, appno, submission, toc_suffix_or_None, note)
# toc_suffix: the {APPNO}Orig1s000 (or exception form) part before "TOC.html"; None = not yet posted
ROWS = [
(1, "Zycubo", "copper histidinate", "2026-01-12",
 "To treat Menkes disease", "Rare Disease / Metabolic", "Sentynl Therapeutics",
 "NDA 211241", "Original (Orig1)", "211241Orig1s000", ""),

(2, "Adquey", "difamilast", "2026-02-12",
 "To treat mild to moderate atopic dermatitis", "Dermatology", "Acrotech Biopharma",
 "NDA 219474", "Original (Orig1)", "219474Orig1s000", ""),

(3, "Bysanti", "milsaperidone", "2026-02-20",
 "To treat schizophrenia and to treat manic or mixed episodes associated with bipolar I disorder",
 "Psychiatry / CNS", "Vanda Pharmaceuticals",
 "NDA 220358", "Original (Orig1)", "220358Orig1s000", ""),

(4, "Loargys", "pegzilarginase-nbln", "2026-02-23",
 "To treat hyperarginemia in adults and pediatric patients two years and older with Arginase 1 Deficiency, in conjunction with dietary protein restriction",
 "Rare Disease / Metabolic", "Immedica Pharma AB",
 "BLA 761211", "Original (Orig1)", "761211Orig1s000",
 "Folder corrected: BLA review documents are filed under the /nda/ path on accessdata.fda.gov, not /bla/"),

(5, "Yuviwel", "navepegritide", "2026-02-27",
 "To increase linear growth in pediatric patients 2 years and older with achondroplasia with open epiphyses",
 "Rare Disease / Endocrinology", "Ascendis Pharma Growth Disorders A/S",
 "NDA 219164", "Original (Orig1)", "219164Orig1s000", ""),

(6, "Lynavoy", "linerixibat", "2026-03-17",
 "To treat cholestatic pruritus associated with primary biliary cholangitis",
 "Hepatology", "GSK",
 "NDA 220295", "Original (Orig1)", "220295Orig1s000", ""),

(7, "Icotyde", "icotrokinra", "2026-03-17",
 "To treat moderate-to-severe plaque psoriasis in patients 12 years and older who weigh at least 40 kg and who are candidates for systemic therapy or phototherapy",
 "Dermatology / Immunology", "Janssen Biotech",
 "NDA 220149", "Original (Orig1)", "220149Orig1s000", ""),

(8, "Avlayah", "tividenofusp alfa-eknm", "2026-03-24",
 "To treat certain individuals with Hunter syndrome (Mucopolysaccharidosis type II or MPS II)",
 "Rare Disease / Metabolic", "Denali Therapeutics",
 "BLA 761485", "Original (Orig1)", "761485Orig1s000",
 "Folder corrected (BLA docs live under /nda/). Confirmed working TOC link."),

(9, "Lifyorli", "relacorilant", "2026-03-25",
 "To treat platinum-resistant epithelial ovarian, fallopian tube, or primary peritoneal cancer after one to three prior systemic treatment regimens, at least one of which included bevacizumab",
 "Oncology", "Corcept Therapeutics",
 "NDA 220641", "Original (Orig1)", "220641Orig1s000", ""),

(10, "Awiqli", "insulin icodec-abae", "2026-03-26",
 "To improve glycemic control in adults with type 2 diabetes mellitus",
 "Endocrinology / Metabolic", "Novo Nordisk",
 "BLA 761326 (Orig2)", "Resubmission (Orig2)", "761326Orig2s000",
 "Folder corrected (BLA docs live under /nda/). Novo Nordisk's first Awiqli submission (Orig1) was not approved; the approved application is the resubmission cycle, Orig2."),

(11, "Foundayo", "orforglipron", "2026-04-01",
 "To reduce excess body weight and maintain weight reduction long term in adults with obesity or adults with overweight in the presence of at least one weight-related comorbid condition, in combination with a reduced-calorie diet and increased physical activity",
 "Endocrinology / Metabolic", "Eli Lilly",
 "NDA 220934", "Original (Orig1)", "220934Orig1s000", ""),

(12, "Idvynso", "doravirine and islatravir", "2026-04-20",
 "To treat HIV-1 infection (as a complete regimen) in adults to replace the current antiretroviral regimen in those who are virologically-suppressed on a stable antiretroviral regimen with no history of virologic treatment failure and no known substitutions associated with resistance to doravirine",
 "Infectious Disease", "Merck",
 "NDA 216964", "Original (Orig1)", "216964s000",
 "Confirmed: this application's TOC filename omits the 'Orig1' segment (216964s000TOC.html), unlike most other 2026 NDAs. Still an original (first-cycle) submission."),

(13, "Veppanu", "vepdegestrant", "2026-05-01",
 "To treat estrogen receptor-positive, human epidermal growth factor receptor 2-negative, ESR1-mutated advanced or metastatic breast cancer with disease progression following at least one line of endocrine therapy",
 "Oncology", "Arvinas / Pfizer",
 "NDA 219835", "Original (Orig1)", "219835Orig1s000",
 "Correction: the previously listed NDA 250810 was wrong — a mismatch from an unrelated search result. The correct application number is NDA 219835, confirmed by direct user check."),

(14, "Beqalzi", "sonrotoclax", "2026-05-13",
 "To treat adults with relapsed or refractory mantle cell lymphoma after at least two lines of systemic therapy, including a Bruton's tyrosine kinase inhibitor",
 "Oncology / Hematology", "BeOne Medicines",
 "NDA 220711", "Original (Orig1)", "220711Orig1s000", ""),

(15, "Baxfendy", "baxdrostat", "2026-05-15",
 "To treat hypertension in combination with other antihypertensive drugs",
 "Cardiovascular", "AstraZeneca AB",
 "NDA 219878", "Original (Orig1)", "219878Orig1s000",
 "Review PDFs saved locally (ChemR, ClinPharmR, MedR, NameR, OtherR, PharmR, RiskR, AdminCorres, OEList) in C:\\0_MBA\\Healthcare\\Baxfendy"),

(16, "Hepcludex", "bulevirtide-gmod", "2026-05-22",
 "To treat chronic hepatitis delta virus infection in adults without cirrhosis or with compensated cirrhosis",
 "Infectious Disease / Hepatology", "Gilead Sciences",
 "BLA 761468", "Original (Orig1)", "761468s000",
 "BLA 761468 confirmed by direct user check on Drugs@FDA. The Orig1s000TOC.html form 404'd; using the no-'Orig1' form (same exception pattern as Idvynso)."),

(17, "Decnupaz", "pivekimab sunirine-pvzy", "2026-05-27",
 "To treat adults with blastic plasmacytoid dendritic cell neoplasm",
 "Oncology / Hematology", "AbbVie",
 "BLA 761460", "Original (Orig1)", "761460Orig1s000",
 "Correction: application number confirmed by direct user check as BLA 761460 (not previously identified via search)."),

(18, "Zaynich", "cefepime and zidebactam", "2026-05-29",
 "To treat complicated urinary tract infections, including pyelonephritis, caused by designated susceptible microorganisms",
 "Infectious Disease", "Wockhardt",
 "NDA 220787", "Original (Orig1)", "220787Orig1s000", ""),

(19, "Xocova", "ensitrelvir", "2026-05-29",
 "To use as post-exposure prophylaxis of coronavirus disease 2019 (COVID-19) following contact with an individual who has COVID-19",
 "Infectious Disease", "Shionogi",
 "NDA 220442", "Original (Orig1)", "220442Orig1s000",
 "Application number confirmed by direct user check as NDA 220442."),

(20, "Cypsedo", "cipepofol", "2026-05-29",
 "To induce general anesthesia in adults undergoing surgery",
 "Anesthesiology", "Haisco-USA Pharmaceuticals",
 "NDA 220482", "Original (Orig1)", "220482Orig1s000",
 "UPDATED 2026-08-22: Application number now indexed on Drugs@FDA — found under the active-ingredient name \"CIPEPOFOL\" (not the brand name \"Cypsedo\"), applicant Haisco Pharmaceutical Group Co Ltd. NDA 220482, Type 1 NME, Standard review. Previously listed as unconfirmed (and before that, an incorrectly matched NDA 219491 belonging to an unrelated drug)."),

(21, "Ambelvist", "gadoquatrane", "2026-06-12",
 "To detect and visualize lesions with abnormal vascularity, in conjunction with MRI",
 "Diagnostic / Radiology", "Bayer",
 "NDA 219627", "Original (Orig1)", "219627Orig1s000",
 "UPDATED 2026-08-22: Application number now indexed on Drugs@FDA — NDA 219627, applicant Bayer Healthcare, Type 1 NME, Standard review + Orphan. Previously listed as unconfirmed."),

(22, "Utebzi", "tebipenem pivoxil", "2026-06-17",
 "To treat complicated urinary tract infections, including pyelonephritis, caused by several susceptible microorganisms in adults who have limited or no alternative oral treatment options",
 "Infectious Disease", "GSK / Spero Therapeutics",
 "NDA 215960", "Original (Orig1)", "215960Orig1s000",
 "Application number confirmed by direct user check as NDA 215960. This NDA number is notably older/lower than other 2026 applications, consistent with this being a years-long resubmitted program (GSK/Spero) even though it is an Orig1 (no prior approval) at the FDA application level."),

(23, "Lumvoa", "veligrotug-vvze", "2026-06-26",
 "To treat thyroid eye disease",
 "Endocrinology / Ophthalmology", "Viridian Therapeutics",
 "BLA 761530", "Original (Orig1)", "761530Orig1s000",
 "UPDATED 2026-08-22: Application number now indexed on Drugs@FDA — BLA 761530, applicant Viridian Therapeutics Inc, Orig-1. Previously listed as unconfirmed."),

# ---- New entries added 2026-08-22 (FDA list content current as of 08/19/2026) ----

(24, "Trutakna", "atacicept-vymj", "2026-07-07",
 "To reduce proteinuria in adults with primary immunoglobulin A nephropathy at risk for disease progression",
 "Nephrology / Immunology", "Vera Therapeutics",
 "BLA 761486", "Original (Orig1)", None,
 "Accelerated Approval (first dual BAFF/APRIL inhibitor for IgA nephropathy). As of 2026-08-22 (46 days post-approval) only the Label and Approval Letter are posted on Drugs@FDA — no Review (TOC) package yet, longer than the typical ~30-day posting lag."),

(25, "Revtorpyk", "gedatolisib", "2026-07-14",
 "In combination with fulvestran, to treat hormone receptor-positive, human epidermal growth factor receptor 2-negative, locally advanced or metastatic breast cancer without a PIK3CA mutation detected following progression on or after treatment with at least one line of endocrine therapy in the metastatic setting",
 "Oncology", "Celcuity",
 "NDA 219908", "Original (Orig1)", "219908Orig1s000",
 "Type 1 New Molecular Entity, Priority Review. First approved dual class I PI3K/mTORC1/mTORC2 inhibitor."),

(26, "Lipfendra", "enlicitide decanoate", "2026-07-15",
 "To reduce low-density lipoprotein cholesterol",
 "Cardiovascular", "Merck",
 "NDA 220848", "Original (Orig1)", None,
 "First oral PCSK9 inhibitor approved. Type 1 NME, Priority Review. As of 2026-08-22, only the Approval Letter is posted on Drugs@FDA — Label and Review package not yet available. Listed as \"MSD\" (Merck's ex-US corporate name) on Drugs@FDA."),

(27, "Jideytro", "zidesamtinib", "2026-07-22",
 "To treat adults with locally advanced or metastatic ROS1-positive non-small cell lung cancer after receiving a ROS1 kinase inhibitor",
 "Oncology", "GSK (Nuvalent)",
 "NDA 220185", "Original (Orig1)", None,
 "Type 1 NME, Standard Review, Orphan Drug. Applicant of record on Drugs@FDA is Nuvalent (acquired by GSK; GSK led the public approval announcement). Like Idvynso, this application's label filename omits the 'Orig1' segment (220185s000lbl.pdf). No Review package posted yet as of 2026-08-22."),

(28, "Lytenava", "bevacizumab-vikg", "2026-07-24",
 "To treat patients with neovascular (wet) age-related macular degeneration",
 "Ophthalmology", "Outlook Therapeutics",
 "BLA 761320", "Original (Orig1)", None,
 "First FDA-approved ophthalmic formulation of bevacizumab. Despite press coverage describing this as a 'resubmission,' Drugs@FDA shows this BLA number (761320) as ORIG-1 — a standalone application, not a later review cycle of an earlier CRL'd BLA. No Review package posted yet as of 2026-08-22."),

(29, "Simtriyo", "centanafadine", "2026-07-24",
 "To treat attention-deficit hyperactivity disorder",
 "Psychiatry / CNS", "Otsuka",
 "NDA 218145", "Original (Orig1)", None,
 "First approved norepinephrine-dopamine-serotonin reuptake inhibitor (NDSRI) for ADHD. Type 1 NME, Priority Review. No Review package posted yet as of 2026-08-22."),

(30, "Orzeyful", "oveporexton", "2026-08-05",
 "To treat narcolepsy type 1",
 "Neurology / Sleep Medicine", "Takeda",
 "NDA 220860", "Original (Orig1)", None,
 "First orexin receptor 2 (OX2R) agonist approved; internal code TAK-861. Type 1 NME, Priority Review + Orphan Drug. No Review package posted yet as of 2026-08-22 (17 days post-approval — expected)."),

(31, "Tauklarify", "florquinitau F 18", "2026-08-13",
 "To be used for positron emission tomography of the brain in adults with cognitive impairment who are being evaluated for Alzheimer disease to identify patients with tau neurofibrillary tangle pathology",
 "Diagnostic / Radiology", "Lantheus (Cerveau Technologies)",
 "NDA 220496", "Original (Orig1)", None,
 "F18-labeled tau PET imaging agent (internal code MK-6240). Type 1 NME, Standard Review. Applicant on Drugs@FDA is Cerveau Technologies Inc, a Lantheus company. No Review package posted yet as of 2026-08-22 (9 days post-approval — expected)."),

(32, "Zenbexus", "iberdomide", "2026-08-13",
 "To be used in combination with daratumumab and hyaluronidase-fihj and dexamethasone for adults with multiple myeloma who have received at least one prior line of therapy, including a proteasome inhibitor and an immunomodulatory agent",
 "Oncology / Hematology", "Bristol Myers Squibb",
 "NDA 221075", "Original (Orig1)", None,
 "Accelerated Approval — first FDA-approved CELMoD (cereblon-modulating protein degrader), and the first accelerated approval in myeloma based on minimal residual disease (MRD) as an early endpoint. Type 1 NME, Priority Review + Orphan Drug. No Review package posted yet as of 2026-08-22 (9 days post-approval — expected)."),

(33, "Pasatru", "garetosmab-grts", "2026-08-19",
 "To reduce new heterotopic ossification and clinician-assessed disease flare-ups in adults with fibrodysplasia ossificans progressiva",
 "Rare Disease / Musculoskeletal", "Regeneron",
 None, "Unknown", None,
 "Application Number not yet indexed on Drugs@FDA as of 2026-08-22 (only 3 days post-approval) — searched by both brand name \"Pasatru\" and active ingredient \"garetosmab\", no match found under either. Not even the Label/Approval Letter are posted yet. First and only approved treatment for FOP (fibrodysplasia ossificans progressiva); first-in-class Activin A inhibitor."),
]

NOTES = [
    "Content current as of: FDA's Novel Drug Approvals for 2026 page states \"Content current as of: 08/19/2026\". The list's last entry (Pasatru) is approved 2026-08-19, and no entries beyond that date were present when checked on 2026-08-22.",
    "Application numbers were resolved via Drugs@FDA (browse-by-letter and overview.process&varApplNo=) and cross-checked against web search / press releases. Rows 20 (Cypsedo), 21 (Ambelvist), and 23 (Lumvoa) — previously unconfirmed — were newly resolved in this 2026-08-22 update.",
    "Therapeutic Area is inferred from the FDA-approved use on approval date — not an official FDA classification field.",
    "Submission column: \"Original (Orig1)\" means this was the application's first review cycle that led to approval. \"Resubmission (Orig2)\" means an earlier original submission was not approved and the approved application is a later review cycle. Awiqli is the only confirmed Orig2 in this list. Pasatru is marked \"Unknown\" because the application number itself is unconfirmed.",
    "BLA review documents are filed under the accessdata.fda.gov /nda/ path, not /bla/ — applies to Loargys, Avlayah, Awiqli, Hepcludex, Decnupaz, Trutakna, Lytenava.",
    "TOC filename exceptions: Idvynso (216964s000TOC.html) and Hepcludex (761468s000TOC.html) omit the \"Orig1\" segment used by most other 2026 applications.",
    "Drugs@FDA column logic: when the Application Number is confirmed, Drugs@FDA links via event=overview.process&varApplNo={number}. Only when unconfirmed (Pasatru) does it fall back to the blank search page with the drug name shown as a typing reminder.",
    "Review (TOC) lag: FDA review documents (Multi-Discipline/Clinical/Statistical Review etc.) typically post ~30 days after approval, after the Label and Approval Letter (which post within days). As of 2026-08-22, eight recently-approved drugs (Trutakna, Lipfendra, Jideytro, Lytenava, Simtriyo, Orzeyful, Tauklarify, Zenbexus) do not yet have a Review package posted — this is expected, not a search failure. Revtorpyk (approved 7/14) does already have its Review package posted.",
    "Baxfendy (NDA 219878) review documents are already downloaded as PDFs in C:\\0_MBA\\Healthcare\\Baxfendy.",
]


def build_xlsx():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "2026 Novel Drugs"
    headers = ["No.", "Drug Name", "Active Ingredient", "Approval Date", "FDA-approved use on approval date",
               "Therapeutic Area", "Company", "Application Number", "Submission", "Drugs@FDA",
               "FDA Application Review", "Note"]
    ws.append(headers)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="2F5496")
        c.alignment = Alignment(wrap_text=True, vertical="center")

    for row in ROWS:
        no, drug, ing, date, use, ta, company, appno, submission, toc_suffix, note = row
        appno_num = re.search(r"\d+", appno).group() if appno else None
        ws.append([no, drug, ing, date, use, ta, company, appno or "", submission,
                   "Drugs@FDA" if appno_num else "Drugs@FDA (search)",
                   "FDA Review (TOC)" if toc_suffix else "",
                   note])
        r = ws.max_row
        if appno_num:
            ws.cell(r, 10).hyperlink = DAF.format(appno_num)
        if toc_suffix:
            ws.cell(r, 11).hyperlink = TOC.format(toc_suffix)
        ws.cell(r, 5).alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(r, 12).alignment = Alignment(wrap_text=True, vertical="top")

    widths = [4, 14, 20, 12, 45, 20, 22, 14, 16, 12, 14, 45]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[ws.cell(1, i).column_letter].width = w
    ws.freeze_panes = "A2"

    ws2 = wb.create_sheet("Notes")
    for n in NOTES:
        ws2.append([n])
    ws2.column_dimensions["A"].width = 140
    for c in ws2["A"]:
        c.alignment = Alignment(wrap_text=True, vertical="top")

    wb.save(XLSX_PATH)
    print(f"wrote {XLSX_PATH}")


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_html():
    rows_html = []
    for row in ROWS:
        no, drug, ing, date, use, ta, company, appno, submission, toc_suffix, note = row
        appno_num = re.search(r"\d+", appno).group() if appno else None
        if appno_num:
            daf_cell = f'<td><a href="{DAF.format(appno_num)}">Drugs@FDA</a></td>'
        else:
            daf_cell = (f'<td><a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm">Drugs@FDA'
                        f'<br><span class=\'hint\'>검색창에 "{esc(drug)}" 입력</span></a></td>')
        if toc_suffix:
            toc_cell = f'<td><a href="{TOC.format(toc_suffix)}">FDA Review (TOC)</a></td>'
        else:
            toc_cell = '<td><span class="no-link">아직 게시되지 않음 (리뷰 문서 미게시)</span></td>'
        row_class = ' class="baxfendy"' if drug == "Baxfendy" else ""
        rows_html.append(
            f'<tr{row_class}>\n'
            f'<td>{no}</td><td>{esc(drug)}</td><td>{esc(ing)}</td><td>{date}</td><td>{esc(use)}</td>\n'
            f'<td>{esc(ta)}</td>\n'
            f'<td>{esc(company)}</td><td>{esc(appno or "")}</td><td>{esc(submission)}</td>\n'
            f'{daf_cell}\n'
            f'{toc_cell}\n'
            f'<td>{esc(note)}</td>\n'
            f'</tr>'
        )

    notes_html = "\n".join(f"<li>{esc(n)}</li>" for n in NOTES)

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>FDA Novel Drug Approvals 2026 Dashboard</title>
<style>
  @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css');
  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Pretendard", "Segoe UI", -apple-system, "Apple SD Gothic Neo", Arial, sans-serif;
    margin: 32px; background: #f5f6f8; color: #1f2328;
    -webkit-font-smoothing: antialiased; line-height: 1.55;
  }}
  h1 {{ font-size: 23px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 6px; color: #16243f; }}
  .meta {{ color: #5b6472; font-size: 13.5px; margin-bottom: 20px; }}
  .meta a {{ font-weight: 600; }}
  table {{ border-collapse: collapse; width: 100%; background: #fff; box-shadow: 0 2px 8px rgba(20,30,60,0.08); border-radius: 8px; overflow: hidden; }}
  th, td {{ border: 1px solid #e6e8ec; padding: 10px 12px; font-size: 13.5px; vertical-align: top; letter-spacing: -0.01em; }}
  th {{ background: #2F5496; color: #fff; font-weight: 600; position: sticky; top: 0; }}
  tr:nth-child(even) {{ background: #fafbfc; }}
  tr.baxfendy {{ background: #fff7d6; }}
  tr:hover {{ background: #eef3fb; }}
  a {{ color: #1a5fb4; text-decoration: none; font-weight: 500; }}
  a:hover {{ text-decoration: underline; }}
  .no-link {{ color: #98a1ad; font-style: italic; font-weight: 400; }}
  .hint {{ font-size: 11.5px; color: #8a93a0; font-style: italic; font-weight: 400; }}
  .notes {{ margin-top: 22px; font-size: 13.5px; background: #fff; border: 1px solid #e6e8ec; border-left: 4px solid #2F5496; border-radius: 6px; padding: 16px 20px; box-shadow: 0 1px 4px rgba(20,30,60,0.06); }}
  .notes strong {{ color: #16243f; }}
  .notes li {{ margin-bottom: 8px; line-height: 1.6; }}
</style>
</head>
<body>
<h1>FDA Novel Drug Approvals 2026 Dashboard</h1>
<div class="meta">Source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2026">FDA Novel Drug Approvals for 2026</a> &middot; Updated 2026-08-22 &middot; List current through 2026-08-19 (Pasatru), per FDA's "Content current as of: 08/19/2026"</div>
<table>
<thead>
<tr>
<th>No.</th><th>Drug Name</th><th>Active Ingredient</th><th>Approval Date</th><th>FDA-approved use on approval date</th>
<th>Therapeutic Area</th>
<th>Company</th><th>Application Number</th><th>Submission</th><th>Drugs@FDA</th><th>FDA Application Review</th><th>Note</th>
</tr>
</thead>
<tbody>
{"".join(rows_html)}
</tbody>
</table>

<div class="notes">
<strong>Notes</strong>
<ul>
{notes_html}
</ul>
</div>
</body>
</html>
"""
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"wrote {HTML_PATH}")


if __name__ == "__main__":
    build_xlsx()
    build_html()
    print(f"total rows: {len(ROWS)}")
