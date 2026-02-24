---
name: public-finance-data
description: Retrieve Estonian Ministry of Finance fiscal records (RES, annual budgets, liabilities, investor relations, payments, and consolidated accounting) from fin.ee pages, document tables, and embedded dashboards.
---

# Estonia Public Finance Data (fin.ee)

## Use when
- You need state budget strategy (RES), annual budget package records, debt/liability context, investor disclosures, payment dashboards, or consolidated state accounting reports.
- You need reproducible Ministry of Finance source documents with publication dates.

## Avoid when
- You need transaction-level tax administration data (use tax-specific sources).

## Inputs
- Topic scope: `res`, `annual-budget`, `liabilities`, `investor-relations`, `government-payments`, `consolidated-accounting`.
- Year or year range.

## Outputs
- Source-linked extract of files/records and key fiscal metadata.

## Access reality statement
- Access type: `download files` + `UI copy-only` (embedded PowerBI/Tableau views).
- Verified on 2026-02-24.
- fin.ee document tables are exposed as HTML-embedded JSON blocks (`script type="application/json" id="datatable-..."`).

## Primary endpoints
- RES: https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/riigi-eelarvestrateegia
- Annual budget package: https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/riigieelarved
- State financial liabilities: https://www.fin.ee/riigi-rahandus-ja-maksud/riigikassa/riigi-finantskohustised
- Treasury investor relations: https://www.fin.ee/riigi-rahandus-ja-maksud/riigikassa/investorsuhted
- Government-sector payments: https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine/valitsussektori-maksed
- Consolidated accounting reports: https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine/riigi-raamatupidamise-koondaruanded

## Retrieval workflow (reproducible)
1. Open the target page and capture the retrieval timestamp.
2. Extract the `datatable-...` JSON script block when present.
3. Parse each row into: file/link title, publication date (`time datetime`), and download/view URL.
4. Normalize relative file links (prefix with `https://www.fin.ee`).
5. For dashboard-only sections (PowerBI/Tableau), store the exact embed URL and page name/tab information.
6. Return a structured result with source URL, row-level evidence URL, and date fields.

## Request/query contract
- No auth required for listed endpoints.
- Table records are in page HTML under `script type="application/json" id="datatable-..."`.
- Relative download links use `/sites/default/files/...` and must be expanded to absolute URLs.
- Dashboard endpoints are embed URLs (PowerBI/Tableau) without stable public query parameter docs; treat as UI sources.

## Output schema expectations
- `topic`
- `source_page_url`
- `record_title`
- `record_type` (`pdf`, `docx`, `xlsx`, `dashboard`, `external-link`)
- `publication_date`
- `download_or_view_url`
- `language` (if inferable from title/page)
- `notes`

## Limits and caveats
- fin.ee pages may mix historical and current records in one table; always preserve publication date.
- Embedded dashboards may expose visuals but not bulk-download APIs.
- Some sections include external platforms (PowerBI/Tableau) with separate availability/rate behavior.

## Verification hooks
- RES page contains datatable id `datatable-4c339daab36efadd390fbb6908c78b5635eb583225568a6d442c092e63518767` and files such as `State budget strategy 2026–2029.docx`.
- Consolidated reports page contains datatable id `datatable-97d8713fb37cf99b9a68b086553d26f8326da874bfde3a5778cb22808f71889d` and files such as `Riigi 2024. aasta majandusaasta koondaruanne`.
- Government payments page includes a PowerBI embed URL at `app.powerbi.com/view?...`.
