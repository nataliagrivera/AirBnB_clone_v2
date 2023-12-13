#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask
from flask import render_template
from models.state import storage
from models.state import State
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


# New route
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number" .format(n)


# New route
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


# New route
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


# New route
@app.route('/states_list', strict_slashes=False)
def states_list():
    state_li = storage.all(State).values()
    return render_template('7-states_list.html', states=state_li)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    state_li = storage.all(State).values()
    return render_template('7-states_list.html', states=state_li)


@app.route('cities_by_states', strict_slashes=False)
def cities_by_states():
    city_li = storage.all(State).values()
    return render_template('8-cities_by_states.html', cities=city_li)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
