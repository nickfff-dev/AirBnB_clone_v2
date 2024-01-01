#!/usr/bin/python3
""" This module defines a flask basic app """


from flask import Flask, render_template
import models
from models.state import State
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states_list():
    """ Method for query cities by states """
    states = models.storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Method to close the session after each request """
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
