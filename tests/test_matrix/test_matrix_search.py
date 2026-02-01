"""Tests for Matrix search algorithms.

Tests Popperian Falsification Invariants:
    P1: Found element exists in matrix
    P2: Not found means element doesn't exist
    P3: Works on empty matrix
    P4: Works on single element matrix
"""

from __future__ import annotations

import unittest

from algorithm_corpus.matrix.matrix_search import (
    search_matrix,
    search_matrix_2d,
)


class TestSearchMatrix(unittest.TestCase):
    """Unit tests for search_matrix."""

    def test_found(self) -> None:
        """Test element found."""
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 9))

    def test_not_found(self) -> None:
        """Test element not found."""
        matrix = [[1, 3, 5], [7, 9, 11]]
        self.assertFalse(search_matrix(matrix, 6))

    def test_empty(self) -> None:
        """Test empty matrix."""
        self.assertFalse(search_matrix([], 1))


class TestSearchMatrix2d(unittest.TestCase):
    """Unit tests for search_matrix_2d."""

    def test_found(self) -> None:
        """Test element found."""
        matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertTrue(search_matrix_2d(matrix, 5))

    def test_not_found(self) -> None:
        """Test element not found."""
        matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertFalse(search_matrix_2d(matrix, 10))

    def test_empty(self) -> None:
        """Test empty matrix."""
        self.assertFalse(search_matrix_2d([], 1))


class TestMatrixSearchInvariants(unittest.TestCase):
    """Popperian falsification tests for matrix search invariants."""

    def test_p1_found_exists(self) -> None:
        """P1: Found element exists in matrix."""
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        all_elements = [v for row in matrix for v in row]
        for val in all_elements:
            self.assertTrue(search_matrix(matrix, val))

    def test_p2_not_found_doesnt_exist(self) -> None:
        """P2: Not found means element doesn't exist."""
        matrix = [[1, 3, 5], [7, 9, 11]]
        all_elements = {v for row in matrix for v in row}
        for val in [2, 4, 6, 8, 10, 12]:
            if val not in all_elements:
                self.assertFalse(search_matrix(matrix, val))

    def test_p3_empty_matrix(self) -> None:
        """P3: Works on empty matrix."""
        self.assertFalse(search_matrix([], 1))
        self.assertFalse(search_matrix_2d([], 1))

    def test_p4_single_element(self) -> None:
        """P4: Works on single element matrix."""
        self.assertTrue(search_matrix([[5]], 5))
        self.assertFalse(search_matrix([[5]], 3))
        self.assertTrue(search_matrix_2d([[5]], 5))
        self.assertFalse(search_matrix_2d([[5]], 3))


if __name__ == "__main__":
    unittest.main()
