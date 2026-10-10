# Tiago Dinis

**Portfolio website:** [View selected environmental engineering and LCA projects](https://tiagodinis.vercel.app)

**Environmental Engineer & Systems Developer**

Chemical and environmental engineer based in Portugal, with an MSc in Chemical and Biochemical Engineering from FCT NOVA (NOVA University Lisbon). I worked as a Technical Product Specialist at One Click LCA, maintaining LCA software configurations, moving data structures from JSON to TypeScript and testing calculation behaviour across versions.

My technical interests are life cycle assessment, environmental data provenance, scientific software and reproducible calculations.

## Selected case studies

Two short, publicly readable case studies explain the methods, implemented work and limitations behind the ongoing larger projects. The application repositories remain private; these are **not claims of released source code**.

- **[Almada environmental evidence](case-studies/almada-environmental-evidence.md)** — official CAOP2025 geography, derived COSc2024 land cover, source lineage and a separately reproducible 2023–2024 waste-indicator analysis.
- **[LCA computation and provenance](case-studies/lca-calculation-and-provenance.md)** — calculation boundaries, functional equivalence, EPD comparison and inspectable validation examples.

## Engineering work

Most environmental projects are still under active development and are not presented as finished or independently validated software.

- **STRATA LCA** (private): experiments with LCA calculation structures, data modelling, benchmarking and validation.
- **Almada Urban Metabolism** (private): territorial indicators, land-cover data and the distinction between official, derived, estimated and simulated evidence.
- **LCA Data Provenance** (private): research tooling for traceability and reproducibility of environmental data; not an EPD certification tool.

## Engineering micro-labs

Six small, tested Python CLIs for mass and energy balances, EPD module comparison, hourly energy data, EUR-Lex text changes, measurement uncertainty and industrial sensor data quality.

Start with **[Process Balance Checker](https://github.com/tiagodinis90/process-balance-checker)** and **[Measurement Uncertainty Lab](https://github.com/tiagodinis90/measurement-uncertainty-lab)** for examples of engineering calculations with explicit assumptions and tests.

See [all six micro-labs, their scope and limitations](ENGINEERING_MICRO_LABS.md). All bundled datasets are synthetic.

## Applied engineering prototypes

These small Python exercises focus on engineering calculations and configuration quality:

- **[Configuration Migration Validator](https://github.com/tiagodinis90/configuration-migration-validator)**: catch unexpected changes while migrating configuration data.
- **[Industrial Heat Electrification](https://github.com/tiagodinis90/industrial-heat-electrification)**: compare gas-fired, electric and heat-pump heat supply under explicit assumptions.
- **[Industrial Water Reuse Screener](https://github.com/tiagodinis90/industrial-water-reuse-screener)**: check mixing and water-quality constraints for an illustrative reuse case.

They are screening and test exercises, not validated operational engineering tools.

### Additional engineering labs

Three further Python projects are available together in [Engineering Next-Labs](engineering-next-labs/): DPP record completeness, EU funding-call preflight and reproduction of Anscombe's quartet. They include tests, method notes and sample data. This shared location is temporary until each can have its own repository.

## Public technical prototypes

- **[qwencoder](https://github.com/tiagodinis90/qwencoder)**: a deterministic provenance-verification prototype.
- **[Job Search Agent](https://github.com/tiagodinis90/job-search-agent-prototype)**: a local-first Python prototype for evidence-aware vacancy discovery, scoring and offline approval simulation. No real emails or applications are sent.
- **[Agent Control Plane](https://github.com/tiagodinis90/agent-control-plane)**: experimental infrastructure for coordinating local tooling.

These are prototypes with documented boundaries rather than production services.

## Other experiments

I also build narrative games as a way to explore state machines, branching dialogue, navigation and research-driven storytelling. They are **separate from my environmental engineering portfolio**.

The two public experiments, COSMOS (Alexander von Humboldt) and KIRIFUSHI, are listed and explained in [Creative experiments](CREATIVE_EXPERIMENTS.md). Neither is presented as a finished game.

## Background

**Environmental engineering:** LCA, EPD workflows, carbon data, environmental assessment and physical-system modelling.

**Software:** TypeScript, JavaScript, Python, React, JSON/data modelling, testing and debugging.

[LinkedIn](https://www.linkedin.com/in/tiagotdinis90/)

## Research publications: Almada, material flows and political ecology

[**Almada 2026 — public working papers and socioecological theory notebook**](publications/almada-2026/README.md) brings together a reproducible municipal-waste indicator comparison (2023–2024), research protocols on policy observability, cultural-building reuse and material sufficiency, and a clearly identified personal political-ecology notebook. These are independent working papers and essays, **not peer-reviewed research** or party publications. The evidence register notes important discrepancies between waste accounting sources.
