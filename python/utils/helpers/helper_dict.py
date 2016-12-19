import unittest

def get_dict_keys(dicts):
	return {key for d in dicts for key in d}

def combine_dicts(dicts, combiner, default=None):
	return {key: combiner([d.get(key, default) for d in dicts]) for key in get_dict_keys(dicts)}

class Test(unittest.TestCase):
	def test_get_dict_keys(self):
		f = get_dict_keys
		self.assertEquals(f([{}]), set())
		self.assertEquals(f([{1: 2}]), {1})
		self.assertEquals(f([{}, {1: 1}, {1: 1, 2: 2}, {1: 1, 3: 3}]), {1, 2, 3})

	def test_combine_dicts(self):
		f = lambda dicts: combine_dicts(dicts, sum, 1)

		dict_0 = {}
		dict_1 = {"a": 100, "b": 200}
		dict_2 = {"a": 1000, "c": 300}

		self.assertEquals(f([dict_0]), dict_0)
		self.assertEquals(f([dict_1]), dict_1)
		self.assertEquals(f([dict_0, dict_1, dict_2]), {"a": 1101, "b": 202, "c": 302})
