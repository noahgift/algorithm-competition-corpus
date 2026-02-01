"""Tests for Binary Search Bounds algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.binary_search.bounds import (
    count_occurrences,
    lower_bound,
    search_insert_position,
    upper_bound,
)


class TestLowerBound(unittest.TestCase):
    """Unit tests for lower_bound."""

    def test_found(self) -> None:
        """Test target found."""
        self.assertEqual(lower_bound([1, 2, 4, 4, 5], 4), 2)

    def test_not_found(self) -> None:
        """Test target not found."""
        self.assertEqual(lower_bound([1, 2, 4, 4, 5], 3), 2)


class TestUpperBound(unittest.TestCase):
    """Unit tests for upper_bound."""

    def test_found(self) -> None:
        """Test target found."""
        self.assertEqual(upper_bound([1, 2, 4, 4, 5], 4), 4)

    def test_not_found(self) -> None:
        """Test target not found."""
        self.assertEqual(upper_bound([1, 2, 4, 4, 5], 3), 2)


class TestCountOccurrences(unittest.TestCase):
    """Unit tests for count_occurrences."""

    def test_multiple(self) -> None:
        """Test multiple occurrences."""
        self.assertEqual(count_occurrences([1, 2, 4, 4, 4, 5], 4), 3)

    def test_none(self) -> None:
        """Test no occurrences."""
        self.assertEqual(count_occurrences([1, 2, 5], 4), 0)


class TestSearchInsertPosition(unittest.TestCase):
    """Unit tests for search_insert_position."""

    def test_found(self) -> None:
        """Test target found."""
        self.assertEqual(search_insert_position([1, 3, 5, 6], 5), 2)

    def test_insert(self) -> None:
        """Test insert position."""
        self.assertEqual(search_insert_position([1, 3, 5, 6], 2), 1)


if __name__ == "__main__":
    unittest.main()
