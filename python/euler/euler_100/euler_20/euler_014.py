# coding=utf-8
"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import unittest

from utils.math.seqs.helpers.seq_terminating_len import SeqTerminatingLen
from utils.math.seqs.seq_collatz import SeqCollatz

def euler_014(limit):
	seq_aggr = SeqTerminatingLen(SeqCollatz)
	return max((seq_aggr.get_terminating_len(n), n) for n in xrange(2, limit))

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_014(1000000), (525, 837799))
