"""Tests for Permutation algorithms.

Tests Popperian Falsification Invariants:
    P1: All permutations are valid arrangements
    P2: No duplicate permutations in result
    P3: Correct number of permutations generated
    P4: Empty input returns empty permutation
"""

from __future__ import annotations

import math
import unittest

from algorithm_corpus.backtracking.permutations import (
    permutations,
    permutations_unique,
)


class TestPermutations(unittest.TestCase):
    """Unit tests for permutations."""

    def test_three_elements(self) -> None:
        """Test three elements."""
        result = sorted(permutations([1, 2, 3]))
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(result, expected)

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(permutations([1]), [[1]])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(permutations([]), [[]])


class TestPermutationsUnique(unittest.TestCase):
    """Unit tests for permutations_unique."""

    def test_with_duplicates(self) -> None:
        """Test with duplicate elements."""
        result = sorted(permutations_unique([1, 1, 2]))
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(result, expected)


class TestPermutationsInvariants(unittest.TestCase):
    """Popperian falsification tests for permutation invariants."""

    def test_p1_valid_arrangements(self) -> None:
        """P1: All permutations are valid arrangements."""
        nums = [1, 2, 3]
        result = permutations(nums)
        for perm in result:
            self.assertEqual(sorted(perm), sorted(nums))

    def test_p2_no_duplicates(self) -> None:
        """P2: No duplicate permutations in result."""
        nums = [1, 2, 3, 4]
        result = permutations(nums)
        result_tuple = [tuple(p) for p in result]
        self.assertEqual(len(result_tuple), len(set(result_tuple)))

    def test_p3_correct_count(self) -> None:
        """P3: Correct number of permutations generated."""
        for n in range(1, 6):
            nums = list(range(n))
            result = permutations(nums)
            self.assertEqual(len(result), math.factorial(n))

    def test_p4_empty_returns_empty_perm(self) -> None:
        """P4: Empty input returns empty permutation."""
        self.assertEqual(permutations([]), [[]])


if __name__ == "__main__":
    unittest.main()
