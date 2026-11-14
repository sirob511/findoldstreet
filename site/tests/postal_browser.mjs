import {chromium,expect} from '@playwright/test';
import fs from 'node:fs';
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:390,height:844}});
const errors=[];page.on('pageerror',e=>errors.push(e.message));
const files=fs.readdirSync('data/sources').filter(f=>/^pass-\d+-additions\.json$/.test(f));
for(const file of files){
 const items=JSON.parse(fs.readFileSync('data/sources/'+file));
 const sample=items[0];
 await page.goto('http://localhost:4173/en/?q='+encodeURIComponent(sample.formerName+', '+sample.city));
 const link=page.locator(`a[href="/en/street/postal-ua-${sample.sourceStreetId}/"]`);
 await expect(link).toBeVisible();await link.click();
 await expect(page.locator('h1')).toContainText(sample.currentName);
 await expect(page.locator('.timeline')).toContainText('Date not recorded');
 await expect(page.locator('.timeline a')).toHaveAttribute('href',/index\.ukrposhta\.ua/);
 await expect(page.locator('input[type=search]')).toHaveCount(1);
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Mobile overflow: '+file);
}
await page.goto('http://localhost:4173/en/?q='+encodeURIComponent('Chervonohrad'));
await expect(page.locator('#resultgrid')).toContainText('Шептицький');
await page.locator('#resultgrid .detail-link').first().click();
await expect(page.locator('h1')).toContainText('Шептицький');
await expect(page.locator('.metadata')).toContainText('Львівська');
await expect(page.locator('.timeline')).toContainText('Date not recorded');
await expect(page.locator('.timeline a')).toHaveAttribute('href',/index\.ukrposhta\.ua/);
if(errors.length)throw Error(errors.join('\n'));
await browser.close();console.log('Postal search → detail → source flow passed for',files.length,'passes.');
