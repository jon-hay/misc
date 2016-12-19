import operator

from utils.math.seqs.bases.seq_base import SeqBase

class SeqReduce(SeqBase):
	def __init__(self, reduce_func, base_seq):
		self.reduce_func = reduce_func
		self.base_seq = base_seq
		self.base_seq_gen = self.base_seq.generate()
		super(SeqReduce, self).__init__()

	def _get_init_vals(self):
		return [self.base_seq_gen.next()]

	def _get_next_val(self):
		return self.reduce_func(self.curr_vals[-1], self.base_seq_gen.next())

	def _reset(self):
		self.base_seq_gen = self.base_seq.generate()
		self.base_seq_gen.next()  # Consume initial value.
		super(SeqReduce, self)._reset()

class SeqSums(SeqReduce):
	def __init__(self, base_seq):
		super(SeqSums, self).__init__(operator.add, base_seq)

class SeqProducts(SeqReduce):
	def __init__(self, base_seq):
		super(SeqProducts, self).__init__(operator.mul, base_seq)
