const onBtn = document.getElementById('on_btn');;

/**
 * Update button style for enabled
 * @param {boolean} enabled Ext enabled?
 */
function updateButton(enabled) {
    onBtn.style.backgroundColor = enabled ? '#00C853' : '#DD2C00';
    onBtn.innerText = enabled ? 'ON' : 'OFF';
}

// Load settings
let enabled = true;
browser.storage.sync.get(['settings'], settings => {
    enabled = settings.settings.ENABLED;
    updateButton(enabled);
});

onBtn.onclick = e => {
    enabled = !enabled;
    updateButton(enabled);
    browser.storage.sync.get(['settings'], settings => {
        settings = settings.settings;
        settings.ENABLED = enabled;
        browser.storage.sync.set({ settings });
    });
}

document.getElementById('open_settings').onclick = e => {
    browser.runtime.openOptionsPage();
}
