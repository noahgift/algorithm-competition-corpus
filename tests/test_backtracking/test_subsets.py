"""Tests for Subset and Combination algorithms.

Tests Popperian Falsification Invariants:
    P1: All subsets are valid subsets of input
    P2: Correct number of subsets (2^N)
    P3: No duplicate subsets
    P4: combinations(n, k) returns C(n, k) results
"""

from __future__ import annotations

import math
import unittest

from algorithm_corpus.backtracking.subsets import (
    combinations,
    subsets,
)


class TestSubsets(unittest.TestCase):
    """Unit tests for subsets."""

    def test_three_elements(self) -> None:
        """Test three elements."""
        result = sorted([sorted(s) for s in subsets([1, 2, 3])])
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(result, expected)

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(subsets([]), [[]])

    def test_single(self) -> None:
        """Test single element."""
        result = sorted(subsets([1]))
        self.assertEqual(result, [[], [1]])


class TestCombinations(unittest.TestCase):
    """Unit tests for combinations."""

    def test_n4_k2(self) -> None:
        """Test C(4, 2)."""
        result = combinations(4, 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertEqual(result, expected)

    def test_n3_k3(self) -> None:
        """Test C(3, 3)."""
        self.assertEqual(combinations(3, 3), [[1, 2, 3]])

    def test_k0(self) -> None:
        """Test k=0."""
        self.assertEqual(combinations(3, 0), [[]])


class TestSubsetsInvariants(unittest.TestCase):
    """Popperian falsification tests for subsets invariants."""

    def test_p1_valid_subsets(self) -> None:
        """P1: All subsets are valid subsets of input."""
        nums = [1, 2, 3, 4]
        result = subsets(nums)
        for subset in result:
            for elem in subset:
                self.assertIn(elem, nums)

    def test_p2_correct_count_subsets(self) -> None:
        """P2: Correct number of subsets (2^N)."""
        for n in range(6):
            nums = list(range(n))
            result = subsets(nums)
            self.assertEqual(len(result), 2**n)

    def test_p3_no_duplicate_subsets(self) -> None:
        """P3: No duplicate subsets."""
        nums = [1, 2, 3, 4]
        result = subsets(nums)
        result_tuple = [tuple(sorted(s)) for s in result]
        self.assertEqual(len(result_tuple), len(set(result_tuple)))

    def test_p4_combinations_count(self) -> None:
        """P4: combinations(n, k) returns C(n, k) results."""
        for n in range(1, 7):
            for k in range(n + 1):
                result = combinations(n, k)
                expected = math.comb(n, k)
                self.assertEqual(len(result), expected)


if __name__ == "__main__":
    unittest.main()
