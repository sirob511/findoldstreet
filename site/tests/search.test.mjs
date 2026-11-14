import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {search,normalize} from '../src/search.mjs';
const countries=['UA','PL','ZA','VN','KZ','IN','international','places'];const all=countries.flatMap(c=>JSON.parse(fs.readFileSync(new URL('../data/'+c+'.json',import.meta.url))));
test('exact old-name lookup in each country',()=>{for(const [q,c,target] of [['Горького','UA','Антоновича'],['Lecha Kaczyńskiego','PL','Armii Ludowej'],['Smith Street','ZA','Anton Lembede'],['Xa lộ Hà Nội','VN','Võ Nguyên Giáp'],['Юрия Гагарина','KZ','Серкебаева'],['Aurangzeb Road','IN','Abdul Kalam']])assert.ok(search(all,q,'',c).some(r=>r.currentName.includes(target)),c)});
test('accentless, generated transliteration, city alias, partial address',()=>{assert.ok(search(all,'Xa lo Ha Noi','Saigon').length);assert.ok(search(all,'Horkoho','Kyiv').length);assert.ok(search(all,'123 Smith Street','eThekwini').length);assert.ok(search(all,'Lecha Kaczynskiego','Warsaw').length)});
test('Warsaw reversal remains chronological and latest name restored',()=>{const r=search(all,'Lecha Kaczyńskiego','Warsaw')[0];assert.equal(r.currentName,'Aleja Armii Ludowej');assert.equal(r.events.length,2);assert.equal(r.events[1].status,'reversal');assert.equal(r.events[1].date,'2018-12-07')});
test('real multiple rename plus reversal has three events',()=>{const r=all.find(r=>r.country==='PL'&&r.events.length===3);assert.ok(r);assert.equal(r.events.at(-1).currentName,r.currentName);assert.equal(r.events.at(-1).date,'2019-08-03')});
test('same former name in distinct Almaty districts stays separate',()=>{const rr=search(all,'улица Абай','','KZ').filter(r=>r.formerName==='улица Абай');assert.ok(rr.length>=2);assert.ok(new Set(rr.map(r=>r.district)).size>=2);assert.equal(new Set(rr.map(r=>r.id)).size,rr.length)});
test('partial renames retain scope and never claim house-number carryover',()=>{for(const c of ['KZ','VN']){const r=all.find(r=>r.country===c&&r.segment&&r.status==='verified');assert.ok(r.segment.length>25);assert.equal(r.houseNumbersVerified,false);assert.equal(r.geometry,null)}});
test('stable identifiers are unique; review records never searchable',()=>{assert.equal(new Set(all.map(r=>r.id)).size,all.length);const r=all.find(r=>r.status==='review');assert.ok(r);assert.ok(!search(all,r.formerName).some(x=>x.id===r.id));for(const r of all)assert.ok(r.events.every(e=>e.sourceUrl&&e.locator))});
test('locale dictionaries complete',()=>{const t=JSON.parse(fs.readFileSync(new URL('../src/i18n.json',import.meta.url)));const keys=Object.keys(t.en).sort();assert.equal(Object.keys(t).length,11);for(const [l,d] of Object.entries(t))assert.deepEqual(Object.keys(d).sort(),keys,l)});

test('numbered names remain distinct and house-number fallback stays street-level',()=>{
 const make=(id,name)=>({id,formerName:name,currentName:name,city:'Example',country:'ZA',status:'verified',events:[],aliases:[],transliterations:[]});
 const rows=[make('a','1 May Street'),make('b','2 May Street'),make('c','Smith Road')];
 assert.deepEqual(search(rows,'1 May Street').map(r=>r.id),['a']);
 assert.deepEqual(search(rows,'123 Smith Rd').map(r=>r.id),['c']);
 assert.equal(search(rows,'999').length,0);
 assert.deepEqual(search(rows,'123 Smith Rd, South Africa').map(r=>r.id),['c']);
 assert.deepEqual(search(rows,'1 May St').map(r=>r.id),['a']);
 assert.equal(search(rows,'Smith Rd','Wrong City').length,0);
});

