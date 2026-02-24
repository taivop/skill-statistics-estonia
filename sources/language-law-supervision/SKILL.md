---
name: language-law-supervision
description: Retrieve language-law supervision and annual activity report records from Keeleamet oversight pages and embedded document tables.
---

# Language-Law Supervision (Keeleamet)

## Use when
- You need official language-law supervision context and annual oversight reports.
- You need downloadable supervision/activity report files from Keeleamet.

## Avoid when
- You need court judgments on language-law disputes (use judiciary/legal sources).

## Inputs
- Year range.
- Focus area (`tegevusaruanded`, supervision topic).

## Outputs
- Report index with document URLs, dates, and supervision context metadata.

## Access reality statement
- Access type: `download files` + `UI copy-only`.
- Verified on 2026-02-24.
- Keeleamet oversight pages use embedded datatable JSON containing PDF report links.

## Primary endpoints
- Oversight section root: https://www.keeleamet.ee/keeleameti-tegevused-ja-eesmargid/keeleseaduse-ja-teiste-keeleoskust-ja-keelekasutust
- Supervision results page: https://www.keeleamet.ee/keeleameti-tegevused-ja-eesmargid/keeleseaduse-ja-teiste-keeleoskust-ja-keelekasutust-3

## Retrieval workflow (reproducible)
1. Open supervision results page (`...-3`) and locate datatable JSON script.
2. Parse each row for report title, date, and file URL.
3. Expand relative file links to absolute `https://www.keeleamet.ee/...`.
4. Classify reports by year and institution naming (Keeleamet / Keeleinspektsioon historical records).
5. Return structured report index and optional extracted KPI summary per report.

## Request/query contract
- No auth required.
- Report rows are embedded in `script type="application/json" id="datatable-..."`.
- Row columns include title/link, insertion date, and download action link.

## Output schema expectations
- `source_page_url`
- `report_title`
- `report_date`
- `report_url`
- `institution_label`
- `year`
- `notes`

## Limits and caveats
- Content is Estonian and may include historical institution naming changes.
- Some file names contain legacy spelling/format variations.

## Verification hooks
- Page title is `Järelevalvetulemused`.
- Embedded datatable id observed: `datatable-d9c85bdb9fd9aead061de6c29867b7356307006a708a4723a9d19accccabc7e3`.
- Rows include files such as `Keeleameti 2024. aasta tegevuse aruanne.pdf`.
