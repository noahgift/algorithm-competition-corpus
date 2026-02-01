"""Tests for Search Range algorithm.

Tests Popperian Falsification Invariants:
    P1: If found, arr[start:end+1] all equal target
    P2: If not found, result == [-1, -1]
    P3: start <= end when found
    P4: No elements equal to target exist outside [start, end]
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.binary_search.search_range import (
    search_range,
)


class TestSearchRange(unittest.TestCase):
    """Unit tests for search_range."""

    def test_found(self) -> None:
        """Test finding range."""
        self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_not_found(self) -> None:
        """Test element not present."""
        self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(search_range([], 0), [-1, -1])

    def test_single_element_found(self) -> None:
        """Test single element found."""
        self.assertEqual(search_range([1], 1), [0, 0])

    def test_single_element_not_found(self) -> None:
        """Test single element not found."""
        self.assertEqual(search_range([1], 2), [-1, -1])


class TestSearchRangeInvariants(unittest.TestCase):
    """Popperian falsification tests for search_range invariants."""

    def test_p1_range_contains_target(self) -> None:
        """P1: If found, arr[start:end+1] all equal target."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted(rng.randint(0, 10) for _ in range(n))
            target = rng.choice(arr)
            start, end = search_range(arr, target)
            self.assertNotEqual(start, -1)
            for i in range(start, end + 1):
                self.assertEqual(arr[i], target)

    def test_p2_not_found_returns_minus_one(self) -> None:
        """P2: If not found, result == [-1, -1]."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(search_range(arr, 100), [-1, -1])

    def test_p3_start_leq_end(self) -> None:
        """P3: start <= end when found."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted(rng.randint(0, 10) for _ in range(n))
            target = rng.choice(arr)
            start, end = search_range(arr, target)
            self.assertLessEqual(start, end)

    def test_p4_no_target_outside_range(self) -> None:
        """P4: No elements equal to target exist outside [start, end]."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted(rng.randint(0, 10) for _ in range(n))
            target = rng.choice(arr)
            start, end = search_range(arr, target)
            # Check outside range
            for i in range(start):
                self.assertNotEqual(arr[i], target)
            for i in range(end + 1, n):
                self.assertNotEqual(arr[i], target)


if __name__ == "__main__":
    unittest.main()
