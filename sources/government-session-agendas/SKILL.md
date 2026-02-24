---
name: government-session-agendas
description: Track Estonian government session agenda publications and related operational updates from valitsus.ee.
---

# Government Session Agendas

## Use when
- You need cabinet session agenda publications and related updates.
- You need chronology of session communications.

## Avoid when
- You need formal legal text of adopted acts.

## Inputs
- Date range and topic keywords.

## Outputs
- Session agenda publication list with dates and links.

## Primary endpoints
- Search seed (agenda keyword): https://valitsus.ee/otsing?filters%5Btype%5D=Uudis&filters%5Bkeyword%5D=Istungi%20p%C3%A4evakord&sort=created&page=1
- Main portal: https://valitsus.ee/en

## Workflow
1. Start from agenda-keyword search.
2. Collect matching publications with dates and titles.
3. Open item pages for links to related materials.
4. Return timeline of agenda publications.

## Human setup (when needed)
- If language/UI ambiguity blocks extraction, ask user to open the target publication in browser and share URL; then continue.

## Quality checks
- Separate agenda announcements from post-meeting communications.
- Preserve publication timestamps exactly.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://valitsus.ee/otsing?filters%5Btype%5D=Uudis&filters%5Bkeyword%5D=Istungi%20p%C3%A4evakord&sort=created&page=1 (HTTP 200, text/html;, file links detected: 1)
- https://valitsus.ee/en (HTTP 200, text/html;, file links detected: 1)

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
