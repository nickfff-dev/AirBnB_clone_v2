#!/usr/bin/python3
""" This module defines a flask basic app """


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """ Display a list of all states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('9-states.html', states=states, id=None)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Display a list of all states """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=states, id=id)
    return render_template('9-states.html', states=states, id=None)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
