# Duo Auto-login Chrome Extension Setup

Chrome extension to auto-login on pages that have Duo. Make sure you followed the server setup guide first!

## Setup

### Modifying what sites to run on
(Ignore this if you're an RPI user and have no issues with the extension)

Scroll down to `matches` and add url patterns for pages where your Duo login appears, as shown below:
```js
    "content_scripts": [
        {
            "matches": [
                "https://*.duosecurity.com/frame/prompt?sid=*",
                "https://cas.auth.rpi.edu/cas/login?*",
                "https://cas-sis.auth.rpi.edu/cas/login?*"
            ],
```

## Installation
Go to `chrome://extensions` and check that `Developer mode` toggle on the top right corner. Then click `Load Unpacked` on the top left corner, and select the `duo_ext_chrome` folder. You should see the extension is now installed.


## Configuring Server
1. In the chrome task bar, click the extensions on the top right and find this extension.
2. Click on it, and click the "Settings page" hyperlink.
3. For server url, put the url to the server. If you're hosting it on your own computer with the default port of `9123`, put in `http://localhost:9123`. You can use `https` if your server has SSL enabled.
4. For User ID, put in the username you created for yourself on the server.
5. For User Key (optional) put in your user encryption key you put on the server.
6. Click "Save Settings"

You can turn off the extension at any time by clicking on the icon and clicking the "ON" button to turn it off.

