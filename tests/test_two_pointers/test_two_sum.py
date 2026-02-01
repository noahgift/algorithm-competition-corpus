"""Tests for Two Sum algorithms.

Tests Popperian Falsification Invariants:
    P1: If found, elements sum to target
    P2: Indices are valid within array bounds
    P3: Works on sorted arrays (two_sum_sorted)
    P4: Three sum finds all unique triplets
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.two_pointers.two_sum import (
    three_sum,
    two_sum_sorted,
)


class TestTwoSumSorted(unittest.TestCase):
    """Unit tests for two_sum_sorted."""

    def test_found(self) -> None:
        """Test finding pair."""
        result = two_sum_sorted([2, 7, 11, 15], 9)
        self.assertEqual(result, (0, 1))

    def test_middle_pair(self) -> None:
        """Test pair in middle."""
        result = two_sum_sorted([2, 3, 4], 6)
        self.assertEqual(result, (0, 2))

    def test_not_found(self) -> None:
        """Test no pair exists."""
        result = two_sum_sorted([1, 2, 3], 10)
        self.assertIsNone(result)

    def test_empty(self) -> None:
        """Test empty array."""
        result = two_sum_sorted([], 5)
        self.assertIsNone(result)


class TestThreeSum(unittest.TestCase):
    """Unit tests for three_sum."""

    def test_found_triplets(self) -> None:
        """Test finding triplets."""
        result = sorted(three_sum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual(result, [(-1, -1, 2), (-1, 0, 1)])

    def test_no_triplets(self) -> None:
        """Test no triplets exist."""
        result = three_sum([0, 1, 1])
        self.assertEqual(result, [])

    def test_all_zeros(self) -> None:
        """Test all zeros."""
        result = three_sum([0, 0, 0])
        self.assertEqual(result, [(0, 0, 0)])


class TestTwoSumInvariants(unittest.TestCase):
    """Popperian falsification tests for two sum invariants."""

    def test_p1_sum_equals_target(self) -> None:
        """P1: If found, elements sum to target."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 50)
            arr = sorted({rng.randint(0, 100) for _ in range(n)})
            if len(arr) < 2:
                continue
            # Pick two random elements and compute target
            i = rng.randint(0, len(arr) - 2)
            j = rng.randint(i + 1, len(arr) - 1)
            target = arr[i] + arr[j]
            result = two_sum_sorted(arr, target)
            if result is not None:
                self.assertEqual(arr[result[0]] + arr[result[1]], target)

    def test_p2_indices_valid(self) -> None:
        """P2: Indices are valid within array bounds."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 50)
            arr = sorted(rng.randint(0, 100) for _ in range(n))
            target = rng.randint(0, 200)
            result = two_sum_sorted(arr, target)
            if result is not None:
                self.assertGreaterEqual(result[0], 0)
                self.assertLess(result[1], len(arr))
                self.assertLess(result[0], result[1])

    def test_p4_three_sum_all_unique(self) -> None:
        """P4: Three sum finds all unique triplets."""
        arr = [-1, 0, 1, 2, -1, -4]
        result = three_sum(arr)
        # Check uniqueness
        result_set = set(result)
        self.assertEqual(len(result), len(result_set))
        # Check all sum to 0
        for triplet in result:
            self.assertEqual(sum(triplet), 0)


if __name__ == "__main__":
    unittest.main()
