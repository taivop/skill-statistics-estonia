---
name: estonia-government-public-sources
description: Get evidence-based answers about Estonian government operations, decisions, spending, registries, and oversight by quickly selecting the right official source skill.
---

# Estonia Government Public Sources

## Use when
- You need fast, evidence-backed answers about how Estonian government operates or has operated.
- You need to identify the right official source for governance, legal, policy, spending, registry, oversight, or municipal questions.

## Avoid when
- You already know the exact source skill and can open it directly.

## What the user gets
- A fast path to the best official source for the question.
- Source-specific workflows that produce structured, traceable outputs.
- Manual fallback guidance when a source needs user interaction (login/export/captcha), then continued automated analysis from user-provided files.

## Routing workflow
1. Classify the user request (parliament, government operations, justice, business/asset registry, finance, municipal, etc.).
2. Use the high-level index below to narrow to a source family.
3. Open `SOURCE_MAP.md` for precise source-to-question routing.
4. Open the specific `sources/<source-name>/SKILL.md` and execute that workflow.

## High-Level Index
- Core national statistics and macro context:
  `sources/querying-statistics-estonia-api`, `sources/querying-bank-of-estonia-statistics`, `sources/analyzing-estonia-public-finance-data`, `sources/querying-tax-customs-data`
- Parliament, lawmaking, and legal texts:
  `sources/querying-riigikogu-open-data`, `sources/tracking-riigikogu-draft-laws`, `sources/tracking-estonia-legislation-workflow-eis`, `sources/querying-legal-acts-data`
- Government operations and transparency records:
  `sources/querying-ministry-document-registries`, `sources/querying-government-office-document-register`, `sources/tracking-estonia-lobby-meetings`, `sources/querying-official-notices`
- Oversight, supervision, and enforcement:
  `sources/querying-state-audit-reports`, `sources/querying-ombudsman-opinions`, `sources/querying-financial-supervision-decisions`, `sources/querying-data-protection-enforcement`
- Registries, ownership, and organization context:
  `sources/using-estonia-business-register-open-data`, `sources/querying-land-register-kinnistusraamat`, `sources/querying-economic-activities-register-mtr`, `sources/querying-state-ownership-data`
- Public spending, subsidies, and projects:
  `sources/analyzing-estonia-procurement-data`, `sources/querying-party-funding-data`, `sources/querying-agricultural-subsidies-pria`, `sources/querying-eu-funded-projects`
- Justice and internal security operations:
  `sources/querying-court-proceedings-data`, `sources/querying-court-system-statistics`, `sources/querying-prosecution-statistics`, `sources/querying-police-operational-statistics`
- Health, welfare, and labor operations:
  `sources/querying-health-statistics`, `sources/querying-health-supervision-decisions`, `sources/querying-social-insurance-statistics`, `sources/querying-unemployment-statistics`
- Spatial, environment, and infrastructure:
  `sources/using-estonia-geospatial-open-data`, `sources/querying-planning-decisions`, `sources/querying-construction-register`, `sources/querying-transport-traffic-data`
- Municipal and local-government sources:
  `sources/querying-local-council-volis`, `sources/querying-tallinn-open-data`, `sources/querying-tallinn-council-documents`, `sources/querying-tartu-document-register`
- Digital-state and service delivery context:
  `sources/querying-public-sector-it-systems-riha`, `sources/querying-state-services-catalog`, `sources/querying-x-road-usage-statistics`, `sources/querying-digital-government-studies`

## Detailed map
- Use `SOURCE_MAP.md` for fast source selection by user intent and keyword.
