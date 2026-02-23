---
name: weather-data
description: Query Estonian Weather Service XML feeds for forecast and observation data usable in time-series and impact analysis.
---

# Estonia Weather Data

## Use when
- You need weather observations or forecast feeds from official service.
- You need weather covariates for demand, transport, or health models.

## Avoid when
- You need climate normals that are not available in feed endpoints.

## Inputs
- Feed type (forecast/observations), stations/locations, period.

## Outputs
- Parsed weather dataset with timestamps and variable schema.

## Primary endpoints
- Forecast XML: https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php
- Observations XML: https://www.ilmateenistus.ee/ilma_andmed/xml/observations.php

## Workflow
1. Pull required XML feed.
2. Parse timestamps, station/location fields, and numeric variables.
3. Convert units/timezones consistently.
4. Return tidy tabular output.

## Human setup (when needed)
- Usually none.

## Quality checks
- Handle missing station readings safely.
- Document timezone assumptions explicitly.
