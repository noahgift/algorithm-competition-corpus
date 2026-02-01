"""Tests for Radix Sort algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.sorting.radix_sort import (
    radix_sort,
    radix_sort_strings,
)


class TestRadixSort(unittest.TestCase):
    """Unit tests for radix_sort."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(
            radix_sort([170, 45, 75, 90, 802, 24, 2, 66]),
            [2, 24, 45, 66, 75, 90, 170, 802],
        )

    def test_empty(self) -> None:
        """Test empty."""
        self.assertEqual(radix_sort([]), [])

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(radix_sort([5]), [5])


class TestRadixSortStrings(unittest.TestCase):
    """Unit tests for radix_sort_strings."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(
            radix_sort_strings(["cab", "abc", "bca", "aab"]),
            ["aab", "abc", "bca", "cab"],
        )

    def test_empty(self) -> None:
        """Test empty."""
        self.assertEqual(radix_sort_strings([]), [])


if __name__ == "__main__":
    unittest.main()
