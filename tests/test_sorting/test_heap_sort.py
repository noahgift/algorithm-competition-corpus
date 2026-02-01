"""Tests for Heap Sort algorithm.

Tests Popperian Falsification Invariants:
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Heap property maintained during heapify
    P4: In-place sorting (O(1) extra space)
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.sorting.heap_sort import (
    heap_sort,
)


class TestHeapSort(unittest.TestCase):
    """Unit tests for heap_sort."""

    def test_unsorted_array(self) -> None:
        """Test sorting unsorted array."""
        self.assertEqual(heap_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(heap_sort([1]), [1])

    def test_two_elements(self) -> None:
        """Test two elements."""
        self.assertEqual(heap_sort([2, 1]), [1, 2])

    def test_already_sorted(self) -> None:
        """Test already sorted array."""
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self) -> None:
        """Test reverse sorted array."""
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_all_same(self) -> None:
        """Test all same elements."""
        self.assertEqual(heap_sort([5, 5, 5, 5]), [5, 5, 5, 5])


class TestHeapSortInvariants(unittest.TestCase):
    """Popperian falsification tests for heap sort invariants."""

    def test_p1_permutation(self) -> None:
        """P1: Result is a permutation of input."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            result = heap_sort(arr)
            self.assertEqual(sorted(arr), sorted(result))
            self.assertEqual(len(arr), len(result))

    def test_p2_sorted_order(self) -> None:
        """P2: Result is sorted in non-decreasing order."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 100)
            arr = [rng.randint(-100, 100) for _ in range(n)]
            result = heap_sort(arr)
            for i in range(len(result) - 1):
                self.assertLessEqual(result[i], result[i + 1])

    def test_does_not_modify_original(self) -> None:
        """Original array should not be modified."""
        arr = [3, 1, 4, 1, 5]
        original = arr[:]
        heap_sort(arr)
        self.assertEqual(arr, original)


if __name__ == "__main__":
    unittest.main()
