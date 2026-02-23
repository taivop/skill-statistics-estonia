---
name: using-estonia-geospatial-open-data
description: Use Land and Spatial Board geospatial open data services for maps, cadastral, and address-linked analysis in Estonia.
---

# Estonia Geospatial Open Data

## Use when
- You need base maps, cadastral context, or map-service layers.
- You need interoperable geospatial services (WMS/WFS/WMTS).

## Avoid when
- You only need non-spatial time series indicators.

## Inputs
- Area of interest (address, municipality, coordinates, polygon).
- Required layer/theme and output format.

## Outputs
- Layer/service URLs.
- Retrieved geospatial dataset or map extract.

## Primary endpoints
- Geoportal: https://geoportaal.maaamet.ee/eng/
- Public services index: https://geoportaal.maaamet.ee/eng/services/public-wms-wfs-p346.html

## Workflow
1. Open the public services page and select the right layer family.
2. Use GetCapabilities endpoint listed there to discover exact layers.
3. Query layer subset by bbox/filter.
4. Export in a reusable format and document CRS/projection.

## Human setup (when needed)
- If a map layer requires manual portal selection, instruct the user exactly which layer to enable and where to copy the service URL.

## Quality checks
- Always report CRS and geometry type.
- Check if layer is authoritative or contextual.
