#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(_name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    close the current sqlalchemmy session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    """
    states = sorted(staorage.all("State").values(), key=lambda x: x.name)
    return render_template('cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
