---
name: digital-government-studies
description: Query RIA studies, analyses, and overviews for digital-government operational evidence and policy context.
---

# Digital Government Studies (RIA)

## Use when
- You need official studies/analyses on state digital systems and governance.
- You need contextual evidence for operational-government assessments.

## Avoid when
- You need transactional system data instead of analytical publications.

## Inputs
- Topic keywords and date range.

## Outputs
- Publication index with metadata and links.

## Primary endpoint
- Studies/analyses page: https://www.ria.ee/en/authority-news-and-contact/news-media-contact/studies-analyses-overviews

## Workflow
1. Collect study/overview entries by topic/date.
2. Extract titles, dates, and downloadable links.
3. Tag each entry by domain (cyber, services, infrastructure, etc.).
4. Return structured publication table.

## Human setup (when needed)
- If files are embedded behind UI components, guide user through download steps and continue from local files.

## Quality checks
- Keep publication date and source institution.
- Avoid mixing RIA studies with unrelated news posts.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.ria.ee/en/authority-news-and-contact/news-media-contact/studies-analyses-overviews (HTTP 200, text/html;, file links detected: 1)

## Request contract
- Use the listed primary endpoints as authoritative entry points.
- If API/query parameters are only visible in-browser, preserve exact request URL, params, and headers in output metadata.
- If endpoint is UI-only, document click path and extraction method used.

## Output schema expectations
- Keep at least: source URL, retrieval timestamp, publication/update date (if available), title/record label, and extracted governance-relevant fields.
- Preserve original field names when present in downloadable/API output.

## Limits and caveats
- Confirm whether data is open-download, UI-only, or authenticated before claiming full access.
- Separate narrative/guidance text from measurable records.

## Verification hooks
- Validate endpoint reachability and content type before extraction.
- Validate that each extracted claim is linked to a concrete source URL.
