import unittest

from utils.helpers.helper_reduce import mul

def get_prime_factors(n):
	if n in [0, 1]:
		return {}

	assert n >= 2

	prime_factors = {}
	factor = 2
	while n > 1:
		if n % factor == 0:
			prime_factors[factor] = prime_factors.get(factor, 0) + 1
			n /= factor
		else:
			factor += 1
	return prime_factors

def get_num_factors(prime_factors=None, n=None):
	prime_factors = prime_factors or get_prime_factors(n)
	return mul(power + 1 for power in prime_factors.itervalues())

def get_factors(prime_factors=None, n=None):
	prime_factors = prime_factors or get_prime_factors(n)
	factors = {1}
	for prime_factor, power in prime_factors.iteritems():
		factors = {factor * prime_factor ** p for p in xrange(power + 1) for factor in factors}
	return factors

def sum_proper_factors(n):
	return sum(get_factors(n=n)) - n

def is_deficient(n):
	return sum_proper_factors(n) < n

def is_perfect(n):
	return sum_proper_factors(n) == n

def is_abundant(n):
	return sum_proper_factors(n) > n

def get_amicable_loop(n, loop_len):
	if n in [0, 1]:
		return []

	assert n >= 2
	assert loop_len >= 1

	succ = n
	amicable_loop = []
	for i in xrange(loop_len):
		succ = sum_proper_factors(succ)
		if succ in amicable_loop:
			return []
		amicable_loop.append(succ)

	if amicable_loop[-1] == n:
		return amicable_loop
	else:
		return []

def is_perfect_via_loop(n):
	return bool(get_amicable_loop(n, loop_len=1))

def is_amicable(n):
	return bool(get_amicable_loop(n, loop_len=2))

class Test(unittest.TestCase):
	def test_get_prime_factors(self):
		f = get_prime_factors
		self.assertEquals(f(n=1), {})
		self.assertEquals(f(n=2), {2: 1})
		self.assertEquals(f(n=36), {2: 2, 3: 2})

	def test_get_num_factors(self):
		f = get_num_factors
		self.assertEquals(f(n=1), 1)
		self.assertEquals(f(n=2), 2)
		self.assertEquals(f(n=36), 9)

	def test_get_factors(self):
		f = get_factors
		self.assertEquals(f(n=1), {1})
		self.assertEquals(f(n=2), {1, 2})
		self.assertEquals(f(n=36), {1, 2, 3, 4, 6, 9, 12, 18, 36})

	def test_get_amicable_partner(self):
		f = get_amicable_loop

		for n in xrange(3):
			for loop_len in xrange(1, 3):
				self.assertEquals(f(n=n, loop_len=loop_len), [])

		for n in [6, 28]:
			self.assertEquals(f(n, loop_len=1), [n])
			self.assertEquals(f(n, loop_len=2), [])

		self.assertEquals(f(220, loop_len=2), [284, 220])
		self.assertEquals(f(284, loop_len=2), [220, 284])
