---
name: muis-open-data
description: Retrieve machine-readable MuIS museum/collection records from opendata.muis.ee RDF endpoints and related open-data resource paths.
---

# MuIS Open Data

## Use when
- You need machine-readable museum object, collection, place, event, thesaurus, or person-group records.
- You need RDF-compatible cultural heritage operational data.

## Avoid when
- You only need monument protection status (use cultural-heritage-register skill).

## Inputs
- Endpoint family (`object`, `media-list`, `collection`, `person-group`, `place`, `event`, `thesaurus`).
- Entity id(s).

## Outputs
- RDF/XML records and parsed entity metadata with endpoint-level provenance.

## Access reality statement
- Access type: `API` (RDF over HTTP).
- Verified on 2026-02-24.
- Endpoints are publicly reachable; content negotiation via `Accept: application/rdf+xml` is supported.

## Primary endpoints
- Open data docs page: https://opendata.muis.ee/
- Example object endpoint: https://opendata.muis.ee/object/1
- RDF schema: https://opendata.muis.ee/rdf-schema/muis.rdfs
- Additional endpoint patterns listed on docs page (object, media-list, person-group, thesaurus, event, place, collection, objects-by-museum).

## Retrieval workflow (reproducible)
1. Open `opendata.muis.ee` and select endpoint family + id.
2. Request resource with `Accept: application/rdf+xml`.
3. Store raw RDF response and parse key triples/fields required for task.
4. For bulk transfer, use `accept-encoding: gzip` where supported.
5. Return parsed entities with endpoint URL and retrieval timestamp.

## Request/query contract
- Method: `GET`.
- Required parameter: path id in endpoint URL (e.g., `/object/{id}`).
- Recommended header: `Accept: application/rdf+xml`.
- Optional header for compressed downloads: `accept-encoding: gzip`.
- Response body: RDF/XML content.

## Output schema expectations
- `endpoint_url`
- `entity_type`
- `entity_id`
- `rdf_format`
- `label_or_title`
- `museum_or_collection_ref` (if present)
- `time_or_period` (if present)
- `raw_reference`

## Limits and caveats
- Response `Content-Type` header may not always strictly advertise RDF even when RDF body is returned.
- Some linked resources require follow-up requests for full context.
- IDs are source-system identifiers and should not be re-coded.

## Verification hooks
- `https://opendata.muis.ee/object/1` is reachable.
- `curl -H "Accept: application/rdf+xml" https://opendata.muis.ee/object/1522095` returns RDF body.
- Docs page lists endpoint examples and gzip retrieval examples.
