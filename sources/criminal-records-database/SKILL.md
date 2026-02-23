---
name: criminal-records-database
description: Use RIK criminal records database public consultation pages for record-availability rules, lookup procedures, and related official outputs.
---

# Criminal Records Database

## Use when
- You need official criminal-record consultation procedures and public-access context.
- You need structured outputs from publicly available consultation views.

## Avoid when
- You need restricted personal data not publicly exposed.

## Inputs
- Query scope, legal basis, and allowed search parameters.

## Outputs
- Structured consultation results and access-limit notes.

## Primary endpoints
- Data consultation: https://www.rik.ee/en/criminal-records-database/data-consultation
- Issuing notices in database: https://www.rik.ee/en/criminal-records-database/issuing-notices-database
- Legal persons route: https://www.rik.ee/en/criminal-records-database/legal-persons

## Workflow
1. Determine what lookup/output is publicly allowed.
2. Run available consultation or issuing-notices/legal-persons flow as applicable.
3. Extract structured fields and identifiers.
4. Return results with access-scope caveats.

## Human setup (when needed)
- If access requires authentication or role rights, guide the user through that process and continue from the provided output.

## Quality checks
- Clearly mark public vs restricted fields.
- Keep legal/access constraints attached to outputs.
