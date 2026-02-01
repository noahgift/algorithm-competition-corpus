"""Tests for Interval operations.

Tests Popperian Falsification Invariants:
    P1: Merged intervals are non-overlapping
    P2: Insert maintains sorted order
    P3: Intersection is subset of both inputs
    P4: Empty input returns empty
"""

from __future__ import annotations

import unittest

from algorithm_corpus.interval.interval_ops import (
    insert_interval,
    interval_intersection,
    merge_overlapping,
)


class TestMergeOverlapping(unittest.TestCase):
    """Unit tests for merge_overlapping."""

    def test_basic(self) -> None:
        """Test basic merge."""
        intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
        expected = [(1, 6), (8, 10), (15, 18)]
        self.assertEqual(merge_overlapping(intervals), expected)

    def test_touching(self) -> None:
        """Test touching intervals."""
        self.assertEqual(merge_overlapping([(1, 4), (4, 5)]), [(1, 5)])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(merge_overlapping([]), [])


class TestInsertInterval(unittest.TestCase):
    """Unit tests for insert_interval."""

    def test_overlap_middle(self) -> None:
        """Test overlap in middle."""
        intervals = [(1, 3), (6, 9)]
        expected = [(1, 5), (6, 9)]
        self.assertEqual(insert_interval(intervals, (2, 5)), expected)

    def test_span_multiple(self) -> None:
        """Test spanning multiple intervals."""
        intervals = [(1, 2), (3, 5), (6, 7), (8, 10)]
        expected = [(1, 2), (3, 10)]
        self.assertEqual(insert_interval(intervals, (4, 8)), expected)

    def test_empty(self) -> None:
        """Test empty intervals."""
        self.assertEqual(insert_interval([], (1, 5)), [(1, 5)])


class TestIntervalIntersection(unittest.TestCase):
    """Unit tests for interval_intersection."""

    def test_basic(self) -> None:
        """Test basic intersection."""
        a = [(0, 2), (5, 10)]
        b = [(1, 5), (8, 12)]
        expected = [(1, 2), (5, 5), (8, 10)]
        self.assertEqual(interval_intersection(a, b), expected)

    def test_no_overlap(self) -> None:
        """Test no overlap."""
        a = [(0, 2), (5, 6)]
        b = [(3, 4), (7, 8)]
        self.assertEqual(interval_intersection(a, b), [])


class TestIntervalOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for interval ops invariants."""

    def test_p1_merged_non_overlapping(self) -> None:
        """P1: Merged intervals are non-overlapping."""
        intervals = [(1, 3), (2, 6), (8, 10), (9, 11)]
        result = merge_overlapping(intervals)
        for i in range(1, len(result)):
            self.assertGreater(result[i][0], result[i - 1][1])

    def test_p2_insert_maintains_order(self) -> None:
        """P2: Insert maintains sorted order."""
        intervals = [(1, 2), (5, 6), (9, 10)]
        result = insert_interval(intervals, (3, 4))
        for i in range(1, len(result)):
            self.assertLessEqual(result[i - 1][0], result[i][0])

    def test_p3_intersection_subset(self) -> None:
        """P3: Intersection is subset of both inputs."""
        a = [(0, 5), (10, 15)]
        b = [(2, 8), (12, 20)]
        result = interval_intersection(a, b)
        for start, end in result:
            # Must be within some interval in both a and b
            in_a = any(s <= start and end <= e for s, e in a)
            in_b = any(s <= start and end <= e for s, e in b)
            self.assertTrue(in_a)
            self.assertTrue(in_b)

    def test_p4_empty_returns_empty(self) -> None:
        """P4: Empty input returns empty."""
        self.assertEqual(merge_overlapping([]), [])
        self.assertEqual(interval_intersection([], [(1, 2)]), [])


if __name__ == "__main__":
    unittest.main()
