#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Return Hello HBNB! message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB .* message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_(text):
    """return text .* message"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def Python_(text):
    """return text .* message"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def num_(n):
    """return Number .* message"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """return Number .* message"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """return Number .* message"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    """Run the app in debug mode"""
    app.run(host="0.0.0.0", port=5000)
