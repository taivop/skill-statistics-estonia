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
| 1 | [Statistics Estonia (andmed.stat.ee)](https://andmed.stat.ee/en/stat) | Core official statistics across most domains; foundational for many analyses | PXWeb API (`/api/v1`) + metadata pages | `statistics-api` (existing; keep and upgrade) |
| 2 | [Estonian Open Data Portal (andmed.eesti.ee)](https://andmed.eesti.ee/) | National discovery layer across agencies; good for routing to domain datasets | CKAN-style portal/catalog + APIs listed per dataset | `open-data` |
| 3 | [Land and Spatial Board Geoportal](https://geoportaal.maaamet.ee/eng/) | Base geospatial layer (addresses, cadastral, map services) used in many workflows | WMS/WFS/tiles/download services | `geospatial-open-data` |
| 4 | [Bank of Estonia statistics](https://statistika.eestipank.ee/) | Monetary, financial, external sector indicators not fully covered elsewhere | SDMX/statistical portal exports | `bank-of-statistics` |
| 5 | [Elering Dashboard](https://dashboard.elering.ee/) | Energy system time series (electricity/gas balance, price-related context) | Public API endpoints and dashboard datasets | `energy-data` |
| 6 | [State finances portal (RiigiRaha)](https://riigiraha.fin.ee/) | Government budget/expenditure transparency; key for public finance analysis | Portal datasets/exports | `public-finance-data` |
| 7 | [Business Register open data](https://avaandmed.ariregister.rik.ee/en/downloading-open-data) | Company-level legal entity baseline for business ecosystem analysis | Downloadable open-data extracts | `business-register-open-data` |
| 8 | [Public procurement register](https://www.riigihanked.riik.ee/rhr-web/) | Contracts/tenders for public spending and market analysis | Web datasets / registry endpoints | `procurement-data` |
| 9 | [Tax and Customs Board statistics/open data](https://www.emta.ee/en/business-client/statistics-and-open-data) | Tax revenue/trade/taxpayer indicators for macro and sector signals | Official stats pages + downloadable data | `tax-customs-data` |
| 10 | [Estonian Environmental Portal](https://www.keskkonnaportaal.ee/en) | Environmental indicators (air, water, nature) used in policy and ESG analysis | Portal datasets and services | `environmental-data` |
| 11 | [Estonian Weather Service data feeds](https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php) | Weather series needed for many explanatory models | Public XML endpoints (forecast/observations) | `weather-data` |
| 12 | [Health Statistics DB (TAI)](https://statistika.tai.ee/) | Official health outcomes/utilization indicators | Statistical database exports/API-like querying | `health-statistics` |
| 13 | [TEHIK open data page](https://teabekeskus.tehik.ee/et/avaandmed) | Additional health/welfare administrative open datasets | Open data catalog links/downloads | `health-welfare-open-data` |
| 14 | [HaridusSilm](https://www.haridussilm.ee/ee/avaleht) | Education system indicators (schools, outcomes, staffing, geography) | Portal-based query/download flows | `education-data` |
| 15 | [Transport Administration traffic data](https://www.transpordiamet.ee/liiklussagedus) | Traffic intensity and mobility proxies for economic/transport analyses | Downloadable tables/traffic datasets | `transport-traffic-data` |
| 16 | [Elections archive/statistics](https://www.valimised.ee/et/toimunud-valimiste-arhiiv) | Electoral behavior and turnout trends over time | Archive pages + downloadable results | `election-results-data` |
| 17 | [Riigikogu Open Data API](https://api.riigikogu.ee/swagger-ui.html) | Parliamentary votes, members, agendas for political analysis | REST API (Swagger documented) | `riigikogu-open-data` |
| 18 | [Riigi Teataja](https://www.riigiteataja.ee/) | Legal acts corpus for regulation-aware analysis pipelines | Structured legal text search/download endpoints | `legal-acts-data` |
| 19 | [Tallinn Open Data](https://avaandmed.tallinn.ee/) | High-value city-level transport, environment, urban datasets | Municipal portal/API endpoints | `tallinn-open-data` |
| 20 | [Tartu Open Data](https://www.tartu.ee/en/open-data) | Strong municipal counterpart to Tallinn; useful for cross-city comparisons | Municipal portal + national open-data listings | `tartu-open-data` |

## Implementation Status (2026-02-23)

All 20 skills have been implemented under `sources/<skill-slug>/SKILL.md`.

1. `statistics-api` - implemented
2. `open-data` - implemented
3. `geospatial-open-data` - implemented
4. `bank-of-statistics` - implemented
5. `energy-data` - implemented
6. `public-finance-data` - implemented
7. `business-register-open-data` - implemented
8. `procurement-data` - implemented
9. `tax-customs-data` - implemented
10. `environmental-data` - implemented
11. `weather-data` - implemented
12. `health-statistics` - implemented
13. `health-welfare-open-data` - implemented
14. `education-data` - implemented
15. `transport-traffic-data` - implemented
16. `election-results-data` - implemented
17. `riigikogu-open-data` - implemented
18. `legal-acts-data` - implemented
19. `tallinn-open-data` - implemented
20. `tartu-open-data` - implemented

## Suggested Delivery Phases

### Phase 1 (highest leverage)

1. `open-data`
2. `geospatial-open-data`
3. `bank-of-statistics`
4. `energy-data`
5. `public-finance-data`
6. `business-register-open-data`

### Phase 2 (sector depth)

1. `procurement-data`
2. `tax-customs-data`
3. `environmental-data`
4. `weather-data`
5. `health-statistics`
6. `health-welfare-open-data`
7. `education-data`

### Phase 3 (governance + municipal)

1. `transport-traffic-data`
2. `election-results-data`
3. `riigikogu-open-data`
4. `legal-acts-data`
5. `tallinn-open-data`
6. `tartu-open-data`

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
