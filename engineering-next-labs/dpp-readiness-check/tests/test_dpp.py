import unittest
from dpp_check import check
S={'schema_id':'test','schema_version':'1','fields':[{'key':'id','required':True,'type':'string','evidence_required':True},{'key':'optional','required':False,'type':'string'}]}
class DPPTests(unittest.TestCase):
    def test_present_evidence(self):self.assertEqual(check({'id':'p1','evidence':{'id':{'source_url':'https://example.org/x'}}},S)['screening_status'],'READY_FOR_REVIEW')
    def test_missing_evidence(self):self.assertEqual(check({'id':'p1'},S)['checks'][0]['status'],'MISSING_EVIDENCE')
    def test_missing_required(self):self.assertEqual(check({},S)['screening_status'],'INCOMPLETE')
    def test_optional_missing(self):self.assertEqual(check({'id':'x','evidence':{'id':{'source_url':'https://a.b'}}},S)['checks'][1]['status'],'MISSING_OPTIONAL')
    def test_false_not_string(self):self.assertEqual(check({'id':False},S)['checks'][0]['status'],'WRONG_TYPE')
    def test_duplicate_schema_rule(self):
        with self.assertRaises(ValueError):check({},dict(S,fields=S['fields']*2))
    def test_bad_scheme(self):self.assertEqual(check({'id':'x','evidence':{'id':{'source_url':'javascript:alert(1)'}}},S)['checks'][0]['status'],'MISSING_EVIDENCE')
