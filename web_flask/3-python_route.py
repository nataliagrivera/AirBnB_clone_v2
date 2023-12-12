#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)  # route definition
def hello_hbnb():  # content to display on that route
    return "Hello HBNB!"


# New route
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


# New route
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}" .format(text.replace("_", " "))


# New route
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    return "Python {}" .format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)