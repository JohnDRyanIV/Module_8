import unittest
from more_fun_with_collections import assign_average as a


class MyTestCase(unittest.TestCase):

    def test_keys(self):  # Including all keys in one test due to similarity of tests
        self.assertEqual(a.switch_average('A'), 90)
        self.assertEqual(a.switch_average('B'), 80)
        self.assertEqual(a.switch_average('C'), 70)
        self.assertEqual(a.switch_average('D'), 60)
        self.assertEqual(a.switch_average('F'),  0)

    def test_non_key(self):
        self.assertEqual(a.switch_average('Q'), KeyError)


if __name__ == '__main__':
    unittest.main()
