---
name: environmental-permit-decisions
description: Query KOTKAS environmental decision system for permits, approvals, and environmental administrative decisions.
---

# Environmental Permit Decisions (KOTKAS)

## Use when
- You need permit/approval decision records in environmental domain.
- You need operational permit lifecycle tracking.

## Avoid when
- You need only environmental indicators without permit process context.

## Inputs
- Permit type, area/entity, date range, authority.

## Outputs
- Permit decision records with status chronology.

## Primary endpoint
- KOTKAS: https://kotkas.envir.ee/

## Workflow
1. Search for permit cases by type and geography.
2. Extract decision dates, statuses, and case identifiers.
3. Link associated documents where available.
4. Return permit lifecycle dataset.

## Human setup (when needed)
- If detailed records require UI navigation/login context, guide user through exact search and record-opening steps, then continue from shared URLs/exports.

## Quality checks
- Preserve case/permit identifiers.
- Separate application, review, and final-decision stages.
