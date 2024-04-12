#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Returns the list of all cities in the database."""
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    amenity = sorted(storage.all("Amenity").values(), key=lambda s: s.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda c: c.name)
    return render_template(
        "10-hbnb_filters.html\
",
        states=states,
        amenity=amenity,
    )


@app.teardown_appcontext
def close(self):
    """Closes the database session."""
    storage.close()


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
