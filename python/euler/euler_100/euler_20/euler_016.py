"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""
import unittest

from utils.math.radix import get_digits

def euler_016(base, power):
	return sum(get_digits(base ** power))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_016(2, 15), 26)
		self.assertEquals(euler_016(2, 1000), 1366)
