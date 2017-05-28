import copy
import heapq
import random
import unittest


class MinHeapBase(object):
	def __init__(self):
		self.clear()

	def clear(self):
		self.items = []

	def is_empty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[0]

	def apply(self, op, **kwargs):
		if op == "pop":
			kwargs = {}

		if op.startswith("pop") and self.is_empty():
			return None

		return getattr(self, op)(**kwargs)

	def apply_all(self, ops):
		for op, kwargs in ops:
			self.apply(op, **kwargs)

	def heapify(self, items):
		raise NotImplementedError

	def push(self, item):
		raise NotImplementedError

	def pop(self):
		raise NotImplementedError

	def pushpop(self, item):
		raise NotImplementedError

	def poppush(self, item):
		raise NotImplementedError


class MinHeapPython(MinHeapBase):
	def heapify(self, items):
		self.items = copy.copy(list(items))
		return heapq.heapify(self.items)

	def push(self, item):
		return heapq.heappush(self.items, item)

	def pop(self):
		return heapq.heappop(self.items)

	def pushpop(self, item):
		return heapq.heappushpop(self.items, item)

	def poppush(self, item):
		return heapq.heapreplace(self.items, item)


class MinHeap(MinHeapBase):
	def heapify(self, items):
		self.items = copy.copy(list(items))
		last_child_index = self.size() - 1
		last_parent_index = self._parent_index(last_child_index)
		for i in xrange(last_parent_index, -1, -1):
			self._sift_down(i)

	def push(self, item):
		self.items.append(item)
		self._sift_up(self.size() - 1)

	def pop(self):
		root = self.items[0]
		self.items[0] = self.items[-1]
		del self.items[-1]

		if not self.is_empty():
			self._sift_down(0)

		return root

	def pushpop(self, item):
		if self.is_empty():
			return item

		root = self.items[0]
		if item < root:
			return item

		self.items[0] = item
		self._sift_down(0)
		return root

	def poppush(self, item):
		root = self.items[0]
		self.items[0] = item
		self._sift_down(0)
		return root

	@staticmethod
	def _parent_index(index):
		return (index + 1) / 2 - 1

	@staticmethod
	def _left_child_index(index):
		return (index + 1) * 2 - 1

	@staticmethod
	def _right_child_index(index):
		return (index + 1) * 2

	def _sift_up(self, index):
		item = self.items[index]

		while index:
			parent_index = self._parent_index(index)
			parent = self.items[parent_index]

			if item < parent:
				self.items[index] = parent
				index = parent_index
			else:
				break

		self.items[index] = item

	def _sift_down(self, index):
		size = self.size()
		item = self.items[index]

		while index < size:
			left_child_index = self._left_child_index(index)
			if left_child_index >= size:
				break

			right_child_index = self._right_child_index(index)
			if right_child_index >= size:
				min_child_index = left_child_index
			else:
				left_child = self.items[left_child_index]
				right_child = self.items[right_child_index]
				if left_child < right_child:
					min_child_index = left_child_index
				else:
					min_child_index = right_child_index

			min_child = self.items[min_child_index]
			if min_child < item:
				self.items[index] = min_child
				index = min_child_index
			else:
				break

		self.items[index] = item


class Test(unittest.TestCase):
	heaps = [MinHeap(), MinHeapPython()]

	def test_heapify(self):
		items = range(10000)
		random.shuffle(items)

		results = []
		for heap in self.heaps:
			heap.heapify(items)

			result = []
			while not heap.is_empty():
				result.append(heap.pop())

			results.append(result)

		self.assertEqual(results[0], results[1])

	def test_heap(self):
		for heap in self.heaps:
			heap.clear()

		for i in xrange(10000):
			op = random.choice(["push", "pop", "pushpop", "poppush"])
			item = random.randint(0, 20)

			results = [heap.apply(op, item=item) for heap in self.heaps]
			self.assertEquals(len(set(results)), 1)

			sizes = [heap.size() for heap in self.heaps]
			self.assertEquals(len(set(sizes)), 1)
