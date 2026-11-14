"""Extract historical labels from captured museum-backed Brno street profiles."""
import json,re
from bs4 import BeautifulSoup
from international_coverage import S,clean,save

def brno_index():
    index={}
    for p in sorted(S.glob('brno-index-*.json')):
        soup=BeautifulSoup(' '.join(json.loads(p.read_text())['html'].values()),'html.parser')
        for a in soup.select('a.card-link'):
            sid=a['href'].split('load=')[-1]
            index[sid]=dict(name=clean(a.get_text()),abolished='ulice zrušena' in a.parent.get_text(' ',strip=True),source=p.stem)
    return index

def profile(sid):
    soup=BeautifulSoup((S/f'brno-profile-{sid}.html').read_bytes(),'html.parser')
    title=clean(soup.select_one('h2.mb-4.mt-4').get_text())
    fields={b.select_one('h5').get_text(strip=True):b for b in soup.select('.attr-block') if b.select_one('h5')}
    district=clean(fields['katastr'].select_one('p').get_text()) if 'katastr' in fields else None
    history=[]
    for p in fields['historický vývoj'].select('p'):
        label=p.select_one('a,b')
        if label:history.append(dict(label=clean(label.get_text()),text=clean(p.get_text()),linked=label.name=='a'))
    return title,district,history

def main():
    out=[]
    for sid,index in brno_index().items():
        path=S/f'brno-profile-{sid}.html'
        if not path.exists():continue
        new,district,history=profile(sid)
        for i,event in enumerate(history):
            old=event['label']
            r=dict(country='CZ',city='Brno',district=district,formerName=old,currentName=new,source=f'brno-profile-{sid}',locator=f'Historical development (historický vývoj), entry {i+1}',evidenceRow=i,sourceHistory=history,extraSources=[index['source']],locationAliases=['Brno','Brünn'],language='cs',script='Latin',nameNote='The museum-backed Encyclopedia of Brno links this historical label to the current street profile. Cadastral districts are retained. Dates in that profile describe the full name history; no direct old-to-current effective date or unchanged historical boundary is inferred.')
            if index['abolished']:r['holdReason']='Street explicitly marked abolished in source index'
            elif index['name']!=new or not history or history[-1]['label']!=new:r['holdReason']='Profile title, index or latest historical label disagree'
            elif not district:r['holdReason']='Missing cadastral locality'
            elif old=='Samoty':r['holdReason']='Isolated-house settlement label requires boundary reconciliation'
            elif any(x in old for x in [' - ',' – ',' — ','(',')','/',';','+',',',' část',' též ',' nebo ']):r['holdReason']='Combined bilingual or annotated historical label'
            out.append(r)
    save(9,out,'Brno, Czechia: museum-backed street histories, current-index checks and abolished-street exclusions')
if __name__=='__main__':main()
