const puppeteer = require('puppeteer-core');

const DIAL_URL = 'https://cas.auth.rpi.edu/cas/login?service=https%3A%2F%2Fapex.cct.rpi.edu%2Fapex%2FSimon_Apex.cas_login_redirect%3FAPP%3D244%26SESSION%3D15316674116217';

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
        headless: false
    });
    const page = await browser.newPage();
    await page.goto(DIAL_URL);
    // await page.screenshot({ path: 'example.png' });

    // todo: SEARCH for chrome installation
    // TODO: take password from env variables
    // login
    // use Duo automatically

    await page.waitFor('#username');
    await page.evaluate(() => {
        document.getElementById('username').value = 'Dallas'; 
        document.getElementById('password').value = 'hello';
        document.querySelector('.btn.btn-block.btn-submit').click();
    });

    // await browser.close();
})();
