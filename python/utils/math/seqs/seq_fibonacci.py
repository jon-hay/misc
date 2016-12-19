import unittest

from utils.math.seqs.bases.seq_base import SeqBase

class SeqFibonacci(SeqBase):
	def _get_init_vals(self):
		return [0, 1]

	def _get_next_val(self):
		return self.curr_vals[-1] + self.curr_vals[-2]

class Test(unittest.TestCase):
	def test_get_fibonacci(self):
		seq = SeqFibonacci()
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [0])
		self.assertEquals(f(max_idx=2), [0, 1])
		self.assertEquals(f(max_idx=8), [0, 1, 1, 2, 3, 5, 8, 13])

		self.assertEquals(f(max_val=0), [0])
		self.assertEquals(f(max_val=1), [0, 1, 1])
		self.assertEquals(f(max_val=2), [0, 1, 1, 2])
		self.assertEquals(f(max_val=8), [0, 1, 1, 2, 3, 5, 8])
