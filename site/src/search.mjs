export function normalize(s=''){return s.normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase().replace(/[ł]/g,'l').replace(/[đ]/g,'d').replace(/['’ʼ`]/g,'').replace(/[^\p{L}\p{N}]+/gu,' ').trim()}
const cityAliases={'Київ':['Kyiv','Kiev','Киев'],'Алматы':['Almaty','Alma Ata'],'Астана':['Astana','Nur Sultan','Нур Султан'],'Warszawa':['Warsaw'],'Hồ Chí Minh City':['Ho Chi Minh City','Saigon','Sài Gòn','TP HCM'],'Chennai':['Madras'],'New Delhi':['Delhi','नई दिल्ली'],'Durban':['eThekwini'],'Pretoria':['Tshwane']};
export function searchable(r){return normalize([r.formerName,r.currentName,...r.aliases,...r.transliterations,...r.events.flatMap(e=>[e.formerName,e.currentName]),r.city,r.district,...(cityAliases[r.city]||[])].join(' '))}
export function search(records,query='',city='',country=''){
 const tokens=normalize(query).split(' ').filter(t=>t&&!/^\d+[a-zа-я]?$/u.test(t)); const loc=normalize(city).split(' ').filter(Boolean);
 return records.filter(r=>r.status==='verified'&&(!country||r.country===country)&&tokens.every(t=>searchable(r).includes(t))&&loc.every(t=>normalize([r.city,r.district,...(cityAliases[r.city]||[])].join(' ')).includes(t))).sort((a,b)=>{
 const q=normalize(query);return Number(normalize(b.formerName)===q||normalize(b.currentName)===q)-Number(normalize(a.formerName)===q||normalize(a.currentName)===q)
 });
}
