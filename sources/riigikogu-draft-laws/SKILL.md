---
name: riigikogu-draft-laws
description: Track Riigikogu draft laws and proceedings status from the parliamentary draft-law portal.
---

# Riigikogu Draft Laws Tracker

## Use when
- You need bill-level progress in parliament.
- You need linked materials (initiators, committee stage, readings).

## Avoid when
- You need voting-level machine API records (use Riigikogu open data API skill).

## Inputs
- Draft number, title, sponsor, or date range.

## Outputs
- Bill status summary and action timeline.

## Primary endpoint
- Draft laws page: https://www.riigikogu.ee/tegevus/eelnoud/

## Workflow
1. Find bill by number/title.
2. Capture stage, committee references, and event dates.
3. Collect linked documents and related proceedings entries.
4. Return machine-friendly status table.

## Human setup (when needed)
- If bill details require manual filtering in UI, walk user through exact filters and ask for target bill URL.

## Quality checks
- Preserve original bill identifiers.
- Distinguish initiated, in process, and concluded statuses.
