import unittest

from utils.math.seqs.bases.seq_base import SeqBase

FIRST_PRIME = 2

class SeqPrimes(SeqBase):
	_primes = [FIRST_PRIME]

	def _get_init_vals(self):
		return self._primes

	def _get_next_val(self):
		n = self.curr_vals[-1] + 1
		while not self._is_prime(n):
			n += 1
		self._primes.append(n)
		return n

	def _reset(self):
		super(SeqPrimes, self)._reset()
		self._primes = [FIRST_PRIME]

	def generate(self, max_idx=None, max_val=None):
		if max_val is not None:
			return self._get_primes_using_sieve(max_val)
		else:
			return super(SeqPrimes, self).generate(max_idx=max_idx, max_val=max_val)

	def _is_prime(self, n):
		for prime in self._primes:
			if n % prime == 0:
				return False
		return True

	@staticmethod
	def _get_primes_using_sieve(max_val):
		primes = set()
		composites = set()
		for i in xrange(FIRST_PRIME, max_val + 1):
			if i in composites:
				continue
			primes.add(i)
			for j in xrange(i * 2, max_val + 1, i):
				composites.add(j)
		return primes

class Test(unittest.TestCase):
	def test_get_primes(self):
		seq = SeqPrimes()
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [2])
		self.assertEquals(f(max_idx=2), [2, 3])
		self.assertEquals(f(max_idx=7), [2, 3, 5, 7, 11, 13, 17])

		self.assertEquals(f(max_val=0), [])
		self.assertEquals(f(max_val=1), [])
		self.assertEquals(f(max_val=2), [2])
		self.assertEquals(f(max_val=7), [2, 3, 5, 7])
