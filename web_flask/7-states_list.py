#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a list of all states and cities"""
    stateslist = sorted(storage.all("State").values(),
                        key=lambda item: item.name)

    for state in stateslist:
        state.cities = sorted(state.cities, key=lambda item: item.name)
    return render_template("8-cities_by_states.html", stateslist=stateslist)


@app.teardown_appcontext
def remove_sess(self):
    """removing the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    """Run the app in debug mode"""
    app.run(host="0.0.0.0", port=5000)
