# coding=utf-8
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
import unittest

from utils.math.factorisation import is_amicable

def euler_020(limit):
	return sum(n for n in xrange(2, limit) if is_amicable(n))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_020(285), 220 + 284)
		self.assertEquals(euler_020(10000), 31626)
