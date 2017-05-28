import math
import operator
import unittest


def _factorial_recursive(n):
	return n * _factorial_recursive(n - 1) if n else 1


def _factorial_recursive_tail(n):
	def _helper(current, result):
		return _helper(current - 1, current * result) if current else result

	return _helper(n, 1)


def _factorial_iterative(n):
	result = 1
	for current in xrange(1, n + 1):
		result *= current
	return result


def _factorial_iterative_reduce(n):
	return reduce(operator.mul, xrange(1, n + 1), 1)


def _factorial_python(n):
	return math.factorial(n)


factorial_implementations = [
	_factorial_recursive,
	_factorial_recursive_tail,
	_factorial_iterative,
	_factorial_iterative_reduce,
	_factorial_python,
]

factorial = _factorial_python


class Test(unittest.TestCase):
	def test_factorial(self):
		for f in factorial_implementations:
			self.assertEquals(f(0), 1)
			self.assertEquals(f(1), 1)
			self.assertEquals(f(10), 3628800)
