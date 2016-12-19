import unittest

from utils.math.factorisation import is_abundant, is_deficient, is_perfect
from utils.math.seqs.bases.seq_cond import SeqCond

class SeqDeficient(SeqCond):
	def __init__(self):
		super(SeqDeficient, self).__init__(is_deficient)

class SeqPerfect(SeqCond):
	def __init__(self):
		super(SeqPerfect, self).__init__(is_perfect)

class SeqAbundant(SeqCond):
	def __init__(self):
		super(SeqAbundant, self).__init__(is_abundant)

class Test(unittest.TestCase):
	def test_get_perfect(self):
		seq = SeqPerfect()
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [6])
		self.assertEquals(f(max_idx=2), [6, 28])

		self.assertEquals(f(max_val=0), [])
		self.assertEquals(f(max_val=6), [6])
