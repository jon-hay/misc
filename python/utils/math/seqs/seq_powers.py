import unittest

from utils.math.seqs.bases.seq_func import SeqFunc
from utils.math.seqs.bases.seq_reduce import SeqSums

def get_triangle(n):
	return n * (n + 1) / 2

class SeqPowers(SeqFunc):
	def __init__(self, power):
		self.power = power
		super(SeqPowers, self).__init__(lambda n: n ** self.power)

class SeqNaturals(SeqPowers):
	def __init__(self):
		super(SeqNaturals, self).__init__(1)

class SeqSquares(SeqPowers):
	def __init__(self):
		super(SeqSquares, self).__init__(2)

class SeqCubes(SeqPowers):
	def __init__(self):
		super(SeqCubes, self).__init__(3)

class SeqPowerSums(SeqSums):
	def __init__(self, power):
		super(SeqPowerSums, self).__init__(SeqPowers(power))

class SeqTriangles(SeqPowerSums):
	def __init__(self):
		super(SeqTriangles, self).__init__(1)

class Test(unittest.TestCase):
	def test_get_naturals(self):
		seq = SeqNaturals()
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [1])
		self.assertEquals(f(max_idx=10), range(1, 11))

		self.assertEquals(f(max_val=0), [])
		self.assertEquals(f(max_val=1), [1])
		self.assertEquals(f(max_val=10), range(1, 11))

	def test_get_squares(self):
		seq = SeqSquares()
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [1])
		self.assertEquals(f(max_idx=9), [1, 4, 9, 16, 25, 36, 49, 64, 81])

		self.assertEquals(f(max_val=0), [])
		self.assertEquals(f(max_val=1), [1])
		self.assertEquals(f(max_val=9), [1, 4, 9])

	def test_get_triangles(self):
		seq = SeqTriangles()
		f = seq.get_list

		self.assertEquals(f(max_idx=0), [])
		self.assertEquals(f(max_idx=1), [1])
		self.assertEquals(f(max_idx=10), [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

		self.assertEquals(f(max_val=0), [])
		self.assertEquals(f(max_val=1), [1])
		self.assertEquals(f(max_val=10), [1, 3, 6, 10])
