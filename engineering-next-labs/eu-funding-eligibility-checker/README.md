# EU Funding Eligibility Checker

An evidence-aware checklist for an **operator-transcribed** EU funding call. Evaluates deadline, organisation role, consortium size and declared documents, without determining eligibility.

Run:

    python funding_check.py examples/call.synthetic.json examples/applicant.synthetic.json --as-of 2026-10-09T12:00:00+01:00
    python -m unittest discover -s tests -v

The demonstration call is invented. The EU Funding & Tenders Portal and applicable official call documents are authoritative. See [Method and limitations](docs/METHOD.md).

Official context: https://commission.europa.eu/funding-and-tenders/how-apply/application-process_en
