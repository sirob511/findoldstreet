"""Record the net addition against the previous root-repository commit."""
import json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=R/'data';number=int(sys.argv[1])
files=['UA','PL','ZA','VN','KZ','IN','international','places']
before=[];after=[]
for f in files:
    result=subprocess.run(['git','show',f'HEAD:site/data/{f}.json'],cwd=R.parent,capture_output=True,text=True)
    if result.returncode==0:before+=json.loads(result.stdout)
    after+=json.loads((D/(f+'.json')).read_text())
old={r['id'] for r in before if r['status']=='verified'};new={r['id'] for r in after if r['status']=='verified'}
assert old<=new,'Existing published records removed'
review=json.loads((D/f'sources/international-pass-{number}-review.json').read_text())
assert len(new-old)==review['approved'],(len(new-old),review['approved'])
p=D/'coverage-passes.json';passes=json.loads(p.read_text());assert not any(x['passNumber']==number for x in passes)
passes.append(dict(passNumber=number,target=500,newPublishedRecords=len(new-old),totalPublishedRecords=len(new),scope=review['scope'],heldCandidates=review['held'],sourceReview=f'data/sources/international-pass-{number}-review.json',validation=['Source hash and exact-pair checks','Search regression tests','Static build and SEO checks']))
p.write_text(json.dumps(passes,ensure_ascii=False,indent=2)+'\n');print(passes[-1])
