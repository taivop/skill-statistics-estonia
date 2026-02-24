---
name: public-consultations-feed
description: Monitor Estonia public consultation updates via OSALE RSS feed and produce incremental change summaries.
---

# OSALE Consultation Feed Monitoring

## Use when
- You need ongoing monitoring of newly published/updated consultations.
- You need low-latency change detection from an official feed.

## Avoid when
- You need full consultation document parsing without feed context.

## Inputs
- Monitoring window and topic filters.

## Outputs
- New/changed consultation entries with links and timestamps.

## Primary endpoint
- RSS feed: https://www.osale.ee/main/mount/rss/home/publicConsult.rss

## Workflow
1. Pull RSS feed and parse entries.
2. Filter by topic/institution keywords.
3. Compare with prior snapshot if available.
4. Return incremental update report.

## Human setup (when needed)
- Usually none. If historical snapshot is required and not available, ask user to provide prior file/source used for baseline.

## Quality checks
- Track item GUID/link and publication date.
- Avoid duplicate reporting for unchanged entries.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.osale.ee/main/mount/rss/home/publicConsult.rss (HTTP 200, text/html;charset=UTF-8, file links detected: 0)

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
