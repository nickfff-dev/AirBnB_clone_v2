#!/usr/bin/python3
""" This module defines a flask basic app """


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Method for simple server """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hnbnb():
    """ hollas HBNB! """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cRoute(text):
    """ the c route a dymanic path"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pRoute(text='is_cool'):
    """ the python route a dymanic path"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def nRoute(n):
    """ the python route a dymanic path"""
    return str(n) + ' is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def templtRoute(n):
    """ the python route a dymanic path"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddevenRoute(n):
    """ the python route a dymanic path"""
    if n % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
