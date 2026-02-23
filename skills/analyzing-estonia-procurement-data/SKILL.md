---
name: analyzing-estonia-procurement-data
description: Analyze Estonian public procurement register data for tenders, contracts, and buyer-supplier market patterns.
---

# Estonia Procurement Data

## Use when
- You need public tender/contract activity by buyer, supplier, or sector.
- You need procurement trend or concentration analysis.

## Avoid when
- You need broader budget-level reporting without tender detail.

## Inputs
- Time range, authority/buyer scope, and procedure type.

## Outputs
- Extracted procurement records and aggregation-ready fields.

## Primary endpoint
- Register: https://www.riigihanked.riik.ee/rhr-web/

## Workflow
1. Locate relevant procurement report/search view.
2. Filter by period and category.
3. Export available results and normalize entity names/IDs.
4. Build summary tables (count, value, concentration, repeat winners).

## Human setup (when needed)
- If export requires login or anti-bot interaction, walk the user through login/export steps and continue from provided files.

## Quality checks
- Separate notices, awards, and amendments.
- Track whether values are estimated or awarded.
