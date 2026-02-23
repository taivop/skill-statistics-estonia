---
name: querying-estonia-agricultural-subsidies-pria
description: Query PRIA support-recipient and open-data views for agricultural subsidies, recipient-level allocations, and support-program trends.
---

# Agricultural Subsidies (PRIA)

## Use when
- You need support-recipient data for agricultural/rural subsidies.
- You need program-level subsidy trend analysis.

## Avoid when
- You only need non-agricultural state aid.

## Inputs
- Support measure, year/period, region, and recipient scope.

## Outputs
- Recipient-program subsidy extract with period metadata.

## Primary endpoints
- Support recipients: https://www.pria.ee/toetused/toetusesaajad
- Open data: https://www.pria.ee/avaandmed
- Public registry data: https://www.pria.ee/registrid/avalikud-andmed

## Workflow
1. Locate relevant support-recipient/open-data view.
2. Filter by period, measure, and recipient scope.
3. Extract recipient, amount, and program identifiers.
4. Return normalized dataset with measure dictionary notes.

## Human setup (when needed)
- If PRIA pages require manual interaction to export, instruct the user through each click and continue from downloaded files.

## Quality checks
- Preserve source measure names/codes.
- Keep gross/net amount semantics exactly as published.
