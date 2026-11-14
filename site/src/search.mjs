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
const countryNames={MD:'Moldova Молдова',EE:'Estonia Eesti Эстония Естонія',LT:'Lithuania Lietuva Литва',UZ:'Uzbekistan Oʻzbekiston Узбекистан',UA:'Ukraine Україна Украина',PL:'Poland Polska',ZA:'South Africa',VN:'Vietnam Việt Nam',KZ:'Kazakhstan Қазақстан Казахстан',IN:'India भारत',SZ:'Eswatini Swaziland',LK:"Sri Lanka",BJ:"Benin",BF:"Burkina Faso",CD:"Democratic Republic of the Congo",WS:"Samoa",TH:"Thailand",IR:"Iran",JO:"Jordan",SR:"Suriname",RO:"Romania",MM:"Myanmar",CV:"Cabo Verde",CI:"Côte d’Ivoire",TR:"Türkiye",TL:"Timor-Leste",KH:"Cambodia",CZ:"Czechia",MK:"North Macedonia",LS:"Lesotho",MW:"Malawi",BZ:"Belize",VU:"Vanuatu"};
const cache = new WeakMap();
export function locationNames(r) { return [r.city, r.district, ...(r.locationAliases || []), ...(cityAliases[r.city] || [])].filter(Boolean); }
function indexed(r) {
  if (!cache.has(r)) {
    const names = [r.formerName, r.currentName, ...(r.aliases || []), ...(r.transliterations || []), ...(r.events || []).flatMap(e => [e.formerName, e.currentName])];
    cache.set(r, {names: names.map(canonical), text: canonical([...names, ...locationNames(r), countryNames[r.country] || r.country].join(' ')), location: canonical(locationNames(r).join(' '))});
  }
  return cache.get(r);
}
// Resolve historic city spellings from verified city records, scoped by country.
// Cache per dataset so one dataset cannot leak aliases into another.
const datasetCache = new WeakMap();
function datasetIndex(records) {
  if (datasetCache.has(records)) return datasetCache.get(records);
  const cities = records.filter(r => r.kind === 'city' && r.status === 'verified');
  const byLocation = new Map();
  for (const city of cities) {
    for (const name of [city.city, city.currentName]) {
      const key = city.country + ':' + canonical(name);
      if (!byLocation.has(key)) byLocation.set(key, new Set());
      byLocation.get(key).add(city);
    }
  }
  const result = new Map(records.map(r => {
    const matches = new Set();
    if (!r.kind || r.kind === 'street') {
      for (const name of [r.city, ...(r.locationAliases || []), ...(cityAliases[r.city] || [])]) {
        const found = byLocation.get(r.country + ':' + canonical(name));
        // A shared locality name is insufficient to identify a city.
        if (found?.size === 1) matches.add([...found][0]);
      }
    }
    const aliases = matches.size === 1 ? indexed([...matches][0]).names.join(' ') : '';
    const base = indexed(r);
    return [r, {...base, text: base.text + ' ' + aliases, location: base.location + ' ' + aliases}];
  }));
  datasetCache.set(records, result);
  return result;
}
export function searchable(r) { return indexed(r).text; }
export function search(records, query = '', city = '', country = '') {
  const index = datasetIndex(records);
  const q = canonical(query), tokens = q.split(' ').filter(Boolean), loc = canonical(city).split(' ').filter(Boolean);
  const candidates = records.filter(r => r.status === 'verified' && (!country || r.country === country) && loc.every(t => index.get(r).location.includes(t)));
  const match = words => candidates.filter(r => words.every(t => { const text=index.get(r).text; return /^\d+$/.test(t) ? text.split(' ').includes(t) : t==='st' ? ['street','saint','st'].some(v=>text.split(' ').includes(v)) : text.includes(t); }));
  let results = match(tokens);
  // Preserve numbered street names first. Only retry a failed address without a leading house number.
  if (!results.length && tokens.length > 1 && /^\d+[a-zа-я]?$/u.test(tokens[0])) results = match(tokens.slice(1));
  return results.sort((a, b) => Number(indexed(b).names.includes(q)) - Number(indexed(a).names.includes(q)));
}
