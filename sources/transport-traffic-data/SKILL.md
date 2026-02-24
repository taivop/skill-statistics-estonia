---
name: transport-traffic-data
description: Retrieve Estonian transport operations data from Transport Administration pages and national public transport APIs (Peatus GraphQL and related public endpoints).
---

# Transport and Public Transit Data

## Use when
- You need transport operations data, especially public transit stops/routes and traffic context.
- You need repeatable API-based extraction for national public transport routing data.

## Avoid when
- You only need municipal-only transport portals.

## Inputs
- Geography and period.
- Entity scope (`stops`, `routes`, `patterns`, `traffic context`).

## Outputs
- Structured transit/traffic dataset with source endpoint metadata.

## Access reality statement
- Access type: `API` + `download files`/`UI copy-only`.
- Verified on 2026-02-24.
- Peatus GraphQL endpoint is queryable via POST JSON.

## Primary endpoints
- Peatus portal: https://www.peatus.ee/
- Peatus GraphQL endpoint: https://api.peatus.ee/routing/v1/routers/estonia/index/graphql
- Peatus public notifications API: https://web.peatus.ee/admin/api/public/notifications
- Transport Administration main site: https://www.transpordiamet.ee/en
- Traffic frequency page: https://www.transpordiamet.ee/liiklussagedus

## Retrieval workflow (reproducible)
1. For public transit entities, send POST requests to Peatus GraphQL endpoint.
2. Start with schema sanity query (`{__typename}`), then run scoped queries (`stops`, `routes`, etc.).
3. For operational notices, fetch JSON from notifications endpoint.
4. For road traffic context, collect files or published tables from Transport Administration pages.
5. Return parsed records with original query text and response timestamp.

## Request/query contract
- Peatus GraphQL requires:
  - Method: `POST`
  - Header: `Content-Type: application/json`
  - Body: `{"query":"...GraphQL..."}`
- GET on GraphQL endpoint can return server error; use POST.
- Notifications endpoint returns JSON without authentication.

## Output schema expectations
- `source_system` (`peatus_graphql`, `peatus_notifications`, `transpordiamet`)
- `query` (for GraphQL extractions)
- `entity_type`
- `gtfsId` (if present)
- `name`
- `lat`/`lon` (if present)
- `mode` (if present)
- `published_at` (for notifications)
- `source_url`

## Limits and caveats
- GraphQL schema can evolve; always include query used.
- Some transport context pages are ET-only and UI-centric.
- API responses can be large; paginate/scope queries where possible.

## Verification hooks
- POST `{"query":"{__typename}"}` returns `{"data":{"__typename":"QueryType"}}`.
- Query `stops(name:"Tallinn"){name gtfsId lat lon}` returns structured stop records.
- `https://web.peatus.ee/admin/api/public/notifications` returns `application/json`.
