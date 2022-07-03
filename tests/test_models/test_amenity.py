#!/usr/bin/python3
"""
    TestAmenity module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        TestAmenity class
    """

    def test_should_create_amenity_instance(self):
        """
            Test amenity
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_shoudl_create_instance_variables(self):
        """
            Test variables
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
