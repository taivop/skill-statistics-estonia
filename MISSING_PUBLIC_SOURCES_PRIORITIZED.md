# Missing Estonian Public Sources (Prioritized)

Scope: Compared current repository coverage in `sources/*/SKILL.md` against other first-party Estonian public sources relevant to public-sector operations/history.  
Date checked: 2026-02-24.

Legend:
- `Structured` = API/feed/download table
- `Semi-structured` = repeatable list/table pages and linked docs
- `Unstructured` = mostly narrative pages/PDFs, still operationally useful
- `Gap status`: `Missing` = no dedicated source skill; `Partial` = some adjacent coverage exists but no focused source workflow

## Tier 1 (Highest Signal): Core decision records, state strategy, and fiscal control

| Source | Owner | Type | Why it matters | Main entry URL | Gap status |
|---|---|---|---|---|---|
| President decisions and decrees | Office of the President | Semi-structured | Constitutional decisions (appointments, promulgation, veto, decorations) with historical trace | https://www.president.ee/en/official-duties/decisions/ | Missing |
| National Electoral Committee decisions | National Electoral Committee / valimised.ee | Semi-structured | Official election governance decisions (complaints, rulings), complementary to election results | https://www.valimised.ee/et/korraldajad/vabariigi-valimiskomisjon/otsused | Missing |
| Government action programme | Government Office (`valitsus.ee`) | Unstructured | What government committed to execute and how priorities changed over time | https://www.valitsus.ee/valitsuse-eesmargid-ja-tegevused/valitsemise-alused/tegevusprogramm-0 | Missing |
| Estonia 2035 action plan | Government Office (`valitsus.ee`) | Semi-structured | Official cross-government execution framework for long-term policy implementation | https://www.valitsus.ee/strateegia-eesti-2035-arengukavad-ja-planeering/eesti-2035-tegevuskava | Missing |
| Strategic development documents registry | Government Office (`valitsus.ee`) | Semi-structured | Master index of active/in-preparation state development plans | https://www.valitsus.ee/strateegia-eesti-2035-arengukavad-ja-planeering/strateegilised-arengudokumendid/kehtivad | Missing |
| State budget strategy (RES) | Ministry of Finance (`fin.ee`) | Semi-structured | Medium-term fiscal planning and policy envelope before annual budgets | https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/riigi-eelarvestrateegia | Partial |
| State budget package pages (annual budgets) | Ministry of Finance (`fin.ee`) | Semi-structured | Annual legal/fiscal package context, annexes, and explanatory materials | https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/riigieelarved | Partial |
| State financial liabilities (debt/obligations) | Ministry of Finance / Treasury | Semi-structured | Debt and liability-side view of state finances, not just spending | https://www.fin.ee/riigi-rahandus-ja-maksud/riigikassa/riigi-finantskohustised | Missing |
| Treasury investor relations | Ministry of Finance / Treasury | Semi-structured | Sovereign financing disclosures and investor-facing fiscal documentation | https://www.fin.ee/riigi-rahandus-ja-maksud/riigikassa/investorsuhted | Missing |
| Government-sector payments | Ministry of Finance | Structured/Semi-structured | Transaction/flow-level public-sector payment view for execution analysis | https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine/valitsussektori-maksed | Missing |

## Tier 2 (High Signal): State operations management (workforce, accounting, assets, service systems)

| Source | Owner | Type | Why it matters | Main entry URL | Gap status |
|---|---|---|---|---|---|
| Public-sector statistics | Ministry of Finance | Semi-structured | State/local workforce and administrative structure indicators | https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/riigihaldus/avaliku-sektori-statistika | Missing |
| Civil service pay system and salary governance | Ministry of Finance | Semi-structured | Public payroll framework and compensation governance context | https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/avalik-teenistus/palgakorraldus | Missing |
| Consolidated state accounting reports | Ministry of Finance | Semi-structured | Whole-of-government accounting view, complements budget execution portals | https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine/riigi-raamatupidamise-koondaruanded | Partial |
| State real estate register open data | Ministry of Finance | Structured | State property inventory/management records in reusable form | https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/riigi-kinnisvararegister/avaandmed | Partial |
| EHIS (Education Information System) | Ministry of Education/Harno | Structured/Semi-structured | Core education registry layer beyond indicator dashboards | https://www.ehis.ee/ | Missing |
| ETIS (Research Information System) | Ministry of Education/ETAg | Structured/Semi-structured | Public R&D project/funding/institution records for science governance | https://www.etis.ee/ | Missing |
| National public transport portal (`peatus.ee`) | Public transport authorities | Structured/Semi-structured | Public transport service operations (routes/stops/timetables) | https://www.peatus.ee/ | Missing |
| e-Residency operational dashboard | e-Residency programme (state programme) | Structured/Semi-structured | Longitudinal digital public-service delivery and uptake metrics | https://www.e-resident.gov.ee/dashboard/ | Missing |

