import unittest
import sys
from pathlib import Path

# Add parent directory to path to import functions module
sys.path.insert(0, str(Path(__file__).parent.parent))

from functions import add, multiply, is_even, reverse_string, find_max


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-5, 10), 5)


class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)


class TestIsEvenFunction(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_zero(self):
        self.assertTrue(is_even(0))


class TestReverseStringFunction(unittest.TestCase):
    def test_reverse_simple_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")


class TestFindMaxFunction(unittest.TestCase):
    def test_find_max_positive_numbers(self):
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)

    def test_find_max_negative_numbers(self):
        self.assertEqual(find_max([-1, -5, -3]), -1)

    def test_find_max_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_find_max_single_element(self):
        self.assertEqual(find_max([42]), 42)


if __name__ == '__main__':
    unittest.main()
