"""Tests for Max Subarray DC algorithm.

Tests Popperian Falsification Invariants:
    P1: Result is a valid subarray sum
    P2: Result equals optimal subarray sum
    P3: Works with negative numbers
    P4: Empty array returns 0
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.divide_and_conquer.max_subarray_dc import (
    max_subarray_divide_conquer,
)


class TestMaxSubarrayDC(unittest.TestCase):
    """Unit tests for max_subarray_divide_conquer."""

    def test_example(self) -> None:
        """Test standard example."""
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_divide_conquer(arr), 6)

    def test_all_positive(self) -> None:
        """Test all positive."""
        self.assertEqual(max_subarray_divide_conquer([1, 2, 3, 4, 5]), 15)

    def test_all_negative(self) -> None:
        """Test all negative."""
        self.assertEqual(max_subarray_divide_conquer([-1, -2, -3]), -1)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(max_subarray_divide_conquer([]), 0)


class TestMaxSubarrayDCInvariants(unittest.TestCase):
    """Popperian falsification tests for max subarray DC invariants."""

    def test_p1_valid_subarray_sum(self) -> None:
        """P1: Result is a valid subarray sum."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(-50, 50) for _ in range(rng.randint(1, 30))]
            result = max_subarray_divide_conquer(arr)
            # Check that this sum exists as a contiguous subarray
            found = False
            for i in range(len(arr)):
                current_sum = 0
                for j in range(i, len(arr)):
                    current_sum += arr[j]
                    if current_sum == result:
                        found = True
                        break
                if found:
                    break
            self.assertTrue(found)

    def test_p2_equals_optimal(self) -> None:
        """P2: Result equals optimal subarray sum."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(-50, 50) for _ in range(rng.randint(1, 30))]
            result = max_subarray_divide_conquer(arr)
            # Brute force optimal
            optimal = float("-inf")
            for i in range(len(arr)):
                current_sum = 0
                for j in range(i, len(arr)):
                    current_sum += arr[j]
                    optimal = max(optimal, current_sum)
            self.assertEqual(result, optimal)

    def test_p3_negative_numbers(self) -> None:
        """P3: Works with negative numbers."""
        self.assertEqual(max_subarray_divide_conquer([-5]), -5)
        self.assertEqual(max_subarray_divide_conquer([-1, -2, -3]), -1)

    def test_p4_empty_returns_zero(self) -> None:
        """P4: Empty array returns 0."""
        self.assertEqual(max_subarray_divide_conquer([]), 0)


if __name__ == "__main__":
    unittest.main()
