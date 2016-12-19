# coding=utf-8
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import unittest

from utils.math.combinatorics import combination

def euler_015(n):
	return combination(2 * n, n)

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_015(2), 6)
		self.assertEquals(euler_015(20), 137846528820)
