#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Return Hello HBNB! message"""
    return "Hello HBNB!"


@app.route("/", strict_slashes=False)
def HBNB():
    """return HBNB .* message"""
    return "HBNB"


if __name__ == "__main__":
    """Run the app in debug mode"""
    app.run(host="0.0.0.0", port=5000)
