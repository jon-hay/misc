import timeit

from algorithms.factorial import factorial_implementations


def _benchmark_func(func, n):
	try:
		result = "%.3f" % timeit.timeit(
			setup="from algorithms import factorial",
			stmt="factorial.{func}({n})".format(func=func.__name__, n=n),
			number=10 ** 6 / n,
		)
	except:
		result = "Failed"

	print "{0: >30}".format(func.__name__), result


def _benchmark_n(n):
	print "n: {n}".format(n=n)
	for func in factorial_implementations:
		_benchmark_func(func, n)


def _benchmark():
	for exp in xrange(1, 5):
		_benchmark_n(10 ** exp)


if __name__ == "__main__":
	_benchmark()
