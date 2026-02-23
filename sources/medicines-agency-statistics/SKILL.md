---
name: medicines-agency-statistics
description: Use State Agency of Medicines statistical yearbooks for medicines market, pharmacy, and regulatory activity indicators.
---

# Medicines Agency Statistics

## Use when
- You need medicines/pharmacy statistics from the medicines agency.
- You need annual regulatory/market context indicators.

## Avoid when
- You need individual medicine record lookup only.

## Inputs
- Year range and thematic section.

## Outputs
- Structured yearbook indicators and trend tables.

## Primary endpoints
- Statistical yearbooks: https://www.ravimiamet.ee/en/statistics/statistical-yearbooks

## Workflow
1. Retrieve yearbook(s) for selected years.
2. Extract relevant indicator tables.
3. Normalize category labels across editions.
4. Return dataset and definitions metadata.

## Human setup (when needed)
- If content is PDF-based, guide user through file retrieval and continue from tables.

## Quality checks
- Track edition year and section source.
- Keep supply, utilization, and regulatory indicators distinct.
