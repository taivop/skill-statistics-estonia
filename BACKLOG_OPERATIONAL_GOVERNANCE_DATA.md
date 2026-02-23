# Backlog: Operational Governance Data Stores (Estonia)

Date: 2026-02-23  
Scope: public operational records (meeting notes, agendas, decisions, official notices, permits, proceedings)

## Coverage Summary

- Clearly covered now: 20
- Partially covered now: 0
- Not covered now: 0

Covered by skills in this repo:

1. `riigikogu-open-data` (Riigikogu API)
2. `legal-acts-data` (Riigi Teataja legal acts API)
3. `procurement-data` (public procurement register)
4. `election-results-data` (election archive/open data)
5. `court-proceedings-data`
6. `legislation-workflow-eis`
7. `riigikogu-draft-laws`
8. `riigikogu-stenograms`
9. `riigikogu-agendas`
10. `government-session-agendas`
11. `riigiteataja-draft-acts`
12. `official-notices`
13. `local-council-volis`
14. `tallinn-legal-acts-register`
15. `tallinn-council-documents`
16. `tartu-webaktid`
17. `tartu-document-register`
18. `environmental-permit-decisions`
19. `construction-register`
20. `planning-decisions`

## Top 20 Operational Data Stores Backlog

| Rank | Data store | Main URL | Why useful | Covered? | Proposed skill (if uncovered) |
|---|---|---|---|---|---|
| 1 | EIS (draft law coordination workflow) | https://eelnoud.valitsus.ee/main/main | Core inter-ministerial draft-law lifecycle and coordination events | Yes | `legislation-workflow-eis` |
| 2 | Riigikogu Open Data API | https://api.riigikogu.ee/swagger-ui.html | Votes, sittings, members, and legislative operations | Yes | Existing: `riigikogu-open-data` |
| 3 | Riigikogu draft laws tracker | https://www.riigikogu.ee/tegevus/eelnoud/ | Bill progress, statuses, linked docs | Yes | `riigikogu-draft-laws` |
| 4 | Riigikogu stenograms | https://www.riigikogu.ee/tegevus/stenogrammid/ | Full parliamentary debate transcripts | Yes | `riigikogu-stenograms` |
| 5 | Riigikogu calendar/agendas | https://www.riigikogu.ee/tegevus/kalender/ | Meeting schedule and agenda-level operational visibility | Yes | `riigikogu-agendas` |
| 6 | Government session agenda/news search | https://valitsus.ee/otsing?filters%5Btype%5D=Uudis&filters%5Bkeyword%5D=Istungi%20p%C3%A4evakord&sort=created&page=1 | Cabinet-level meeting agenda publications | Yes | `government-session-agendas` |
| 7 | Riigi Teataja legal acts API | https://www.riigiteataja.ee/api/oigusakt_otsing/1/otsi?leht=1 | Official, machine-readable legal acts and validity periods | Yes | Existing: `legal-acts-data` |
| 8 | Riigi Teataja draft acts search | https://www.riigiteataja.ee/eelnoud/otsing.html | Public legal drafting stream complementary to EIS | Yes | `riigiteataja-draft-acts` |
| 9 | Riigi Teataja court/judicial proceedings | https://www.riigiteataja.ee/kohtulahendid/koik_menetlused.html | Judicial proceedings corpus for decision tracking | Yes | `court-proceedings-data` |
| 10 | Ametlikud Teadaanded URI search | https://www.ametlikudteadaanded.ee/avalik/uriotsing | Official notices (bankruptcy, summons, announcements) | Yes | `official-notices` |
| 11 | Public procurement register | https://www.riigihanked.riik.ee/rhr-web/ | Tender and award decisions; procurement operations | Yes | Existing: `procurement-data` |
| 12 | Election archive open data | https://www.valimised.ee/en/archive/open-data-estonian-elections | Election process outcomes and operational history | Yes | Existing: `election-results-data` |
| 13 | VOLIS (local council information system) | https://www.volis.ee/ | Municipal council agendas, votes, and decisions | Yes | `local-council-volis` |
| 14 | Tallinn legal acts register | https://oigusaktid.tallinn.ee/ | City legal acts and decisions | Yes | `tallinn-legal-acts-register` |
| 15 | Tallinn council documents (TEELE) | https://teele.tallinn.ee/documents/council/acts?page=1&pageSize=10&sortColumn=publishedAt&sortDirection=desc | Council acts and draft workflows | Yes | `tallinn-council-documents` |
| 16 | Tartu legal acts register (WebAktid) | https://info.raad.tartu.ee/webaktid.nsf | Tartu city legal acts and decisions | Yes | `tartu-webaktid` |
| 17 | Tartu document register (DHS) | https://info.raad.tartu.ee/dhs.nsf | City document workflow and records | Yes | `tartu-document-register` |
| 18 | KOTKAS environmental decision system | https://kotkas.envir.ee/ | Permits, approvals, and environmental administrative decisions | Yes | `environmental-permit-decisions` |
| 19 | EHR (construction register) | https://www.ehr.ee/en | Building permits/operations and related official records | Yes | `construction-register` |
| 20 | National planning register | https://www.planeeringud.ee/ | Spatial planning decisions and plan lifecycle | Yes | `planning-decisions` |

## Implementation Status

All 20 operational backlog items are now implemented as skills in this repository.

## Notes

- This list intentionally prioritizes operational public records over statistical datasets.
- Several stores are UI-first rather than API-first. For those, skills should include explicit human-guided extraction steps and then continue automatically from user-provided files/URLs.
