"""Tests for Sudoku algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.backtracking.sudoku import (
    is_valid_sudoku,
    solve_sudoku,
)


class TestIsValidSudoku(unittest.TestCase):
    """Unit tests for is_valid_sudoku."""

    def test_valid(self) -> None:
        """Test valid board."""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(is_valid_sudoku(board))


class TestSolveSudoku(unittest.TestCase):
    """Unit tests for solve_sudoku."""

    def test_solvable(self) -> None:
        """Test solvable board."""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(solve_sudoku(board))
        self.assertEqual(board[0][2], "4")


if __name__ == "__main__":
    unittest.main()
