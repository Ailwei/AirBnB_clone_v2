#!/usr/bin/python3
"""
The script starts a flask web application.
The web application listens on 0.0.0.0, port 5000
Routes:
    /: display "Hello HBNB!"
    you must use the option strict_slashes=False i my route
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
