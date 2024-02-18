#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
#from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown application context
    """
    storage.close()
from models import storage

@app.route('/states', strict_slashes=False)
def states_list():
    """
    Display a HTML page with the list of all State objects
    """

    states = sorted(list(storage.all(Storage).values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities_list(id):
    """
     Display a HTML page with the list of City objects linked to the State
    """

    state = storage.get(State, id)
    if state:
        return render_template('9-states_cities', state=state)
    return render_template('9-not_found.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
