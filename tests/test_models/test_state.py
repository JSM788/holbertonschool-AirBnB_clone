#!/usr/bin/python3
"""
    TestState module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
        TestState class
    """

    def test_should_create_state_instance(self):
        """
            TestState
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_should_create_state_variable(self):
        """
            TestVariable
        """
        state = State()
        self.assertIsInstance(state.name, str)
