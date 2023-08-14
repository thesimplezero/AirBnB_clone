#!/usr/bin/env python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_default_name(self):
        """
        Test the default value of the 'name' attribute.
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
