import {search,cityComparison} from './search.mjs';
const locale=document.documentElement.lang||'en';
document.querySelector('#locale')?.addEventListener('change',e=>{const parts=location.pathname.split('/');if(parts[1]===locale)parts[1]=e.target.value;else parts.splice(1,0,e.target.value);location.href=parts.join('/')+location.search+location.hash});
const share=document.querySelector('#copylink');
if(share){share.hidden=false;share.addEventListener('click',async()=>{const status=document.querySelector('#copystatus');try{await navigator.clipboard.writeText(location.href);status.textContent=share.dataset.copied}catch{status.textContent=share.dataset.failed}})}
const form=document.querySelector('#searchform');
if(form){
 const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 try{
 const [records,translations]=await Promise.all([fetch('/records.json').then(r=>{if(!r.ok)throw Error('Data unavailable');return r.json()}),fetch('/i18n.json').then(r=>{if(!r.ok)throw Error('Translations unavailable');return r.json()})]);
 const t=translations[locale],query=document.querySelector('#query'),grid=document.querySelector('#resultgrid');
 const results=document.querySelector('#results'),choices=document.querySelector('#locations');
 let country='',selectedLocation='',limit=12,matched=[],timer;
 const locationKey=r=>JSON.stringify([r.country,r.city,r.district||'']);
 const row=r=>{
  const city=cityComparison(records,r,query.value);
  const locality=city?(city.former===city.current?city.current:`${city.former} → ${city.current}`):'';
  const type=r.sourceStreetId&&!/^(?:вулиця|вул\.?|провулок|пров\.?|проспект|просп\.?|пр-т|бульвар|бул\.?|площа|пл\.?|узвіз|тупик|проїзд|шосе|набережна|наб\.?|дорога|в[’'ʼ]їзд)\s/iu.test(r.formerName)?r.streetType:'';
  return `<article class="answer-row"><div><div class="answer-names"><div class="answer-before"><span class="sr-only">${esc(t.old)}: </span>${esc(r.formerName)}</div><span class="answer-arrow" aria-hidden="true">→</span><div class="answer-after"><span class="sr-only">${esc(t.current)}: </span><strong>${esc(r.currentName)}</strong></div></div><p class="answer-location">${esc([locality,t.countryNames[r.country]].filter(Boolean).join(' · '))}${r.segment?' · '+esc(t.partial):''}${type?` <span class="answer-type" title="${esc(t.typeContext)}">${esc(t.recordedType)}: ${esc(type)}</span>`:''}</p></div><a class="detail-link" aria-label="${esc(t.detail+': '+r.formerName+' → '+r.currentName)}" href="/${locale}/${r.kind?'place':'street'}/${encodeURIComponent(r.id)}/">${esc(t.detail)} <span aria-hidden="true">↗</span></a></article>`;
 };

 function render(){
  const visible=selectedLocation?matched.filter(r=>locationKey(r)===selectedLocation):matched;
  grid.innerHTML=visible.slice(0,limit).map(row).join('');
  document.querySelector('#empty').hidden=visible.length>0;
  document.querySelector('#more').hidden=limit>=visible.length;
  document.querySelector('#resultcount').textContent=`(${visible.length})${country?' · '+(t.countryNames[country]||country):''}`;
  document.querySelector('#clear').hidden=!(query.value||country);
  choices.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.location===selectedLocation)));
 }
 function run(update=true){
  clearTimeout(timer);limit=12;
  const active=Boolean(query.value.trim()||country);results.hidden=!active;document.querySelector('.lookup-hero').classList.toggle('has-results',active);
  matched=active?search(records,query.value,'',country):[];
  const locations=[...new Map(matched.filter(r=>!r.kind).map(r=>[locationKey(r),r])).entries()];
  document.querySelector('#disambiguation').hidden=locations.length<2;
  choices.replaceChildren();
  if(locations.length>1){
   for(const [key,label] of [['',t.allLocations],...locations.map(([key,r])=>[key,[r.city,r.district,t.countryNames[r.country]].filter(Boolean).join(' · ')])]){
    const b=document.createElement('button');b.type='button';b.className='chip';b.dataset.location=key;b.textContent=label;
    b.addEventListener('click',()=>{selectedLocation=key;limit=12;render();saveUrl()});choices.append(b);
   }
  }
  render();if(update)saveUrl();
 }
 function saveUrl(){const p=new URLSearchParams();if(query.value.trim())p.set('q',query.value.trim());if(country)p.set('country',country);if(selectedLocation)p.set('location',selectedLocation);history.replaceState({},'',location.pathname+(p.size?'?'+p:''))}
 query.addEventListener('input',()=>{selectedLocation='';clearTimeout(timer);timer=setTimeout(run,180)});
 form.addEventListener('submit',e=>{e.preventDefault();run();if(!results.hidden)results.scrollIntoView({block:'start'})});
 document.querySelectorAll('[data-query]').forEach(b=>b.addEventListener('click',()=>{query.value=b.dataset.query;country='';selectedLocation='';run();results.scrollIntoView({block:'start'})}));
 document.querySelector('#more').addEventListener('click',()=>{limit+=12;render()});
 document.querySelector('#clear').addEventListener('click',()=>{query.value='';country='';selectedLocation='';run();query.focus()});
 function restore(){const p=new URLSearchParams(location.search);query.value=[p.get('q'),p.get('city')].filter(Boolean).join(', ');country=p.get('country')||'';selectedLocation=p.get('location')||'';run(false)}
 restore();window.addEventListener('popstate',restore);
 }catch(error){const note=document.createElement('p');note.className='error';note.setAttribute('role','alert');note.textContent=translationsFallback(locale);form.after(note);form.querySelector('button[type=submit]').disabled=true;console.error(error)}
}
function translationsFallback(l){return ({en:'Search data could not load. Please reload the page.',uk:'Не вдалося завантажити дані. Оновіть сторінку.',ru:'Не удалось загрузить данные. Обновите страницу.'})[l]}
