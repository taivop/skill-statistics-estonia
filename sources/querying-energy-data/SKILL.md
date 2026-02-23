---
name: querying-energy-data
description: Query Elering dashboard API for Estonia electricity and system data, including market and balance time series.
---

# Estonia Energy Data (Elering)

## Use when
- You need near-real-time electricity system and market series.
- You need energy context for macro, climate, or operations analysis.

## Avoid when
- You need only annual energy aggregates from statistical yearbooks.

## Inputs
- Start/end timestamps (ISO UTC).
- Data family (price, system balance, production/consumption).

## Outputs
- Time-series JSON extract with harmonized timestamps.

## Primary endpoints
- Dashboard: https://dashboard.elering.ee/
- NPS price API: `https://dashboard.elering.ee/api/nps/price?start=...&end=...`
- System with plan API: `https://dashboard.elering.ee/api/system/with-plan?start=...&end=...`

## Workflow
1. Choose relevant endpoint and set UTC time window.
2. Fetch JSON and parse the `data` object by region/series.
3. Convert timestamps consistently and document timezone handling.
4. Return cleaned series and missing-data notes.

## Human setup (when needed)
- Usually none.

## Quality checks
- Validate interval consistency (e.g., 15-minute or hourly).
- Flag daylight-saving boundaries and missing points.
