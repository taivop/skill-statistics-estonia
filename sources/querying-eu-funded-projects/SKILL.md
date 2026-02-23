---
name: querying-eu-funded-projects
description: Query EU-funded project information from RTK and Structural Funds sources for programme-level and beneficiary-level project tracking in Estonia.
---

# EU-Funded Projects

## Use when
- You need supported-project data for EU funding programmes in Estonia.
- You need beneficiary/programme/project-level tracking context.

## Avoid when
- You only need domestic non-EU subsidy flows.

## Inputs
- Programme, period, beneficiary/region, and project theme.

## Outputs
- Project-level dataset with programme and funding fields.

## Primary endpoints
- RTK implementation info: https://www.rtk.ee/en/funds-and-programmes/implementation
- Structural funds supported projects: https://www.struktuurifondid.ee/et/toetatud-projektid

## Workflow
1. Identify programme and funding period.
2. Retrieve supported-project listing/export.
3. Normalize beneficiary, project, and funding fields.
4. Return project table plus programme-level summaries.

## Human setup (when needed)
- If Structural Funds site fails automated SSL/network checks in the current environment, guide the user to download/export manually and continue from provided data.

## Quality checks
- Track funding-period and programme identifiers.
- Keep approved vs paid amounts distinct.

## Limitations
- Some environments may fail TLS validation for `struktuurifondid.ee`; use manual export fallback.
