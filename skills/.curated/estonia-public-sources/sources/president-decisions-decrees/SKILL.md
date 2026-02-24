---
name: president-decisions-decrees
description: Retrieve public decision/decree records published by the Office of the President, with anti-bot-aware browser workflow and record-level citation output.
---

# President Decisions and Decrees

## Use when
- You need constitutional decision records by the President (appointments, promulgation-related decisions, decorations, etc.).
- You need chronologically traceable official decision pages.

## Avoid when
- You only need laws or draft laws without presidential action context.

## Inputs
- Time range.
- Decision topic or keyword.

## Outputs
- Decision list with date/title/link and optional detailed extraction from decision pages.

## Access reality statement
- Access type: `UI copy-only`.
- Verified on 2026-02-24.
- Site may present anti-bot/Cloudflare challenge to non-browser fetchers; browser workflow is the reliable path.

## Primary endpoints
- Estonian decisions page: https://www.president.ee/et/ametitegevus/otsused/
- English decisions page: https://www.president.ee/en/official-duties/decisions/

## Retrieval workflow (reproducible)
1. Open decisions page in a full browser session (not raw curl-only workflow).
2. Apply language and any available year/topic filters.
3. Capture list entries: title, date, and detail URL.
4. Open each selected detail page and extract decision type and text summary.
5. Return records with exact listing URL and detail URL provenance.

## Request/query contract
- No documented public API contract.
- Retrieval is page-based; browser-rendered session may be required due anti-bot protection.
- If network panel reveals JSON/payload calls, log endpoint URL and response type as metadata for that run.

## Output schema expectations
- `listing_url`
- `decision_date`
- `decision_title`
- `decision_url`
- `decision_type` (if inferable)
- `summary`
- `language`

## Limits and caveats
- Anti-bot challenge can block automated HTTP clients.
- Pagination/filter behavior may be JS-driven and require interactive browsing.
- Naming conventions differ across years and languages.

## Verification hooks
- `https://www.president.ee/et/ametitegevus/otsused/` is reachable in browser and serves the decision listing route.
- At least one decision detail URL should be captured per extraction run.
