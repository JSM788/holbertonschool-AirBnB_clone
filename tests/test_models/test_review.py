#!/usr/bin/python3
"""
    TestReview module
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
        TestReview class
    """

    def test_shoudl_create_review_instance(self):
        """
            tests
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_should_create_instance_variables(self):
        """
            Tests
        """
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
