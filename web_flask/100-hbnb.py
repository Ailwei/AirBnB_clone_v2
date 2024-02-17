#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown application context
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display a HTML page like 8-index.html with data from DBStorage
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    cities = sorted(list(storage.all(City).values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all(Amenity).values()), key=lambda x: x.name)
    places = sorted(list(storage.all(Place).values()), key=lambda x: x.name)
    return render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
