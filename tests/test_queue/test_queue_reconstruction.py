"""Tests for Queue reconstruction algorithm.

Tests Popperian Falsification Invariants:
    P1: Each person has correct count in front
    P2: Result length matches input length
    P3: All original people are in result
    P4: Empty input returns empty
"""

from __future__ import annotations

import unittest

from algorithm_corpus.queue.queue_reconstruction import (
    reconstruct_queue,
)


class TestReconstructQueue(unittest.TestCase):
    """Unit tests for reconstruct_queue."""

    def test_basic(self) -> None:
        """Test basic case."""
        people = [(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]
        expected = [(5, 0), (7, 0), (5, 2), (6, 1), (4, 4), (7, 1)]
        self.assertEqual(reconstruct_queue(people), expected)

    def test_single(self) -> None:
        """Test single person."""
        self.assertEqual(reconstruct_queue([(5, 0)]), [(5, 0)])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(reconstruct_queue([]), [])


class TestQueueReconstructionInvariants(unittest.TestCase):
    """Popperian falsification tests for queue reconstruction invariants."""

    def test_p1_correct_count(self) -> None:
        """P1: Each person has correct count in front."""
        people = [(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]
        result = reconstruct_queue(people)

        for i, (height, count) in enumerate(result):
            # Count people in front with height >= this person's height
            taller_or_equal = sum(1 for h, _ in result[:i] if h >= height)
            self.assertEqual(taller_or_equal, count)

    def test_p2_result_length_matches(self) -> None:
        """P2: Result length matches input length."""
        people = [(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]
        result = reconstruct_queue(people)
        self.assertEqual(len(result), len(people))

    def test_p3_all_people_in_result(self) -> None:
        """P3: All original people are in result."""
        people = [(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]
        result = reconstruct_queue(people)
        self.assertEqual(sorted(result), sorted(people))

    def test_p4_empty_returns_empty(self) -> None:
        """P4: Empty input returns empty."""
        self.assertEqual(reconstruct_queue([]), [])


if __name__ == "__main__":
    unittest.main()
