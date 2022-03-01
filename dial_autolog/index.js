const puppeteer = require('puppeteer-core');
require('dotenv').config();

const duo = require('./src/duo.js');
const config = require('./config.js');

const DIAL_URL = 'https://covid19.rpi.edu/dailycheckin';
const USERNAME = process.env.DIAL_USERNAME;
const PASSWORD = process.env.DIAL_PASSWORD;

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
        headless: false,
        args: [
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process'
        ],
        ignoreDefaultArgs: ['--disable-extensions'],
    });
    const page = await browser.newPage();
    await page.goto(DIAL_URL, { waitUntil: 'domcontentloaded' });

    // todo: SEARCH for chrome installation


    await page.evaluate((USERNAME, PASSWORD) => {
        document.getElementById('username').value = USERNAME; 
        document.getElementById('password').value = PASSWORD;
        document.querySelector('.btn.btn-block.btn-submit').click();
    }, USERNAME, PASSWORD);

    // Duo auth
    if (false) {

    }
    else {
        // TODO: get OTP
        const OTP = await duo.getOTPFromServer(
            config.loginCredentials.serverAddress,
            config.loginCredentials.userid,
            config.loginCredentials.userkey);

        // Auto login
        await page.waitForNavigation();

        // Get Duo iframe
        const frame = (await page.frames()).find(f =>f.url().includes('duo'));
        await frame.waitForNavigation();

        await frame.evaluate(OTP => {
            [...document.getElementsByTagName('button')]
                .filter(x => x.innerText.includes('Enter a Passcode'))[0].click();
            let inputs = [...document.getElementsByTagName('input')]
                .filter(x => x.name === 'passcode' && x.type === 'text')[0].value = OTP;
            let buttons = [...document.getElementsByTagName('button')]
                .filter(x => x.innerText.includes('Log In'))[0].click();
        }, OTP);

        // TODO: update file otherwise
        // TODO: check if actually logged in at this point
        await duo.updateCounterFromServer(
            config.loginCredentials.serverAddress,
            config.loginCredentials.userid,
            config.loginCredentials.userkey);

        // DIAL
        await page.waitForNavigation();
        await page.evaluate(() => {
            async function poll(func) {
                return await new Promise(resolve => {
                    const poll = setInterval(() => {
                        let r = func();
                        if (r) {
                            clearInterval(poll);
                            resolve(r);
                        };
                    }, 20);
                });
            }

            (async () => {
                // Expand menu
                (await poll(() => document.getElementById('t_Button_navControl'))).click();
            
                // Daily Health Check link
                (await poll(() => [...document.getElementsByTagName('a')]
                        .filter(e => e.innerText === 'Daily Health Check')[0])).click();

                // Get iframe
                let iframe = await poll(() => document.getElementsByTagName('iframe')[0]);
                iframe.addEventListener('load', async () => {
                    iframe = iframe.contentDocument;

                    // Click checkbox & submit
                    let checkbox = await poll(() => [...iframe.getElementsByTagName('tr')]
                        .filter(e => e.innerText.includes('None'))[0]);
                    checkbox.getElementsByTagName('input')[0].click();
                    iframe.querySelector('span.t-Button-label').parentElement.click();
                });
            })();
        });
    }

    await browser.close();
})();
