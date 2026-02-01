"""Tests for Palindrome algorithms.

Tests Popperian Falsification Invariants:
    P1: Empty string is a palindrome
    P2: Single character is a palindrome
    P3: Palindrome reads same forwards and backwards
    P4: Longest palindromic substring is actually a palindrome
"""

from __future__ import annotations

import unittest

from algorithm_corpus.two_pointers.palindrome import (
    is_palindrome,
    longest_palindromic_substring,
)


class TestIsPalindrome(unittest.TestCase):
    """Unit tests for is_palindrome."""

    def test_complex_palindrome(self) -> None:
        """Test complex palindrome with spaces and punctuation."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self) -> None:
        """Test non-palindrome."""
        self.assertFalse(is_palindrome("race a car"))

    def test_empty(self) -> None:
        """Test empty string."""
        self.assertTrue(is_palindrome(""))

    def test_single_char(self) -> None:
        """Test single character."""
        self.assertTrue(is_palindrome("a"))


class TestLongestPalindromicSubstring(unittest.TestCase):
    """Unit tests for longest_palindromic_substring."""

    def test_example1(self) -> None:
        """Test first example."""
        result = longest_palindromic_substring("babad")
        self.assertIn(result, ("bab", "aba"))

    def test_example2(self) -> None:
        """Test second example."""
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

    def test_empty(self) -> None:
        """Test empty string."""
        self.assertEqual(longest_palindromic_substring(""), "")

    def test_single_char(self) -> None:
        """Test single character."""
        self.assertEqual(longest_palindromic_substring("a"), "a")


class TestPalindromeInvariants(unittest.TestCase):
    """Popperian falsification tests for palindrome invariants."""

    def test_p1_empty_is_palindrome(self) -> None:
        """P1: Empty string is a palindrome."""
        self.assertTrue(is_palindrome(""))

    def test_p2_single_char_is_palindrome(self) -> None:
        """P2: Single character is a palindrome."""
        for c in "abcxyz123":
            self.assertTrue(is_palindrome(c))

    def test_p3_palindrome_reverse(self) -> None:
        """P3: Palindrome reads same forwards and backwards."""
        palindromes = ["racecar", "level", "noon", "deed"]
        for p in palindromes:
            self.assertTrue(is_palindrome(p))
            self.assertEqual(p, p[::-1])

    def test_p4_longest_is_palindrome(self) -> None:
        """P4: Longest palindromic substring is actually a palindrome."""
        test_cases = ["babad", "cbbd", "abcba", "abacdfgdcaba"]
        for s in test_cases:
            result = longest_palindromic_substring(s)
            # Check it's a palindrome
            self.assertEqual(result, result[::-1])
            # Check it's a substring
            self.assertIn(result, s)


if __name__ == "__main__":
    unittest.main()
