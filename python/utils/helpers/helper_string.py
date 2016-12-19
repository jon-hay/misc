import unittest

def is_palindrome(s):
	s = str(s)
	return s == s[::-1]

class Test(unittest.TestCase):
	def test_is_palindrome(self):
		f = is_palindrome
		self.assertEquals(f(""), True)
		self.assertEquals(f("a"), True)
		self.assertEquals(f("aba"), True)
		self.assertEquals(f("abba"), True)
		self.assertEquals(f("abbaa"), False)
		self.assertEquals(f(121), True)
