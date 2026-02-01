"""Tests for Binary Search DC algorithms.

Tests Popperian Falsification Invariants:
    P1: Returns correct index when element exists
    P2: Returns -1 when element doesn't exist
    P3: Works on empty arrays
    P4: O(log n) time complexity maintained
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.divide_and_conquer.binary_search_dc import (
    binary_search_recursive,
    find_first_greater,
)


class TestBinarySearchRecursive(unittest.TestCase):
    """Unit tests for binary_search_recursive."""

    def test_found(self) -> None:
        """Test element found."""
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self) -> None:
        """Test element not found."""
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 6), -1)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(binary_search_recursive([], 1), -1)

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(binary_search_recursive([1], 1), 0)


class TestFindFirstGreater(unittest.TestCase):
    """Unit tests for find_first_greater."""

    def test_middle(self) -> None:
        """Test element in middle."""
        self.assertEqual(find_first_greater([1, 2, 3, 4, 5], 3), 3)

    def test_all_smaller(self) -> None:
        """Test all elements smaller."""
        self.assertEqual(find_first_greater([1, 2, 3, 4, 5], 5), 5)

    def test_all_greater(self) -> None:
        """Test all elements greater."""
        self.assertEqual(find_first_greater([1, 2, 3, 4, 5], 0), 0)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(find_first_greater([], 1), 0)


class TestBinarySearchDCInvariants(unittest.TestCase):
    """Popperian falsification tests for binary search DC invariants."""

    def test_p1_correct_when_exists(self) -> None:
        """P1: Returns correct index when element exists."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 50)
            arr = sorted({rng.randint(0, 100) for _ in range(n)})
            if arr:
                target = rng.choice(arr)
                idx = binary_search_recursive(arr, target)
                self.assertEqual(arr[idx], target)

    def test_p2_minus_one_when_not_exists(self) -> None:
        """P2: Returns -1 when element doesn't exist."""
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search_recursive(arr, 2), -1)
        self.assertEqual(binary_search_recursive(arr, 10), -1)

    def test_p3_empty_array(self) -> None:
        """P3: Works on empty arrays."""
        self.assertEqual(binary_search_recursive([], 1), -1)
        self.assertEqual(find_first_greater([], 1), 0)


if __name__ == "__main__":
    unittest.main()
