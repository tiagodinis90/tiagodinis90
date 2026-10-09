import unittest
from funding_check import check
C={'call_id':'SYNTHETIC','official_url':'https://commission.europa.eu/page','deadline':'2026-11-01T17:00:00+01:00','minimum_organisations':3,'permitted_roles':['beneficiary'],'required_evidence':['doc']}
A={'consortium_organisations':3,'applicant_role':'beneficiary','evidence_documents':{'doc':'test'}}
NOW='2026-10-09T12:00:00+01:00'
class FundingTests(unittest.TestCase):
    def test_checks_pass_but_no_eligibility(self):self.assertEqual(check(C,A,NOW)['status'],'CHECKS_PASSED_NOT_ELIGIBILITY')
    def test_expired(self):self.assertEqual(check(C,A,'2027-01-01T12:00:00+01:00')['status'],'FAIL')
    def test_no_date_zone(self):
        with self.assertRaises(ValueError):check(C,A,'2026-10-09T12:00:00')
    def test_missing_doc_unknown(self):self.assertEqual(check(C,{**A,'evidence_documents':{}},NOW)['status'],'NEEDS_REVIEW')
    def test_insufficient_consortium(self):self.assertEqual(check(C,{**A,'consortium_organisations':2},NOW)['status'],'FAIL')
    def test_wrong_role(self):self.assertEqual(check(C,{**A,'applicant_role':'observer'},NOW)['status'],'FAIL')
    def test_invalid_source(self):
        with self.assertRaises(ValueError):check({**C,'official_url':'file:///etc/passwd'},A,NOW)
