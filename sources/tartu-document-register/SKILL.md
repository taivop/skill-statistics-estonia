---
name: tartu-document-register
description: Query Tartu city document register (DHS) for municipal document workflow, records, and operational traceability.
---

# Tartu Document Register (DHS)

## Use when
- You need Tartu municipal document-level operational records.
- You need incoming/outgoing document and workflow references.

## Avoid when
- You only need legal acts (use Tartu WebAktid skill).

## Inputs
- Document keywords, departments, date range.

## Outputs
- Document register extract and metadata mapping.

## Primary endpoint
- DHS register: https://info.raad.tartu.ee/dhs.nsf

## Workflow
1. Search register by keyword/date/department.
2. Capture document references, dates, and status fields.
3. Normalize metadata for analysis.
4. Return structured register table.

## Human setup (when needed)
- If register navigation is manual-only, walk user through exact search form entries and ask for result links.

## Quality checks
- Preserve document reference numbers exactly.
- Keep published status as-is; do not infer confidentiality flags.
