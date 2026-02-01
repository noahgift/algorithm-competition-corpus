"""Tests for Matrix path algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.matrix.matrix_path import (
    min_path_sum,
    unique_paths,
    unique_paths_with_obstacles,
    word_search,
)


class TestUniquePaths(unittest.TestCase):
    """Unit tests for unique_paths."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(unique_paths(3, 7), 28)

    def test_small(self) -> None:
        """Test small grid."""
        self.assertEqual(unique_paths(3, 2), 3)


class TestUniquePathsWithObstacles(unittest.TestCase):
    """Unit tests for unique_paths_with_obstacles."""

    def test_basic(self) -> None:
        """Test basic case."""
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(unique_paths_with_obstacles(grid), 2)


class TestMinPathSum(unittest.TestCase):
    """Unit tests for min_path_sum."""

    def test_basic(self) -> None:
        """Test basic case."""
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        self.assertEqual(min_path_sum(grid), 7)


class TestWordSearch(unittest.TestCase):
    """Unit tests for word_search."""

    def test_found(self) -> None:
        """Test word found."""
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        self.assertTrue(word_search(board, "ABCCED"))

    def test_not_found(self) -> None:
        """Test word not found."""
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        self.assertFalse(word_search(board, "ABCB"))


if __name__ == "__main__":
    unittest.main()
