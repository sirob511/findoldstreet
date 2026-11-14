import {chromium,expect} from '@playwright/test';
import fs from 'node:fs';
const records=JSON.parse(fs.readFileSync('data/international.json'));
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:390,height:844}});
const errors=[];page.on('pageerror',e=>errors.push(e.message));
for(const pass of new Set(records.map(r=>r.coveragePass))){
 const sample=records.find(r=>r.coveragePass===pass);
 await page.goto('http://localhost:4173/en/?q='+encodeURIComponent(sample.formerName+', '+(sample.locationAliases?.[0]||sample.city)));
 const link=page.locator(`a[href="/en/street/${sample.id}/"]`);
 await expect(link).toBeVisible();await link.click();
 await expect(page.locator('h1')).toContainText(sample.currentName);
 await expect(page.locator('.timeline a').first()).toHaveAttribute('href',sample.sources[0].url);
 await expect(page.locator('input[type=search]')).toHaveCount(1);
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Mobile overflow: pass '+pass);
}
if(errors.length)throw Error(errors.join('\n'));
await browser.close();console.log('International single-box search → answer → source flows passed.');
