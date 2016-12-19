"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import unittest

from utils.math.seqs.seq_perfect import SeqAbundant

def euler_023(limit):
	abundant_numbers = SeqAbundant().get_list(max_val=limit)
	abundant_sums = {m + n for m in abundant_numbers for n in abundant_numbers}
	non_abundant_sums = set(xrange(1, limit + 1)).difference(abundant_sums)
	return sum(non_abundant_sums)

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_023(28123), 4179871)