## Tier 3 (Medium Signal): Sector operations, grants, and enforcement domains

| Source | Owner | Type | Why it matters | Main entry URL | Gap status |
|---|---|---|---|---|---|
| MuIS (Museum Information System) | Ministry of Culture / MuIS | Structured/Semi-structured | Public cultural heritage operations (collections/institutions/object metadata) | https://www.muis.ee/ | Missing |
| Kultuurkapital grants data | Estonian Cultural Endowment (public-law body) | Semi-structured | Public cultural funding allocations and recipient history | https://www.kulka.ee/ | Missing |
| Prison service statistics page | Estonian Prison Service | Semi-structured | Operational prison indicators between annual-review publications | https://www.vangla.ee/et/statistika | Partial |
| Development cooperation & humanitarian aid records | Ministry of Foreign Affairs | Semi-structured | Government external spending and programme implementation records | https://www.vm.ee/en/activity/development-cooperation-and-humanitarian-aid | Missing |
| MFA sanctions implementation pages | Ministry of Foreign Affairs | Semi-structured | Estonian sanctions implementation guidance and updates | https://www.vm.ee/en/activity/international-sanctions/sanctions-government-republic-estonia | Missing |
| MFA sanctions API endpoint (used by portal) | Ministry of Foreign Affairs | Structured (API, query-driven) | Machine-accessible sanctions search backend for repeatable extraction | https://search.service.eu-live.vportal.ee/v1/sanctions/vm | Missing |
| Defence public-opinion surveys | Ministry of Defence | Semi-structured | Long-run survey series on defence legitimacy, readiness, and policy support | https://www.kaitseministeerium.ee/et/eesmargid-tegevused/avalik-arvamus-riigikaitsest | Missing |

## Tier 4 (Lower Signal but Reusable): Niche sources with selective governance value

| Source | Owner | Type | Why it matters | Main entry URL | Gap status |
|---|---|---|---|---|---|
| Language-law supervision pages | Language Board (`Keeleamet`) | Semi-structured | Enforcement/supervision context in official-language compliance domain | https://www.keeleamet.ee/keeleameti-tegevused-ja-eesmargid/keeleseaduse-ja-teiste-keeleoskust-ja-keelekasutust | Missing |
| Defence budget policy pages | Ministry of Defence | Unstructured/Semi-structured | Domain budget context and prioritization history not captured by procurement alone | https://www.kaitseministeerium.ee/et/eesmargid-tegevused/kaitse-eelarve | Missing |
| Defence policy/legal base documents | Ministry of Defence | Unstructured/Semi-structured | Institutional policy baselines and doctrine references | https://www.kaitseministeerium.ee/et/eesmargid-tegevused/alusdokumendid-ja-oigusaktid | Missing |
| Tourism information system open dataset | Public tourism information system (via andmed.eesti.ee) | Structured | Public-service delivery dataset (tourism services/inventory), useful for regional service analysis | https://andmed.eesti.ee/datasets/turismitoodete-ja-teenuste-andmed-puhkaeestis.ee-ja-visitestonia.com-eesti-riiklikus-turismiinfosusteemis | Missing |
| Internal security annual reviews (access friction) | Internal Security Service (`kapo.ee`) | Unstructured | High-value institutional historical signal, but automated access may be blocked | https://www.kapo.ee/aastaraamat/ | Missing (low automation reliability) |

## Notes on overlap with existing repo

- Existing skills already cover many adjacent themes (e.g., `public-finance-data`, `local-government-finance-benchmarks`, `state-assets-register`, `election-results-data`, `prison-annual-reviews`).
- Entries marked `Partial` are areas where current coverage exists at a broad level but no dedicated source workflow for this specific first-party source.
