"""Tests for Window Pattern algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.sliding_window.window_patterns import (
    find_anagrams,
    min_size_subarray_sum,
    min_window_substring,
)


class TestMinSizeSubarraySum(unittest.TestCase):
    """Unit tests for min_size_subarray_sum."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(min_size_subarray_sum(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_none_found(self) -> None:
        """Test no valid subarray."""
        self.assertEqual(min_size_subarray_sum(11, [1, 1, 1, 1, 1]), 0)


class TestFindAnagrams(unittest.TestCase):
    """Unit tests for find_anagrams."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(find_anagrams("cbaebabacd", "abc"), [0, 6])

    def test_overlapping(self) -> None:
        """Test overlapping anagrams."""
        self.assertEqual(find_anagrams("abab", "ab"), [0, 1, 2])


class TestMinWindowSubstring(unittest.TestCase):
    """Unit tests for min_window_substring."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(min_window_substring("ADOBECODEBANC", "ABC"), "BANC")

    def test_single(self) -> None:
        """Test single char."""
        self.assertEqual(min_window_substring("a", "a"), "a")


if __name__ == "__main__":
    unittest.main()
