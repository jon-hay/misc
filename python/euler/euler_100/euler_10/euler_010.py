"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import unittest

from utils.math.seqs.seq_primes import SeqPrimes

def euler_010(max_val):
	return sum(SeqPrimes().get_list(max_val=max_val - 1))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_010(max_val=10), 17)
		self.assertEquals(euler_010(max_val=2000000), 142913828922)
