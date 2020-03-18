import unittest
from more_fun_with_collections import set_membership as a
from more_fun_with_collections import dict_membership as b


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(a.in_set({1, 2, 3}, 1))

    def test_in_set_false(self):
        self.assertFalse(a.in_set({1, 2, 3}, 4))

    def test_in_dict_true(self):
        self.assertTrue(b.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'F'))

    def test_in_dict_false(self):
        self.assertFalse(b.in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'Q'))


if __name__ == '__main__':
    unittest.main()
