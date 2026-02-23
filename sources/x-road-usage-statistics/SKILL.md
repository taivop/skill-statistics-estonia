---
name: x-road-usage-statistics
description: Query X-Road facts and figures for digital government interoperability usage metrics and cross-system transaction context.
---

# X-Road Usage Statistics

## Use when
- You need official X-Road usage and interoperability metrics.
- You need digital-state transaction volume context.

## Avoid when
- You need system-level architecture details for a specific RIHA entry.

## Inputs
- Period and metric scope (transactions, members, services).

## Outputs
- X-Road usage metrics table with periodized indicators.

## Primary endpoints
- Facts and figures: https://x-tee.ee/facts-and-figures/

## Workflow
1. Retrieve published X-Road metric snapshots.
2. Extract values, units, and period references.
3. Normalize metric labels for time-series use.
4. Return structured statistics with citation links.

## Human setup (when needed)
- If values are embedded in charts without direct API export, guide user to capture/download chart data and continue from provided files.

## Quality checks
- Keep unit and period exactly as published.
- Mark estimated/rounded values explicitly.
