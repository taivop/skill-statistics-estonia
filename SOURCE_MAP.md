# Source Map (Fast Routing)

Purpose: pick the right official source skill quickly.

## Quick Chooser

| If user asks about... | Start with source skill(s) |
|---|---|
| "official stats", "time series", "national indicators" | `sources/querying-statistics-estonia-api`, `sources/discovering-estonia-open-data` |
| Parliament votes, MPs, sittings | `sources/querying-riigikogu-open-data` |
| Draft law lifecycle and ministry coordination | `sources/tracking-estonia-legislation-workflow-eis`, `sources/tracking-riigikogu-draft-laws`, `sources/querying-riigiteataja-draft-acts` |
| Final laws and legal texts | `sources/querying-estonia-legal-acts-data` |
| Cabinet/government meeting agendas | `sources/tracking-estonia-government-session-agendas` |
| Government document trails and registries | `sources/querying-estonia-ministry-document-registries`, `sources/querying-estonia-government-office-document-register`, `sources/querying-estonia-government-journal-records` |
| Lobbying transparency | `sources/tracking-estonia-lobby-meetings` |
| Public consultations and participation windows | `sources/tracking-estonia-public-consultations-osale`, `sources/monitoring-estonia-public-consultations-feed` |
| Procurement/tenders/contracts | `sources/analyzing-estonia-procurement-data` |
| Party finance and party membership | `sources/querying-estonia-party-funding-data`, `sources/analyzing-estonia-political-party-membership` |
| State audits/constitutional oversight | `sources/querying-estonia-state-audit-reports`, `sources/querying-estonia-ombudsman-opinions` |
| Supreme Court and court case flows | `sources/querying-estonia-supreme-court-judgments`, `sources/querying-estonia-court-proceedings-data`, `sources/querying-estonia-court-system-statistics` |
| Prosecution and police operational context | `sources/querying-estonia-prosecution-statistics`, `sources/querying-estonia-police-operational-statistics` |
| Official notices, insolvency announcements, summons | `sources/querying-estonia-official-notices` |
| Business entities and company baseline data | `sources/using-estonia-business-register-open-data` |
| Property rights / land register | `sources/querying-estonia-land-register-kinnistusraamat` |
| Licensed economic activity (MTR) | `sources/querying-estonia-economic-activities-register-mtr` |
| State aid / state assets / state ownership | `sources/querying-estonia-state-aid-register`, `sources/querying-estonia-state-assets-register`, `sources/querying-estonia-state-ownership-data` |
| Agriculture support recipients / EU funded projects | `sources/querying-estonia-agricultural-subsidies-pria`, `sources/querying-estonia-eu-funded-projects` |
| Taxes and public tax inquiries | `sources/querying-estonia-tax-customs-data`, `sources/querying-estonia-tax-public-inquiries` |
| Budget, public finance, municipal benchmarking | `sources/analyzing-estonia-public-finance-data`, `sources/querying-estonia-local-government-finance-benchmarks` |
| Health stats, medicines, health supervision | `sources/querying-estonia-health-statistics`, `sources/querying-estonia-medicines-register`, `sources/querying-estonia-health-supervision-decisions` |
| Welfare and unemployment | `sources/querying-estonia-social-insurance-statistics`, `sources/querying-estonia-unemployment-statistics`, `sources/using-estonia-health-welfare-open-data` |
| Environment, permits, weather | `sources/querying-estonia-environmental-data`, `sources/querying-estonia-environmental-permit-decisions`, `sources/querying-estonia-weather-data` |
| Planning, construction, cadaster/geospatial | `sources/querying-estonia-planning-decisions`, `sources/querying-estonia-construction-register`, `sources/using-estonia-geospatial-open-data` |
| Transport/traffic and energy system operations | `sources/querying-estonia-transport-traffic-data`, `sources/querying-estonia-energy-data` |
| Cyber incidents and digital government operations | `sources/querying-estonia-cyber-incidents-cert-ee`, `sources/querying-estonia-public-sector-it-systems-riha`, `sources/querying-estonia-x-road-usage-statistics`, `sources/querying-estonia-digital-government-studies` |
| Municipal operations (Tallinn/Tartu/VOLIS) | `sources/querying-estonia-local-council-volis`, `sources/querying-tallinn-open-data`, `sources/querying-tallinn-legal-acts-register`, `sources/querying-tallinn-council-documents`, `sources/querying-tartu-open-data`, `sources/querying-tartu-webaktid`, `sources/querying-tartu-document-register` |
| Elections and political process outcomes | `sources/analyzing-estonia-election-results-data` |
| Cultural heritage / monuments | `sources/querying-estonia-cultural-heritage-register` |
| Historical governance archives | `sources/querying-estonia-national-archives-governance-records` |
| Consumer, competition, data-protection, financial supervision enforcement | `sources/querying-estonia-consumer-technical-regulator-decisions`, `sources/querying-estonia-competition-authority-decisions`, `sources/querying-estonia-data-protection-enforcement`, `sources/querying-estonia-financial-supervision-decisions` |
| State services catalog and public-service delivery | `sources/querying-estonia-state-services-catalog` |
| Interest declarations / anti-corruption declaration process | `sources/querying-estonia-officials-interest-declarations` |
| Rescue incidents and emergency operations | `sources/querying-estonia-rescue-incident-data` |

## Routing notes

- Prefer source-specific skills over generic discovery when user intent is clear.
- Use `sources/discovering-estonia-open-data` first when the user gives only a vague topic.
- If a source is UI-only or access-controlled, pick the skill that includes human-guided export steps and continue from user-provided files.
