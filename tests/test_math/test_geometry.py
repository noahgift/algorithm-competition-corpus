"""Tests for Geometry algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.math.geometry import (
    max_points_on_line,
    valid_square,
)


class TestMaxPointsOnLine(unittest.TestCase):
    """Unit tests for max_points_on_line."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(max_points_on_line([(1, 1), (2, 2), (3, 3)]), 3)

    def test_complex(self) -> None:
        """Test complex case."""
        points = [(1, 1), (3, 2), (5, 3), (4, 1), (2, 3), (1, 4)]
        self.assertEqual(max_points_on_line(points), 4)


class TestValidSquare(unittest.TestCase):
    """Unit tests for valid_square."""

    def test_valid(self) -> None:
        """Test valid square."""
        self.assertTrue(valid_square((0, 0), (1, 1), (1, 0), (0, 1)))

    def test_invalid(self) -> None:
        """Test invalid square."""
        self.assertFalse(valid_square((0, 0), (1, 1), (1, 0), (0, 2)))


if __name__ == "__main__":
    unittest.main()
