const {chromium}=require('/Users/woosyume/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');const out='/Users/woosyume/Documents/apps/jikyuchan-docs/docs/product-redesign';
(async()=>{
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});const report=[];
 for(const width of [320,390,768,1280,1920]){
  const context=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1,reducedMotion:'reduce'});const page=await context.newPage();const errors=[];
  page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
  await page.goto('http://127.0.0.1:4175/',{waitUntil:'networkidle'});
  await page.evaluate(async()=>{const images=[...document.images];images.forEach(i=>i.loading='eager');await Promise.all(images.map(i=>i.complete?Promise.resolve():new Promise(r=>{i.onload=r;i.onerror=r})));});
  const checks=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overflows:[...document.querySelectorAll('main *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+1||r.left< -1)}).map(e=>({tag:e.tagName,class:e.className})),screens:[...document.querySelectorAll('figure img')].filter(e=>e.getBoundingClientRect().width).map(e=>({src:e.src.split('/').pop(),width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})),responsiveImages:[...document.querySelectorAll('img[srcset]')].map(e=>({src:e.src.split('/').pop(),current:e.currentSrc.split('/').pop()})),cta:[...document.querySelectorAll('main [data-store]')].map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})),canonical:document.querySelector('[rel=canonical]').href}));
  if(width<=700){await page.locator('.menu-toggle').click();if(!await page.locator('#navigation').isVisible())errors.push('Menu open failed');await page.locator('#navigation a').first().click();if(await page.locator('#navigation').isVisible())errors.push('Menu close failed');}
  await page.locator('.hero [data-store]').click();if(!await page.locator('#store-dialog').isVisible())errors.push('CTA failed');await page.keyboard.press('Escape');if(await page.locator('#store-dialog').isVisible())errors.push('Escape failed');
  await page.locator('.final-cta [data-store]').click();if(!await page.locator('#store-dialog').isVisible())errors.push('Final CTA failed');await page.locator('#store-dialog .dialog-close').click();
  await page.locator('#faq summary').first().click();if(await page.locator('#faq details').first().getAttribute('open')===null)errors.push('FAQ failed');
  await page.locator('.privacy-story a').click();if(new URL(page.url()).hash!=='#privacy')errors.push('Privacy link failed');
  if(width<=700){await page.locator('.mobile-home summary').click();if(!await page.locator('.mobile-home figure').isVisible())errors.push('Mobile Home disclosure failed');await page.locator('.mobile-home summary').click();}
  await page.emulateMedia({reducedMotion:'reduce'});await page.evaluate(async()=>{document.activeElement?.blur();await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
  const total=await page.evaluate(()=>document.documentElement.scrollHeight);for(let y=0;y<total;y+=800){await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(35);}
  await page.evaluate(()=>window.scrollTo({top:0,behavior:'instant'}));await page.waitForTimeout(300);checks.captureScrollY=await page.evaluate(()=>scrollY);
  await page.screenshot({path:`${out}/preview-${width}.png`,fullPage:true});
  if(width===390||width===1280){for(const name of ['hero','deposit-section','price-section','choice-section','summary-section','discovery-section','goal-section']) await page.locator('.'+name).screenshot({path:`${out}/${name}-${width}.png`,style:'.site-header, .skip-link {visibility:hidden !important}'});}
  await page.emulateMedia({reducedMotion:'reduce'});checks.reducedMotion=await page.evaluate(()=>({scroll:getComputedStyle(document.documentElement).scrollBehavior,animated:[...document.querySelectorAll('*')].filter(e=>getComputedStyle(e).animationName!=='none').length}));
  checks.errors=errors;report.push(checks);await context.close();
 }
 const context=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});const p=await context.newPage();await p.goto('http://127.0.0.1:4175/');report.push({javascriptDisabled:await p.locator('#navigation').isVisible()&&await p.locator('#discovery').isVisible()});await context.close();
 const keyboard=await browser.newContext({viewport:{width:390,height:844}});const p2=await keyboard.newPage();await p2.goto('http://127.0.0.1:4175/');await p2.keyboard.press('Tab');await p2.keyboard.press('Enter');report.push({keyboardSkipLink:await p2.evaluate(()=>location.hash==='#main')});await keyboard.close();
 fs.writeFileSync(`${out}/browser-qa.json`,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report.map(r=>({width:r.width,scrollWidth:r.scrollWidth,overflows:r.overflows,brokenImages:r.brokenImages,errors:r.errors,reducedMotion:r.reducedMotion,javascriptDisabled:r.javascriptDisabled,keyboardSkipLink:r.keyboardSkipLink})),null,2));await browser.close();
 if(report.some(r=>r.errors?.length||r.scrollWidth>r.width||r.brokenImages?.length||r.overflows?.length||r.javascriptDisabled===false||r.keyboardSkipLink===false))process.exitCode=1;
})();
