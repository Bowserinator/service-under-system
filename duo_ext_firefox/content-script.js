/**
 * Poll until a function is completed, and return the result
 * @param {Function} func Func to poll, return a non-falsy value when done
 * @return Output of the polled function
 */
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

/**
 * Send a POST request to an endpoint of the server
 * @param {string} endpoint Endpoint, ie /inc_count
 * @param {object} params Parameters to post as an obj, ie { key: value }
 * @param {Function} cb Callback of the XMLHttpRequest, passing in status, response
 */
function postEndpoint(endpoint, params, cb) {
    const req = new XMLHttpRequest();
    const urlParams = (new URLSearchParams(params)).toString(); // `userid=duotoken`;

    console.log(endpoint, urlParams)

    req.open('POST', settings.SERVER_URL + endpoint, true);
    req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    req.send(urlParams);
    req.onreadystatechange = () => cb(req.readyState === XMLHttpRequest.DONE && req.status === 200, req.response);
}

let settings = {};
(async () => {
    settings = (await browser.storage.sync.get(['settings'])).settings;
    let defaultObj = { userid: settings.USER_ID };
    if (settings.USER_KEY)
        defaultObj.userkey = settings.USER_KEY;

    if (!settings.ENABLED)
        return;

    // 1. Get "password" btn
    let password_btn = await poll(() => {
        let buttons = [...document.getElementsByTagName('button')]
            .filter(x => x.innerText.includes('Enter a Passcode'));
        return buttons[0];
    });

    // 1.5. Begin request for OTP
    let OTP = null;
    postEndpoint('/get_otp', defaultObj, (ok, response) => {
        console.log(ok, response)
        if (ok) {
            let data = JSON.parse(response);
            if (!data.error) OTP = data.otp;
        }
    });

    // 2. Click the password button
    password_btn.click();

    // 3. Select input box
    let input_box = await poll(() => {
        let inputs = [...document.getElementsByTagName('input')]
            .filter(x => x.name === 'passcode' && x.type === 'text');
        return inputs[0];
    });

    // 4. Input OTP into the input box
    let event = new Event('input', {
        'bubbles': true,
        'cancelable': true
    });

    await poll(() => OTP); // Wait for OTP to be ready
    input_box.value = OTP;
    input_box.dispatchEvent(event);

    // 5. Click "login"
    let login_btn = await poll(() => {
        let buttons = [...document.getElementsByTagName('button')]
            .filter(x => x.innerText.includes('Log In'));
        return buttons[0];
    });
    login_btn.click();

    // 6. Increment count
    postEndpoint('/inc_count', defaultObj, (ok, response) => {
        if (ok) {
            let data = JSON.parse(response);
            if (data.error)
                alert(data.error);
        }
    });
})();
