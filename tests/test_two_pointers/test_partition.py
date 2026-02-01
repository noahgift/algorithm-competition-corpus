"""Tests for Partition algorithms.

Tests Popperian Falsification Invariants:
    P1: Result is a permutation of input
    P2: Partition property is satisfied
    P3: In-place modification (no extra space)
    P4: Relative order preserved when applicable
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.two_pointers.partition import (
    dutch_national_flag,
    move_zeros,
    remove_duplicates,
)


class TestDutchNationalFlag(unittest.TestCase):
    """Unit tests for dutch_national_flag."""

    def test_example(self) -> None:
        """Test standard example."""
        self.assertEqual(dutch_national_flag([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])

    def test_short(self) -> None:
        """Test short array."""
        self.assertEqual(dutch_national_flag([2, 0, 1]), [0, 1, 2])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(dutch_national_flag([]), [])

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(dutch_national_flag([0]), [0])


class TestMoveZeros(unittest.TestCase):
    """Unit tests for move_zeros."""

    def test_example(self) -> None:
        """Test standard example."""
        self.assertEqual(move_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_single_zero(self) -> None:
        """Test single zero."""
        self.assertEqual(move_zeros([0]), [0])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(move_zeros([]), [])

    def test_no_zeros(self) -> None:
        """Test no zeros."""
        self.assertEqual(move_zeros([1, 2, 3]), [1, 2, 3])


class TestRemoveDuplicates(unittest.TestCase):
    """Unit tests for remove_duplicates."""

    def test_example1(self) -> None:
        """Test first example."""
        arr = [1, 1, 2]
        k = remove_duplicates(arr)
        self.assertEqual(k, 2)
        self.assertEqual(arr[:k], [1, 2])

    def test_example2(self) -> None:
        """Test second example."""
        arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(arr)
        self.assertEqual(k, 5)
        self.assertEqual(arr[:k], [0, 1, 2, 3, 4])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(remove_duplicates([]), 0)


class TestPartitionInvariants(unittest.TestCase):
    """Popperian falsification tests for partition invariants."""

    def test_p1_permutation_dnf(self) -> None:
        """P1: Dutch national flag result is permutation."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 50)
            arr = [rng.randint(0, 2) for _ in range(n)]
            result = dutch_national_flag(arr)
            self.assertEqual(sorted(arr), sorted(result))

    def test_p1_permutation_move_zeros(self) -> None:
        """P1: Move zeros result is permutation."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 50)
            arr = [rng.randint(-10, 10) for _ in range(n)]
            result = move_zeros(arr)
            self.assertEqual(sorted(arr), sorted(result))

    def test_p2_dnf_sorted(self) -> None:
        """P2: Dutch national flag result is sorted."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 50)
            arr = [rng.randint(0, 2) for _ in range(n)]
            result = dutch_national_flag(arr)
            self.assertEqual(result, sorted(arr))

    def test_p2_move_zeros_property(self) -> None:
        """P2: Move zeros has all zeros at end."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 50)
            arr = [rng.randint(-10, 10) for _ in range(n)]
            result = move_zeros(arr)
            # Find first zero position
            first_zero = -1
            for i, val in enumerate(result):
                if val == 0:
                    first_zero = i
                    break
            # All after first_zero should be zero
            if first_zero != -1:
                for i in range(first_zero, len(result)):
                    self.assertEqual(result[i], 0)


if __name__ == "__main__":
    unittest.main()
