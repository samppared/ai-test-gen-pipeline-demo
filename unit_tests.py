from unit_tests import *
from code_to_be_tested import *
import unittest

class TestSimpleFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_addition(self):
        self.assertEqual(addition(2, 3), 6)
        self.assertEqual(addition(-1, 1), -1)
        self.assertEqual(addition(0, 5), 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concatenate_strings("", "Test"), "Test")
        self.assertEqual(concatenate_strings("Test", ""), "Test")

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([-1, -2, -3]), -1)
        self.assertEqual(find_max([]), None)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()))

if __name__ == '__main__':
    unittest.main()
