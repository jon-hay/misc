"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import unittest

from utils.math.factorisation import get_prime_factors

def euler_003(n):
	return max(get_prime_factors(n))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_003(n=13195), 29)
		self.assertEquals(euler_003(n=600851475143), 6857)
