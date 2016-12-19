"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
import unittest

from utils.math.seqs.seq_primes import SeqPrimes

def euler_007(max_idx):
	return SeqPrimes().get_list(max_idx=max_idx)[-1]

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_007(max_idx=6), 13)
		self.assertEquals(euler_007(max_idx=10001), 104743)
