# FDA Novel Drug Approvals Dashboards (2021–2026)

## 👉 [대시보드 바로 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/)

아래 링크를 클릭하면 표가 웹페이지로 바로 열립니다. (저장소의 `.html` 파일을 직접 클릭하면 소스 코드가 보이므로, 아래 링크를 이용하세요.)

| 연도 | 건수 | 승인 목록 | 치료영역·회사 분석 |
|---|---|---|---|
| 2021 | 50 | [대시보드 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%20Novel%20Drug%20Approvals%202021%20Dashboard.html) | [분석 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%202021%20Novel%20Drugs%20-%20TA%20and%20Company%20Analysis.html) |
| 2022 | 37 | [대시보드 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%20Novel%20Drug%20Approvals%202022%20Dashboard.html) | [분석 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%202022%20Novel%20Drugs%20-%20TA%20and%20Company%20Analysis.html) |
| 2023 | 55 | [대시보드 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%20Novel%20Drug%20Approvals%202023%20Dashboard.html) | [분석 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%202023%20Novel%20Drugs%20-%20TA%20and%20Company%20Analysis.html) |
| 2024 | 54 | [대시보드 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%20Novel%20Drug%20Approvals%202024%20Dashboard.html) | [분석 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%202024%20Novel%20Drugs%20-%20TA%20and%20Company%20Analysis.html) |
| 2025 | 46 | [대시보드 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%20Novel%20Drug%20Approvals%202025%20Dashboard.html) | [분석 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%202025%20Novel%20Drugs%20-%20TA%20and%20Company%20Analysis.html) |
| 2026 | 45 (2026-09-28 기준) | [대시보드 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%20Novel%20Drug%20Approvals%202026%20Dashboard.html) | [분석 보기](https://sjheo125.github.io/fda-novel-drug-dashboard/FDA%202026%20Novel%20Drugs%20-%20TA%20and%20Company%20Analysis.html) |

---

## 프로젝트 진행 현황 (작업 기록)

**항상 이 파일을 먼저 읽고 이어서 작업할 것.**

## 목표
FDA "Novel Drug Approvals for {year}" 목록을 연도별(2021~2026)로 수집해, 각 약물의 Drugs@FDA 신청번호(NDA/BLA)·리뷰문서 링크까지 채운 데이터셋(xlsx)과 HTML 대시보드, 치료영역(TA)·회사유형(Big Pharma/Biotech) 분석 리포트를 유지한다.

## 파일 구조 (연도별 3종 세트 패턴)
- `FDA Novel Drug Approvals {year} Dashboard.html` — 원자료 테이블 (No/약물명/성분명/승인일/적응증/치료영역/회사/신청번호/Submission/Drugs@FDA링크/TOC리뷰링크/Note)
- `FDA {year} Novel Drugs - TA and Company Analysis.html` — 치료영역·Big Pharma vs Biotech 분석 (막대차트/교차표/insights)
- `FDA_{year}_Novel_Drugs_Dashboard.xlsx` — 원자료 엑셀 (Drugs@FDA·TOC 리뷰 링크는 셀 하이퍼링크로 저장)
- `build_{year}_dashboard.py` / `build_{year}_analysis.py` — 연도별 생성 스크립트 (2021~2025 보유, **2026은 2026-08-22 세션에 `update_2026_list.py`로 신규 작성**)

## 연도별 현재 건수 (대시보드 HTML의 행 개수 기준)
| 연도 | 건수 | 스크립트 | 비고 |
|---|---|---|---|
| 2021 | 50 | build_2021_dashboard.py / build_2021_analysis.py | |
| 2022 | 37 | build_2022_dashboard.py / build_2022_analysis.py | |
| 2023 | 55 | build_2023_dashboard.py / build_2023_analysis.py | |
| 2024 | 54 | build_2024_dashboard.py / build_2024_analysis.py | |
| 2025 | 46 | build_2025_dashboard.py / build_2025_analysis.py | |
| **2026** | **45** | **update_2026_list.py** | 2026-10-04 기준, FDA 목록 "Content current as of: 09/28/2026" |

폴더에 남아있는 `! 할일_ 22, 21년 확인 후 26년 다시.txt`는 내용이 비어 있는 사용자 메모(2021/2022 재검증 후 2026 재작업 예정이었던 것으로 추정) — 아직 미착수.

## 세션 로그

### 세션 A (~2026-07-02, 스크립트 없이 진행) — 2026년 리스트 최초 구축
- FDA "Novel Drug Approvals for 2026" 페이지 기준 23건(Zycubo~Lumvoa, 2026-06-26까지) 수집
- 각 약물의 Drugs@FDA 신청번호를 web search로 조사, 신뢰도 낮은 결과는 사용자 직접확인으로 보정 (Veppanu, Decnupaz, Hepcludex, Xocova, Utebzi 등)
- Cypsedo/Ambelvist/Lumvoa 3건은 신청번호 미확인 상태로 남김

### 세션 B (2026-08-22) — 2026년 리스트 33건으로 갱신 + 신규 빌드 스크립트 작성
1. **`fda-novel-drug-reviews` 스킬 로드** 후 Drugs@FDA 조회 방법론 확인
2. FDA 공식 페이지(Claude_Browser로 접속 — WebFetch는 이 도메인에서 404 발생)에서 33건 전체 테이블 확보. "Content current as of: 08/19/2026"
3. 신규 10건(No.24 Trutakna ~ No.33 Pasatru)의 신청번호·회사·Submission 정보를 Drugs@FDA 브라우즈(`browseByLetter.page`) + `overview.process&varApplNo=` 페이지에서 직접 확인
   - Trutakna BLA 761486(Vera Therapeutics, 가속승인) · Revtorpyk NDA 219908(Celcuity) · Lipfendra NDA 220848(Merck) · Jideytro NDA 220185(GSK/Nuvalent) · Lytenava BLA 761320(Outlook Therapeutics) · Simtriyo NDA 218145(Otsuka) · Orzeyful NDA 220860(Takeda) · Tauklarify NDA 220496(Lantheus/Cerveau) · Zenbexus NDA 221075(BMS, 가속승인) · Pasatru(Regeneron, 신청번호 미색인 — 8/19 승인 3일 경과라 아직 안 뜸)
4. **부수 발견**: 기존 미확인 3건도 이번에 재검색해서 해결 — Cypsedo NDA 220482(브랜드명이 아니라 활성성분명 "CIPEPOFOL"로만 색인되어 있었음), Ambelvist NDA 219627, Lumvoa BLA 761530
5. `update_2026_list.py` 신규 작성 (2026년 최초의 빌드 스크립트) — xlsx + Dashboard.html을 33건 데이터로 동시 생성. 신청번호 파싱 버그(정규식 `\d+` 미사용으로 "BLA 761326 (Orig2)" 같은 케이스에서 링크 깨짐) 발견 후 수정
6. `FDA 2026 Novel Drugs - TA and Company Analysis.html` 전면 재계산 (23건→33건)
   - Oncology/Hematology가 7건으로 최다 치료영역 등극 (기존 1위였던 Infectious Disease 5건 추월)
   - 신규 치료영역 3개 첫 등장: Nephrology(Trutakna), Ophthalmology(Lytenava), Neurology/Sleep(Orzeyful) — 모두 first-in-class
   - 가속승인 0건 → 2건으로 반전 (Trutakna, Zenbexus — Zenbexus는 MRD 기반 혈액암 가속승인 업계 최초 사례)
   - Big Pharma : Biotech = 12:11(52:48) → 18:15(55:45)로 이동
7. 브라우저 프리뷰로 두 HTML 모두 검증 (행 개수, 신청번호 링크, 콘솔 에러 없음 확인). `.claude/launch.json`에 "FDA New Drug Approval Dashboard" 프리뷰 서버(포트 8770) 설정 추가

### 세션 C (2026-10-04) — 45건으로 갱신
- 신규 12건(No.34 Rasonque ~ No.45 Emcitate, 8/26~9/28) 추가, 모두 Drugs@FDA browseByLetter로 신청번호 확인
- Pasatru = BLA 761508 확인. 24~33번 리뷰(TOC) 전부 게시 확인 → 링크 반영. 신규 중 리뷰 게시는 Mimrylo·Zanvastro뿐
- Analysis HTML 45건 기준 재작성: Oncology 11, Rare 9, Biotech 23 : Big Pharma 22 역전, Rheumatology 신규 TA
- GitHub Pages(https://sjheo125.github.io/fda-novel-drug-dashboard/)용 index.html을 폴더에 생성(2026 = 45, as of 2026-09-28) — 업로드는 사용자가 직접
- 신규 12건의 가속승인 여부는 미확인(승인서한 PDF가 스크립트로 열리지 않음)

## 다음 세션 시 참고
- 2026년 갱신은 `update_2026_list.py`의 `ROWS` 리스트에 신규 항목을 추가하고 재실행하면 됨 (`python update_2026_list.py`) — xlsx와 Dashboard.html이 함께 갱신됨. `TA and Company Analysis.html`은 수작업 서술형이라 별도로 숫자·insight를 다시 계산해서 반영해야 함(자동화 안 되어 있음)
- 리뷰(TOC) 미게시 10건(34~45번 중 Mimrylo·Zanvastro 제외) 다음 갱신 때 재확인, 가속승인 여부도 함께 확인
- 갱신 후 index.html의 2026 건수/기준일도 수정해 GitHub에 함께 업로드
- 2026-10-04 후속: 모든 build 스크립트 출력 경로를 상대경로로 변경. 2021/2024/2025 스크립트를 공개 HTML(이전 세션에서 Claude가 HTML만 직접 패치했던 것)과 일치시키고 오류 정정 — 이제 스크립트 재실행 결과가 공개본과 동일. 앞으로 수정은 HTML이 아니라 스크립트에 할 것.
