# LCA calculation workflows and environmental-data provenance

**Independent technical case study · October 2026 · Experimental software**

## Engineering problem

Life-cycle assessment (LCA) software needs to represent declared units, system boundaries, material and energy flows, impact factors, and versions of source data. Even when a calculation is repeatable, that does not prove its environmental interpretation is correct.

## Work in progress: STRATA LCA

STRATA is a **private, experimental repository** investigating browser-based LCA workspaces, calculation structures, persisted records, supplier and product information, and reproducible evaluation workflows. Work under review includes comparisons across LCA engines, handling explicit functional units and tracking the provenance of inputs and transformations.

This is a description of engineering work, **not** a claim of independent scientific validation, full ISO 14040/44 conformity, EN 15804+A2 certification, or production readiness. Private implementation details and third-party/licensed datasets are not published here.

## Inspectable public example: EPD Module Comparator

[EPD Module Comparator](https://github.com/tiagodinis90/epd-module-comparator) is a deliberately narrow, tested Python command-line tool.

- Reads **manually transcribed** indicator values from JSON records.
- Checks declared units, PCR/version and metadata required for the comparison.
- Requires a documented operator review of functional equivalence.
- Reports per-module differences; **module D remains separate**, rather than being silently netted against product life-cycle stages.
- Detects missing modules and avoids undefined relative percentages with a zero baseline.

Its bundled records are **synthetic**, and its checks do not make it an EPD parser, an impact-assessment engine or a verification service.

Run the public example after cloning the tool:

```bash
python epd_compare.py examples/epd_a.synthetic.json examples/epd_b.synthetic.json --indicator GWP-total
python -m unittest discover -s tests -v
```

## A second public example: measurement uncertainty

[Measurement Uncertainty Lab](https://github.com/tiagodinis90/measurement-uncertainty-lab) compares first-order analytical uncertainty propagation with seeded Monte Carlo samples. It uses a restricted expression evaluator and explicit assumptions; correlated inputs and full GUM conformity are out of scope.

## Design principles demonstrated

1. **Make the comparison target explicit:** indicator, module, declared unit, methodological version and functional equivalence.
2. **Separate computational integrity from environmental validity:** a consistent output hash or passing unit test is not proof of a sound life-cycle model.
3. **Make negative tests visible:** reject incompatible inputs rather than silently producing an impressive number.
4. **Trace assumptions:** synthetic fixtures and missing dataset coverage must stay identifiable.

## What would make STRATA ready for a public technical release

A reviewed, licence-safe subset of its calculation and provenance code; documented fixture provenance; runnable cross-engine regression tests; a clear functional-unit contract; a concise reproducibility guide; and an explicit account of unresolved upstream database, methodology and compliance questions.

**Portfolio framing:** TypeScript/Python, scientific software validation, environmental product data, LCA computation and reproducibility.
