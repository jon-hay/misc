"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import unittest

from utils.helpers.helper_dict import combine_dicts
from utils.helpers.helper_reduce import mul
from utils.math.factorisation import get_prime_factors

def euler_005(limit):
	prime_factors = combine_dicts([get_prime_factors(n) for n in xrange(2, limit + 1)], max, 0)
	return mul(prime_factor ** count for (prime_factor, count) in prime_factors.iteritems())

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_005(limit=10), 2520)
		self.assertEquals(euler_005(limit=20), 232792560)
