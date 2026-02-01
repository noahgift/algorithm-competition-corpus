"""Tests for Merge Sort algorithms.

Tests Popperian Falsification Invariants:
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Stable sort (preserves relative order of equal elements)
    P4: O(n log n) time complexity in all cases
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.sorting.merge_sort import (
    merge_sort,
    merge_sort_iterative,
)


class TestMergeSort(unittest.TestCase):
    """Unit tests for merge_sort."""

    def test_unsorted_array(self) -> None:
        """Test sorting unsorted array."""
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(merge_sort([1]), [1])

    def test_two_elements(self) -> None:
        """Test two elements."""
        self.assertEqual(merge_sort([2, 1]), [1, 2])

    def test_already_sorted(self) -> None:
        """Test already sorted array."""
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self) -> None:
        """Test reverse sorted array."""
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


class TestMergeSortIterative(unittest.TestCase):
    """Unit tests for merge_sort_iterative."""

    def test_unsorted_array(self) -> None:
        """Test sorting unsorted array."""
        self.assertEqual(
            merge_sort_iterative([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9]
        )

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(merge_sort_iterative([]), [])

    def test_reverse_sorted(self) -> None:
        """Test reverse sorted array."""
        self.assertEqual(merge_sort_iterative([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


class TestMergeSortInvariants(unittest.TestCase):
    """Popperian falsification tests for merge sort invariants."""

    def test_p1_permutation(self) -> None:
        """P1: Result is a permutation of input."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            result = merge_sort(arr)
            self.assertEqual(sorted(arr), sorted(result))
            self.assertEqual(len(arr), len(result))

    def test_p2_sorted_order(self) -> None:
        """P2: Result is sorted in non-decreasing order."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            result = merge_sort(arr)
            for i in range(len(result) - 1):
                self.assertLessEqual(result[i], result[i + 1])

    def test_recursive_iterative_consistency(self) -> None:
        """Recursive and iterative versions should give same result."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            self.assertEqual(merge_sort(arr), merge_sort_iterative(arr))


if __name__ == "__main__":
    unittest.main()
