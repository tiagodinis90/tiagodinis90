"""Transcribed-call preflight; UNKNOWN for absent evidence, no official eligibility verdict."""
import argparse, json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

def parse_dt(s):
    if not isinstance(s,str):raise ValueError('timestamp must be string')
    d=datetime.fromisoformat(s.replace('Z','+00:00'))
    if d.tzinfo is None or d.utcoffset() is None:raise ValueError('explicit timezone required')
    return d

def check(call,applicant,now):
    if not isinstance(call,dict) or not isinstance(applicant,dict):raise ValueError('expected objects')
    u=urlsplit(call['official_url'])
    if u.scheme!='https' or not u.hostname:raise ValueError('official URL required')
    deadline=parse_dt(call['deadline'])
    date=parse_dt(now) if isinstance(now,str) else now
    if date.tzinfo is None:raise ValueError('timezone required')
    results=[{'criterion':'deadline','status':'FAIL' if date>deadline else 'PASS','source':call['official_url']}]
    n=applicant.get('consortium_organisations')
    if n is None: s='UNKNOWN'
    elif isinstance(n,bool) or not isinstance(n,int) or n<0:raise ValueError('consortium size must be nonnegative integer')
    else:s='PASS' if n>=call['minimum_organisations'] else 'FAIL'
    results.append({'criterion':'minimum_organisations','status':s,'source':call['official_url']})
    role=applicant.get('applicant_role')
    results.append({'criterion':'applicant_role','status':'UNKNOWN' if role is None else ('PASS' if role in call['permitted_roles'] else 'FAIL'),'source':call['official_url']})
    docs=applicant.get('evidence_documents')
    for doc in call['required_evidence']:
        results.append({'criterion':'evidence:'+doc,'status':'UNKNOWN' if not isinstance(docs,dict) or doc not in docs else ('PASS' if isinstance(docs[doc],str) and docs[doc].strip() else 'FAIL'),'source':call['official_url']})
    status='FAIL' if any(r['status']=='FAIL' for r in results) else ('NEEDS_REVIEW' if any(r['status']=='UNKNOWN' for r in results) else 'CHECKS_PASSED_NOT_ELIGIBILITY')
    return {'call_id':call['call_id'],'status':status,'checks':results,'warning':'Human review of current call document and General Annexes required; no grant eligibility determined.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('call',type=Path);p.add_argument('applicant',type=Path);p.add_argument('--as-of',required=True);a=p.parse_args()
    print(json.dumps(check(json.loads(a.call.read_text(encoding='utf8')),json.loads(a.applicant.read_text(encoding='utf8')),a.as_of),indent=2))
if __name__=='__main__':main()
