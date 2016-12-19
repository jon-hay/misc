# coding=utf-8
"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
import unittest

from utils.math.combinatorics import factorial
from utils.math.radix import get_digits

def euler_020(n):
	return sum(get_digits(factorial(n)))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_020(10), 27)
		self.assertEquals(euler_020(100), 648)
