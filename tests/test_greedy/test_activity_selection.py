"""Tests for Activity Selection algorithm.

Tests Popperian Falsification Invariants:
    P1: Selected activities don't overlap
    P2: Number of activities is maximized
    P3: All activities in result are valid
    P4: Empty input returns empty result
"""

from __future__ import annotations

import unittest

from algorithm_corpus.greedy.activity_selection import (
    activity_selection,
    max_activities,
)


class TestActivitySelection(unittest.TestCase):
    """Unit tests for activity_selection."""

    def test_example(self) -> None:
        """Test standard example."""
        activities = [
            (1, 4),
            (3, 5),
            (0, 6),
            (5, 7),
            (3, 8),
            (5, 9),
            (6, 10),
            (8, 11),
            (8, 12),
            (2, 13),
            (12, 14),
        ]
        result = activity_selection(activities)
        self.assertEqual(result, [(1, 4), (5, 7), (8, 11), (12, 14)])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(activity_selection([]), [])

    def test_single(self) -> None:
        """Test single activity."""
        self.assertEqual(activity_selection([(1, 2)]), [(1, 2)])


class TestMaxActivities(unittest.TestCase):
    """Unit tests for max_activities."""

    def test_example(self) -> None:
        """Test counting activities."""
        activities = [(1, 4), (3, 5), (0, 6), (5, 7)]
        self.assertEqual(max_activities(activities), 2)

    def test_consecutive(self) -> None:
        """Test consecutive activities."""
        activities = [(1, 2), (2, 3), (3, 4)]
        self.assertEqual(max_activities(activities), 3)


class TestActivitySelectionInvariants(unittest.TestCase):
    """Popperian falsification tests for activity selection invariants."""

    def test_p1_no_overlap(self) -> None:
        """P1: Selected activities don't overlap."""
        activities = [(1, 4), (3, 5), (5, 7), (6, 8), (8, 10)]
        result = activity_selection(activities)
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i][1], result[i + 1][0])

    def test_p3_all_valid(self) -> None:
        """P3: All activities in result are valid."""
        activities = [(1, 4), (3, 5), (0, 6), (5, 7)]
        result = activity_selection(activities)
        for activity in result:
            self.assertIn(activity, activities)

    def test_p4_empty_returns_empty(self) -> None:
        """P4: Empty input returns empty result."""
        self.assertEqual(activity_selection([]), [])
        self.assertEqual(max_activities([]), 0)


if __name__ == "__main__":
    unittest.main()
