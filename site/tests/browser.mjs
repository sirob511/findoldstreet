import {chromium} from '@playwright/test';
import fs from 'node:fs';
const browser=await chromium.launch({headless:true});
const errors=[];const page=await browser.newPage({viewport:{width:1440,height:1000}});page.on('pageerror',e=>errors.push(e.message));
await page.goto('http://localhost:4173/en/');await page.waitForTimeout(700);await page.screenshot({path:'/tmp/findoldstreet-desktop.png',fullPage:true});
await page.locator('#query').fill('Smith Street');await page.locator('#searchform').evaluate(f=>f.requestSubmit());await page.waitForTimeout(200);
if(!await page.locator('#resultgrid').innerText().then(t=>t.includes('Anton Lembede')))throw Error('Search failed');
await page.locator('.names').first().click();await page.waitForLoadState();if(!await page.locator('h1').innerText().then(t=>t.includes('Anton Lembede')))throw Error('Detail failed');
await page.selectOption('#locale','uk');await page.waitForLoadState();if(await page.locator('html').getAttribute('lang')!=='uk')throw Error('Locale failed');
await page.setViewportSize({width:390,height:844});await page.goto('http://localhost:4173/en/');await page.screenshot({path:'/tmp/findoldstreet-mobile.png',fullPage:true});
for(const locale of ['en','uk','ru','pl','vi','zu','kk','hi','mr','bn','ta']){
 await page.goto(`http://localhost:4173/${locale}/`);
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Overflow '+locale);
}
console.log(JSON.stringify({desktopSearch:true,detail:true,localeSwitch:true,mobileLocales:11,errors}));await browser.close();
