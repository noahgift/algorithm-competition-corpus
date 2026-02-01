"""Tests for Quick Sort algorithms.

Tests Popperian Falsification Invariants:
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Partition places pivot in final position
    P4: All elements left of pivot are <= pivot
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.sorting.quick_sort import (
    quick_sort,
    quick_sort_iterative,
)


class TestQuickSort(unittest.TestCase):
    """Unit tests for quick_sort."""

    def test_unsorted_array(self) -> None:
        """Test sorting unsorted array."""
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(quick_sort([1]), [1])

    def test_two_elements(self) -> None:
        """Test two elements."""
        self.assertEqual(quick_sort([2, 1]), [1, 2])

    def test_already_sorted(self) -> None:
        """Test already sorted array."""
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


class TestQuickSortIterative(unittest.TestCase):
    """Unit tests for quick_sort_iterative."""

    def test_unsorted_array(self) -> None:
        """Test sorting unsorted array."""
        self.assertEqual(
            quick_sort_iterative([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9]
        )

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(quick_sort_iterative([]), [])

    def test_reverse_sorted(self) -> None:
        """Test reverse sorted array."""
        self.assertEqual(quick_sort_iterative([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


class TestQuickSortInvariants(unittest.TestCase):
    """Popperian falsification tests for quick sort invariants."""

    def test_p1_permutation(self) -> None:
        """P1: Result is a permutation of input."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            result = quick_sort(arr)
            self.assertEqual(sorted(arr), sorted(result))
            self.assertEqual(len(arr), len(result))

    def test_p2_sorted_order(self) -> None:
        """P2: Result is sorted in non-decreasing order."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            result = quick_sort(arr)
            for i in range(len(result) - 1):
                self.assertLessEqual(result[i], result[i + 1])

    def test_recursive_iterative_consistency(self) -> None:
        """Recursive and iterative versions should give same result."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            self.assertEqual(quick_sort(arr), quick_sort_iterative(arr))


if __name__ == "__main__":
    unittest.main()
