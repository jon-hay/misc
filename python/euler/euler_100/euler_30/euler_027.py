# coding=utf-8
"""
Euler discovered the remarkable quadratic formula: n**2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,40**2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41**2+41+41 is clearly divisible by 41.
The incredible formula n**2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n**2+an+b, where |a|<1000 and |b|≤1000
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
import unittest

from utils.math.seqs.seq_primes import SeqPrimes

def euler_027(limit):
	max_prime = 2 * limit ** 2 + limit
	primes = set(SeqPrimes().generate(max_val=max_prime))
	b_primes = {p for p in primes if p <= limit}

	closest_odd = limit - 1 if limit % 2 == 0 else limit
	a_odds = xrange(-closest_odd, closest_odd, 2)

	max_primes, max_a, max_b = 0, 0, 0
	for a in a_odds:
		for b in b_primes:
			curr_primes = 0
			for n in xrange(limit):
				value = n ** 2 + a * n + b
				if value in primes:
					curr_primes += 1
				else:
					if curr_primes > max_primes:
						max_primes, max_a, max_b = curr_primes, a, b
					break
	return max_a, max_b

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_027(41), (1, 41))
		self.assertEquals(euler_027(1601), (-79, 1601))
		self.assertEquals(euler_027(1000), (-61, 971))
