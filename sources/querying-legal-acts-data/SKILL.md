---
name: querying-legal-acts-data
description: Query Riigi Teataja legal acts API and related endpoints for Estonian legislation search, retrieval, and legal text linking.
---

# Estonia Legal Acts Data (Riigi Teataja)

## Use when
- You need official legal acts, metadata, and structured legal search.
- You need regulation references for compliance-aware analysis.

## Avoid when
- You only need plain-language summaries without legal text retrieval.

## Inputs
- Query terms, legal act type, effective-date constraints.

## Outputs
- Legal search results and retrieved act links/text references.

## Primary endpoints
- Portal: https://www.riigiteataja.ee/
- Search API example: `https://www.riigiteataja.ee/api/oigusakt_otsing/1/otsi?leht=1`

## Workflow
1. Query legal acts API with relevant search filters.
2. Parse results and capture `url`/ID fields.
3. Fetch referenced act representations as needed.
4. Return legal dataset with citation-ready links.

## Human setup (when needed)
- Usually none.

## Quality checks
- Distinguish current vs historical validity periods.
- Preserve original legal identifiers and publication context.
