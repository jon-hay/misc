import unittest

from utils.helpers.helper_reduce import mul

def factorial(n):
	return mul(xrange(1, n + 1))

def permutation(n, r):
	return factorial(n) / factorial(n - r)

def combination(n, r):
	return permutation(n, r) / factorial(r)

class Test(unittest.TestCase):
	def test_factorial(self):
		f = factorial
		self.assertEquals(f(0), 1)
		self.assertEquals(f(1), 1)
		self.assertEquals(f(10), 3628800)

	def test_permutation(self):
		p = permutation
		self.assertEquals(p(0, 0), 1)
		self.assertEquals(p(1, 1), 1)
		self.assertEquals(p(6, 3), 120)

	def test_combination(self):
		c = combination
		self.assertEquals(c(0, 0), 1)
		self.assertEquals(c(1, 1), 1)
		self.assertEquals(c(6, 3), 20)
