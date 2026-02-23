---
name: tallinn-open-data
description: Query Tallinn city open data API and documentation for municipal datasets and city-level analysis workflows.
---

# Tallinn Open Data

## Use when
- You need Tallinn-specific municipal datasets.
- You need direct city API access for repeatable pulls.

## Avoid when
- You need national cross-agency discovery first.

## Inputs
- Table name, columns, filters, pagination.

## Outputs
- API response dataset and query log.

## Primary endpoints
- API root: https://avaandmed.tallinn.ee/
- Swagger UI: https://avaandmed.tallinn.ee/docs
- OpenAPI schema: https://avaandmed.tallinn.ee/openapi.json
- Data query endpoint pattern: `https://avaandmed.tallinn.ee/data/?table=...&columns=...&filters=...&page=...&per_page=...`

## Workflow
1. Inspect table names and parameters from docs.
2. Query `/data/` with bounded filters/pagination.
3. Validate field types and missing values.
4. Return cleaned municipal dataset.

## Human setup (when needed)
- If table name is unknown, ask the user for the dataset reference from andmed.eesti.ee and then construct the query together.

## Quality checks
- Respect API limits and timeout constraints.
- Keep query params in output metadata for reproducibility.
