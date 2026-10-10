# Almada environmental evidence: geography, land cover and municipal waste

**Independent engineering case study · October 2026 · Work in progress**

## Question

How can environmental decisions for Almada be grounded in geographical data and reproducible municipal indicators without treating simulated dashboards, official records and derived calculations as interchangeable evidence?

## Work completed

- **Administrative geography:** processed the Portuguese DGT **CAOP2025** boundary data for Almada and its five freguesias. The working prototype supports geographic selection and documents source versions, projected-area calculations and display-geometry limitations.
- **Land cover:** implemented a freguesia-level analysis from **DGT COSc2024**. Land-cover shares are *derived from a classified raster*, not independent measurements of vegetation health, heat exposure or environmental benefit.
- **Provenance rules:** separated **Official**, **Derived**, **Estimated** and **Simulated** values, with unavailable indicators left blank rather than inferred.
- **Waste observability:** separately published a reproducible working paper transcribing and analysing 2023–2024 operator indicators. A 54-entry dataset covers nine municipalities, three reported series and two years; the source/accounting perimeters still need reconciliation.

The geographic dashboard implementation is currently developed in a **private repository**. This page reports scope and methods; it is not a link to publicly inspectable source code for that application. The municipal-waste analysis and its script **are already public**.

## Public evidence to inspect

- [Working paper WP01: municipal waste observability, 2023–2024](../publications/almada-2026/municipal-evidence/WP01-waste-observability.md)
- [Waste input dataset (CSV)](../publications/almada-2026/municipal-evidence/data/amarsul-2023-2024.csv)
- [Reproducible analysis script](../publications/almada-2026/municipal-evidence/scripts/amarsul-summary.mjs)
- [Sources and limitations](../publications/almada-2026/SOURCES_AND_LIMITATIONS.md)
- [DGT CAOP administrative geography](https://www.dgterritorio.gov.pt/atividades/cartografia/cartografia-tematica/caop?language=pt)
- [DGT land-cover information](https://www.dgterritorio.gov.pt/)

To reproduce the public waste analysis from the root of this profile repository:

```bash
node publications/almada-2026/municipal-evidence/scripts/amarsul-summary.mjs
node --test publications/almada-2026/municipal-evidence/scripts/amarsul-summary.test.mjs
```

## What this does **not** establish

- The dashboard's waste KPIs and scenarios use **synthetic values**. They are not Almada measurements.
- The geographic layer does not itself establish cooling, flooding, biodiversity or energy savings.
- The waste series are operator-reported indicators, not a municipal recycling rate or a closed material-flow balance. They require reconciliation with other reporting systems.
- The working paper is **not peer-reviewed**; the dashboard is not an independently validated environmental assessment or commissioned municipal study.

## Next verifiable milestone

A public, reproducible snapshot of the geography/land-cover pipeline, with attribution, licence review, provenance manifests, regression tests and a clearly identified demonstration interface. Operational waste, thermal and building-stock analyses should be added only after suitable original sources have been reconciled.

**Portfolio framing:** environmental data engineering, geospatial processing, provenance-aware visualisation, reproducible research and municipal decision-support methods.
