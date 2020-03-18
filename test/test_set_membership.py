import unittest
from more_fun_with_collections import set_membership as a


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(a.in_set({1, 2, 3}, 1))

    def test_in_set_false(self):
        self.assertFalse(a.in_set({1, 2, 3}, 4))


if __name__ == '__main__':
    unittest.main()
