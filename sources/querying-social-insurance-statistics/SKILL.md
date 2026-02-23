---
name: querying-social-insurance-statistics
description: Query Social Insurance Board statistical publications for benefits, social protection services, and caseload trends.
---

# Social Insurance Statistics

## Use when
- You need Social Insurance Board caseload/benefit statistics.
- You need social-protection service trend context.

## Avoid when
- You only need unemployment service data.

## Inputs
- Benefit/service type, period, and region/group.

## Outputs
- Social-insurance statistics dataset with period metadata.

## Primary endpoints
- Statistics page: https://www.sotsiaalkindlustusamet.ee/asutus-uudised-ja-kontakt/praktiline-teave/statistika

## Workflow
1. Locate relevant publication/table on statistics page.
2. Extract indicators by period/group.
3. Normalize metric definitions and units.
4. Return analysis-ready dataset with caveats.

## Human setup (when needed)
- If data is offered in document downloads only, walk user through downloads and continue from supplied files.

## Quality checks
- Preserve source terminology for benefits/services.
- Separate counts, rates, and monetary values.
