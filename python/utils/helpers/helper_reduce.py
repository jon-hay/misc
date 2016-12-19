import operator
import unittest

def mul(iterable):
	return reduce(operator.mul, iterable, 1)

class Test(unittest.TestCase):
	def test_reduce_mul(self):
		f = mul
		self.assertEquals(f([]), 1)
		self.assertEquals(f([2]), 2)
		self.assertEquals(f([1, 2, 3, 4, 5]), 120)
