---
name: analyzing-estonia-political-party-membership
description: Analyze Estonian political party membership trends using official Business Register party statistics and related public records.
---

# Political Party Membership Analysis

## Use when
- You need party membership trend context by party and period.
- You need official organization-level party statistics.

## Avoid when
- You need campaign finance flows (use ERJK funding skill).

## Inputs
- Party scope and analysis period.

## Outputs
- Membership trend dataset and summary indicators.

## Primary endpoint
- Party statistics page: https://ariregister.rik.ee/eng/statistics/political_parties

## Workflow
1. Retrieve party statistics for selected periods.
2. Extract membership-related fields.
3. Harmonize party naming and period labels.
4. Return trend-ready table and interpretation notes.

## Human setup (when needed)
- If tables require manual download, walk user through exact clicks and continue from exported file.

## Quality checks
- Preserve official party identifiers where available.
- Clearly mark whether counts are point-in-time or annual summaries.
