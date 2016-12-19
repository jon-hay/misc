def exception_safe(exception_return):
	def _dec(func):
		def _func(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except:
				return exception_return

		return _func

	return _dec
