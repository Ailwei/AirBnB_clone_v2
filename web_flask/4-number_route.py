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
                    (replace underscore _ symbols with a space )
    /number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text='C'):
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text='is cool'):
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
