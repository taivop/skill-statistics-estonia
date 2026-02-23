# Estonian Public Sources Skill

This repository is a unified routing skill for official/public Estonian governance sources.

## Project Goal

Cover, via reusable source skills, any information that can be found from public and official Estonian sources about:

- How government operates now.
- How government has operated historically.
- Context data needed to interpret government operations.

Sources include both APIs/datasets and official websites/registries.

## Structure

```text
.
├── SKILL.md
├── SOURCE_MAP.md
├── README.md
├── BACKLOG_MULTI_SKILL_EXPANSION.md
├── BACKLOG_OPERATIONAL_GOVERNANCE_DATA.md
├── BACKLOG_PRIORITY_MISSING_GOVERNMENT_COVERAGE.md
└── sources/
    ├── <source-skill-slug-1>/
    │   └── SKILL.md
    ├── <source-skill-slug-2>/
    │   └── SKILL.md
    └── ...
```

## Rules

- The root `SKILL.md` is the router skill.
- `SOURCE_MAP.md` is the fast lookup map for selecting the right source.
- Each source skill lives in its own folder under `sources/`.
- Each source folder has its own `SKILL.md`.
- Any source-specific scripts/examples stay inside that source folder.

## Source Index

- `sources/analyzing-estonia-election-results-data`
- `sources/analyzing-estonia-political-party-membership`
- `sources/analyzing-estonia-procurement-data`
- `sources/analyzing-estonia-public-finance-data`
- `sources/discovering-estonia-open-data`
- `sources/monitoring-estonia-public-consultations-feed`
- `sources/querying-bank-of-estonia-statistics`
- `sources/querying-estonia-agricultural-subsidies-pria`
- `sources/querying-estonia-competition-authority-decisions`
- `sources/querying-estonia-construction-register`
- `sources/querying-estonia-consumer-technical-regulator-decisions`
- `sources/querying-estonia-court-proceedings-data`
- `sources/querying-estonia-court-system-statistics`
- `sources/querying-estonia-cultural-heritage-register`
- `sources/querying-estonia-cyber-incidents-cert-ee`
- `sources/querying-estonia-data-protection-enforcement`
- `sources/querying-estonia-digital-government-studies`
- `sources/querying-estonia-economic-activities-register-mtr`
- `sources/querying-estonia-education-data`
- `sources/querying-estonia-energy-data`
- `sources/querying-estonia-environmental-data`
- `sources/querying-estonia-environmental-permit-decisions`
- `sources/querying-estonia-eu-funded-projects`
- `sources/querying-estonia-financial-supervision-decisions`
- `sources/querying-estonia-government-journal-records`
- `sources/querying-estonia-government-office-document-register`
- `sources/querying-estonia-health-statistics`
- `sources/querying-estonia-health-supervision-decisions`
- `sources/querying-estonia-land-register-kinnistusraamat`
- `sources/querying-estonia-legal-acts-data`
- `sources/querying-estonia-local-council-volis`
- `sources/querying-estonia-local-government-finance-benchmarks`
- `sources/querying-estonia-medicines-register`
- `sources/querying-estonia-ministry-document-registries`
- `sources/querying-estonia-national-archives-governance-records`
- `sources/querying-estonia-official-notices`
- `sources/querying-estonia-officials-interest-declarations`
- `sources/querying-estonia-ombudsman-opinions`
- `sources/querying-estonia-party-funding-data`
- `sources/querying-estonia-planning-decisions`
- `sources/querying-estonia-police-operational-statistics`
- `sources/querying-estonia-prosecution-statistics`
- `sources/querying-estonia-public-sector-it-systems-riha`
- `sources/querying-estonia-rescue-incident-data`
- `sources/querying-estonia-social-insurance-statistics`
- `sources/querying-estonia-state-aid-register`
- `sources/querying-estonia-state-assets-register`
- `sources/querying-estonia-state-audit-reports`
- `sources/querying-estonia-state-ownership-data`
- `sources/querying-estonia-state-services-catalog`
- `sources/querying-estonia-supreme-court-judgments`
- `sources/querying-estonia-tax-customs-data`
- `sources/querying-estonia-tax-public-inquiries`
- `sources/querying-estonia-transport-traffic-data`
- `sources/querying-estonia-unemployment-statistics`
- `sources/querying-estonia-weather-data`
- `sources/querying-estonia-x-road-usage-statistics`
- `sources/querying-riigikogu-open-data`
- `sources/querying-riigikogu-stenograms`
- `sources/querying-riigiteataja-draft-acts`
- `sources/querying-statistics-estonia-api`
- `sources/querying-tallinn-council-documents`
- `sources/querying-tallinn-legal-acts-register`
- `sources/querying-tallinn-open-data`
- `sources/querying-tartu-document-register`
- `sources/querying-tartu-open-data`
- `sources/querying-tartu-webaktid`
- `sources/tracking-estonia-government-session-agendas`
- `sources/tracking-estonia-legislation-workflow-eis`
- `sources/tracking-estonia-lobby-meetings`
- `sources/tracking-estonia-public-consultations-osale`
- `sources/tracking-riigikogu-agendas`
- `sources/tracking-riigikogu-draft-laws`
- `sources/using-estonia-business-register-open-data`
- `sources/using-estonia-geospatial-open-data`
- `sources/using-estonia-health-welfare-open-data`

## Backlog

- Planning and limitations are tracked in `BACKLOG_MULTI_SKILL_EXPANSION.md`.
- Operational-governance sources backlog is tracked in `BACKLOG_OPERATIONAL_GOVERNANCE_DATA.md`.
- Priority missing-coverage backlog is tracked in `BACKLOG_PRIORITY_MISSING_GOVERNMENT_COVERAGE.md`.
