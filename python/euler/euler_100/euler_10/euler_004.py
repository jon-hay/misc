# coding=utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import unittest

from utils.helpers.helper_string import is_palindrome

def euler_004(limit):
	result = 0
	for i in xrange(limit, limit / 10 - 1, -1):
		for j in xrange(limit, limit / 10 - 1, -1):
			n = i * j
			if n > result and is_palindrome(n):
				result = n
	return result

class Test(unittest.TestCase):
	def test(self):
		self.assertEquals(euler_004(limit=100), 9009)
		self.assertEquals(euler_004(limit=1000), 906609)
