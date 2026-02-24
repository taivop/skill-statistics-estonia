---
name: aviation-safety-reports
description: Use aviation safety report pages for official safety reporting outputs, trend context, and structured extraction of published materials.
---

# Aviation Safety Reports

## Use when
- You need official aviation safety reporting outputs and trends.
- You need structured extraction from published safety materials.

## Avoid when
- You need aircraft registration records only.

## Access reality
- Public access type: direct PDF file downloads from official reports page.

## Inputs
- Safety topic, period, and report scope.

## Outputs
- Structured aviation safety report indicators and references.

## Primary endpoints
- Reports page: https://www.transpordiamet.ee/en/aviation-and-aviation-safety/aviation-safety/reports
- Example direct report files:
  - https://www.transpordiamet.ee/sites/default/files/documents/2021-07/safety_oversight_annual_report_2015.pdf
  - https://www.transpordiamet.ee/sites/default/files/documents/2021-07/safety_oversight_annual_report_2014.pdf
  - https://www.transpordiamet.ee/sites/default/files/documents/2021-07/annual_safety_report_2013_1.pdf

## Retrieval workflow
1. Open reports page and collect all linked report PDFs.
2. Download report files directly from `sites/default/files/documents/...` links.
3. Extract publication year, scope, indicators, and recommendations.
4. Return normalized metrics with per-metric source report citation.

## Request contract
- Files are served as public PDFs via direct GET.
- No API is required for report retrieval in this source skill.

## Output schema expectations
- Keep at least:
  - report title
  - report year / edition
  - indicator name and value (if numeric)
  - unit and period
  - recommendation or finding text (if requested)
  - source PDF URL

## Limits and caveats
- Coverage on this page may be historical and not continuous to current year.
- Metrics can be embedded in tables/images; extraction quality can vary by PDF layout.

## Verification hooks
- Verify each extracted metric is linked to one specific PDF URL and year.
- Verify downloaded file content type is `application/pdf`.

## Quality checks
- Keep report edition/date with every extracted metric.
- Distinguish incident counts from risk recommendations.
