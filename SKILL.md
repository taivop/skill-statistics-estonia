---
name: estonia-government-public-sources
description: Route Estonia public/official governance questions to the right source skill under sources/ using a high-level index and source map.
---

# Estonia Government Public Sources

## Use when
- You need to find which official Estonian source to use for a governance, legal, policy, operations, finance, registry, or municipal question.
- You need to route quickly to the correct source-specific skill in `sources/`.

## Avoid when
- You already know the exact source skill and can open it directly.

## Routing workflow
1. Classify the user request (parliament, government operations, justice, business/asset registry, finance, municipal, etc.).
2. Use the high-level index below to narrow to a source family.
3. Open `SOURCE_MAP.md` for precise source-to-question routing.
4. Open the specific `sources/<source-name>/SKILL.md` and execute that workflow.

## High-Level Index
- Core national statistics and macro context:
  `sources/querying-statistics-estonia-api`, `sources/querying-bank-of-estonia-statistics`, `sources/querying-estonia-public-finance-data`, `sources/querying-estonia-tax-customs-data`
- Parliament, lawmaking, and legal texts:
  `sources/querying-riigikogu-open-data`, `sources/tracking-riigikogu-draft-laws`, `sources/tracking-estonia-legislation-workflow-eis`, `sources/querying-estonia-legal-acts-data`
- Government operations and transparency records:
  `sources/querying-estonia-ministry-document-registries`, `sources/querying-estonia-government-office-document-register`, `sources/tracking-estonia-lobby-meetings`, `sources/querying-estonia-official-notices`
- Oversight, supervision, and enforcement:
  `sources/querying-estonia-state-audit-reports`, `sources/querying-estonia-ombudsman-opinions`, `sources/querying-estonia-financial-supervision-decisions`, `sources/querying-estonia-data-protection-enforcement`
- Registries, ownership, and organization context:
  `sources/using-estonia-business-register-open-data`, `sources/querying-estonia-land-register-kinnistusraamat`, `sources/querying-estonia-economic-activities-register-mtr`, `sources/querying-estonia-state-ownership-data`
- Public spending, subsidies, and projects:
  `sources/analyzing-estonia-procurement-data`, `sources/querying-estonia-party-funding-data`, `sources/querying-estonia-agricultural-subsidies-pria`, `sources/querying-estonia-eu-funded-projects`
- Justice and internal security operations:
  `sources/querying-estonia-court-proceedings-data`, `sources/querying-estonia-court-system-statistics`, `sources/querying-estonia-prosecution-statistics`, `sources/querying-estonia-police-operational-statistics`
- Health, welfare, and labor operations:
  `sources/querying-estonia-health-statistics`, `sources/querying-estonia-health-supervision-decisions`, `sources/querying-estonia-social-insurance-statistics`, `sources/querying-estonia-unemployment-statistics`
- Spatial, environment, and infrastructure:
  `sources/using-estonia-geospatial-open-data`, `sources/querying-estonia-planning-decisions`, `sources/querying-estonia-construction-register`, `sources/querying-estonia-transport-traffic-data`
- Municipal and local-government sources:
  `sources/querying-estonia-local-council-volis`, `sources/querying-tallinn-open-data`, `sources/querying-tallinn-council-documents`, `sources/querying-tartu-document-register`
- Digital-state and service delivery context:
  `sources/querying-estonia-public-sector-it-systems-riha`, `sources/querying-estonia-state-services-catalog`, `sources/querying-estonia-x-road-usage-statistics`, `sources/querying-estonia-digital-government-studies`

## Detailed map
- Use `SOURCE_MAP.md` for fast source selection by user intent and keyword.
