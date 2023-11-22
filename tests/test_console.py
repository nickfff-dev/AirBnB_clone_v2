#!/usr/bin/python3
"""This module defines tests on the console"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """
    Test cases for the console
    """

    def test_do_create(self):
        """
        Test the do_create method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    # Add more test methods as needed


if __name__ == "__main__":
    unittest.main()
