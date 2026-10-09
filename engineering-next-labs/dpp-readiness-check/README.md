# DPP Readiness Check

Check completeness and evidence metadata in a product record against an **illustrative, versioned** schema. This is not a validated industrial or legal system; the sample inputs are synthetic.

Run:

    python dpp_check.py examples/product.synthetic.json examples/schema.synthetic.json
    python -m unittest discover -s tests -v

This does not certify compliance with the Ecodesign for Sustainable Products Regulation. Product-specific requirements need the applicable delegated acts.

Context: https://eur-lex.europa.eu/eli/reg/2024/1781/oj/eng
See [Method and limitations](docs/METHOD.md).
