const serverUrl = document.getElementById('server_url');
const userid = document.getElementById('userid');
const userkey = document.getElementById('userkey');
const saveBtn = document.getElementById('save_btn');
const popup = document.getElementById('popup');


// Load settings
let settings = {};
browser.storage.sync.get(['settings'], settings => {
    settings = settings.settings;
    serverUrl.value = settings.SERVER_URL || ''; 
    userid.value = settings.USER_ID || ''; 
    userkey.value = settings.USER_KEY || ''; 
});

// Save settings
saveBtn.onclick = e => {
    browser.storage.sync.set({
        settings: {
            SERVER_URL: serverUrl.value,
            USER_ID: userid.value,
            USER_KEY: userkey.value,
            ENABLED: settings.enabled === undefined ? true : settings.enabled
        }
    });
    popup.classList.add('visible');
    setTimeout(() => popup.classList.remove('visible'), 1500);
};
