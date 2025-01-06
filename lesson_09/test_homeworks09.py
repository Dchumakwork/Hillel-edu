import unittest
from homeworks import only_strings_finder, sum_even, average, back_string

class TestStringFinderFunc(unittest.TestCase):
    def test_all_str(self):
        result = only_strings_finder(["fstStr", "secStr", "thrdStr"])
        self.assertEqual(result, ["fstStr", "secStr", "thrdStr"])
    def test_not_all_str(self):
        result = only_strings_finder(["fstStr", 1, "secStr", 2, "thrdStr", True])
        self.assertEqual(result, ["fstStr", "secStr", "thrdStr"])
    def test_empty(self):
        result = only_strings_finder([])
        self.assertEqual(result, [])

class TestSumEvenFunc(unittest.TestCase):
    def test_simple(self):
        result = sum_even([1,2,3,4,5,6,10,11,12])
        self.assertEqual(result, 34)
    def test_odds(self):
        result = sum_even([1,3,5,7,9,77])
        self.assertEqual(result, 0)
    def test_empty(self):
        result = sum_even([])
        self.assertEqual(result, 0)

class TestAverageFunc(unittest.TestCase):
    def test_simple(self):
        result = average([1,2,3,4])
        self.assertEqual(result, 2.5)
    def test_one(self):
        result = average([1000])
        self.assertEqual(result, 1000)
    def test_empty(self):
        result = average([])
        self.assertNotEqual(result, 0)

class TestBackStringFunc(unittest.TestCase):
    def test_simple(self):
        result = back_string("asdf")
        self.assertEqual(result, "fdsa")
    def test_2(self):
        result = back_string("12345")
        self.assertEqual(result, "54321")
    def test_empty(self):
        result = back_string("")
        self.assertEqual(result, "")



if __name__ == '__main__':
    unittest.main(verbosity=0)