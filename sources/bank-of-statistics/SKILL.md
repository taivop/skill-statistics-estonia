---
name: bank-of-statistics
description: Retrieve macro-financial and monetary statistics from the Bank of Estonia statistics portal for banking, external sector, and monetary analysis.
---

# Bank of Estonia Statistics

## Use when
- You need central-bank indicators (monetary, financial, external sector).
- You need statistics complementary to Statistics Estonia.

## Avoid when
- The indicator is already fully available from Statistics Estonia and no financial split is needed.

## Inputs
- Indicator topic and period.
- Preferred granularity and format.

## Outputs
- Downloaded indicator series and source citation.

## Primary endpoints
- Portal: https://statistika.eestipank.ee/

## Workflow
1. Find the exact indicator table in the portal.
2. Set period/frequency and dimensions.
3. Export to CSV/Excel/SDMX if available.
4. Normalize timestamps and units for downstream analysis.

## Human setup (when needed)
- If export controls are only in browser UI, guide the user click-by-click to export the file, then continue from the downloaded file.

## Quality checks
- Confirm frequency (monthly/quarterly/annual).
- Confirm whether values are stock or flow.
