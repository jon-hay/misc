"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import unittest

from utils.math.seqs.seq_fibonacci import SeqFibonacci

def euler_025(limit):
	return len(SeqFibonacci().get_list(max_val=limit))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_025(10 ** 2), 12)
		self.assertEquals(euler_025(10 ** 999), 4782)
