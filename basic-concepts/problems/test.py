import unittest

import a_maximum_sub_array_sum


class TestMaximumSubArraySum(unittest.TestCase):
    def test_o_n_3(self):
        self.assertEqual(a_maximum_sub_array_sum.maximum_sub_array_sum_1([-1, 2, 4, -3, 5, 2, -5, 2]), 10)

    def test_o_n_2(self):
        self.assertEqual(a_maximum_sub_array_sum.maximum_sub_array_sum_2([-1, 2, 4, -3, 5, 2, -5, 2]), 10)

    def test_o_n(self):
        self.assertEqual(a_maximum_sub_array_sum.maximum_sub_array_sum_3([-1, 2, 4, -3, 5, 2, -5, 2]), 10)


if __name__ == '__main__':
    unittest.main()
