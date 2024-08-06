from code_to_be_tested import *
import unittest

class TestFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_addition(self):
        self.assertEqual(addition(2, 3), 6)
        self.assertEqual(addition(-1, 1), -1)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concatenate_strings("", "Test"), "Test")

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4]), 4)
        self.assertEqual(find_max([-1, -2, -3]), -1)
        self.assertIsNone(find_max([]))

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
