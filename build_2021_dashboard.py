# -*- coding: utf-8 -*-
import os
"""Build FDA 2021 Novel Drug Approvals Dashboard HTML"""

DAF_BASE = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&varApplNo="
TOC_BASE = "https://www.accessdata.fda.gov/drugsatfda_docs/nda/{year}/{appno}Orig1s000TOC.html"

CUSTOM_TOC = {}

def daf_link(appno_num):
    return DAF_BASE + appno_num

def toc_link(appno_num, year=2021):
    return TOC_BASE.format(year=year, appno=appno_num)

# Data tuple:
# (no, name, ingredient, date, use, ta, company, co_type, appno_disp, appno_num, submission, toc_year, note)

drugs = [
    (1, 'Verquvo', 'vericiguat', '2021-01-09',
     'Reduce risk of cardiovascular death and heart failure hospitalization in adults with symptomatic chronic heart failure with ejection fraction <45% following a worsening HF event',
     'Cardiovascular', 'Bayer / Merck', 'Big Pharma', 'NDA 214377', '214377', 'Original', 2021,
     'First-in-class sGC stimulator for heart failure; targets nitric oxide–sGC–cGMP pathway'),

    (2, 'Cabenuva', 'cabotegravir + rilpivirine', '2021-01-22',
     'Complete HIV-1 regimen for virologically stable adults on a stable antiretroviral regimen (monthly long-acting injectable; intramuscular)',
     'Infectious Disease', 'ViiV Healthcare / Janssen', 'Big Pharma', 'NDA 212888', '212888', 'Original', 2021,
     'First complete long-acting injectable HIV-1 regimen; replaces daily oral therapy with once-monthly injections'),

    (3, 'Lupkynis', 'voclosporin', '2021-01-22',
     'Active lupus nephritis in adults, in combination with background immunosuppressive therapy',
     'Nephrology', 'Aurinia Pharmaceuticals', 'Biotech', 'NDA 213716', '213716', 'Original', 2021,
     'First calcineurin inhibitor specifically approved for lupus nephritis; novel analog with more predictable PK than tacrolimus'),

    (4, 'Ukoniq', 'umbralisib', '2021-02-05',
     'Adults with relapsed or refractory marginal zone lymphoma (MZL) after ≥1 prior anti-CD20-based regimen, and follicular lymphoma (FL) after ≥3 prior lines',
     'Oncology', 'TG Therapeutics', 'Biotech', 'NDA 213176', '213176', 'Original', 2021,
     'Accelerated Approval – voluntary market withdrawal 2022 after clinical trial showed possible increased mortality risk'),

    (5, 'Evkeeza', 'evinacumab-dgnb', '2021-02-11',
     'Adjunct to other LDL-lowering therapies for adults and pediatric patients ≥12 years with homozygous familial hypercholesterolemia (HoFH)',
     'Cardiovascular', 'Regeneron', 'Big Pharma', 'BLA 761181', '761181', 'Original', 2021,
     'First-in-class ANGPTL3 inhibitor; reduces LDL-C by ~47% in HoFH patients regardless of LDLR mutation status'),

    (6, 'Cosela', 'trilaciclib', '2021-02-26',
     'Decrease the incidence of chemotherapy-induced myelosuppression in adults when administered prior to certain chemotherapy regimens for extensive-stage SCLC',
     'Oncology', 'G1 Therapeutics', 'Biotech', 'NDA 214200', '214200', 'Original', 2021,
     'First-in-class myeloprotection agent; CDK4/6 inhibitor given before chemo to transiently arrest hematopoietic stem cells'),

    (7, 'Tepmetko', 'tepotinib', '2021-02-26',
     'Adults with metastatic NSCLC harboring MET exon 14 skipping alterations',
     'Oncology', 'EMD Serono / Merck KGaA', 'Big Pharma', 'NDA 214096', '214096', 'Original', 2021,
     'Accelerated Approval – first once-daily oral MET inhibitor approved for METex14 NSCLC'),

    (8, 'Amondys 45', 'casimersen', '2021-02-25',
     'Duchenne muscular dystrophy (DMD) in patients with a confirmed mutation amenable to exon 45 skipping',
     'Neurology', 'Sarepta Therapeutics', 'Biotech', 'NDA 213026', '213026', 'Original', 2021,
     'Accelerated Approval – antisense oligonucleotide for exon 45 skipping; applies to ~8% of DMD patients'),

    (9, 'Pepaxto', 'melphalan flufenamide', '2021-02-26',
     'Adults with relapsed or refractory multiple myeloma who have received ≥4 prior lines of therapy (in combination with dexamethasone)',
     'Oncology', 'Oncopeptides', 'Biotech', 'NDA 214383', '214383', 'Original', 2021,
     'Accelerated Approval – voluntary market withdrawal October 2021 after confirmatory OCEAN trial showed worse OS vs comparator'),

    (10, 'Nulibry', 'fosdenopterin', '2021-03-05',
     'Reduce the risk of mortality in patients with molybdenum cofactor deficiency (MoCD) type A',
     'Rare Disease', 'PTC Therapeutics', 'Biotech', 'NDA 214018', '214018', 'Original', 2021,
     'First FDA-approved treatment for MoCD type A; cofactor precursor substitution for this fatal infantile neurological disease'),

    (11, 'Ponvory', 'ponesimod', '2021-03-18',
     'Relapsing forms of multiple sclerosis (CIS, RRMS, active SPMS) in adults (once-daily oral S1P receptor modulator)',
     'Neurology', 'Janssen / J&J', 'Big Pharma', 'NDA 213498', '213498', 'Original', 2021,
     ''),

    (12, 'Fotivda', 'tivozanib', '2021-03-10',
     'Adults with relapsed or refractory renal cell carcinoma (RCC) after two or more prior systemic therapies (once-daily oral VEGFR inhibitor)',
     'Oncology', 'AVEO Pharmaceuticals', 'Biotech', 'NDA 212904', '212904', 'Original', 2021,
     'highly selective VEGFR1/2/3 inhibitor with favorable tolerability profile'),

    (13, 'Azstarys', 'serdexmethylphenidate + dexmethylphenidate', '2021-03-31',
     'Attention-deficit/hyperactivity disorder (ADHD) in patients 6 years and older (once-daily oral extended-release capsule)',
     'Neurology', 'KemPharm / Corium', 'Biotech', 'NDA 212994', '212994', 'Original', 2021,
     'Novel prodrug (SDX) co-formulated with d-MPH; longer duration with delayed peak vs immediate-release MPH'),

    (14, 'Zegalogue', 'dasiglucagon', '2021-03-22',
     'Severe hypoglycemia in patients with diabetes mellitus ≥6 years of age (subcutaneous injection; first glucagon analog)',
     'Endocrinology', 'Zealand Pharma', 'Biotech', 'NDA 214060', '214060', 'Original', 2021,
     'First glucagon analog (non-human) for severe hypoglycemia'),

    (15, 'Qelbree', 'viloxazine', '2021-04-02',
     'Attention-deficit/hyperactivity disorder (ADHD) in pediatric patients 6–17 years (non-stimulant; once-daily oral extended-release capsule)',
     'Neurology', 'Supernus Pharmaceuticals', 'Biotech', 'NDA 211964', '211964', 'Original', 2021,
     'First non-stimulant SNRI-class agent approved for pediatric ADHD since Strattera (atomoxetine, 2003)'),

    (16, 'Jemperli', 'dostarlimab-gxly', '2021-04-22',
     'Adults with dMMR recurrent or advanced endometrial cancer that progressed during or following prior treatment with a platinum-containing regimen',
     'Oncology', 'GlaxoSmithKline', 'Big Pharma', 'BLA 761174', '761174', 'Original', 2021,
     'Accelerated Approval – anti-PD-1 antibody; first approval specifically for dMMR/MSI-H endometrial cancer'),

    (17, 'Zynlonta', 'loncastuximab tesirine-lpyl', '2021-04-23',
     'Adults with relapsed or refractory large B-cell lymphoma (LBCL) after ≥2 prior lines of systemic therapy',
     'Oncology', 'ADC Therapeutics', 'Biotech', 'BLA 761196', '761196', 'Original', 2021,
     'Accelerated Approval – first CD19-targeting antibody-drug conjugate (ADC) using a DNA-crosslinking pyrrolobenzodiazepine (PBD) payload'),

    (18, 'Nextstellis', 'drospirenone + estetrol', '2021-05-07',
     'Prevention of pregnancy in females of reproductive potential (24/4 oral contraceptive regimen)',
     "Women's Health", 'Mayne Pharma / Theramex', 'Biotech', 'NDA 214154', '214154', 'Original', 2021,
     'First oral contraceptive containing estetrol (E4), a native human estrogen synthesized by the fetal liver'),

    (19, 'Empaveli', 'pegcetacoplan', '2021-05-14',
     'Adults with paroxysmal nocturnal hemoglobinuria (PNH) (targeted C3 complement inhibitor; subcutaneous infusion twice weekly)',
     'Hematology', 'Apellis Pharmaceuticals', 'Biotech', 'NDA 215014', '215014', 'Original', 2021,
     'First C3-targeting complement inhibitor; acts more proximally than C5 inhibitors, addressing both intravascular and extravascular hemolysis'),

    (20, 'Rybrevant', 'amivantamab-vmjw', '2021-05-21',
     'Adults with locally advanced or metastatic NSCLC with EGFR exon 20 insertion mutations, following platinum-based chemotherapy',
     'Oncology', 'Janssen / J&J', 'Big Pharma', 'BLA 761210', '761210', 'Original', 2021,
     'Accelerated Approval – first EGFR-MET bispecific antibody; mechanism enables activity in EGFR exon 20 insertions'),

    (21, 'Pylarify', 'piflufolastat F 18', '2021-05-27',
     'PET imaging of PSMA-positive lesions in men with prostate cancer — staging of high-risk disease and detection of suspected metastatic or recurrent disease',
     'Radiology', 'Lantheus Holdings', 'Biotech', 'NDA 214793', '214793', 'Original', 2021,
     'First PSMA-targeted PET imaging agent approved in the US; identifies disease at staging and recurrence with high sensitivity'),

    (22, 'Lumakras', 'sotorasib', '2021-05-28',
     'Adults with KRAS G12C-mutated locally advanced or metastatic NSCLC, as determined by an FDA-approved test, after at least one prior systemic therapy',
     'Oncology', 'Amgen', 'Big Pharma', 'NDA 214665', '214665', 'Original', 2021,
     "Accelerated Approval – first KRAS inhibitor ever approved; breakthrough for a target long considered 'undruggable'"),

    (23, 'Truseltiq', 'infigratinib', '2021-05-28',
     'Adults with previously treated, unresectable locally advanced or metastatic cholangiocarcinoma harboring FGFR2 fusions or other rearrangements',
     'Oncology', 'BridgeBio / QED Therapeutics', 'Biotech', 'NDA 214622', '214622', 'Original', 2021,
     'Accelerated Approval – voluntary withdrawal January 2023 after PROOF confirmatory trial was discontinued'),

    (24, 'Lybalvi', 'olanzapine + samidorphan', '2021-05-28',
     'Schizophrenia in adults, and manic or mixed episodes associated with bipolar I disorder in adults (once-daily oral tablet)',
     'Neurology', 'Alkermes', 'Biotech', 'NDA 213378', '213378', 'Original', 2021,
     'Fixed-dose combination with opioid antagonist (samidorphan) added to reduce olanzapine-associated weight gain'),

    (25, 'Brexafemme', 'ibrexafungerp', '2021-06-01',
     'Vulvovaginal candidiasis (vaginal yeast infections) in adult and postmenarchal pediatric females (oral triterpenoid antifungal)',
     'Infectious Disease', 'SCYNEXIS', 'Biotech', 'NDA 214900', '214900', 'Original', 2021,
     'First-in-class glucan synthase inhibitor (triterpenoid) for vaginal candidiasis; non-azole oral treatment option'),

    (26, 'Aduhelm', 'aducanumab-avwa', '2021-06-07',
     "Alzheimer's disease (intravenous infusion; targets amyloid beta plaques)",
     'Neurology', 'Biogen', 'Big Pharma', 'BLA 761178', '761178', 'Original', 2021,
     'Accelerated Approval – highly controversial; FDA advisory committee voted 10–0 against approval; approval later rescoped to early AD; withdrawn from market 2024'),

    (27, 'Rylaze', 'asparaginase erwinia chrysanthemi (recombinant)-rywn', '2021-06-30',
     'Component of multi-agent chemotherapeutic regimen for ALL or LBL in adults and pediatric patients ≥1 month with hypersensitivity to E. coli-derived asparaginase',
     'Oncology', 'Jazz Pharmaceuticals', 'Biotech', 'BLA 761179', '761179', 'Original', 2021,
     'First recombinant erwinia asparaginase; provides consistent asparaginase activity throughout treatment without E. coli cross-reactivity'),

    (28, 'Kerendia', 'finerenone', '2021-07-09',
     'Reduce the risk of sustained eGFR decline, end-stage kidney disease, cardiovascular death, non-fatal MI, and hospitalization for HF in adults with CKD associated with type 2 diabetes',
     'Nephrology', 'Bayer', 'Big Pharma', 'NDA 215341', '215341', 'Original', 2021,
     'First non-steroidal mineralocorticoid receptor antagonist (MRA) with cardiorenal protective indication; more selective than spironolactone'),

    (29, 'Rezurock', 'belumosudil', '2021-07-16',
     'Chronic graft-versus-host disease (cGVHD) in adults and pediatric patients ≥12 years after failure of at least two prior lines of systemic therapy',
     'Hematology', 'Kadmon Pharmaceuticals', 'Biotech', 'NDA 214783', '214783', 'Original', 2021,
     'First-in-class selective ROCK2 inhibitor; novel immunomodulatory mechanism for cGVHD after multi-line failure'),

    (30, 'Fexinidazole', 'fexinidazole', '2021-07-19',
     'First-stage (hemolymphatic) and second-stage (meningoencephalitic) human African trypanosomiasis (HAT) due to T.b. gambiense in patients ≥6 years weighing ≥20 kg',
     'Infectious Disease', 'Sanofi / DNDi', 'Big Pharma', 'NDA 214429', '214429', 'Original', 2021,
     'First all-oral treatment for both stages of sleeping sickness; nitroimidazole developed through Sanofi–DNDi public-private partnership'),

    (31, 'Bylvay', 'odevixibat', '2021-07-20',
     'Pruritus in patients ≥3 months of age with progressive familial intrahepatic cholestasis (PFIC) (oral pellets or capsules; once daily)',
     'Rare Disease', 'Albireo Pharma', 'Biotech', 'NDA 215498', '215498', 'Original', 2021,
     'First ileal bile acid transporter (IBAT) inhibitor approved for PFIC; reduces bile acid recirculation to relieve severe cholestatic pruritus'),

    (32, 'Saphnelo', 'anifrolumab-fnia', '2021-07-30',
     'Moderate-to-severe systemic lupus erythematosus (SLE) in adults on a standard therapy regimen (intravenous infusion monthly)',
     'Immunology', 'AstraZeneca', 'Big Pharma', 'BLA 761123', '761123', 'Original', 2021,
     'First type I interferon receptor (IFNAR1) antagonist approved for SLE; targets a key cytokine pathway driving lupus pathophysiology'),

    (33, 'Nexviazyme', 'avalglucosidase alfa-ngpt', '2021-08-06',
     'Patients ≥1 year of age with late-onset Pompe disease (GAA enzyme replacement therapy; biweekly IV infusion)',
     'Rare Disease', 'Sanofi / Genzyme', 'Big Pharma', 'BLA 761194', '761194', 'Original', 2021,
     'Next-generation ERT with enhanced M6P receptor uptake; superior to alglucosidase alfa (Lumizyme) in Phase 3 COMET trial'),

    (34, 'Welireg', 'belzutifan', '2021-08-13',
     'Adults with VHL disease who require therapy for associated renal cell carcinoma (RCC), CNS hemangioblastomas, or pancreatic neuroendocrine tumors (pNET)',
     'Oncology', 'Merck', 'Big Pharma', 'NDA 215383', '215383', 'Original', 2021,
     'First-in-class HIF-2α inhibitor; first approved systemic therapy for von Hippel-Lindau disease-associated tumors'),

    (35, 'Korsuva', 'difelikefalin', '2021-08-23',
     'Moderate-to-severe pruritus associated with chronic kidney disease (CKD) in adults undergoing hemodialysis (intravenous; three times weekly post-dialysis)',
     'Nephrology', 'Cara Therapeutics', 'Biotech', 'NDA 214916', '214916', 'Original', 2021,
     'First-in-class peripherally restricted kappa opioid receptor (KOR) agonist; targets peripheral itch pathway without CNS effects'),

    (36, 'Skytrofa', 'lonapegsomatropin-tcgd', '2021-08-25',
     'Pediatric patients ≥1 year with growth failure due to inadequate growth hormone (GH) secretion (once-weekly subcutaneous injection)',
     'Endocrinology', 'Ascendis Pharma', 'Biotech', 'BLA 761177', '761177', 'Original', 2021,
     'First once-weekly growth hormone replacement (TransCon PEG technology); reduces injection burden from daily to weekly'),

    (37, 'Exkivity', 'mobocertinib', '2021-09-15',
     'Adults with locally advanced or metastatic NSCLC with EGFR exon 20 insertion mutations, whose disease progressed on or after platinum-based chemotherapy',
     'Oncology', 'Takeda', 'Big Pharma', 'NDA 215310', '215310', 'Original', 2021,
     'Accelerated Approval – first oral EGFR TKI designed specifically for exon 20 insertions; approval voluntarily withdrawn 2024 after PAPILLON trial favored amivantamab+chemo'),

    (38, 'Tivdak', 'tisotumab vedotin-tftv', '2021-09-20',
     'Adults with recurrent or metastatic cervical cancer with disease progression on or after chemotherapy',
     'Oncology', 'Seagen / Genmab', 'Biotech', 'BLA 761208', '761208', 'Original', 2021,
     'Accelerated Approval – first tissue factor (TF)-targeting antibody-drug conjugate; first ADC approved for cervical cancer'),

    (39, 'Qulipta', 'atogepant', '2021-09-28',
     'Preventive treatment of episodic migraine in adults (once-daily oral CGRP receptor antagonist)',
     'Neurology', 'AbbVie', 'Big Pharma', 'NDA 215206', '215206', 'Original', 2021,
     'First oral CGRP receptor antagonist (gepant) approved specifically for migraine prevention; prior gepants were only for acute treatment'),

    (40, 'Livmarli', 'maralixibat', '2021-09-29',
     'Cholestatic pruritus in patients ≥1 year with Alagille syndrome (ALGS) (oral solution; once daily)',
     'Rare Disease', 'Mirum Pharmaceuticals', 'Biotech', 'NDA 214662', '214662', 'Original', 2021,
     'IBAT inhibitor for Alagille syndrome-associated pruritus; first approved treatment for ALGS-associated cholestatic pruritus'),

    (41, 'Tavneos', 'avacopan', '2021-10-07',
     'Severe active ANCA-associated vasculitis (granulomatosis with polyangiitis [GPA] and microscopic polyangiitis [MPA]) in adults, as adjunctive treatment with standard of care therapy',
     'Immunology', 'ChemoCentryx', 'Biotech', 'NDA 214487', '214487', 'Original', 2021,
     'First C5a receptor (C5aR1) inhibitor approved for ANCA vasculitis; reduces corticosteroid dependence in GPA/MPA treatment'),

    (42, 'Scemblix', 'asciminib', '2021-10-29',
     'Philadelphia chromosome-positive CML in chronic phase previously treated with ≥2 TKIs, and for CML in CP with T315I mutation (oral once or twice daily)',
     'Oncology', 'Novartis', 'Big Pharma', 'NDA 215358', '215358', 'Original', 2021,
     'Accelerated Approval (T315I arm) – first STAMP inhibitor (Specifically Targeting ABL Myristoyl Pocket); unique allosteric mechanism active against T315I gatekeeper mutation'),

    (43, 'Besremi', 'ropeginterferon alfa-2b-njft', '2021-11-12',
     'Adults with polycythemia vera (PV) (subcutaneous injection every 2 weeks initially, then monthly)',
     'Oncology', 'PharmaEssentia', 'Biotech', 'BLA 761166', '761166', 'Original', 2021,
     'First interferon specifically approved for polycythemia vera; long-acting PEGylated form enables biweekly to monthly dosing'),

    (44, 'Voxzogo', 'vosoritide', '2021-11-19',
     'Increase linear growth in pediatric patients with achondroplasia aged ≥5 years with open epiphyses (once-daily subcutaneous injection)',
     'Rare Disease', 'BioMarin Pharmaceutical', 'Biotech', 'NDA 214938', '214938', 'Original', 2021,
     'Accelerated Approval – first approved treatment to increase linear growth in achondroplasia; C-type natriuretic peptide (CNP) analogue targeting FGFR3 pathway'),

    (45, 'Livtencity', 'maribavir', '2021-11-23',
     'Post-transplant cytomegalovirus (CMV) infection and/or disease refractory to treatment (with or without resistance) in adults and pediatric patients ≥12 years (oral twice daily)',
     'Infectious Disease', 'Takeda', 'Big Pharma', 'NDA 215596', '215596', 'Original', 2021,
     'First-in-class pUL97 protein kinase inhibitor for CMV; first new antiviral mechanism for CMV infection in over two decades'),

    (46, 'Cytalux', 'pafolacianine', '2021-11-29',
     'Adjunct to identify malignant ovarian cancer lesions in adult women during surgery (intravenous injection; intraoperative NIR fluorescence imaging)',
     'Oncology', 'On Target Laboratories', 'Biotech', 'NDA 214907', '214907', 'Original', 2021,
     'first FDA-approved fluorescent imaging agent targeting folate receptor alpha for intraoperative visualization of ovarian cancer lesions'),

    (47, 'Vyvgart', 'efgartigimod alfa-fcab', '2021-12-17',
     'Generalized myasthenia gravis (gMG) in adults who are anti-acetylcholine receptor (AChR) antibody positive (intravenous infusion; 4-week cycle)',
     'Neurology', 'argenx', 'Biotech', 'BLA 761195', '761195', 'Original', 2022,
     'First FcRn (neonatal Fc receptor) antagonist approved for gMG; reduces pathogenic IgG antibodies by blocking FcRn-mediated IgG recycling'),

    (48, 'Tezspire', 'tezepelumab-ekko', '2021-12-17',
     'Add-on maintenance treatment of adults and pediatric patients ≥12 years with severe asthma (subcutaneous injection monthly)',
     'Pulmonology', 'AstraZeneca / Amgen', 'Big Pharma', 'BLA 761224', '761224', 'Original', 2021,
     'First-in-class anti-TSLP antibody; only severe asthma biologic approved regardless of eosinophil count or type 2 inflammation status'),

    (49, 'Leqvio', 'inclisiran', '2021-12-22',
     'Adjunct to diet and maximally tolerated statin therapy in adults with HeFH or clinical ASCVD who require additional LDL-C lowering (subcutaneous injection; twice yearly)',
     'Cardiovascular', 'Novartis', 'Big Pharma', 'NDA 214012', '214012', 'Original', 2022,
     'First siRNA therapy approved for cardiovascular disease; targets PCSK9 mRNA; twice-yearly office-administered injection'),

    (50, 'Adbry', 'tralokinumab-ldrm', '2021-12-27',
     'Moderate-to-severe atopic dermatitis in adults whose disease is not adequately controlled with topical prescription therapies (subcutaneous injection every 2 weeks)',
     'Dermatology', 'LEO Pharma', 'Biotech', 'BLA 761180', '761180', 'Original', 2022,
     'First IL-13-specific monoclonal antibody for atopic dermatitis; selectively neutralizes IL-13 without blocking IL-4 signaling'),

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
<title>FDA 2021 Novel Drug Approvals Dashboard</title>
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
    <h1>FDA 2021 Novel Drug Approvals Dashboard</h1>
    <p>Content current as of {today} &nbsp;|&nbsp; Source: FDA Novel Drug Approvals 2021 (CDER NMEs and new therapeutic biologics) &nbsp;|&nbsp; Total: {total} novel drug approvals researched</p>
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
    Data source: <a href="https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2021" target="_blank">FDA Novel Drug Approvals for 2021</a>
    &nbsp;|&nbsp; TOC links: accessdata.fda.gov &nbsp;|&nbsp; Built: {today}
  </div>

</div>
</body>
</html>"""

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FDA Novel Drug Approvals 2021 Dashboard.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Dashboard saved to: {output_path}")
print(f"Total: {total} | Big Pharma: {n_bigpharma} | Biotech: {n_biotech}")
print(f"Accelerated Approval: {n_accel} | Resubmission: {n_resub} | Oncology: {n_oncology}")
