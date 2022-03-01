# Stolen from https://github.com/rcslab/duo-cli

import pyotp
import requests
import base64
import json

USER_DATA_DIR = "accounts/"


def register(qr_url: str, user_id: str) -> str:
    """
    Register a user to the server
    :param qr_url: URL to the QR code (or activation link) (string) when registering
                   a new mobile device
    :param user_id: user_id (string), used for filename. Unique per user
    :throws KeyError: Invalid request
    :return: HOTP secret
    """

    # Regular activation links sent in a email follow this format:
    # https://m-XXXXXXXX.duosecurity.com/android/YYYYYYYYYYYYYYYYYYYY
    host = "api-%s" % (qr_url.split("/")[2].split("-")[1],)
    code = qr_url.rsplit("/",1)[1]

    # Handle QR code urls, which are a similar format:
    # https://api-XXXXXXXX.duosecurity.com/frame/qr?value=YYYYYYYYYYYYYYYYYYYY-ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # Note: we only care about the X and Y parts, the Z is just the API domain but base64 encoded
    if "qr?" in code:
        code = code.split("qr?value=")[1].split("-")[0]

    url = "https://{host}/push/v2/activation/{code}?customer_protocol=1".format(host=host, code=code)
    headers = { "User-Agent": "okhttp/2.7.5" }
    data = {"jailbroken": "false",
            "architecture": "armv7",
            "region": "US",
            "app_id": "com.duosecurity.duomobile",
            "full_disk_encryption": "true",
            "passcode_status": "true",
            "platform": "Android",
            "app_version": "3.23.0",
            "app_build_number": "323001",
            "version": "8.1",
            "manufacturer": "unknown",
            "language": "en",
            "model": "Pixel C",
            "security_patch_level": "2018-12-01"}

    r = requests.post(url, headers=headers, data=data)
    response = json.loads(r.text)

    # Data fields
    secret = base64.b32encode(response["response"]["hotp_secret"].encode()).decode()
    customer_name = response["response"]["customer_name"]
    reactivation_token = response["response"]["reactivation_token"]

    f = open(f"{USER_DATA_DIR}{user_id}/secret.hotp", "w")
    f.write(secret + "\n")        # HOTP secret
    f.write("0" + "\n")           # Activation key count
    f.write(customer_name + "\n") # Customer name (your service provider)
    f.write(reactivation_token)   # Reactivation token
    f.close()

    return secret


def update_count(user_id: str, count: int):
    """
    Update the count of a user in a file to [count]
    :param user_id: User id (string), unique per user, used for filename
    :param count: New count to update to
    :throws IOError: Invalid secret file
    """
    if count < 0:
        raise ValueError("Count must be greater than or equal to 0")

    f = open(f"{USER_DATA_DIR}{user_id}/secret.hotp", "r+")
    _ = f.readline()[0:-1]
    offset = f.tell()

    f.seek(offset)
    f.write(str(count))
    f.close()


def generate_code(user_id: str):
    """
    Generate a one time auth code for a user.

    :param user_id: User id (string), unique per user, used for filename
    :return: OTP, count
    :throws IOError: Invalid secret file
    """

    f = open(f"{USER_DATA_DIR}{user_id}/secret.hotp", "r+")
    secret = f.readline()[0:-1]
    count = int(f.readline())

    hotp = pyotp.HOTP(secret)
    return hotp.at(count), count


def increment_count(user_id: str):
    """
    Increment the count for a user

    :param user_id: User id (string), unique per user, used for filename
    :return: new count
    :throws IOError: Invalid secret file
    """

    f = open(f"{USER_DATA_DIR}{user_id}/secret.hotp", "r+")
    lines = f.readlines()

    count = int(lines[1])
    lines[1] = str(count + 1) + "\n"

    f.seek(0)
    f.write("".join(lines))
    f.close()

    return count + 1
