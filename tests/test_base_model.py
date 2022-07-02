#!/usr/bin/python3
""" TestBaseModel class """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
        Tests base model class
    """

    def test_instance_creation_of_base_model(self):
        """
            Tests instance creation of the base model
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_avoid_id_duplication_for_instance(self):
        """
            Tests avoid ID duplications
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_assignment_of_created_at_attribute(self):
        """"
            Tests created_at attribute
        """
        bm = BaseModel()
        c_at = bm.created_at
        self.assertIsInstance(c_at, datetime)
