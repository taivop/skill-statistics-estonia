---
name: e-residency-dashboard
description: Extract operational e-Residency metrics from the official dashboard page’s embedded data payload and chart sections.
---

# e-Residency Operational Dashboard

## Use when
- You need official programme KPI series (applications, e-residents, companies by country/time).
- You need country-level and top-figure operational metrics from the dashboard.

## Avoid when
- You need legal/company registry truth data (use Business Register for legal-entity records).

## Inputs
- Metric family (`top-figures`, `country-series`, `applications`, `companies`).
- Time period/country focus.

## Outputs
- Structured metric extracts with dashboard keys and source timestamp.

## Access reality statement
- Access type: `UI copy-only` (embedded JSON/data in page source).
- Verified on 2026-02-24.
- Dashboard page contains large serialized data payload in HTML/Next.js stream.

## Primary endpoints
- Dashboard page: https://www.e-resident.gov.ee/dashboard/

## Retrieval workflow (reproducible)
1. Fetch dashboard page HTML and locate serialized data segments in Next.js stream.
2. Extract known metric blocks by keys (for example: `top-figures`, `top-countries-by-number-of-applications-in-the-last-12-months`, `top-countries-by-number-of-e-residents`).
3. Parse arrays/objects into tabular metric records.
4. Preserve metric key names and convert to normalized labels.
5. Return records with source page URL and retrieval timestamp.

## Request/query contract
- No standalone documented public API endpoint confirmed for this page.
- Metrics are embedded in page payload; extraction is source-parsing based.
- Use robust parsing that tolerates large inline script content.

## Output schema expectations
- `source_page_url`
- `metric_group_key`
- `metric_name`
- `dimension` (e.g., citizenship/country)
- `dimension_code` (if present)
- `value`
- `period_label` (if present)
- `retrieved_at`

## Limits and caveats
- Embedded payload structure can change with frontend deployments.
- Metric labels may mix localized and English fields.
- Some figures shown visually may not map 1:1 to embedded key names.

## Verification hooks
- Dashboard source contains keys: `top-figures`, `top-countries-by-number-of-applications-in-the-last-12-months`, and `top-countries-by-number-of-e-residents`.
- Page contains visible headline KPIs (total e-residents, companies established by e-residents, etc.).
