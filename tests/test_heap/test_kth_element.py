"""Tests for Kth Element algorithms.

Tests Popperian Falsification Invariants:
    P1: kth_largest returns kth largest element
    P2: kth_smallest returns kth smallest element
    P3: top_k_frequent returns k most frequent
    P4: Results handle edge cases correctly
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.heap.kth_element import (
    kth_largest,
    kth_smallest,
    top_k_frequent,
)


class TestKthLargest(unittest.TestCase):
    """Unit tests for kth_largest."""

    def test_example1(self) -> None:
        """Test first example."""
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_example2(self) -> None:
        """Test second example."""
        self.assertEqual(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(kth_largest([1], 1), 1)


class TestKthSmallest(unittest.TestCase):
    """Unit tests for kth_smallest."""

    def test_example1(self) -> None:
        """Test first example."""
        self.assertEqual(kth_smallest([3, 2, 1, 5, 6, 4], 2), 2)

    def test_example2(self) -> None:
        """Test second example."""
        self.assertEqual(kth_smallest([7, 10, 4, 3, 20, 15], 3), 7)

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(kth_smallest([1], 1), 1)


class TestTopKFrequent(unittest.TestCase):
    """Unit tests for top_k_frequent."""

    def test_example(self) -> None:
        """Test standard example."""
        result = sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
        self.assertEqual(result, [1, 2])

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(top_k_frequent([1], 1), [1])


class TestKthElementInvariants(unittest.TestCase):
    """Popperian falsification tests for kth element invariants."""

    def test_p1_kth_largest_correct(self) -> None:
        """P1: kth_largest returns kth largest element."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 50)
            arr = [rng.randint(0, 100) for _ in range(n)]
            k = rng.randint(1, n)
            result = kth_largest(arr, k)
            sorted_desc = sorted(arr, reverse=True)
            self.assertEqual(result, sorted_desc[k - 1])

    def test_p2_kth_smallest_correct(self) -> None:
        """P2: kth_smallest returns kth smallest element."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 50)
            arr = [rng.randint(0, 100) for _ in range(n)]
            k = rng.randint(1, n)
            result = kth_smallest(arr, k)
            sorted_asc = sorted(arr)
            self.assertEqual(result, sorted_asc[k - 1])

    def test_p3_top_k_frequent_correct(self) -> None:
        """P3: top_k_frequent returns k most frequent."""
        arr = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        result = top_k_frequent(arr, 2)
        # 3 appears 4 times, 1 appears 3 times
        self.assertIn(3, result)
        self.assertIn(1, result)


if __name__ == "__main__":
    unittest.main()
