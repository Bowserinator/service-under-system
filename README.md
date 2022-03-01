# Service Under System

Collection of tools to bypass Duo 2FA / automate logins.

Currently contains the following tools:
```
- Duo OTP auto-login extension (chrome)
- Duo OTP auto-login backend serve
- Duo push auto-accepter (android)
- DIAL Auto-symptom logger
```

## How to setup
- **Server**: See the `duo_server` folder
- **Chrome extension**: See the `duo_ext_chrome` folder
- **Android push automater**: See the `duo_android_push` folder
- **DIAL Autologger**: See the `dial_autolog` folder

## TODO
**Extension / server:**

- SSL & encryption for the server
- Instructions on how to run Flask in production
- Instructions on how to run script in background
- Standalone extension option with a CORS proxy
- Option to reset to last valid count + 1 in the event of desync
- Notify users of extension errors (ie, couldn't connect to server)
- Make cool icon
- Firefox extension
- Retry automatically on "code already used"

**Android push automater:**
- Installation instructions for the android push automater
- Tutorial for VM optimizations
- Make it work on devices that can't properly receive google push notifications (by repeatedly reopening the app to force a re-check)


## Why?
- 2FA is annoying
- Some people don't have working phones, forcing them to go through a lengthy process of getting an OTP code

