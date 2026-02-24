---
name: defence-policy-budget-documents
description: Retrieve Ministry of Defence policy/budget baseline documents, programmes, and legal-base references from official document pages.
---

# Defence Policy and Budget Documents

## Use when
- You need defence budget policy context and baseline policy/legal documents.
- You need official programme and development-document PDFs from MoD pages.

## Avoid when
- You need procurement contract-level records (use procurement sources).

## Inputs
- Topic (`budget`, `policy-base`, `programme`, `result-report`).
- Year range.

## Outputs
- Structured document inventory with publication dates and links.

## Access reality statement
- Access type: `download files` + `UI copy-only`.
- Verified on 2026-02-24.
- Pages publish direct PDF links and legal references (including Riigi Teataja links).

## Primary endpoints
- Defence budget page: https://www.kaitseministeerium.ee/et/eesmargid-tegevused/kaitse-eelarve
- Policy/legal base page: https://www.kaitseministeerium.ee/et/eesmargid-tegevused/alusdokumendid-ja-oigusaktid

## Retrieval workflow (reproducible)
1. Open policy/legal base page and collect linked development documents and legal references.
2. Open defence budget page and collect budget/programme related links.
3. Normalize all relative file links (`/sites/default/files/...`) to absolute URLs.
4. Classify records by type: policy baseline, programme, result report, legal basis.
5. Return records with source page URL and publication/date hints from filename/context.

## Request/query contract
- No auth required.
- Link-based extraction from page HTML.
- Mixed link types: downloadable files and external legal references.

## Output schema expectations
- `source_page_url`
- `document_title`
- `document_url`
- `document_type`
- `publication_year_or_date`
- `legal_reference` (boolean)
- `notes`

## Limits and caveats
- Some links are historical and may route to archived structures.
- Titles are often Estonian and can include long policy naming.
- Budget context may be distributed across multiple ministry pages.

## Verification hooks
- Policy/legal page includes files such as `eesti_julgeolekupoliitika_alused_est_22.02.pdf` and `rkak_2017_2026_avalik_osa.pdf`.
- Policy/legal page includes Riigi Teataja legal links.
- Page includes result reports under `Julgeolek ja riigikaitse` section.
