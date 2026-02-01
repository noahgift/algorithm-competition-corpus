"""Tests for String Operations.

Tests Popperian Falsification Invariants:
    P1: is_anagram returns True iff strings are permutations
    P2: anagram_groups contains all input strings
    P3: reverse_words preserves all characters
    P4: Operations handle empty strings correctly
"""

from __future__ import annotations

import unittest

from algorithm_corpus.string.string_ops import (
    anagram_groups,
    is_anagram,
    reverse_words,
)


class TestIsAnagram(unittest.TestCase):
    """Unit tests for is_anagram."""

    def test_anagrams(self) -> None:
        """Test true anagrams."""
        self.assertTrue(is_anagram("listen", "silent"))

    def test_not_anagrams(self) -> None:
        """Test non-anagrams."""
        self.assertFalse(is_anagram("hello", "world"))

    def test_empty(self) -> None:
        """Test empty strings."""
        self.assertTrue(is_anagram("", ""))

    def test_single_char(self) -> None:
        """Test single character."""
        self.assertTrue(is_anagram("a", "a"))


class TestAnagramGroups(unittest.TestCase):
    """Unit tests for anagram_groups."""

    def test_basic(self) -> None:
        """Test basic grouping."""
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = sorted([sorted(g) for g in anagram_groups(words)])
        expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
        self.assertEqual(result, expected)

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(anagram_groups([]), [])

    def test_single(self) -> None:
        """Test single word."""
        self.assertEqual(anagram_groups(["a"]), [["a"]])


class TestReverseWords(unittest.TestCase):
    """Unit tests for reverse_words."""

    def test_basic(self) -> None:
        """Test basic reversal."""
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_extra_spaces(self) -> None:
        """Test with extra spaces."""
        self.assertEqual(reverse_words("  hello   world  "), "world hello")

    def test_empty(self) -> None:
        """Test empty string."""
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self) -> None:
        """Test single word."""
        self.assertEqual(reverse_words("a"), "a")


class TestStringOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for string ops invariants."""

    def test_p1_anagram_permutation(self) -> None:
        """P1: is_anagram returns True iff strings are permutations."""
        # True cases
        self.assertTrue(is_anagram("abc", "cba"))
        self.assertTrue(is_anagram("aab", "aba"))
        # False cases
        self.assertFalse(is_anagram("abc", "abd"))
        self.assertFalse(is_anagram("aa", "a"))

    def test_p2_all_strings_in_groups(self) -> None:
        """P2: anagram_groups contains all input strings."""
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        groups = anagram_groups(words)
        all_words = []
        for g in groups:
            all_words.extend(g)
        self.assertEqual(sorted(all_words), sorted(words))

    def test_p3_reverse_preserves_chars(self) -> None:
        """P3: reverse_words preserves all characters (excluding extra spaces)."""
        s = "hello world foo"
        result = reverse_words(s)
        # Check words are preserved
        self.assertEqual(sorted(s.split()), sorted(result.split()))

    def test_p4_empty_handling(self) -> None:
        """P4: Operations handle empty strings correctly."""
        self.assertTrue(is_anagram("", ""))
        self.assertEqual(anagram_groups([]), [])
        self.assertEqual(reverse_words(""), "")


if __name__ == "__main__":
    unittest.main()
