import {search,locationNames} from './search.mjs';
const locale=document.documentElement.lang||'en';
document.querySelector('#locale')?.addEventListener('change',e=>{const parts=location.pathname.split('/');if(parts[1]===locale)parts[1]=e.target.value;else parts.splice(1,0,e.target.value);location.href=parts.join('/')+location.search+location.hash});
const share=document.querySelector('#copylink');
if(share){share.hidden=false;share.addEventListener('click',async()=>{const status=document.querySelector('#copystatus');try{await navigator.clipboard.writeText(location.href);status.textContent=share.dataset.copied}catch{status.textContent=share.dataset.failed}})}
const form=document.querySelector('#searchform');
if(form){
 const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 try{
 const [records,translations]=await Promise.all([fetch('/records.json').then(r=>{if(!r.ok)throw Error('Data unavailable');return r.json()}),fetch('/i18n.json').then(r=>r.json())]);
 const t=translations[locale];const query=document.querySelector('#query'),city=document.querySelector('#city'),grid=document.querySelector('#resultgrid');
 let country='',limit=12,matched=[],timer;
 const cityOptions=document.querySelector('#cities');
 function updateCities(){cityOptions.replaceChildren(...[...new Set(records.filter(r=>r.status==='verified'&&(!country||r.country===country)).flatMap(r=>locationNames(r)))].sort((a,b)=>a.localeCompare(b,locale)).map(name=>{const option=document.createElement('option');option.value=name;return option}))}
 updateCities();
 for(const input of [query,city])input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(()=>run(),180)});
 const countryNames=translations.en.countryNames;
 const card=r=>`<article class="card"><div class="cardloc"><span class="countrydot">${r.country}</span>${esc(r.city)}${r.segment?`<span class="badge">${esc(t.partial)}</span>`:''}</div><a class="names" href="/${locale}/street/${r.id}/" aria-label="${esc(t.detail)}: ${esc(r.formerName)}"><span class="label">${esc(t.old)}</span><div class="oldname">${esc(r.formerName)}</div><div class="name-arrow">↓</div><span class="label">${esc(t.current)}</span><div class="currentname">${esc(r.currentName)}</div></a>${r.district?`<span class="district">${esc(r.district)}</span>`:''}<div class="cardbottom"><span class="checked">✓ ${esc(t.verified)}</span><a class="maplink" href="https://www.openstreetmap.org/search?query=${encodeURIComponent([r.currentName,r.city,countryNames[r.country]].join(', '))}" target="_blank" rel="noopener">${esc(t.map)} ↗</a></div></article>`;
 function render(){grid.innerHTML=matched.slice(0,limit).map(card).join('');document.querySelector('#empty').hidden=matched.length>0;document.querySelector('#more').hidden=limit>=matched.length;document.querySelector('#resultcount').textContent=`(${matched.length})`;document.querySelector('#clear').hidden=!(query.value||city.value||country)}
 function run(update=true){clearTimeout(timer);limit=12;matched=search(records,query.value,city.value,country);render();document.querySelectorAll('[data-country]').forEach(b=>{b.classList.toggle('active',b.dataset.country===country);b.setAttribute('aria-pressed',String(b.dataset.country===country))});if(update){const p=new URLSearchParams();if(query.value)p.set('q',query.value);if(city.value)p.set('city',city.value);if(country)p.set('country',country);history.replaceState({},'',location.pathname+(p.size?'?'+p:'')+'#results')}}
 form.addEventListener('submit',e=>{e.preventDefault();run();document.querySelector('#results').scrollIntoView({block:'start'})});
 document.querySelectorAll('[data-country]').forEach(b=>b.addEventListener('click',()=>{country=b.dataset.country;updateCities();run()}));
 document.querySelectorAll('[data-query]').forEach(b=>b.addEventListener('click',()=>{query.value=b.dataset.query;city.value=b.dataset.city;country='';run();document.querySelector('#results').scrollIntoView({block:'start'})}));
 document.querySelector('#more').addEventListener('click',()=>{limit+=12;render()});
 document.querySelector('#clear').addEventListener('click',()=>{query.value='';city.value='';country='';updateCities();run();query.focus()});
 const p=new URLSearchParams(location.search);query.value=p.get('q')||'';city.value=p.get('city')||'';country=p.get('country')||'';
 updateCities();run(false);
 window.addEventListener('popstate',()=>{const p=new URLSearchParams(location.search);query.value=p.get('q')||'';city.value=p.get('city')||'';country=p.get('country')||'';updateCities();run(false)});
 }catch(error){const note=document.createElement('p');note.className='error';note.textContent=translationsFallback(locale);form.after(note);form.querySelector('button[type=submit]').disabled=true;console.error(error)}
}
function translationsFallback(l){return ({en:'Search data could not load. Please reload the page.',uk:'Не вдалося завантажити дані. Оновіть сторінку.',ru:'Не удалось загрузить данные. Обновите страницу.',pl:'Nie udało się wczytać danych. Odśwież stronę.',vi:'Không tải được dữ liệu. Vui lòng tải lại trang.',kk:'Деректер жүктелмеді. Бетті жаңартыңыз.',hi:'डेटा लोड नहीं हुआ। पृष्ठ फिर लोड करें।',zu:'Idatha ayilayishwanga. Vuselela ikhasi.',ta:'தரவை ஏற்ற முடியவில்லை. பக்கத்தை மீண்டும் ஏற்றவும்.',mr:'माहिती लोड झाली नाही. पृष्ठ पुन्हा उघडा.',bn:'তথ্য লোড হয়নি। পাতা আবার খুলুন।'})[l]}
