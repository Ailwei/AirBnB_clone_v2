#!/usr/bin/python3
"""
Script to start a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
                (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”,
    followed by the value of the text variable
"""

from flask import Flask
from werkzeug.utils import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python {}'.format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
