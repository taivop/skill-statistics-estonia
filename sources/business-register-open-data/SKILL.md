---
name: business-register-open-data
description: Use Estonian Business Register open data downloads for legal-entity analysis, registry snapshots, and organization-level trends including political party statistics.
---

# Estonia Business Register Open Data

## Use when
- You need legal entity baseline datasets (registrations, statuses, attributes).
- You need reproducible business population extracts.
- You need organization-level context that also supports party membership trend analysis.

## Avoid when
- You only need high-level macro indicators.

## Inputs
- Entity scope, date range, and required fields.

## Outputs
- Registry extract with schema notes and date stamp.

## Primary endpoints
- Open data page: https://avaandmed.ariregister.rik.ee/en/downloading-open-data
- Related documentation: https://abiinfo.rik.ee/en/e-business-register-queries/open-data-e-business-register

## Workflow
1. Select correct extract type and snapshot period.
2. Download file(s) and inspect schema/encoding.
3. Normalize identifiers and status fields.
4. Return cleaned table with source timestamp.

## Human setup (when needed)
- If download links are session-protected or UI-generated, guide user through the exact download flow and proceed with local files they provide.

## Quality checks
- Preserve original business identifiers.
- Keep snapshot date and provenance in output metadata.
