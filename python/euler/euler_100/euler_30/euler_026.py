"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import unittest

from utils.math.radix import get_reciprocal

def euler_026(limit):
	return max((len(get_reciprocal(n)[1]), n) for n in xrange(2, limit))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_026(1000), (982, 983))
