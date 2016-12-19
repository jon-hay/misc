"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import unittest

def euler_009(n):
	for i in xrange(1, n + 1):
		for j in xrange(1, n - i - 1):
			k = n - i - j
			if i ** 2 + j ** 2 == k ** 2:
				return i * j * k
	return None

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_009(n=12), 60)
		self.assertEquals(euler_009(n=1000), 31875000)