test('one box searches streets, cities and countries',()=>{
 assert.ok(search(all,'Pushkinskaya, Kyiv').some(r=>r.id==='abf6965f2ba96b57'));
 assert.ok(search(all,'Dnipropetrovsk').some(r=>r.kind==='city'&&r.currentName==='Dnipro'));
 assert.ok(search(all,'Дніпропетровськ').some(r=>r.currentName==='Dnipro'));
 assert.ok(search(all,'Swaziland').some(r=>r.kind==='country'&&r.currentName==='Eswatini'));
 assert.ok(search(all,'Eswatini').some(r=>r.formerName==='Swaziland'));
 assert.ok(search(all,'123 Smith Street, Durban').some(r=>r.currentName.includes('Anton Lembede')));
});

test('expanded city and country coverage works in the shared box',()=>{
 for(const [q,target] of [['Ceylon','Sri Lanka'],['Siam','Thailand'],['Bangalore','Bengaluru'],['Nur-Sultan','Астана'],['Madras','Chennai'],['Allahabad','Prayagraj'],['Léopoldville, Democratic Republic of the Congo','Kinshasa']]){
  assert.ok(search(all,q).some(r=>r.currentName===target),q);
 }
 const ambiguous=search(all,'Артемівськ').filter(r=>r.kind==='city');
 assert.equal(ambiguous.length,2);
 assert.equal(new Set(ambiguous.map(r=>r.district)).size,2);
 assert.ok(search(all,'Shymkent').length>=171);
 assert.ok(search(all,'Drohobych').length>0);
});


test('postal snapshot mappings support one-box locality searches without invented dates',()=>{
 const r=search(all,'Брюллова, Dnipro').find(r=>r.id==='postal-ua-166995');
 assert.ok(r);assert.equal(r.currentName,'провулок Бойчуківський');
 assert.equal(r.events[0].date,null);assert.equal(r.events[0].datePrecision,'unknown');
});


test('newly renamed cities use the same search and preserve their region',()=>{
 for(const [q,name] of [['Новомосковськ','Самар'],['Chervonohrad','Шептицький'],['Южне','Південне']]) {
  const r=search(all,q).find(r=>r.kind==='city'&&r.currentName===name);
  assert.ok(r,q);assert.equal(r.events[0].date,null);assert.ok(r.district.includes('область'));
 }
});

test('international source pairs work in the single box with locality aliases',()=>{
 const international=all.filter(r=>r.coveragePass);
 for(const pass of new Set(international.map(r=>r.coveragePass))){
  const group=international.filter(r=>r.coveragePass===pass);
  for(const r of [group[0],group.at(-1)]){
   const city=r.locationAliases?.[0]||r.city;
   assert.ok(search(all,`${r.formerName}, ${city}`,'',r.country).some(x=>x.id===r.id),`${pass}: ${r.formerName}`);
  }
 }
});

test('historic city names qualify a street in the same box',()=>{
 for(const city of ['Днепропетровск','Дніпропетровськ','Dnipropetrovsk','Dnipro']){
  assert.ok(search(all,`Проспект Карла Маркса ${city}`).some(r=>r.currentName==='проспект Дмитра Яворницького'),city);
 }
 assert.ok(search(all,'Проспект Карла Маркса','Днепропетровск').some(r=>r.currentName==='проспект Дмитра Яворницького'));
 assert.ok(!search(all,'Проспект Карла Маркса Warsaw').some(r=>r.currentName==='проспект Дмитра Яворницького'));
 assert.ok(!search(all,'Проспект Карла Маркса Днепропетровск','','PL').length);
 assert.equal(search(all,'Днепропетровск')[0].id,'city-dnipro');
});

test('city aliases do not cross countries or leak across datasets',()=>{
 const street={id:'s',formerName:'Old Road',currentName:'New Road',city:'Newtown',country:'UA',status:'verified'};
 const city={id:'c',kind:'city',formerName:'Oldtown',currentName:'Newtown',city:'Newtown',country:'UA',status:'verified'};
 assert.equal(search([street,city],'Old Road Oldtown').length,1);
 assert.equal(search([street],'Old Road Oldtown').length,0);
 assert.equal(search([{...street,country:'PL'},city],'Old Road Oldtown').length,0);
 assert.equal(search([street,city,{...city,id:'c2',district:'Other district'}],'Old Road Oldtown').length,0);
});
