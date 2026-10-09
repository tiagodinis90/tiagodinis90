# Engineering Micro-Labs

Small, independent Python programs exploring engineering calculations and data quality. Each repository includes a command-line interface, synthetic example data, unit tests, GitHub Actions checks and an MIT license.

They are **teaching and portfolio prototypes**, not validated industrial software, compliance tools or substitutes for engineering review. Their synthetic examples should not be treated as real measurements or published EPD results.

| Project | What it checks | Limits |
| --- | --- | --- |
| [Process Balance Checker](https://github.com/tiagodinis90/process-balance-checker) | Non-reactive steady-state mass, component and sensible-heat consistency | Not a process simulator; requires defined system boundaries |
| [EPD Module Comparator](https://github.com/tiagodinis90/epd-module-comparator) | Module-by-module comparison of manually entered impact indicators | Requires checked PCR, functional equivalence and declared units; not an EPD parser or verification service |
| [Energy Profile Analyser](https://github.com/tiagodinis90/energy-profile-analyser) | Hourly consumption profiles, peak/load features, missing timestamps and optional emissions | Results depend on complete interval data and appropriate emission factors |
| [EU Regulation Change Tracker](https://github.com/tiagodinis90/eu-regulation-change-tracker) | Reproducible snapshots and text diffs of legal content | Text changes are not automatically amendments or legal obligations |
| [Measurement Uncertainty Lab](https://github.com/tiagodinis90/measurement-uncertainty-lab) | Analytical first-order propagation versus seeded Monte Carlo | Assumes independent inputs and supported expressions; nonlinearity may invalidate the first-order result |
| [Industrial Sensor Audit](https://github.com/tiagodinis90/industrial-sensor-audit) | Gaps, out-of-range readings, sudden changes and reference discrepancies | Rule-based data-quality checks, not sensor certification or predictive maintenance |

## How to review

Clone an individual repository, run the example command in its README, then execute the tests:

```bash
python -m unittest discover -s tests -v
```

The tools intentionally use Python's standard library and keep calculations inspectable. Read the test cases and limitations before reusing any output for real engineering decisions.

[Back to the main profile](README.md)
