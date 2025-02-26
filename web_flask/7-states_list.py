#!/usr/bin/python3
"""
Script to start a Flask web application
"""

from flask import Flask, render_template
from models import Storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown methods to clear up 
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display states
    """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
