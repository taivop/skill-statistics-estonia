# Multi-Skill Expansion Backlog (Estonian Public Data)

Date: 2026-02-23  
Scope: backlog + implementation tracking

## Goal

Expand this repository from a single skill into a multi-skill collection covering the most useful generic Estonian public data sources.

## Selection Criteria

- High reuse across many analysis tasks (economy, demography, energy, health, transport, legal, geospatial).
- Public availability and practical machine access (API, CSV/JSON/XML, or stable download endpoints).
- Institutional reliability (official national/state/municipal providers).
- Coverage breadth (national first, then high-value municipal sources).

## Top 20 Data Sources to Cover

| Rank | Source | Why it is high-value | Access mode | Proposed skill slug |
|---|---|---|---|---|
| 1 | [Statistics Estonia (andmed.stat.ee)](https://andmed.stat.ee/en/stat) | Core official statistics across most domains; foundational for many analyses | PXWeb API (`/api/v1`) + metadata pages | `querying-statistics-estonia-api` (existing; keep and upgrade) |
| 2 | [Estonian Open Data Portal (andmed.eesti.ee)](https://andmed.eesti.ee/) | National discovery layer across agencies; good for routing to domain datasets | CKAN-style portal/catalog + APIs listed per dataset | `discovering-estonia-open-data` |
| 3 | [Land and Spatial Board Geoportal](https://geoportaal.maaamet.ee/eng/) | Base geospatial layer (addresses, cadastral, map services) used in many workflows | WMS/WFS/tiles/download services | `using-estonia-geospatial-open-data` |
| 4 | [Bank of Estonia statistics](https://statistika.eestipank.ee/) | Monetary, financial, external sector indicators not fully covered elsewhere | SDMX/statistical portal exports | `querying-bank-of-estonia-statistics` |
| 5 | [Elering Dashboard](https://dashboard.elering.ee/) | Energy system time series (electricity/gas balance, price-related context) | Public API endpoints and dashboard datasets | `querying-energy-data` |
| 6 | [State finances portal (RiigiRaha)](https://riigiraha.fin.ee/) | Government budget/expenditure transparency; key for public finance analysis | Portal datasets/exports | `analyzing-estonia-public-finance-data` |
| 7 | [Business Register open data](https://avaandmed.ariregister.rik.ee/en/downloading-open-data) | Company-level legal entity baseline for business ecosystem analysis | Downloadable open-data extracts | `using-estonia-business-register-open-data` |
| 8 | [Public procurement register](https://www.riigihanked.riik.ee/rhr-web/) | Contracts/tenders for public spending and market analysis | Web datasets / registry endpoints | `analyzing-estonia-procurement-data` |
| 9 | [Tax and Customs Board statistics/open data](https://www.emta.ee/en/business-client/statistics-and-open-data) | Tax revenue/trade/taxpayer indicators for macro and sector signals | Official stats pages + downloadable data | `querying-tax-customs-data` |
| 10 | [Estonian Environmental Portal](https://www.keskkonnaportaal.ee/en) | Environmental indicators (air, water, nature) used in policy and ESG analysis | Portal datasets and services | `querying-environmental-data` |
| 11 | [Estonian Weather Service data feeds](https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php) | Weather series needed for many explanatory models | Public XML endpoints (forecast/observations) | `querying-weather-data` |
| 12 | [Health Statistics DB (TAI)](https://statistika.tai.ee/) | Official health outcomes/utilization indicators | Statistical database exports/API-like querying | `querying-health-statistics` |
| 13 | [TEHIK open data page](https://teabekeskus.tehik.ee/et/avaandmed) | Additional health/welfare administrative open datasets | Open data catalog links/downloads | `using-estonia-health-welfare-open-data` |
| 14 | [HaridusSilm](https://www.haridussilm.ee/ee/avaleht) | Education system indicators (schools, outcomes, staffing, geography) | Portal-based query/download flows | `querying-education-data` |
| 15 | [Transport Administration traffic data](https://www.transpordiamet.ee/liiklussagedus) | Traffic intensity and mobility proxies for economic/transport analyses | Downloadable tables/traffic datasets | `querying-transport-traffic-data` |
| 16 | [Elections archive/statistics](https://www.valimised.ee/et/toimunud-valimiste-arhiiv) | Electoral behavior and turnout trends over time | Archive pages + downloadable results | `analyzing-estonia-election-results-data` |
| 17 | [Riigikogu Open Data API](https://api.riigikogu.ee/swagger-ui.html) | Parliamentary votes, members, agendas for political analysis | REST API (Swagger documented) | `querying-riigikogu-open-data` |
| 18 | [Riigi Teataja](https://www.riigiteataja.ee/) | Legal acts corpus for regulation-aware analysis pipelines | Structured legal text search/download endpoints | `querying-legal-acts-data` |
| 19 | [Tallinn Open Data](https://avaandmed.tallinn.ee/) | High-value city-level transport, environment, urban datasets | Municipal portal/API endpoints | `querying-tallinn-open-data` |
| 20 | [Tartu Open Data](https://www.tartu.ee/en/open-data) | Strong municipal counterpart to Tallinn; useful for cross-city comparisons | Municipal portal + national open-data listings | `querying-tartu-open-data` |

## Implementation Status (2026-02-23)

All 20 skills have been implemented under `sources/<skill-slug>/SKILL.md`.

1. `querying-statistics-estonia-api` - implemented
2. `discovering-estonia-open-data` - implemented
3. `using-estonia-geospatial-open-data` - implemented
4. `querying-bank-of-estonia-statistics` - implemented
5. `querying-energy-data` - implemented
6. `analyzing-estonia-public-finance-data` - implemented
7. `using-estonia-business-register-open-data` - implemented
8. `analyzing-estonia-procurement-data` - implemented
9. `querying-tax-customs-data` - implemented
10. `querying-environmental-data` - implemented
11. `querying-weather-data` - implemented
12. `querying-health-statistics` - implemented
13. `using-estonia-health-welfare-open-data` - implemented
14. `querying-education-data` - implemented
15. `querying-transport-traffic-data` - implemented
16. `analyzing-estonia-election-results-data` - implemented
17. `querying-riigikogu-open-data` - implemented
18. `querying-legal-acts-data` - implemented
19. `querying-tallinn-open-data` - implemented
20. `querying-tartu-open-data` - implemented

## Suggested Delivery Phases

### Phase 1 (highest leverage)

1. `discovering-estonia-open-data`
2. `using-estonia-geospatial-open-data`
3. `querying-bank-of-estonia-statistics`
4. `querying-energy-data`
5. `analyzing-estonia-public-finance-data`
6. `using-estonia-business-register-open-data`

### Phase 2 (sector depth)

1. `analyzing-estonia-procurement-data`
2. `querying-tax-customs-data`
3. `querying-environmental-data`
4. `querying-weather-data`
5. `querying-health-statistics`
6. `using-estonia-health-welfare-open-data`
7. `querying-education-data`

### Phase 3 (governance + municipal)

1. `querying-transport-traffic-data`
2. `analyzing-estonia-election-results-data`
3. `querying-riigikogu-open-data`
4. `querying-legal-acts-data`
5. `querying-tallinn-open-data`
6. `querying-tartu-open-data`

## Notes for Later Implementation

- Keep each skill narrowly scoped by source to avoid oversized SKILL.md files.
- Prefer deterministic helper scripts for fragile APIs or complex query payloads.
- Standardize outputs across skills (JSON + CSV option, plus metadata capture).
- Include source-specific caveats (rate limits, refresh cadence, terminology, language).

## Limitations Found During Implementation

- Source #15 (Transport Administration): previous URL in this backlog returned 404 during validation; skill now uses `https://www.transpordiamet.ee/liiklussagedus` and agency root navigation.
- Source #16 (Elections): previous English archive URL returned 404; skill now uses currently reachable archive/open-data pages under Estonian paths, including `https://www.valimised.ee/et/valimiste-arhiiv/valimiste-avaandmed`.
- Source #17 (Riigikogu): previous Swagger URL was outdated; skill now uses `https://api.riigikogu.ee/swagger-ui.html`.
- Source #20 (Tartu): `https://avaandmed.tartu.ee/` was unreachable; skill uses city open-data landing page and organization-scoped discovery on the national portal.
- Source #6 and #8 (RiigiRaha, Procurement): direct stable public APIs were not confirmed from landing pages; skills include explicit human-guided UI export fallback workflow.
