#!/usr/bin/python3
""" This module defines a flask basic app """


from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
