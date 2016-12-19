# coding=utf-8
"""
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import unittest

from utils.math.seqs.seq_powers import SeqPowers

def euler_006(limit):
	f = lambda n: sum(SeqPowers(n).get_list(max_idx=limit))
	return f(1) ** 2 - f(2)

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_006(limit=10), 2640)
		self.assertEquals(euler_006(limit=100), 25164150)
