---
name: health-insurance-fund-reports
description: Use Estonian Health Insurance Fund annual reports for financing, service volumes, and system performance indicators.
---

# Health Insurance Fund Reports

## Use when
- You need annual financial and service indicators from Tervisekassa.
- You need official health insurance system performance context.

## Avoid when
- You need disease-incidence surveillance data.

## Inputs
- Reporting year and metric scope.

## Outputs
- Structured annual report indicators and metadata.

## Primary endpoints
- Annual reports: https://www.tervisekassa.ee/en/organisation/annual-reports

## Workflow
1. Retrieve selected annual reports.
2. Extract financing, service, and utilization metrics.
3. Normalize indicators across years.
4. Return analysis-ready dataset with definitions.

## Human setup (when needed)
- If reports require manual download, guide the user through download and continue from files.

## Quality checks
- Distinguish budgeted vs realized values.
- Keep indicator units and accounting basis.
