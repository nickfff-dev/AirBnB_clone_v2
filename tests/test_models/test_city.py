#!/usr/bin/python3
""" module defines a class that runs test on class city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os


class test_City(test_basemodel):
    """ defines test on City class"""

    def __init__(self, *args, **kwargs):
        """ test init"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state_id """
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_name(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))
