"""Tests for N-Queens algorithm.

Tests Popperian Falsification Invariants:
    P1: No two queens attack each other
    P2: Exactly N queens placed
    P3: All solutions are distinct
    P4: N=0 returns empty, N=1 returns one solution
"""

from __future__ import annotations

import unittest

from algorithm_corpus.backtracking.n_queens import (
    n_queens,
    n_queens_count,
)


class TestNQueens(unittest.TestCase):
    """Unit tests for n_queens."""

    def test_n4(self) -> None:
        """Test N=4."""
        result = n_queens(4)
        self.assertEqual(result, [[1, 3, 0, 2], [2, 0, 3, 1]])

    def test_n1(self) -> None:
        """Test N=1."""
        self.assertEqual(n_queens(1), [[0]])

    def test_n0(self) -> None:
        """Test N=0."""
        self.assertEqual(n_queens(0), [[]])


class TestNQueensCount(unittest.TestCase):
    """Unit tests for n_queens_count."""

    def test_counts(self) -> None:
        """Test known counts."""
        self.assertEqual(n_queens_count(4), 2)
        self.assertEqual(n_queens_count(8), 92)
        self.assertEqual(n_queens_count(1), 1)


class TestNQueensInvariants(unittest.TestCase):
    """Popperian falsification tests for N-Queens invariants."""

    def test_p1_no_attacks(self) -> None:
        """P1: No two queens attack each other."""
        for n in range(1, 7):
            solutions = n_queens(n)
            for sol in solutions:
                # Check no same column
                self.assertEqual(len(sol), len(set(sol)))
                # Check diagonals
                for i in range(len(sol)):
                    for j in range(i + 1, len(sol)):
                        self.assertNotEqual(abs(sol[i] - sol[j]), abs(i - j))

    def test_p2_n_queens_placed(self) -> None:
        """P2: Exactly N queens placed."""
        for n in range(1, 7):
            solutions = n_queens(n)
            for sol in solutions:
                self.assertEqual(len(sol), n)

    def test_p3_distinct_solutions(self) -> None:
        """P3: All solutions are distinct."""
        for n in range(1, 7):
            solutions = n_queens(n)
            solutions_tuple = [tuple(s) for s in solutions]
            self.assertEqual(len(solutions_tuple), len(set(solutions_tuple)))


if __name__ == "__main__":
    unittest.main()
