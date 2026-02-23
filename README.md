# Estonian Public Sources Skill

Use this repository to get evidence-based answers from official Estonian public sources about how government works, what decisions were made, who was involved, and what changed over time.

## What You Get

- Fast routing to the right official source for policy, law, spending, operations, registries, and oversight questions.
- Reusable source-specific workflows that produce structured, citation-ready outputs.
- Human-guided fallback steps when a source requires manual export, login, or anti-bot interaction.

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
- `sources/querying-agricultural-subsidies-pria`
- `sources/querying-bank-of-estonia-statistics`
- `sources/querying-competition-authority-decisions`
- `sources/querying-construction-register`
- `sources/querying-consumer-technical-regulator-decisions`
- `sources/querying-court-proceedings-data`
- `sources/querying-court-system-statistics`
- `sources/querying-cultural-heritage-register`
- `sources/querying-cyber-incidents-cert-ee`
- `sources/querying-data-protection-enforcement`
- `sources/querying-digital-government-studies`
- `sources/querying-economic-activities-register-mtr`
- `sources/querying-education-data`
- `sources/querying-energy-data`
- `sources/querying-environmental-data`
- `sources/querying-environmental-permit-decisions`
- `sources/querying-eu-funded-projects`
- `sources/querying-financial-supervision-decisions`
- `sources/querying-government-journal-records`
- `sources/querying-government-office-document-register`
- `sources/querying-health-statistics`
- `sources/querying-health-supervision-decisions`
- `sources/querying-land-register-kinnistusraamat`
- `sources/querying-legal-acts-data`
- `sources/querying-local-council-volis`
- `sources/querying-local-government-finance-benchmarks`
- `sources/querying-medicines-register`
- `sources/querying-ministry-document-registries`
- `sources/querying-national-archives-governance-records`
- `sources/querying-official-notices`
- `sources/querying-officials-interest-declarations`
- `sources/querying-ombudsman-opinions`
- `sources/querying-party-funding-data`
- `sources/querying-planning-decisions`
- `sources/querying-police-operational-statistics`
- `sources/querying-prosecution-statistics`
- `sources/querying-public-sector-it-systems-riha`
- `sources/querying-rescue-incident-data`
- `sources/querying-riigikogu-open-data`
- `sources/querying-riigikogu-stenograms`
- `sources/querying-riigiteataja-draft-acts`
- `sources/querying-social-insurance-statistics`
- `sources/querying-state-aid-register`
- `sources/querying-state-assets-register`
- `sources/querying-state-audit-reports`
- `sources/querying-state-ownership-data`
- `sources/querying-state-services-catalog`
- `sources/querying-statistics-estonia-api`
- `sources/querying-supreme-court-judgments`
- `sources/querying-tallinn-council-documents`
- `sources/querying-tallinn-legal-acts-register`
- `sources/querying-tallinn-open-data`
- `sources/querying-tartu-document-register`
- `sources/querying-tartu-open-data`
- `sources/querying-tartu-webaktid`
- `sources/querying-tax-customs-data`
- `sources/querying-tax-public-inquiries`
- `sources/querying-transport-traffic-data`
- `sources/querying-unemployment-statistics`
- `sources/querying-weather-data`
- `sources/querying-x-road-usage-statistics`
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
