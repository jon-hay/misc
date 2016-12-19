import unittest

def get_digits(n, radix=10):
	assert n >= 0
	assert radix > 1

	if n == 0:
		return [0]

	digits = []
	while n:
		digits.append(n % radix)
		n /= radix
	return digits

def get_reciprocal(divisor, dividend=1, radix=10):
	q1 = q2 = None
	quotient = []

	while (q1, q2) not in quotient:
		quotient.append((q1, q2))
		dividend *= radix
		q1, q2 = dividend / divisor, dividend % divisor
		dividend = q2

	idx = quotient.index((q1, q2))
	return [q[0] for q in quotient[1:idx]], [q[0] for q in quotient[idx:]]

class Test(unittest.TestCase):
	def test_get_digits(self):
		f = get_digits

		for radix in xrange(2, 15):
			self.assertEquals(f(0, radix=radix), [0])
			self.assertEquals(f(1, radix=radix), [1])

		self.assertEquals(f(30, radix=2), [0, 1, 1, 1, 1])
		self.assertEquals(f(30, radix=10), [0, 3])
		self.assertEquals(f(30, radix=30), [0, 1])
		self.assertEquals(f(30, radix=100), [30])

	def test_get_reciprocal(self):
		f = get_reciprocal

		self.assertEquals(f(2), ([5], [0]))
		self.assertEquals(f(3), ([], [3]))
		self.assertEquals(f(4), ([2, 5], [0]))
		self.assertEquals(f(5), ([2], [0]))
		self.assertEquals(f(6), ([1], [6]))
		self.assertEquals(f(7), ([], [1, 4, 2, 8, 5, 7]))
		self.assertEquals(f(8), ([1, 2, 5], [0]))
		self.assertEquals(f(9), ([], [1]))
