"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import unittest

def euler_001(limit, factors=(3, 5)):
	return sum(n for n in xrange(limit) if any(f for f in factors if n % f == 0))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_001(limit=10), 23)
		self.assertEquals(euler_001(limit=1000), 233168)
