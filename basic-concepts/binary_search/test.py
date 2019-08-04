import unittest

import a_binary_search


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.x = [1, 2, 4, 7, 10, 12, 46, 243, 243, 2334]
        self.start = 0
        self.len = len(self.x)

    def test_binary_search_recur(self):
        self.assertTrue(a_binary_search.binary_search_recur(self.x, 10, self.start, self.len), )
        self.assertFalse(a_binary_search.binary_search_recur(self.x, 100, self.start, self.len), )
        self.assertFalse(a_binary_search.binary_search_recur(self.x, -1, self.start, self.len), )

    def test_binary_search_iter(self):
        self.assertTrue(a_binary_search.binary_search_iter(self.x, 10, self.start, self.len), )
        self.assertFalse(a_binary_search.binary_search_iter(self.x, 100, self.start, self.len), )
        self.assertFalse(a_binary_search.binary_search_iter(self.x, -1, self.start, self.len), )

    def test_binary_search_jump(self):
        self.assertTrue(a_binary_search.binary_search_jump(self.x, 10), )
        self.assertFalse(a_binary_search.binary_search_jump(self.x, 100), )
        self.assertFalse(a_binary_search.binary_search_jump(self.x, -1), )


class TestBinarySearchFunc(unittest.TestCase):
    def setUp(self):
        self.example = lambda x: x >= 569857489
        self.example2 = lambda x: -x ** 2 + 4 * x - 4

    def test_find_changing_point(self):
        self.assertEqual(a_binary_search.find_changing_point(self.example, 0, 1000000000), 569857489)

    def test_find_maximum_point(self):
        self.assertEqual(a_binary_search.find_maximum_point(self.example2, 0, 10), 2)


if __name__ == '__main__':
    unittest.main()
