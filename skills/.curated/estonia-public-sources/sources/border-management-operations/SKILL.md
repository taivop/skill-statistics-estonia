---
name: border-management-operations
description: Use Ministry of Interior border management pages for official border operations context and structured extraction of governance-relevant materials.
---

# Border Management Operations

## Use when
- You need official border management operations context.
- You need structured extraction of border policy/operations materials.

## Avoid when
- You need person-level border crossing records.

## Access reality
- Public access type: policy/context page with links to operational border information systems.
- Core ministry page is narrative; practical operational data is usually in linked external systems.

## Inputs
- Topic scope, period, and operational focus.

## Outputs
- Structured border-operations references and extracted fields.

## Primary endpoints
- Ministry border management page: https://www.siseministeerium.ee/en/activities/guaranteed-internal-security/border-management
- Border queue system (GoSwift): https://www.eestipiir.ee/yphis/index.action?request_locale=et
- Police border crossing information: https://www.politsei.ee/et/piiriueletusinfo

## Retrieval workflow
1. Open ministry border management page and extract official policy/operational references.
2. Follow linked official operational systems for public operational status information.
3. Extract only publicly available aggregate/operational information.
4. Return structured output with source provenance and publication/update dates.

## Request contract
- Ministry page: HTML document extraction.
- Linked operational systems are separate services with their own UI contracts.
- No person-level or restricted crossing records should be requested or inferred.

## Output schema expectations
- Keep at least:
  - operation/policy topic
  - responsible authority
  - operational indicator or status text (if published)
  - geography/scope
  - source URL and publication/update timestamp

## Limits and caveats
- Ministry source itself is mostly policy context.
- Linked systems may focus on live operational info rather than historical bulk export.
- Avoid personal-data extraction attempts.

## Verification hooks
- Verify each extracted operational claim has direct source URL and date context.
- Verify policy statements and operational metrics are labeled separately.

## Quality checks
- Distinguish policy objectives from operational metrics.
- Keep publication dates and source provenance.
