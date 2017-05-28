import json
import random
import timeit


def _heap_setup(heap_class):
	return "from data_structures import heap; heap_obj = heap.{heap_class}()".format(heap_class=heap_class)


def _benchmark_base(heap_classes, benchmark_name, heap_stmt):
	print benchmark_name

	for exp in xrange(4, 7):
		n = 10 ** exp
		print "n: {n}".format(n=n)

		stmt = heap_stmt(n)

		for heap_class in heap_classes:
			setup = _heap_setup(heap_class)
			result = "%.3f" % timeit.timeit(setup=setup, stmt=stmt, number=1)
			print "{0: >20}".format(heap_class), result


def _benchmark_heapify(heap_classes):
	def _heap_stmt(n):
		items = range(n)
		random.shuffle(items)
		items = json.dumps(items)
		return "heap_obj.heapify({items})".format(items=items)

	return _benchmark_base(heap_classes, "Heapify", _heap_stmt)


def _benchmark_heap_operations(heap_classes):
	def _heap_stmt(n):
		ops = []
		for i in xrange(n):
			op = random.choice(["push", "pop", "pushpop", "poppush"])
			item = random.randint(0, 20)
			ops.append((op, {"item": item}))
		ops = json.dumps(ops)
		return "heap_obj.apply_all({ops})".format(ops=ops)

	return _benchmark_base(heap_classes, "Heap Operations", _heap_stmt)


def _benchmark():
	heap_classes = [
		"MinHeap",
		"MinHeapPython",
	]

	for benchmark in [
		_benchmark_heapify,
		_benchmark_heap_operations,
	]:
		benchmark(heap_classes)


if __name__ == "__main__":
	_benchmark()
