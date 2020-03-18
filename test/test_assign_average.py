import unittest
from more_fun_with_collections import assign_average as a
DICT_TEST = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}


class MyTestCase(unittest.TestCase):

    def test_keys(self):  # Including all keys in one test due to similarity of tests
        self.assertEqual(a.switch_average(DICT_TEST, 'A'), 90)
        self.assertEqual(a.switch_average(DICT_TEST, 'B'), 80)
        self.assertEqual(a.switch_average(DICT_TEST, 'C'), 70)
        self.assertEqual(a.switch_average(DICT_TEST, 'D'), 60)
        self.assertEqual(a.switch_average(DICT_TEST, 'F'),  0)

    def test_non_key(self):
        self.assertEqual(a.switch_average(DICT_TEST, 'Q'), ValueError)



if __name__ == '__main__':
    unittest.main()
