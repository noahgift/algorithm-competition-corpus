"""Tests for Container algorithms.

Tests Popperian Falsification Invariants:
    P1: Result is non-negative
    P2: Result does not exceed theoretical maximum
    P3: Empty array returns 0
    P4: Single element array returns 0
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.two_pointers.container import (
    max_area,
    trap_water,
)


class TestMaxArea(unittest.TestCase):
    """Unit tests for max_area."""

    def test_example(self) -> None:
        """Test standard example."""
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_two_elements(self) -> None:
        """Test two elements."""
        self.assertEqual(max_area([1, 1]), 1)

    def test_symmetric(self) -> None:
        """Test symmetric array."""
        self.assertEqual(max_area([4, 3, 2, 1, 4]), 16)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(max_area([]), 0)


class TestTrapWater(unittest.TestCase):
    """Unit tests for trap_water."""

    def test_example1(self) -> None:
        """Test first example."""
        self.assertEqual(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_example2(self) -> None:
        """Test second example."""
        self.assertEqual(trap_water([4, 2, 0, 3, 2, 5]), 9)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(trap_water([]), 0)

    def test_increasing(self) -> None:
        """Test strictly increasing array."""
        self.assertEqual(trap_water([1, 2, 3]), 0)


class TestContainerInvariants(unittest.TestCase):
    """Popperian falsification tests for container invariants."""

    def test_p1_non_negative(self) -> None:
        """P1: Result is non-negative."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 50)
            arr = [rng.randint(0, 100) for _ in range(n)]
            self.assertGreaterEqual(max_area(arr), 0)
            self.assertGreaterEqual(trap_water(arr), 0)

    def test_p2_max_area_bounded(self) -> None:
        """P2: Result does not exceed theoretical maximum."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 50)
            arr = [rng.randint(0, 100) for _ in range(n)]
            result = max_area(arr)
            max_possible = max(arr) * (n - 1) if arr else 0
            self.assertLessEqual(result, max_possible)

    def test_p3_empty_returns_zero(self) -> None:
        """P3: Empty array returns 0."""
        self.assertEqual(max_area([]), 0)
        self.assertEqual(trap_water([]), 0)

    def test_p4_single_element_returns_zero(self) -> None:
        """P4: Single element array returns 0."""
        self.assertEqual(max_area([5]), 0)
        self.assertEqual(trap_water([5]), 0)


if __name__ == "__main__":
    unittest.main()
