from utils.math.seqs.bases.seq_base import SeqBase

class SeqFunc(SeqBase):
	def __init__(self, val_func):
		self.val_func = val_func
		super(SeqFunc, self).__init__()

	def _get_init_vals(self):
		return [self.val_func(1)]

	def _get_next_val(self):
		return self.val_func(self.curr_idx + 1)
