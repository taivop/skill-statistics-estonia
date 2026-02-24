---
name: prison-annual-reviews
description: Retrieve prison system annual reviews and continuously updated operational dashboard metrics from Vanglateenistus public pages.
---

# Prison Annual Reviews and Operational Stats

## Use when
- You need year-based prison service reports.
- You need current operational indicator dashboard context between annual reports.

## Avoid when
- You need person-level inmate records.

## Inputs
- Year range.
- Scope (`annual-reviews`, `current-dashboard`).

## Outputs
- Structured report list and/or dashboard-derived indicator extract.

## Access reality statement
- Access type: `download files` + `UI copy-only`.
- Verified on 2026-02-24.
- Legacy `vangla.ee/et/statistika` redirects; current data is on `vanglateenistus.ee` pages.

## Primary endpoints
- Annual reviews page: https://vanglateenistus.ee/meist/uudised-ja-arvud/aasta-ulevaated
- Current numeric overview page: https://vanglateenistus.ee/meist/uudised-ja-arvud/paevakohane-arvuline-ulevaade
- Embedded operational dashboard (PowerBI): https://app.fabric.microsoft.com/view?r=eyJrIjoiNTg0YmZmMjAtN2FhZC00MDI3LWE2NTUtMTZiM2IwYTVlNzUzIiwidCI6ImY2MzQyZDcwLWRhYzEtNDYxNC04ZTFhLTQ3YjkxYzE2YjhkZiIsImMiOjl9

## Retrieval workflow (reproducible)
1. Open annual review page and collect each report title/date/download URL.
2. Open numeric overview page and locate embedded dashboard iframe URL.
3. Capture visible metric definitions and latest update text from the page.
4. Extract dashboard values through UI copy/export where available.
5. Return datasets labeled by source type (`annual_report`, `daily_dashboard`).

## Request/query contract
- No public documented REST contract is exposed for prison stats.
- Operational dashboard is embedded via iframe; extraction is UI-based unless direct export is exposed by the dashboard.
- Track redirects from legacy domains when resolving user-provided old links.

## Output schema expectations
- `source_type`
- `source_page_url`
- `record_title` or `metric_name`
- `record_date` or `last_updated`
- `value`
- `unit`
- `download_or_view_url`
- `notes`

## Limits and caveats
- Dashboard schema may change without versioned API documentation.
- Historical comparability may differ between annual-report tables and current dashboard calculations.
- Some values are available only visually in the embedded BI view.

## Verification hooks
- `https://www.vangla.ee/et/statistika` returns redirect to `https://vanglateenistus.ee/`.
- Numeric overview page includes iframe to `app.fabric.microsoft.com/view?...`.
- Page includes `Viimati uuendatud` text (observed date field on the page).
