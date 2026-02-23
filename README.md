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

- `sources/election-results-data`
- `sources/political-party-membership`
- `sources/procurement-data`
- `sources/public-finance-data`
- `sources/open-data`
- `sources/public-consultations-feed`
- `sources/agricultural-subsidies-pria`
- `sources/bank-of-statistics`
- `sources/competition-authority-decisions`
- `sources/construction-register`
- `sources/consumer-technical-regulator-decisions`
- `sources/court-proceedings-data`
- `sources/court-system-statistics`
- `sources/cultural-heritage-register`
- `sources/cyber-incidents-cert-ee`
- `sources/data-protection-enforcement`
- `sources/digital-government-studies`
- `sources/economic-activities-register-mtr`
- `sources/education-data`
- `sources/energy-data`
- `sources/environmental-data`
- `sources/environmental-permit-decisions`
- `sources/eu-funded-projects`
- `sources/financial-supervision-decisions`
- `sources/government-journal-records`
- `sources/government-office-document-register`
- `sources/health-statistics`
- `sources/health-supervision-decisions`
- `sources/land-register-kinnistusraamat`
- `sources/legal-acts-data`
- `sources/local-council-volis`
- `sources/local-government-finance-benchmarks`
- `sources/medicines-register`
- `sources/ministry-document-registries`
- `sources/national-archives-governance-records`
- `sources/official-notices`
- `sources/officials-interest-declarations`
- `sources/ombudsman-opinions`
- `sources/party-funding-data`
- `sources/planning-decisions`
- `sources/police-operational-statistics`
- `sources/prosecution-statistics`
- `sources/public-sector-it-systems-riha`
- `sources/rescue-incident-data`
- `sources/riigikogu-open-data`
- `sources/riigikogu-stenograms`
- `sources/riigiteataja-draft-acts`
- `sources/social-insurance-statistics`
- `sources/state-aid-register`
- `sources/state-assets-register`
- `sources/state-audit-reports`
- `sources/state-ownership-data`
- `sources/state-services-catalog`
- `sources/statistics-api`
- `sources/supreme-court-judgments`
- `sources/tallinn-council-documents`
- `sources/tallinn-legal-acts-register`
- `sources/tallinn-open-data`
- `sources/tartu-document-register`
- `sources/tartu-open-data`
- `sources/tartu-webaktid`
- `sources/tax-customs-data`
- `sources/tax-public-inquiries`
- `sources/transport-traffic-data`
- `sources/unemployment-statistics`
- `sources/weather-data`
- `sources/x-road-usage-statistics`
- `sources/government-session-agendas`
- `sources/legislation-workflow-eis`
- `sources/lobby-meetings`
- `sources/public-consultations-osale`
- `sources/riigikogu-agendas`
- `sources/riigikogu-draft-laws`
- `sources/business-register-open-data`
- `sources/geospatial-open-data`
- `sources/health-welfare-open-data`
