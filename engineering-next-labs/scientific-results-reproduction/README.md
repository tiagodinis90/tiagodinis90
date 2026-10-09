# Scientific Results Reproduction

Reproduce the sample means and least-squares regression of **Anscombe's quartet**, using the published 1973 data table. An optional SVG plot visualizes the four very different datasets.

Run:

    python reproduce.py data/anscombe.csv --svg results/anscombe.svg
    python -m unittest discover -s tests -v

This is a reproduction of a historical statistics example, not new scientific research. The published data are rounded, so coefficients may differ slightly from textbook approximations.

References: Anscombe (1973) https://doi.org/10.1080/00031305.1973.10478966 and R documentation https://search.r-project.org/R/refmans/datasets/help/anscombe.html

See [Method and interpretation](docs/METHOD.md).
