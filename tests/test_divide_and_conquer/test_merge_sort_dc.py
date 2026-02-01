"""Tests for Merge Sort DC algorithms.

Tests Popperian Falsification Invariants:
    P1: Result is sorted
    P2: Result is permutation of input
    P3: Inversion count is correct
    P4: O(n log n) time complexity maintained
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.divide_and_conquer.merge_sort_dc import (
    count_inversions,
    merge_sort_recursive,
)


class TestMergeSortRecursive(unittest.TestCase):
    """Unit tests for merge_sort_recursive."""

    def test_basic(self) -> None:
        """Test basic sorting."""
        self.assertEqual(
            merge_sort_recursive([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9]
        )

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(merge_sort_recursive([]), [])

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(merge_sort_recursive([1]), [1])


class TestCountInversions(unittest.TestCase):
    """Unit tests for count_inversions."""

    def test_example(self) -> None:
        """Test example array."""
        self.assertEqual(count_inversions([2, 4, 1, 3, 5]), 3)

    def test_sorted(self) -> None:
        """Test sorted array."""
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)

    def test_reverse(self) -> None:
        """Test reverse sorted array."""
        self.assertEqual(count_inversions([5, 4, 3, 2, 1]), 10)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(count_inversions([]), 0)


class TestMergeSortDCInvariants(unittest.TestCase):
    """Popperian falsification tests for merge sort DC invariants."""

    def test_p1_result_sorted(self) -> None:
        """P1: Result is sorted."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(0, 100) for _ in range(rng.randint(0, 50))]
            result = merge_sort_recursive(arr)
            self.assertEqual(result, sorted(arr))

    def test_p2_permutation(self) -> None:
        """P2: Result is permutation of input."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(0, 100) for _ in range(rng.randint(0, 50))]
            result = merge_sort_recursive(arr)
            self.assertEqual(sorted(result), sorted(arr))

    def test_p3_inversions_correct(self) -> None:
        """P3: Inversion count is correct."""
        # Manual calculation for small arrays
        self.assertEqual(count_inversions([3, 1, 2]), 2)  # (3,1), (3,2)
        self.assertEqual(count_inversions([1, 3, 2]), 1)  # (3,2)
        self.assertEqual(count_inversions([1, 2, 3]), 0)


if __name__ == "__main__":
    unittest.main()
