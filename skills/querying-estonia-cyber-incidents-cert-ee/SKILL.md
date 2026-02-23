---
name: querying-estonia-cyber-incidents-cert-ee
description: Query CERT-EE public incident-handling and cyber situation resources for operational cybersecurity governance context.
---

# CERT-EE Incident Context

## Use when
- You need public cybersecurity incident and response context.
- You need national cyber governance operational references.

## Avoid when
- You need confidential incident data not publicly released.

## Inputs
- Topic, incident type, period.

## Outputs
- Public CERT-EE references, advisories, and incident-context records.

## Primary endpoint
- CERT-EE section: https://www.ria.ee/en/cyber-security/handling-cyber-incidents-cert-ee

## Workflow
1. Locate relevant CERT-EE pages and advisories.
2. Extract publication dates, incident categories, and guidance links.
3. Normalize into timeline/context dataset.
4. Return references with caveats on public scope.

## Human setup (when needed)
- If incident details are only in downloadable advisories, guide user to fetch files and continue from them.

## Quality checks
- Distinguish incidents, advisories, and procedural guidance.
- Record publication date and source URL for each item.
