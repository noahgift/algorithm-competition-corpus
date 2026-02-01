"""Tests for Advanced Linked List algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.linked_list.list_advanced import (
    add_two_numbers,
    is_palindrome_list,
    rotate_right,
)
from algorithm_corpus.linked_list.list_node import from_list
from algorithm_corpus.linked_list.list_ops import to_list


class TestAddTwoNumbers(unittest.TestCase):
    """Unit tests for add_two_numbers."""

    def test_basic(self) -> None:
        """Test basic case."""
        l1 = from_list([2, 4, 3])
        l2 = from_list([5, 6, 4])
        result = add_two_numbers(l1, l2)
        self.assertEqual(to_list(result), [7, 0, 8])


class TestRotateRight(unittest.TestCase):
    """Unit tests for rotate_right."""

    def test_basic(self) -> None:
        """Test basic case."""
        head = from_list([1, 2, 3, 4, 5])
        result = rotate_right(head, 2)
        self.assertEqual(to_list(result), [4, 5, 1, 2, 3])

    def test_empty(self) -> None:
        """Test empty."""
        self.assertIsNone(rotate_right(None, 1))


class TestIsPalindromeList(unittest.TestCase):
    """Unit tests for is_palindrome_list."""

    def test_palindrome(self) -> None:
        """Test palindrome."""
        self.assertTrue(is_palindrome_list(from_list([1, 2, 2, 1])))

    def test_not_palindrome(self) -> None:
        """Test not palindrome."""
        self.assertFalse(is_palindrome_list(from_list([1, 2])))


if __name__ == "__main__":
    unittest.main()
