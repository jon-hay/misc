import unittest

from utils.math.seqs.bases.seq_base import SeqBase

class SeqCollatz(SeqBase):
	def __init__(self, init_val):
		self.init_val = init_val
		super(SeqCollatz, self).__init__()

	def _get_init_vals(self):
		return [self.init_val]

	def _get_next_val(self):
		n = self.curr_vals[-1]
		if n % 2 == 0:
			return n / 2
		else:
			return 3 * n + 1

	def _terminate(self, val):
		return val == 1

class Test(unittest.TestCase):
	def test_get_collatz(self):
		from utils.math.seqs.helpers.seq_terminating_len import SeqTerminatingLen

		seq = SeqCollatz(13)
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [13])
		self.assertEquals(f(max_idx=10), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
		self.assertEquals(f(max_idx=15), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

		self.assertEquals(f(max_val=0), [])
		self.assertEquals(f(max_val=1), [])
		self.assertEquals(f(max_val=15), [13])

		seq_aggr = SeqTerminatingLen(SeqCollatz)
		g = seq_aggr.get_terminating_len
		self.assertEquals(g(13), 10)
		self.assertEquals(g(40), 9)
