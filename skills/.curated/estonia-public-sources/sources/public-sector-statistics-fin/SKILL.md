---
name: public-sector-statistics-fin
description: Retrieve Ministry of Finance public-sector statistics records, including institution counts, salary overviews, and embedded BI dashboards.
---

# Public-Sector Statistics (fin.ee)

## Use when
- You need public-sector institution/workforce/payroll context published by Ministry of Finance.
- You need downloadable XLSX/PDF records plus official dashboard links.

## Avoid when
- You need legally binding pay rules text only (use civil-service pay governance skill).

## Inputs
- Target year.
- Subtopic (`institutions`, `salary-overview`, `survey`, `dashboard`).

## Outputs
- Structured record list with downloadable files and dashboard references.

## Access reality statement
- Access type: `download files` + `UI copy-only`.
- Verified on 2026-02-24.
- Page exposes multiple direct files and embedded PowerBI links.

## Primary endpoints
- Public-sector statistics page: https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/riigihaldus/avaliku-sektori-statistika

## Retrieval workflow (reproducible)
1. Open page and collect direct file links (`/sites/default/files/documents/...`).
2. Parse title and file extension to classify records (XLSX, PDF).
3. Capture embedded dashboard URLs (`app.powerbi.com/...`, if present).
4. Extract publication context from surrounding text/date markers.
5. Return normalized records with source URL and file URL.

## Request/query contract
- No auth required for listed page/files.
- Files are direct HTTP downloads from fin.ee storage paths.
- Dashboard links are UI embed URLs without documented public query contract.

## Output schema expectations
- `source_page_url`
- `record_title`
- `record_url`
- `record_type`
- `year`
- `publication_date` (if present)
- `topic`

## Limits and caveats
- Page mixes institution, salary, and survey outputs in one place.
- Some dashboard links may not provide direct CSV exports.
- Estonian terminology requires consistent mapping in downstream analysis.

## Verification hooks
- Page includes files such as `Avaliku_sektori_asutused_asutuse_liikide_loikes_juuli_2025.xlsx`.
- Page includes files such as `Ametnike põhipalgad ... kogupalgad ... .xlsx`.
- Page includes PowerBI embed URLs (`app.powerbi.com/view?...`).
