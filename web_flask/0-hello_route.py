#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""Create a Flask application instance"""


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Return Hello HBNB! message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Run the app in debug mode"""
    app.run(host="0.0.0.0", port=5000)
