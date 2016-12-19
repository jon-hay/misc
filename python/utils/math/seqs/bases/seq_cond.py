from utils.math.seqs.bases.seq_base import SeqBase

class SeqCond(SeqBase):
	def __init__(self, cond, init_n=1):
		self.val_cond = cond
		self.vc_init_idx = init_n
		super(SeqCond, self).__init__()

	def _get_init_vals(self):
		return []

	def _get_next_val(self):
		self.vc_curr_idx += 1
		while not self.val_cond(self.vc_curr_idx):
			self.vc_curr_idx += 1
		return self.vc_curr_idx

	def _reset(self):
		self.vc_curr_idx = self.vc_init_idx
		super(SeqCond, self)._reset()
