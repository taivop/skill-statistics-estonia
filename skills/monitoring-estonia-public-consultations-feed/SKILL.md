---
name: monitoring-estonia-public-consultations-feed
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
