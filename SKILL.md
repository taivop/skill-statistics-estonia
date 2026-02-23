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
  `sources/statistics-api`, `sources/bank-of-statistics`, `sources/public-finance-data`, `sources/tax-customs-data`
- Parliament, lawmaking, and legal texts:
  `sources/riigikogu-open-data`, `sources/riigikogu-draft-laws`, `sources/legislation-workflow-eis`, `sources/legal-acts-data`
- Government operations and transparency records:
  `sources/ministry-document-registries`, `sources/government-office-document-register`, `sources/lobby-meetings`, `sources/official-notices`
- Oversight, supervision, and enforcement:
  `sources/state-audit-reports`, `sources/ombudsman-opinions`, `sources/financial-supervision-decisions`, `sources/data-protection-enforcement`
- Registries, ownership, and organization context:
  `sources/business-register-open-data`, `sources/land-register-kinnistusraamat`, `sources/economic-activities-register-mtr`, `sources/state-ownership-data`
- Public spending, subsidies, and projects:
  `sources/procurement-data`, `sources/party-funding-data`, `sources/agricultural-subsidies-pria`, `sources/eu-funded-projects`
- Justice and internal security operations:
  `sources/court-proceedings-data`, `sources/court-system-statistics`, `sources/prosecution-statistics`, `sources/police-operational-statistics`
- Health, welfare, and labor operations:
  `sources/health-statistics`, `sources/health-supervision-decisions`, `sources/social-insurance-statistics`, `sources/unemployment-statistics`
- Spatial, environment, and infrastructure:
  `sources/geospatial-open-data`, `sources/planning-decisions`, `sources/construction-register`, `sources/transport-traffic-data`
- Municipal and local-government sources:
  `sources/local-council-volis`, `sources/tallinn-open-data`, `sources/tallinn-council-documents`, `sources/tartu-document-register`
- Digital-state and service delivery context:
  `sources/public-sector-it-systems-riha`, `sources/state-services-catalog`, `sources/x-road-usage-statistics`, `sources/digital-government-studies`

## Detailed map
- Use `SOURCE_MAP.md` for fast source selection by user intent and keyword.
