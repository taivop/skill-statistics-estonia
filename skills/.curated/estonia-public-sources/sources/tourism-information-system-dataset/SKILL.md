---
name: tourism-information-system-dataset
description: Retrieve tourism services/inventory records from the official andmed.eesti.ee dataset for the national tourism information system.
---

# Tourism Information System Dataset (andmed.eesti.ee)

## Use when
- You need structured tourism service inventory data from the national tourism information system dataset.
- You need direct downloadable distribution files and metadata.

## Avoid when
- You need broad dataset discovery only (use open-data discovery skill).

## Inputs
- Dataset slug (default fixed for this source).
- Distribution format preference (XLSX, etc.).

## Outputs
- Dataset metadata plus downloaded distribution file links/records.

## Access reality statement
- Access type: `API` + `download files`.
- Verified on 2026-02-24.
- Dataset metadata and distribution links are available via andmed.eesti.ee JSON APIs.

## Primary endpoints
- Dataset page: https://andmed.eesti.ee/datasets/turismitoodete-ja-teenuste-andmed-puhkaeestis.ee-ja-visitestonia.com-eesti-riiklikus-turismiinfosusteemis
- Dataset metadata by slug: https://andmed.eesti.ee/api/datasets/slug/turismitoodete-ja-teenuste-andmed-puhkaeestis.ee-ja-visitestonia.com-eesti-riiklikus-turismiinfosusteemis
- Dataset search API: https://andmed.eesti.ee/api/datasets/search
- Distribution file URL pattern (from metadata `accessUrls`): `https://andmed.eesti.ee/api/v2/datasets/<dataset_id>/distribution/<distribution_id>/file`

## Retrieval workflow (reproducible)
1. Query slug endpoint and capture dataset metadata and `distributions` list.
2. Read each distribution `accessUrls` entry and select required format.
3. Request distribution file URL; follow redirect to signed object storage URL.
4. Download and parse selected files.
5. Return metadata + parsed records with distribution IDs and update timestamps.

## Request/query contract
- Metadata endpoints: `GET` JSON.
- Distribution download endpoints: `GET`, returns `302` redirect to signed storage URL.
- Important fields from slug response: `distributions[].id`, `accessUrls[]`, `format`, `createdAt`, `updatedAt`, `fileId`.

## Output schema expectations
- `dataset_slug`
- `dataset_source_url`
- `distribution_id`
- `distribution_title`
- `format`
- `updated_at`
- `download_url`
- `record` (parsed row object)

## Limits and caveats
- Signed distribution URLs expire; store canonical API URL plus retrieval timestamp.
- Distribution structure/columns can change across updates.

## Verification hooks
- Slug endpoint returns `status: COMPLETED` and multiple distributions.
- Distribution `accessUrls` include `/api/v2/datasets/<id>/distribution/<id>/file`.
- File endpoint returns HTTP `302` to signed S3 URL.
