from flask import Flask, request
from flask_limiter import Limiter
from flask_cors import CORS
import json

from src import duo
import config


# App setup
# -------------------
app = Flask(__name__)
CORS(app)
limiter = Limiter(app, key_func=lambda: 0)


# Used to seperate rate limit requests
# -------------------
KEY_FUNC = lambda: request.form.get("userid")


# Endpoints
# -------------------
@app.route("/", methods=["GET"])
def note():
    return "<p>This is the POST datapoint for the Duo Server. See the README for more details.</p>"


@app.route("/update_count", methods=["POST"])
@limiter.limit(config.API_RATE_LIMIT, key_func=KEY_FUNC)
def reset_count():
    userid = request.form.get("userid")
    count = request.form.get("count")

    if not userid:
        return json.dumps({"error": "Missing userid"})
    if not count:
        return json.dumps({"error": "Missing count"})

    # TODO: encryption

    try:
        duo.update_count(userid, int(count))
        return json.dumps({"new_count": count})
    except IOError:
        return json.dumps({"error": "Unknown userid"})
    except ValueError:
        return json.dumps({"error": "Invalid count"})


@app.route("/inc_count", methods=["POST"])
@limiter.limit(config.API_RATE_LIMIT, key_func=KEY_FUNC)
def increment_count():
    userid = request.form.get("userid")
    if not userid:
        return json.dumps({"error": "Missing userid"})

    # TODO: encryption

    try:
        count = duo.increment_count(userid)
        return json.dumps({"new_count": count})
    except IOError:
        return json.dumps({"error": "Unknown userid"})


@app.route("/get_otp", methods=["POST"])
@limiter.limit(config.API_RATE_LIMIT, key_func=KEY_FUNC)
def get_otp():
    userid = request.form.get("userid")
    if not userid:
        return json.dumps({"error": "Missing userid"})

    # TODO: encryption

    try:
        otp, count = duo.generate_code(userid)
        return json.dumps({"otp": otp, "count": count})
    except IOError:
        return json.dumps({"error": "Unknown userid"})


app.run(host=config.HOST,
    port=config.PORT,
    debug=config.FLASK_DEBUG,
    ssl_context=config.SSL_CONTEXT)
