"""Tests for Word Break algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.dynamic_programming.word_break import (
    word_break,
    word_break_all,
)


class TestWordBreak(unittest.TestCase):
    """Unit tests for word_break."""

    def test_can_segment(self) -> None:
        """Test can segment."""
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_cannot_segment(self) -> None:
        """Test cannot segment."""
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))


class TestWordBreakAll(unittest.TestCase):
    """Unit tests for word_break_all."""

    def test_multiple(self) -> None:
        """Test multiple solutions."""
        result = word_break_all("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        self.assertEqual(sorted(result), ["cat sand dog", "cats and dog"])


if __name__ == "__main__":
    unittest.main()
