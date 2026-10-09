# Engineering Next-Labs (temporary source home)

Three small Python projects whose individual GitHub repositories could not yet be created because GitHub temporarily rate-limited repository creation. The complete runnable sources are collected in separate directories here. Once GitHub permits new repositories, each can move to its own repository without changing imports or the command-line interface.

- [DPP Readiness Check](dpp-readiness-check/) — versioned synthetic information schema, missing fields and evidence
- [EU Funding Eligibility Checker](eu-funding-eligibility-checker/) — an operator-transcribed, evidence-aware call checklist
- [Scientific Results Reproduction](scientific-results-reproduction/) — Anscombe quartet means, linear regression and SVG output

All examples except the published Anscombe dataset are synthetic. None of the tools certifies compliance, funding eligibility or industrial safety.

Run the tests from each project's own directory:

    python -m unittest discover -s tests -v

The original standalone layout is retained. The GitHub Actions workflow in the profile repo runs the tests for all three.
