# Source Map (Fast Routing)

Purpose: pick the right official source skill quickly.

## Quick Chooser

| If user asks about... | Start with source skill(s) |
|---|---|
| "official stats", "time series", "national indicators" | `sources/querying-statistics-estonia-api`, `sources/discovering-estonia-open-data` |
| Parliament votes, MPs, sittings | `sources/querying-riigikogu-open-data` |
| Draft law lifecycle and ministry coordination | `sources/tracking-estonia-legislation-workflow-eis`, `sources/tracking-riigikogu-draft-laws`, `sources/querying-riigiteataja-draft-acts` |
| Final laws and legal texts | `sources/querying-legal-acts-data` |
| Cabinet/government meeting agendas | `sources/tracking-estonia-government-session-agendas` |
| Government document trails and registries | `sources/querying-ministry-document-registries`, `sources/querying-government-office-document-register`, `sources/querying-government-journal-records` |
| Lobbying transparency | `sources/tracking-estonia-lobby-meetings` |
| Public consultations and participation windows | `sources/tracking-estonia-public-consultations-osale`, `sources/monitoring-estonia-public-consultations-feed` |
| Procurement/tenders/contracts | `sources/analyzing-estonia-procurement-data` |
| Party finance and party membership | `sources/querying-party-funding-data`, `sources/analyzing-estonia-political-party-membership` |
| State audits/constitutional oversight | `sources/querying-state-audit-reports`, `sources/querying-ombudsman-opinions` |
| Supreme Court and court case flows | `sources/querying-supreme-court-judgments`, `sources/querying-court-proceedings-data`, `sources/querying-court-system-statistics` |
| Prosecution and police operational context | `sources/querying-prosecution-statistics`, `sources/querying-police-operational-statistics` |
| Official notices, insolvency announcements, summons | `sources/querying-official-notices` |
| Business entities and company baseline data | `sources/using-estonia-business-register-open-data` |
| Property rights / land register | `sources/querying-land-register-kinnistusraamat` |
| Licensed economic activity (MTR) | `sources/querying-economic-activities-register-mtr` |
| State aid / state assets / state ownership | `sources/querying-state-aid-register`, `sources/querying-state-assets-register`, `sources/querying-state-ownership-data` |
| Agriculture support recipients / EU funded projects | `sources/querying-agricultural-subsidies-pria`, `sources/querying-eu-funded-projects` |
| Taxes and public tax inquiries | `sources/querying-tax-customs-data`, `sources/querying-tax-public-inquiries` |
| Budget, public finance, municipal benchmarking | `sources/analyzing-estonia-public-finance-data`, `sources/querying-local-government-finance-benchmarks` |
| Health stats, medicines, health supervision | `sources/querying-health-statistics`, `sources/querying-medicines-register`, `sources/querying-health-supervision-decisions` |
| Welfare and unemployment | `sources/querying-social-insurance-statistics`, `sources/querying-unemployment-statistics`, `sources/using-estonia-health-welfare-open-data` |
| Environment, permits, weather | `sources/querying-environmental-data`, `sources/querying-environmental-permit-decisions`, `sources/querying-weather-data` |
| Planning, construction, cadaster/geospatial | `sources/querying-planning-decisions`, `sources/querying-construction-register`, `sources/using-estonia-geospatial-open-data` |
| Transport/traffic and energy system operations | `sources/querying-transport-traffic-data`, `sources/querying-energy-data` |
| Cyber incidents and digital government operations | `sources/querying-cyber-incidents-cert-ee`, `sources/querying-public-sector-it-systems-riha`, `sources/querying-x-road-usage-statistics`, `sources/querying-digital-government-studies` |
| Municipal operations (Tallinn/Tartu/VOLIS) | `sources/querying-local-council-volis`, `sources/querying-tallinn-open-data`, `sources/querying-tallinn-legal-acts-register`, `sources/querying-tallinn-council-documents`, `sources/querying-tartu-open-data`, `sources/querying-tartu-webaktid`, `sources/querying-tartu-document-register` |
| Elections and political process outcomes | `sources/analyzing-estonia-election-results-data` |
| Cultural heritage / monuments | `sources/querying-cultural-heritage-register` |
| Historical governance archives | `sources/querying-national-archives-governance-records` |
| Consumer, competition, data-protection, financial supervision enforcement | `sources/querying-consumer-technical-regulator-decisions`, `sources/querying-competition-authority-decisions`, `sources/querying-data-protection-enforcement`, `sources/querying-financial-supervision-decisions` |
| State services catalog and public-service delivery | `sources/querying-state-services-catalog` |
| Interest declarations / anti-corruption declaration process | `sources/querying-officials-interest-declarations` |
| Rescue incidents and emergency operations | `sources/querying-rescue-incident-data` |

## Routing notes

- Prefer source-specific skills over generic discovery when user intent is clear.
- Use `sources/discovering-estonia-open-data` first when the user gives only a vague topic.
- If a source is UI-only or access-controlled, pick the skill that includes human-guided export steps and continue from user-provided files.
