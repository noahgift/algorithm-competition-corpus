"""Tests for Monotonic stack algorithms.

Tests Popperian Falsification Invariants:
    P1: Next greater is actually greater
    P2: -1 means no greater element exists
    P3: Daily temperatures are non-negative
    P4: Result length matches input length
"""

from __future__ import annotations

import unittest

from algorithm_corpus.stack.monotonic import (
    daily_temperatures,
    next_greater_element,
)


class TestNextGreaterElement(unittest.TestCase):
    """Unit tests for next_greater_element."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(next_greater_element([2, 1, 2, 4, 3]), [4, 2, 4, -1, 4])

    def test_circular(self) -> None:
        """Test circular wrapping."""
        self.assertEqual(next_greater_element([1, 2, 1]), [2, -1, 2])

    def test_decreasing(self) -> None:
        """Test decreasing sequence."""
        self.assertEqual(next_greater_element([3, 2, 1]), [-1, 3, 3])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(next_greater_element([]), [])


class TestDailyTemperatures(unittest.TestCase):
    """Unit tests for daily_temperatures."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )

    def test_increasing(self) -> None:
        """Test increasing temperatures."""
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    def test_decreasing(self) -> None:
        """Test decreasing temperatures."""
        self.assertEqual(daily_temperatures([60, 50, 40, 30]), [0, 0, 0, 0])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(daily_temperatures([]), [])


class TestMonotonicInvariants(unittest.TestCase):
    """Popperian falsification tests for monotonic stack invariants."""

    def test_p1_next_greater_is_greater(self) -> None:
        """P1: Next greater is actually greater."""
        nums = [5, 3, 8, 1, 9, 2]
        result = next_greater_element(nums)
        for i, val in enumerate(result):
            if val != -1:
                self.assertGreater(val, nums[i])

    def test_p2_minus_one_means_none_greater(self) -> None:
        """P2: -1 means no greater element exists (with circular)."""
        nums = [5, 4, 3, 2, 1]
        result = next_greater_element(nums)
        # First element (5) has no greater in circular
        self.assertEqual(result[0], -1)

    def test_p3_daily_temps_non_negative(self) -> None:
        """P3: Daily temperatures are non-negative."""
        temps = [73, 74, 75, 71, 69, 72, 76, 73]
        result = daily_temperatures(temps)
        for wait_days in result:
            self.assertGreaterEqual(wait_days, 0)

    def test_p4_result_length_matches_input(self) -> None:
        """P4: Result length matches input length."""
        for nums in [[], [1], [1, 2, 3], [5, 4, 3, 2, 1]]:
            self.assertEqual(len(next_greater_element(nums)), len(nums))
            self.assertEqual(len(daily_temperatures(nums)), len(nums))


if __name__ == "__main__":
    unittest.main()
