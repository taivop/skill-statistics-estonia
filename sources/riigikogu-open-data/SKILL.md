---
name: riigikogu-open-data
description: Query Riigikogu open data API for parliamentary votings, members, and legislative activity.
---

# Riigikogu Open Data API

## Use when
- You need parliamentary voting and member-level open data.
- You need machine-readable legislative process signals.

## Avoid when
- You need election outcomes (use election archive skill).

## Inputs
- Date range, language, and endpoint family.

## Outputs
- API JSON extract and cleaned analysis tables.

## Primary endpoints
- API root: https://api.riigikogu.ee/
- Swagger: https://api.riigikogu.ee/swagger-ui.html
- Example votings endpoint: `https://api.riigikogu.ee/api/votings?startDate=YYYY-MM-DD&endDate=YYYY-MM-DD&lang=en`

## Workflow
1. Inspect endpoint contract in Swagger.
2. Query bounded date ranges.
3. Normalize IDs, timestamps, and member/vote fields.
4. Return dataset with endpoint and query parameters used.

## Human setup (when needed)
- Usually none.

## Quality checks
- Keep stable IDs for members and votings.
- Store exact query window to ensure reproducibility.
