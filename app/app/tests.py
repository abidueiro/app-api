"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """
    Test the add function of the calc object.
    The add function takes two parameters and returns the sum of the two numbers.
    """
    def test_add(self):
        """ Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract(self):
        """ Test subtracting numbers."""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)

