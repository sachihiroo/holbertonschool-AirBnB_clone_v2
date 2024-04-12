#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", defaults={"id": None})
@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """Returns the list of all cities and state in the database."""
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda c: c.name)
    if id is not None:
        id = "State." + id
        states = storage.all("State")

    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def close(self):
    """Closes the database session."""
    storage.close()


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
