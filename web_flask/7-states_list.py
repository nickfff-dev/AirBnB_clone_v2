#!/usr/bin/python3
""" This module defines a flask basic app """


from flask import Flask, render_template
import models
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Method for simple server """
    states = sorted(list(models.storage.all(State).values()),
                    key=lambda x: x["name"])
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Method to close the session after each request """
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
