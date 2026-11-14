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
await page.goto('http://localhost:4173/en/');
await page.waitForFunction(()=>document.querySelector('#cities').options.length>0);
await page.locator('#query').fill('123 Smith Street');
await page.waitForFunction(()=>document.querySelector('#resultgrid').textContent.includes('Anton Lembede') && document.querySelectorAll('#resultgrid .card').length>1);
await page.locator('#city').fill('Durban');
await page.waitForFunction(()=>document.querySelector('#resultgrid').textContent.includes('Anton Lembede') && document.querySelectorAll('#resultgrid .card').length===1);
if(!(await page.locator('#resultcount').innerText()).includes('1'))throw Error('Live result count failed');
if(!await page.locator('footer a[href="https://oddlogic.ai"]').isVisible())throw Error('Footer credit missing');
await page.locator('#query').fill('not-a-real-street-xyz');
await page.locator('#empty').waitFor({state:'visible'});
if(!await page.locator('#empty a[href="/en/coverage/"]').isVisible())throw Error('Empty-result guidance missing');
await page.locator('#clear').click();
if(await page.locator('#query').inputValue())throw Error('Clear failed');
if(errors.length)throw Error(errors.join('\n'));
console.log(JSON.stringify({desktopSearch:true,detail:true,localeSwitch:true,mobileLocales:11,errors}));await browser.close();
