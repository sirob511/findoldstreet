export function normalize(s = '') {
  return s.normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase().replace(/ł/g, 'l').replace(/đ/g, 'd').replace(/['’ʼ`]/g, '').replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
}
const cityAliases = {
  'Шымкент': ['Shymkent', 'Chimkent'], 'Львів': ['Lviv', 'Lvov'], 'Київ': ['Kyiv', 'Kiev', 'Киев'], 'Харків': ['Kharkiv', 'Kharkov', 'Харьков'], 'Одеса': ['Odesa', 'Odessa', 'Одесса'],
  'Алматы': ['Almaty', 'Alma Ata'], 'Астана': ['Astana', 'Nur Sultan', 'Нур Султан'], 'Warszawa': ['Warsaw'],
  'Hồ Chí Minh City': ['Ho Chi Minh City', 'Saigon', 'Sài Gòn', 'TP HCM'], 'Chennai': ['Madras'],
  'New Delhi': ['Delhi', 'नई दिल्ली'], 'Durban': ['eThekwini'], 'Pretoria': ['Tshwane'], 'Cape Town': ['Kaapstad', 'iKapa']
};
// Expand only unambiguous address abbreviations. "St" may mean Saint.
const abbreviations = {rd:'road', ave:'avenue', blvd:'boulevard', ln:'lane', dr:'drive', pushkinskaya:'pushkinska', пушкинская:'пушкінська', вул:'вулиця', пров:'провулок'};
const canonical = s => normalize(s).split(' ').map(t => abbreviations[t] || t).join(' ');
const countryNames={UZ:'Uzbekistan Oʻzbekiston Узбекистан',UA:'Ukraine Україна Украина',PL:'Poland Polska',ZA:'South Africa',VN:'Vietnam Việt Nam',KZ:'Kazakhstan Қазақстан Казахстан',IN:'India भारत',SZ:'Eswatini Swaziland',LK:"Sri Lanka",BJ:"Benin",BF:"Burkina Faso",CD:"Democratic Republic of the Congo",WS:"Samoa",TH:"Thailand",IR:"Iran",JO:"Jordan",SR:"Suriname",RO:"Romania",MM:"Myanmar",CV:"Cabo Verde",CI:"Côte d’Ivoire",TR:"Türkiye",TL:"Timor-Leste",KH:"Cambodia",CZ:"Czechia",MK:"North Macedonia",LS:"Lesotho",MW:"Malawi",BZ:"Belize",VU:"Vanuatu"};
const cache = new WeakMap();
export function locationNames(r) { return [r.city, r.district, ...(r.locationAliases || []), ...(cityAliases[r.city] || [])].filter(Boolean); }
function indexed(r) {
  if (!cache.has(r)) {
    const names = [r.formerName, r.currentName, ...(r.aliases || []), ...(r.transliterations || []), ...(r.events || []).flatMap(e => [e.formerName, e.currentName])];
    cache.set(r, {names: names.map(canonical), text: canonical([...names, ...locationNames(r), countryNames[r.country] || r.country].join(' ')), location: canonical(locationNames(r).join(' '))});
  }
  return cache.get(r);
}
export function searchable(r) { return indexed(r).text; }
export function search(records, query = '', city = '', country = '') {
  const q = canonical(query), tokens = q.split(' ').filter(Boolean), loc = canonical(city).split(' ').filter(Boolean);
  const candidates = records.filter(r => r.status === 'verified' && (!country || r.country === country) && loc.every(t => indexed(r).location.includes(t)));
  const match = words => candidates.filter(r => words.every(t => { const text=indexed(r).text; return /^\d+$/.test(t) ? text.split(' ').includes(t) : t==='st' ? ['street','saint','st'].some(v=>text.split(' ').includes(v)) : text.includes(t); }));
  let results = match(tokens);
  // Preserve numbered street names first. Only retry a failed address without a leading house number.
  if (!results.length && tokens.length > 1 && /^\d+[a-zа-я]?$/u.test(tokens[0])) results = match(tokens.slice(1));
  return results.sort((a, b) => Number(indexed(b).names.includes(q)) - Number(indexed(a).names.includes(q)));
}
