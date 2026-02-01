"""Tests for Interval scheduling algorithms.

Tests Popperian Falsification Invariants:
    P1: Can attend true means no overlap
    P2: Min arrows <= number of balloons
    P3: Non-overlapping meetings always attendable
    P4: Empty input returns valid result
"""

from __future__ import annotations

import unittest

from algorithm_corpus.interval.interval_scheduling import (
    can_attend,
    min_arrows,
)


class TestCanAttend(unittest.TestCase):
    """Unit tests for can_attend."""

    def test_overlap(self) -> None:
        """Test overlapping meetings."""
        self.assertFalse(can_attend([(0, 30), (5, 10), (15, 20)]))

    def test_no_overlap(self) -> None:
        """Test non-overlapping meetings."""
        self.assertTrue(can_attend([(7, 10), (2, 4)]))

    def test_empty(self) -> None:
        """Test empty meetings."""
        self.assertTrue(can_attend([]))

    def test_single(self) -> None:
        """Test single meeting."""
        self.assertTrue(can_attend([(1, 5)]))


class TestMinArrows(unittest.TestCase):
    """Unit tests for min_arrows."""

    def test_overlapping(self) -> None:
        """Test overlapping balloons."""
        self.assertEqual(min_arrows([(10, 16), (2, 8), (1, 6), (7, 12)]), 2)

    def test_disjoint(self) -> None:
        """Test disjoint balloons."""
        self.assertEqual(min_arrows([(1, 2), (3, 4), (5, 6)]), 3)

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(min_arrows([]), 0)

    def test_single(self) -> None:
        """Test single balloon."""
        self.assertEqual(min_arrows([(1, 5)]), 1)


class TestIntervalSchedulingInvariants(unittest.TestCase):
    """Popperian falsification tests for interval scheduling invariants."""

    def test_p1_can_attend_no_overlap(self) -> None:
        """P1: Can attend true means no overlap."""
        intervals = [(1, 3), (4, 6), (7, 9)]
        self.assertTrue(can_attend(intervals))
        # Verify no overlap exists
        sorted_intervals = sorted(intervals)
        for i in range(1, len(sorted_intervals)):
            self.assertLessEqual(sorted_intervals[i - 1][1], sorted_intervals[i][0])

    def test_p2_arrows_le_balloons(self) -> None:
        """P2: Min arrows <= number of balloons."""
        for balloons in [
            [(1, 5), (2, 6), (3, 7)],
            [(1, 2), (3, 4), (5, 6)],
            [(1, 10)],
        ]:
            arrows = min_arrows(balloons)
            self.assertLessEqual(arrows, len(balloons))

    def test_p3_disjoint_always_attendable(self) -> None:
        """P3: Non-overlapping meetings always attendable."""
        # Build non-overlapping intervals
        intervals = [(i * 10, i * 10 + 5) for i in range(5)]
        self.assertTrue(can_attend(intervals))

    def test_p4_empty_returns_valid(self) -> None:
        """P4: Empty input returns valid result."""
        self.assertTrue(can_attend([]))
        self.assertEqual(min_arrows([]), 0)


if __name__ == "__main__":
    unittest.main()
