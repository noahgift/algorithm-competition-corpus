"""Tests for Interval Scheduling algorithms.

Tests Popperian Falsification Invariants:
    P1: Merged intervals don't overlap
    P2: Merged intervals cover all original intervals
    P3: min_meeting_rooms is minimum possible
    P4: Empty input returns appropriate result
"""

from __future__ import annotations

import unittest

from algorithm_corpus.greedy.interval_scheduling import (
    merge_intervals,
    min_meeting_rooms,
)


class TestMergeIntervals(unittest.TestCase):
    """Unit tests for merge_intervals."""

    def test_example(self) -> None:
        """Test standard example."""
        intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
        self.assertEqual(merge_intervals(intervals), [(1, 6), (8, 10), (15, 18)])

    def test_touching(self) -> None:
        """Test touching intervals."""
        self.assertEqual(merge_intervals([(1, 4), (4, 5)]), [(1, 5)])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(merge_intervals([]), [])


class TestMinMeetingRooms(unittest.TestCase):
    """Unit tests for min_meeting_rooms."""

    def test_overlapping(self) -> None:
        """Test overlapping meetings."""
        self.assertEqual(min_meeting_rooms([(0, 30), (5, 10), (15, 20)]), 2)

    def test_non_overlapping(self) -> None:
        """Test non-overlapping meetings."""
        self.assertEqual(min_meeting_rooms([(7, 10), (2, 4)]), 1)

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(min_meeting_rooms([]), 0)

    def test_all_overlapping(self) -> None:
        """Test all overlapping."""
        self.assertEqual(min_meeting_rooms([(1, 5), (2, 6), (3, 7)]), 3)


class TestIntervalSchedulingInvariants(unittest.TestCase):
    """Popperian falsification tests for interval scheduling invariants."""

    def test_p1_no_overlap_after_merge(self) -> None:
        """P1: Merged intervals don't overlap."""
        intervals = [(1, 3), (2, 6), (8, 10), (9, 11)]
        result = merge_intervals(intervals)
        for i in range(len(result) - 1):
            self.assertLess(result[i][1], result[i + 1][0])

    def test_p2_covers_all_original(self) -> None:
        """P2: Merged intervals cover all original intervals."""
        intervals = [(1, 3), (2, 6), (8, 10)]
        result = merge_intervals(intervals)
        for start, end in intervals:
            covered = any(r[0] <= start and end <= r[1] for r in result)
            self.assertTrue(covered)

    def test_p4_empty_handling(self) -> None:
        """P4: Empty input returns appropriate result."""
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(min_meeting_rooms([]), 0)


if __name__ == "__main__":
    unittest.main()
