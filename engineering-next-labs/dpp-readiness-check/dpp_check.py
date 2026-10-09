"""Schema-driven DPP data completeness check, not legal compliance assessment."""
import argparse, json
from pathlib import Path
from urllib.parse import urlsplit


def check(record,schema):
    if not isinstance(record,dict) or not isinstance(schema,dict):raise ValueError('expected JSON objects')
    if schema.get('schema_id') is None or schema.get('schema_version') is None:raise ValueError('versioned schema required')
    rules=schema.get('fields')
    if not isinstance(rules,list) or not rules:raise ValueError('fields required')
    found=set();results=[]
    for rule in rules:
        field=rule['key'];required=rule['required']
        if not isinstance(required,bool) or field in found:raise ValueError('invalid or duplicate rule')
        found.add(field)
        raw=record.get(field)
        present=raw is not None and (not isinstance(raw,str) or bool(raw.strip()))
        status='PRESENT' if present else ('MISSING_REQUIRED' if required else 'MISSING_OPTIONAL')
        if present and rule.get('type')=='string' and (not isinstance(raw,str) or not raw.strip()):status='WRONG_TYPE'
        if present and rule.get('type')=='number' and (not isinstance(raw,(int,float)) or isinstance(raw,bool)):status='WRONG_TYPE'
        if present and rule.get('type')=='array' and not isinstance(raw,list):status='WRONG_TYPE'
        if present and status=='PRESENT' and rule.get('evidence_required'):
            evidence=record.get('evidence',{}).get(field) if isinstance(record.get('evidence'),dict) else None
            if not isinstance(evidence,dict) or not isinstance(evidence.get('source_url'),str) or urlsplit(evidence['source_url']).scheme!='https' or not urlsplit(evidence['source_url']).netloc:
                status='MISSING_EVIDENCE'
        results.append({'field':field,'status':status,'required':required})
    fail=any(r['required'] and r['status']!='PRESENT' for r in results)
    return {'schema_id':schema['schema_id'],'schema_version':schema['schema_version'],'screening_status':'INCOMPLETE' if fail else 'READY_FOR_REVIEW','checks':results,'warning':'Not an EU Digital Product Passport conformity assessment'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('record',type=Path);ap.add_argument('schema',type=Path);a=ap.parse_args()
    print(json.dumps(check(json.loads(a.record.read_text(encoding='utf8')),json.loads(a.schema.read_text(encoding='utf8'))),indent=2))
if __name__=='__main__':main()
