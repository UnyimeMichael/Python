import unittest
from math import pi
from Object_Oriented_Programming.circles import area_of_circle


class TestArea(unittest.TestCase):
    def test_area_of_circle(self):
        self.assertEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)

    def test_area_function_reject_negative
