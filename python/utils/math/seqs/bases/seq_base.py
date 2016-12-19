class SeqBase(object):
	def __init__(self):
		self.set_init_vals(self._get_init_vals())

	def _get_init_vals(self):
		raise NotImplementedError

	def _get_next_val(self):
		raise NotImplementedError

	def _reset(self):
		self.curr_vals = self.init_vals
		self.curr_idx = 0

	def _terminate(self, val):
		return False

	def set_init_vals(self, init_vals):
		self.init_vals = init_vals
		self.init_len = len(self.init_vals)
		self._reset()

	def generate(self, max_idx=None, max_val=None):
		assert max_idx is None or max_idx >= 0

		self._reset()
		while True:
			if max_idx is not None and self.curr_idx >= max_idx:
				return

			if self.curr_idx < self.init_len:
				next_val = self.init_vals[self.curr_idx]
			else:
				next_val = self._get_next_val()
				if self.curr_vals:
					self.curr_vals = self.curr_vals[1:] + [next_val]

			if max_val is not None and next_val > max_val:
				return

			self.curr_idx += 1
			yield next_val

			if self._terminate(next_val):
				return

	def get_list(self, *args, **kwargs):
		return list(self.generate(*args, **kwargs))
