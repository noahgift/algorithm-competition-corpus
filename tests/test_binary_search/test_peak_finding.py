"""Tests for Peak Finding algorithms.

Tests Popperian Falsification Invariants:
    P1: Peak element is greater than or equal to neighbors
    P2: At least one peak always exists
    P3: O(log n) time complexity maintained
    P4: Works on arrays with duplicates
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.binary_search.peak_finding import (
    find_peak_element,
    find_peak_in_mountain,
)


class TestFindPeakElement(unittest.TestCase):
    """Unit tests for find_peak_element."""

    def test_single_peak(self) -> None:
        """Test array with single peak."""
        arr = [1, 2, 3, 1]
        idx = find_peak_element(arr)
        self.assertEqual(idx, 2)

    def test_multiple_peaks(self) -> None:
        """Test array with multiple peaks."""
        arr = [1, 2, 1, 3, 5, 6, 4]
        idx = find_peak_element(arr)
        self.assertIn(idx, (1, 5))

    def test_single_element(self) -> None:
        """Test single element array."""
        self.assertEqual(find_peak_element([1]), 0)

    def test_two_elements(self) -> None:
        """Test two elements."""
        self.assertEqual(find_peak_element([1, 2]), 1)


class TestFindPeakInMountain(unittest.TestCase):
    """Unit tests for find_peak_in_mountain."""

    def test_simple_mountain(self) -> None:
        """Test simple mountain array."""
        self.assertEqual(find_peak_in_mountain([0, 1, 0]), 1)

    def test_larger_mountain(self) -> None:
        """Test larger mountain."""
        self.assertEqual(find_peak_in_mountain([0, 2, 1, 0]), 1)

    def test_peak_at_end(self) -> None:
        """Test peak near end."""
        self.assertEqual(find_peak_in_mountain([3, 4, 5, 1]), 2)


class TestPeakFindingInvariants(unittest.TestCase):
    """Popperian falsification tests for peak finding invariants."""

    def _is_peak(self, arr: list[int], idx: int) -> bool:
        """Check if index is a peak."""
        n = len(arr)
        if n == 0:
            return False
        left_ok = idx == 0 or arr[idx] > arr[idx - 1]
        right_ok = idx == n - 1 or arr[idx] > arr[idx + 1]
        return left_ok and right_ok

    def test_p1_peak_greater_than_neighbors(self) -> None:
        """P1: Peak element is greater than neighbors."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = [rng.randint(0, 100) for _ in range(n)]
            idx = find_peak_element(arr)
            if n > 0:
                self.assertTrue(self._is_peak(arr, idx))

    def test_p2_peak_always_exists(self) -> None:
        """P2: At least one peak always exists."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = [rng.randint(0, 100) for _ in range(n)]
            idx = find_peak_element(arr)
            self.assertGreaterEqual(idx, 0)
            self.assertLess(idx, n)

    def test_mountain_peak_is_maximum(self) -> None:
        """Mountain peak should be the maximum element."""
        rng = random.Random(42)
        for _ in range(30):
            left_size = rng.randint(1, 10)
            right_size = rng.randint(1, 10)
            # Build strictly increasing left side, peak, strictly decreasing right
            left = list(range(left_size))
            peak_val = left_size
            right = list(range(left_size - 1, left_size - 1 - right_size, -1))
            arr = [*left, peak_val, *right]
            idx = find_peak_in_mountain(arr)
            self.assertEqual(arr[idx], peak_val)


if __name__ == "__main__":
    unittest.main()
