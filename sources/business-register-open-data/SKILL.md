---
name: business-register-open-data
description: Use Estonian Business Register open data downloads for legal-entity analysis, registry snapshots, and organization-level trends including political party statistics.
---

# Estonia Business Register Open Data

## Use when
- You need legal entity baseline datasets (registrations, statuses, attributes).
- You need reproducible business population extracts.
- You need organization-level context that also supports party membership trend analysis.

## Avoid when
- You only need high-level macro indicators.

## Access reality
- Public access type: direct downloadable snapshot files + API/X-road documentation.
- Snapshot files are directly downloadable as zipped CSV/XML/JSON/Parquet from open-data page.

## Inputs
- Entity scope, date range, and required fields.

## Outputs
- Registry extract with schema notes and date stamp.

## Primary endpoints
- Download page: https://avaandmed.ariregister.rik.ee/en/downloading-open-data
- Open data API index: https://avaandmed.ariregister.rik.ee/en/open-data-api/introduction-api-services
- Open data guidance: https://abiinfo.rik.ee/en/e-business-register-queries/open-data-e-business-register
- Beneficial owners guidance: https://abiinfo.rik.ee/en/e-business-register-queries/beneficial-owners
- XML service WSDL (live): https://ariregxmlv6.rik.ee/?wsdl
- XML service WSDL (demo): https://demo-ariregxmlv6.rik.ee/?wsdl

## Retrieval workflow
1. Open download page and choose dataset family (for example `ettevotja_rekvisiidid__...`).
2. Download zip file in desired format (`csv.zip`, `xml.zip`, `json.zip`, `parquet.zip`).
3. Unzip and parse with original delimiter/encoding preserved.
4. If needed, use open-data API documentation pages for query-based enrichment.
5. Keep snapshot file name and retrieval date in output metadata.

## Request contract
- Snapshot downloads: direct GET file URLs under `/sites/default/files/...`.
- API-related docs list service methods and contracts.
- XML service (`ariregxmlv6`) is documented by WSDL and includes paid/demo service contexts.

## Output schema expectations
- Preserve at least:
  - business registry code (`ariregistri_kood`)
  - legal form/status fields
  - registration date fields
  - address/location fields
  - source link and snapshot timestamp/file name
- Keep beneficial-owner fields separate from core legal-entity fields.

## Limits and caveats
- Different datasets use different format families and completeness levels.
- API contracts and access terms can differ from static open-data snapshot access.
- Some related services (contracted APIs) are not free/open in the same way as snapshot files.

## Verification hooks
- Verify downloaded archive is valid zip and contains expected table file.
- Verify header row includes key identifiers (for example `ariregistri_kood`).
- Verify WSDL endpoints respond with XML metadata.

## Quality checks
- Preserve original business identifiers.
- Keep snapshot date and provenance in output metadata.
- Keep beneficial-owner fields and legal-entity fields clearly separated.
