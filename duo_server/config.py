# Modify keys here to config your server

# ----------------
# Server
# ----------------

# Set to 0.0.0.0 if you want to serve to the public
# Otherwise set to localhost\
#   WARNING: may allow arbritary code execution on your computer
#   if you serve to the public and are in Debug mode
HOST = "localhost"

# Port number to serve on. If you're hosting this on a server
# you may need to allow it through a firewall. Make sure no
# other app is using the port!
PORT = 9123

SSL_CONTEXT = None

# Allow users to use the API without an encryption key?
# (Recommended ONLY for local server setups, otherwise
#  anyone can request an OTP for another user)
ALLOW_UNKEYED_USERS = True

# Rate limit applied to the POST endpoints
# in the format defined here: https://flask-limiter.readthedocs.io/en/stable/
# Since the Duo auth code requires file operations and is thus not race condition
# proof this value shouldn't be too low
API_RATE_LIMIT = "1 per second"


# ----------------
# Logging
# ----------------

# Run Flask with debug logging?
FLASK_DEBUG = True

LOG_LEVEL = ""

"""
- ssl cert

- logging level
"""