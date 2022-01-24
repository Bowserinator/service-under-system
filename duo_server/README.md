# Duo Auto-login Server Setup
Most of this server code was stolen from https://github.com/rcslab/duo-cli. It's a simple Flask server that acts as the API (negating the need for a CORS proxy). This is designed to be used with the provided extension.

**NOTE: AT THE TIME OF WRITING SSL AND ENCRYPTION HAVE NOT BEEN IMPLEMENTED, SO ONLY USE THIS ON LOCALHOST**

## Setup

### Install pre-reqs
This server requires `python3`:

```
cd duo_server
pip install -r requirements.txt
```

### Configuring the Server

Open up `config.py` and edit the variables as needed. The comments within should give you a good idea of what values are allowed and the purpose of the config, by default it serves on `localhost:9123`.

### Run the Server
In the `duo_server` folder:
```
python3 main.py
```

## Setup Duo Account

### Add account
Go to your organization's Duo dashboard, and follow the following steps. For RPI this is https://apex.cct.rpi.edu/apex/f?p=119.

(If it says you're signed in with Duo already, that means it remembered you're logged in. Try clearing your cookies, or logging in on another browser or computer).
1. Sign in with Duo, making sure **NOT** to check any box that says 'Remember me'
2. Click `Add a new device` on the bottom left
3. Select 'Tablet' then select 'Android' (Doesn't really matter what OS)
4. Click "I have Duo Mobile Installed"

You now have two options:
- **Option 1:** Right click the QR code image and click "Copy image address"
      It should look something like `https://api-XXXXXXXX.duosecurity.com/frame/qr?value=YYYYYYYYYYYYYYYYYYYY-ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ`
- **Option 2:** Click "email me an activation link", put in an email address and copy the activation link they send you (**DO NOT CLICK IT YET**). It should look something like `https://m-XXXXXXXX.duosecurity.com/android/YYYYYYYYYYYYYYYYYYYY`

Finally, run in the `duo_server` folder, with `your_username` replaced with a username for yourself.
```
python3 activate.py https://m-XXXXXXXX.duosecurity.com/android/YYYYYYYYYYYYYYYYYYYY your_username
```
(Your link formatting might look different if you used the QR code instead)

You should now see in `duo_server/accounts/your_username` there should be a new file called `secret.hotp`. The lines are as follows:
```
SECRET_KEY
COUNTER (Don't let this desync)
CUSTOMER_NAME (Your service provider, RPI)
REACTIVATION_TOKEN (No idea what this does)
```

### Add encryption key to account

TODO: Implement this

