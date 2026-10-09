# Method and interpretation

The data file contains four groups of eleven published point pairs from Anscombe's 1973 paper, also distributed as the R dataset anscombe.

For each group compute the means, ordinary least-squares b = sum[(x - mean x)(y - mean y)] / sum[(x - mean x)^2], intercept a = mean y - b * mean x and R^2 from centered sums.

All four regressions yield approximately intercept 3, slope 0.5, R^2 0.666 and mean y 7.5. The generated SVG illustrates why equal-looking summary statistics do not imply the same data shape.

Sources: https://doi.org/10.1080/00031305.1973.10478966 and https://search.r-project.org/R/refmans/datasets/help/anscombe.html
