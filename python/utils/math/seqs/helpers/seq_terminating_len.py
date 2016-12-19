class SeqTerminatingLen(object):
	def __init__(self, seq_class):
		self.seq = seq_class(None)
		self.cache = {}

	def get_terminating_len(self, init_val):
		if init_val in self.cache:
			return self.cache[init_val]

		self.seq.set_init_vals([init_val])

		values = []
		terminating_len = 0
		for value in self.seq.generate():
			terminating_len = self.cache.get(value, 0)
			if terminating_len:
				break
			values.append(value)

		values.reverse()
		for value in values:
			terminating_len += 1
			self.cache[value] = terminating_len
		return terminating_len
