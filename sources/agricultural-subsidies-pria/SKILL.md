---
name: agricultural-subsidies-pria
description: Query PRIA support-recipient and open-data views for agricultural subsidies, recipient-level allocations, and support-program trends.
---

# Agricultural Subsidies (PRIA)

## Use when
- You need support-recipient data for agricultural/rural subsidies.
- You need program-level subsidy trend analysis.

## Avoid when
- You only need non-agricultural state aid.

## Access reality
- Public access type: UI filters + direct CSV/XLSX/PDF downloads.
- Main machine-readable route: `Toetuste saajad` CSV export endpoint generated from filter form.
- Language reality: key pages and column names are mostly Estonian.

## Inputs
- Year/period, support measure, recipient scope, and region filter.

## Outputs
- Recipient-program subsidy extract with period metadata.

## Primary endpoints
- Support recipients UI: https://www.pria.ee/toetused/toetusesaajad
- Open data hub page: https://www.pria.ee/avaandmed
- Public registry data page: https://www.pria.ee/registrid/avalikud-andmed

## Retrieval workflow
1. Open `https://www.pria.ee/toetused/toetusesaajad`.
2. Set filters through query params or form fields (`year`, `county`, `township`, `name`, `type`, measure selections).
3. Find the export link rendered on the page (`/download/file/PRIA_export_...csv?...form_id=filter_receivers_form...`).
4. Download CSV and preserve raw header names.
5. For registry-side statistics, open `https://www.pria.ee/registrid/avalikud-andmed` and download linked XLSX/PDF files.

## Request contract
- Support recipients export is a generated GET URL under `/download/file/PRIA_export_*.csv`.
- Export URL contains transient form tokens (`form_build_id`) and must be taken from the rendered page state.
- Common filters visible in form:
  - `year`
  - `county`
  - `township`
  - `name`
  - `type`
  - multiple measure keys like `mp[<code>]`

## Output schema expectations
- For support recipient CSV, preserve at least:
  - recipient name (`Toetusesaaja nimi`)
  - county and municipality (`Maakond`, `Omavalitsus`)
  - measure/program labels (`Meede/sekkumisviis/sektor` etc.)
  - amount columns (as published)
  - period/year column
- Keep source file metadata: URL, retrieval timestamp, and filter values used.

## Limits and caveats
- Column labels are Estonian and may include long measure descriptions.
- CSV often begins with `sep=;` and semicolon delimiters.
- Form tokenized export links are page-state dependent.
- `avaandmed` page is mainly a directory and may route to multiple external/open-data locations.

## Verification hooks
- Verify CSV content type is `application/csv` or text CSV.
- Verify first line is separator hint (`sep=;`) and second line contains header row.
- Verify filtered export (for example `year=2024`) includes matching year values in data rows.

## Quality checks
- Preserve source measure names/codes.
- Keep gross/net amount semantics exactly as published.
