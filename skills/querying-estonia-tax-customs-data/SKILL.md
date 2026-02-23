---
name: querying-estonia-tax-customs-data
description: Retrieve and use Estonian Tax and Customs Board public statistics and open-data files for tax and trade related analyses.
---

# Estonia Tax and Customs Data

## Use when
- You need official tax/customs statistics from EMTA.
- You need downloadable open files for reproducible analysis.

## Avoid when
- You need confidential taxpayer-level data.

## Inputs
- Indicator/topic and period.

## Outputs
- Downloaded file(s), cleaned dataset, and field mapping.

## Primary endpoints
- Statistics page: https://www.emta.ee/en/business-client/statistics-and-open-data
- Example direct files:
  - `https://ncfailid.emta.ee/s/e4DneiWeKFfje6d/download/tasutud_maksud_kaesolev_aasta_eng.csv`
  - `https://ncfailid.emta.ee/s/K8snLYNdZnqJCRn/download/tasutud_maksud_varasemad_aastad_eng.csv`

## Workflow
1. Start from EMTA statistics page and pick current/prior period file.
2. Download CSV/XLSX and verify delimiter/encoding.
3. Normalize column names and date formats.
4. Return cleaned table with explicit source URL.

## Human setup (when needed)
- If a file is gated or moved, ask the user to open the EMTA page and share the latest direct link; then continue automatically.

## Quality checks
- Check language-specific column names.
- Verify whether figures are cumulative or period-specific.
