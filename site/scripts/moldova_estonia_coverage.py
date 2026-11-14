"""Conservative PDF-cell and renamed-street-list imports for Chișinău and Tallinn."""
import collections,json,re
import pymupdf
from bs4 import BeautifulSoup
from international_coverage import S,clean,norm,save

def guide_key(name,kind):return kind,tuple(sorted(norm(name).split()))
def guide_inventory(doc):
    inventory=collections.defaultdict(set)
    for number in range(327,337):
        text=doc[number].get_text()
        for m in re.finditer(r'(?m)^([^\n]+?), (strada|stradela|bulevardul|piața|șoseaua)\s+(\d+)',text):
            inventory[guide_key(m[1],m[2])].add(m[1])
        for m in re.finditer(r'(?m)^(Calea [^\n]+?)\s+(\d+)\s*$',text):
            inventory[guide_key(m[1],'strada')].add(m[1])
    return inventory

def destination_key(name):
    kind='strada'
    if name.endswith(', str-la'):name=name.removesuffix(', str-la');kind='stradela'
    elif name.endswith(', bd.'):name=name.removesuffix(', bd.');kind='bulevardul'
    elif name.startswith('Piața '):name=name.removeprefix('Piața ');kind='piața'
    return guide_key(name,kind)

def chisinau():
    out=[];doc=pymupdf.open(S/'chisinau-library-guide.pdf');inventory=guide_inventory(doc)
    for number in range(338,352):
        page=doc[number];tables=sorted(page.find_tables().tables,key=lambda t:t.bbox[0])
        assert len(tables)==2 and all(t.col_count==2 for t in tables),(number,len(tables))
        for column,table in enumerate(tables):
            for i,row in enumerate(table.rows[1:],1):
                c=[clean(page.get_text('text',clip=pymupdf.Rect(cell))) if cell else '' for cell in row.cells]
                old,new=c
                r=dict(country='MD',city='Chișinău',formerName=old,currentName=new,source='chisinau-library-guide',locator=f'Printed page {number} (PDF page {number+1}), {"left" if column==0 else "right"} old/new table, data row {i}',evidencePage=number,evidenceTable=column,evidenceRow=i,evidenceBoxes=row.cells,sourceCells=c,locationAliases=['Chisinau','Kishinev','Кишинёв'],language='ru' if re.search('[А-Яа-я]',old) else 'ro',script='Cyrillic' if re.search('[А-Яа-я]',old) else 'Latin',streetType=destination_key(new)[0],nameNote='Pair documented by the 2017 Chișinău municipal-library guide. The destination also matches that guide’s current-name index, allowing for surname-first ordering. Later renames and present-day geometry have not been verified; no effective date or house-number continuity is inferred.')
                if len(inventory.get(destination_key(new),set()))!=1:r['holdReason']='Destination does not uniquely match the guide’s current street-name index'
                if any(x in old+' '+new for x in ['(',')',';','?']) or re.search('separat|porțiun',old+' '+new,re.I):r['holdReason']='Dated, partial, split or annotated name requires manual historical reconciliation'
                out.append(r)
    return out

def tallinn_inventory():
    soup=BeautifulSoup((S/'tallinn-eki-names.html').read_bytes(),'html.parser');inventory={}
    last=None
    for line in soup.select('pre')[1].get_text().splitlines():
        if line.startswith(' '*25) and last and line.strip():
            inventory[last]+=' '+line.strip()
            continue
        cells=re.split(r'\s{2,}',line.strip())
        if len(cells)==2:
            last=cells[0];inventory[last]=cells[1]
    return inventory

def tallinn_pairs():
    # The source uses optional closing tags for DT/DD; isolate each pair before HTML parsing.
    raw=(S/'tallinn-eki-renames.html').read_bytes().decode('utf-8')
    block=re.search(r'<dl>(.*?)</dl>',raw,re.I|re.S)[1]
    return [(clean(BeautifulSoup(a,'html.parser').get_text(' ',strip=True)),clean(BeautifulSoup(b,'html.parser').get_text(' ',strip=True))) for a,b in re.findall(r'<dt>(.*?)<dd>(.*?)(?=<dt>|$)',block,re.I|re.S)]

def tallinn():
    out=[];inventory=tallinn_inventory()
    for i,(heading,previous) in enumerate(tallinn_pairs()):
        new=re.split(r'\s*\[|\s+[A-ZÕÄÖÜ](?:,[A-ZÕÄÖÜ])?-[A-ZÕÄÖÜ]',heading,maxsplit=1)[0].strip()
        old=clean(re.sub(r'\[[^\]]*\]','',previous))
        r=dict(country='EE',city='Tallinn',district=inventory.get(new),formerName=old,currentName=new,source='tallinn-eki-renames',locator=f'Section 1A (renamed streets, arranged by new name), entry {i+1}',evidenceRow=i,sourceCells=[heading,previous],extraSources=['tallinn-eki-names'],locationAliases=['Tallinn','Reval','Таллин'],language='et',script='Latin',nameNote='Documented rename in the Institute of the Estonian Language’s 2018 Tallinn snapshot. The destination matches its street-name inventory. Partial renames and abolished/new-only names are excluded. Decision dates are not treated as effective dates; later changes and geometry remain unverified.')
        dates=re.findall(r'(\d{2})\.(\d{2})\.(\d{4})',heading.split('{')[0])
        if dates:
            day,month,year=dates[-1];r['decisionDate']=f'{year}-{month}-{day}'
        effective=re.search(r'jõustus (\d{2})\.(\d{2})\.(\d{4})',heading)
        if effective:r.update(date=f'{effective[3]}-{effective[2]}-{effective[1]}',datePrecision='day')
        if new not in inventory:r['holdReason']='Destination absent from the source street inventory'
        if re.search(r'\bosa\b|[;{}()]',old) or not re.search(r' (tn|tee|põik|puiestee|plats|maantee)$',old):r['holdReason']='Partial, combined or non-street former name'
        out.append(r)
    return out
if __name__=='__main__':
    save(10,chisinau()+tallinn(),'Chișinău, Moldova and Tallinn, Estonia: municipal-library name tables and EKI documented renames')
