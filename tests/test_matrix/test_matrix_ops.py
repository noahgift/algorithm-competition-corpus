"""Tests for Matrix operations.

Tests Popperian Falsification Invariants:
    P1: Transpose of transpose equals original
    P2: Four rotations equals original
    P3: Spiral order visits all elements
    P4: Empty matrix returns empty
"""

from __future__ import annotations

import unittest

from algorithm_corpus.matrix.matrix_ops import (
    rotate_90,
    spiral_order,
    transpose,
)


class TestTranspose(unittest.TestCase):
    """Unit tests for transpose."""

    def test_rectangular(self) -> None:
        """Test rectangular matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(transpose(matrix), expected)

    def test_square(self) -> None:
        """Test square matrix."""
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        self.assertEqual(transpose(matrix), expected)

    def test_empty(self) -> None:
        """Test empty matrix."""
        self.assertEqual(transpose([]), [])


class TestRotate90(unittest.TestCase):
    """Unit tests for rotate_90."""

    def test_2x2(self) -> None:
        """Test 2x2 matrix."""
        matrix = [[1, 2], [3, 4]]
        expected = [[3, 1], [4, 2]]
        self.assertEqual(rotate_90(matrix), expected)

    def test_3x3(self) -> None:
        """Test 3x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(rotate_90(matrix), expected)

    def test_empty(self) -> None:
        """Test empty matrix."""
        self.assertEqual(rotate_90([]), [])


class TestSpiralOrder(unittest.TestCase):
    """Unit tests for spiral_order."""

    def test_3x3(self) -> None:
        """Test 3x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(spiral_order(matrix), expected)

    def test_2x2(self) -> None:
        """Test 2x2 matrix."""
        matrix = [[1, 2], [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(spiral_order(matrix), expected)

    def test_empty(self) -> None:
        """Test empty matrix."""
        self.assertEqual(spiral_order([]), [])


class TestMatrixOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for matrix ops invariants."""

    def test_p1_transpose_of_transpose(self) -> None:
        """P1: Transpose of transpose equals original."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = transpose(transpose(matrix))
        self.assertEqual(result, matrix)

    def test_p2_four_rotations_equals_original(self) -> None:
        """P2: Four rotations equals original."""
        matrix = [[1, 2], [3, 4]]
        result = rotate_90(rotate_90(rotate_90(rotate_90(matrix))))
        self.assertEqual(result, matrix)

    def test_p3_spiral_visits_all(self) -> None:
        """P3: Spiral order visits all elements."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = spiral_order(matrix)
        expected_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(sorted(result), expected_elements)

    def test_p4_empty_returns_empty(self) -> None:
        """P4: Empty matrix returns empty."""
        self.assertEqual(transpose([]), [])
        self.assertEqual(rotate_90([]), [])
        self.assertEqual(spiral_order([]), [])


if __name__ == "__main__":
    unittest.main()
