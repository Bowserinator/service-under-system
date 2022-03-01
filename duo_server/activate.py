# Example usage: python3 activate.py https://m-XXXXXXXX.duosecurity.com/android/YYYYYYYYYYYYYYYYYYYY my_username

import argparse
import traceback
import sys
from src import duo

parser = argparse.ArgumentParser(description="Activate a user's Duo auth account")
parser.add_argument("url", type=str, help="Your Duo activation url. See the README for instructions")
parser.add_argument("user", type=str, help="The user ID for the account, must be UNIQUE to them")

args = parser.parse_args()

try:
    duo.register(args.url, args.user)
except IndexError as e:
    print(f"It seems the url '{args.url}' may be malformed")
    print("Valid urls are in either of the following formats:")
    print("- https://api-XXXXXXXX.duosecurity.com/frame/qr?value=YYYYYYYYYYYYYYYYYYYY-ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    print("- https://m-XXXXXXXX.duosecurity.com/android/YYYYYYYYYYYYYYYYYYYY")
    sys.exit(1)
except KeyError as e:
    print("An error has occured trying to register the activation link (maybe it's invalid?)\n")
    print(traceback.format_exc())
    sys.exit(1)

print(f"Successfully registed {args.user}! See instructions for adding user auth in the README")
print("(Which must be done manually)")
