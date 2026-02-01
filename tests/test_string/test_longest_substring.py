"""Tests for Longest Substring algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.string.longest_substring import (
    longest_no_repeat,
    longest_repeating_replacement,
    longest_with_k_distinct,
)


class TestLongestNoRepeat(unittest.TestCase):
    """Unit tests for longest_no_repeat."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(longest_no_repeat("abcabcbb"), 3)

    def test_all_same(self) -> None:
        """Test all same."""
        self.assertEqual(longest_no_repeat("bbbbb"), 1)

    def test_mixed(self) -> None:
        """Test mixed."""
        self.assertEqual(longest_no_repeat("pwwkew"), 3)


class TestLongestWithKDistinct(unittest.TestCase):
    """Unit tests for longest_with_k_distinct."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(longest_with_k_distinct("eceba", 2), 3)

    def test_same(self) -> None:
        """Test same char."""
        self.assertEqual(longest_with_k_distinct("aa", 1), 2)


class TestLongestRepeatingReplacement(unittest.TestCase):
    """Unit tests for longest_repeating_replacement."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(longest_repeating_replacement("ABAB", 2), 4)

    def test_longer(self) -> None:
        """Test longer."""
        self.assertEqual(longest_repeating_replacement("AABABBA", 1), 4)


if __name__ == "__main__":
    unittest.main()
