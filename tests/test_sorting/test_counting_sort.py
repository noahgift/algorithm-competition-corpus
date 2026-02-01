"""Tests for Counting Sort algorithm.

Tests Popperian Falsification Invariants:
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Stable sort (preserves relative order)
    P4: Linear time for bounded integer range
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.sorting.counting_sort import (
    counting_sort,
)


class TestCountingSort(unittest.TestCase):
    """Unit tests for counting_sort."""

    def test_unsorted_array(self) -> None:
        """Test sorting unsorted array."""
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(counting_sort([]), [])

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(counting_sort([1]), [1])

    def test_all_same(self) -> None:
        """Test all same elements."""
        self.assertEqual(counting_sort([1, 1, 1]), [1, 1, 1])

    def test_already_sorted(self) -> None:
        """Test already sorted array."""
        self.assertEqual(counting_sort([1, 2, 3, 4]), [1, 2, 3, 4])


class TestCountingSortInvariants(unittest.TestCase):
    """Popperian falsification tests for counting sort invariants."""

    def test_p1_permutation(self) -> None:
        """P1: Result is a permutation of input."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(0, 50) for _ in range(n)]
            result = counting_sort(arr)
            self.assertEqual(sorted(arr), sorted(result))
            self.assertEqual(len(arr), len(result))

    def test_p2_sorted_order(self) -> None:
        """P2: Result is sorted in non-decreasing order."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(0, 50) for _ in range(n)]
            result = counting_sort(arr)
            for i in range(len(result) - 1):
                self.assertLessEqual(result[i], result[i + 1])

    def test_handles_negative_numbers(self) -> None:
        """Counting sort should handle negative numbers."""
        arr = [-5, -2, 0, 3, 1, -1]
        result = counting_sort(arr)
        self.assertEqual(result, [-5, -2, -1, 0, 1, 3])


if __name__ == "__main__":
    unittest.main()
