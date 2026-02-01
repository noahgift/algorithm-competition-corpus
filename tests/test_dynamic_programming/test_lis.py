"""Tests for LIS algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.dynamic_programming.lis import (
    lis_binary_search,
    lis_dp,
    lis_with_sequence,
)


class TestLisDp(unittest.TestCase):
    """Unit tests for lis_dp."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(lis_dp([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_increasing(self) -> None:
        """Test already increasing."""
        self.assertEqual(lis_dp([1, 2, 3, 4, 5]), 5)

    def test_empty(self) -> None:
        """Test empty."""
        self.assertEqual(lis_dp([]), 0)


class TestLisBinarySearch(unittest.TestCase):
    """Unit tests for lis_binary_search."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(lis_binary_search([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_duplicates(self) -> None:
        """Test duplicates."""
        self.assertEqual(lis_binary_search([7, 7, 7, 7]), 1)


class TestLisWithSequence(unittest.TestCase):
    """Unit tests for lis_with_sequence."""

    def test_basic(self) -> None:
        """Test returns valid sequence."""
        result = lis_with_sequence([10, 9, 2, 5, 3, 7, 101, 18])
        self.assertEqual(len(result), 4)
        # Check it's increasing
        for i in range(1, len(result)):
            self.assertGreater(result[i], result[i - 1])


if __name__ == "__main__":
    unittest.main()
