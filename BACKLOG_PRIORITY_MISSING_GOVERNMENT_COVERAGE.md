# Priority Missing Government-Coverage Backlog

Date: 2026-02-23  
Scope: high-priority missing official/public sources to fully cover government operations context

## Quick Check: Requested Items

| Item | Status now | Notes |
|---|---|---|
| Cadaster | Partial | Covered broadly in `using-estonia-geospatial-open-data`; missing dedicated cadastral operations skill. |
| Business register | Covered | `using-estonia-business-register-open-data` exists. |
| Party funding | Missing | ERJK open-data source exists but no dedicated skill yet. |
| Party membership | Partial | Party statistics exist in Business Register, but no dedicated party-membership skill yet. |
| Tenders | Covered | `analyzing-estonia-procurement-data` exists. |

## Top 20 Missing Sources/Skills (Highest Priority)

| Rank | Source | Main URL | Why high priority | Proposed skill slug |
|---|---|---|---|---|
| 1 | Ministry/agency document registries network | https://adr.rik.ee/ | Core operational record trail (incoming/outgoing docs, internal workflows) across institutions | `querying-estonia-ministry-document-registries` |
| 2 | Government Office document register | https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/dokumendiregister | Central government-office records and references | `querying-estonia-government-office-document-register` |
| 3 | Government Office lobbying meetings | https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/lobitegevus/lobistidega-kohtumised | Decision-influence transparency context | `tracking-estonia-lobby-meetings` |
| 4 | Government Office public journal records | https://dhs.riigikantselei.ee/avalikteave.nsf/byjournalkey?open | Operational log-like records from official journal view | `querying-estonia-government-journal-records` |
| 5 | OSALE public consultations | https://www.osale.ee/main/mount/share/home | Public-policy consultation and participation workflow tracking | `tracking-estonia-public-consultations-osale` |
| 6 | OSALE consultation RSS | https://www.osale.ee/main/mount/rss/home/publicConsult.rss | Change monitoring for new/updated consultations | `monitoring-estonia-public-consultations-feed` |
| 7 | Party funding open data (ERJK) | https://www.erjk.ee/en/open-data | Political finance transparency; high governance relevance | `querying-estonia-party-funding-data` |
| 8 | Party membership statistics context | https://ariregister.rik.ee/eng/statistics/political_parties | Party organization dynamics and historical context | `analyzing-estonia-political-party-membership` |
| 9 | National Audit Office audits | https://www.riigikontroll.ee/en/audits | Independent audit findings about state performance | `querying-estonia-state-audit-reports` |
| 10 | Chancellor of Justice opinions/reports | https://www.oiguskantsler.ee/en/opinions-and-initiatives/annual-reports | Constitutional/rights oversight signals | `querying-estonia-ombudsman-opinions` |
| 11 | Supreme Court judgments (Riigikohus) | https://www.riigikohus.ee/et/lahendid | Case law shaping administrative/governance practice | `querying-estonia-supreme-court-judgments` |
| 12 | RIHA information-systems registry | https://riha.eesti.ee/riha/main/infSystem/search | Visibility into state information systems and responsibilities | `querying-estonia-public-sector-it-systems-riha` |
| 13 | State services catalog (eesti.ee) | https://www.eesti.ee/en/services | Operational view of services government provides | `querying-estonia-state-services-catalog` |
| 14 | RIA CERT-EE incidents and response context | https://www.ria.ee/en/cyber-security/handling-cyber-incidents-cert-ee | Operational resilience and incident-response governance context | `querying-estonia-cyber-incidents-cert-ee` |
| 15 | RIA studies/analyses/overviews | https://www.ria.ee/en/authority-news-and-contact/news-media-contact/studies-analyses-overviews | Policy/operations evidence from state digital authority | `querying-estonia-digital-government-studies` |
| 16 | Financial supervision court decisions | https://www.fi.ee/en/court-decisions-related-supervision-activities | Enforcement and supervisory outcomes | `querying-estonia-financial-supervision-decisions` |
| 17 | Competition authority decisions/precepts | https://www.konkurentsiamet.ee/en | Market-governance enforcement outcomes | `querying-estonia-competition-authority-decisions` |
| 18 | Data protection authority decisions/guidance | https://www.aki.ee/en | Privacy-governance enforcement and interpretation | `querying-estonia-data-protection-enforcement` |
| 19 | Consumer/technical regulator enforcement context | https://ttja.ee/en | Sector supervision and enforcement outcomes | `querying-estonia-consumer-technical-regulator-decisions` |
| 20 | National Archives governance records | https://www.ra.ee/en/archives/ | Historical governance operations and documents | `querying-estonia-national-archives-governance-records` |

## Suggested Build Order

1. `querying-estonia-ministry-document-registries`
2. `tracking-estonia-public-consultations-osale`
3. `querying-estonia-party-funding-data`
4. `querying-estonia-state-audit-reports`
5. `querying-estonia-ombudsman-opinions`
6. `querying-estonia-public-sector-it-systems-riha`
7. `querying-estonia-state-services-catalog`
8. `tracking-estonia-lobby-meetings`
9. `querying-estonia-supreme-court-judgments`
10. `querying-estonia-national-archives-governance-records`
