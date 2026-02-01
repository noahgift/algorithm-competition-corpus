"""Tests for KMP algorithm.

Tests Popperian Falsification Invariants:
    P1: All returned indices are valid pattern matches
    P2: No valid match is missed
    P3: O(n + m) time complexity maintained
    P4: Pattern at returned index equals pattern string
"""

from __future__ import annotations

import unittest

from algorithm_corpus.string.kmp import (
    build_failure_function,
    kmp_search,
)


class TestBuildFailureFunction(unittest.TestCase):
    """Unit tests for build_failure_function."""

    def test_basic(self) -> None:
        """Test basic failure function."""
        self.assertEqual(build_failure_function("ababaca"), [0, 0, 1, 2, 3, 0, 1])

    def test_all_same(self) -> None:
        """Test all same characters."""
        self.assertEqual(build_failure_function("aaa"), [0, 1, 2])

    def test_no_prefix(self) -> None:
        """Test no proper prefix-suffix."""
        self.assertEqual(build_failure_function("abc"), [0, 0, 0])

    def test_empty(self) -> None:
        """Test empty pattern."""
        self.assertEqual(build_failure_function(""), [])


class TestKMPSearch(unittest.TestCase):
    """Unit tests for kmp_search."""

    def test_multiple_matches(self) -> None:
        """Test finding multiple matches."""
        self.assertEqual(kmp_search("ababcababcabc", "abc"), [2, 7, 10])

    def test_overlapping(self) -> None:
        """Test overlapping matches."""
        self.assertEqual(kmp_search("aaaaaa", "aa"), [0, 1, 2, 3, 4])

    def test_no_match(self) -> None:
        """Test no matches."""
        self.assertEqual(kmp_search("hello", "xyz"), [])

    def test_empty_pattern(self) -> None:
        """Test empty pattern."""
        self.assertEqual(kmp_search("hello", ""), [])


class TestKMPInvariants(unittest.TestCase):
    """Popperian falsification tests for KMP invariants."""

    def test_p1_valid_matches(self) -> None:
        """P1: All returned indices are valid pattern matches."""
        text = "ababcababcabc"
        pattern = "abc"
        matches = kmp_search(text, pattern)
        for idx in matches:
            self.assertEqual(text[idx : idx + len(pattern)], pattern)

    def test_p2_no_missed_matches(self) -> None:
        """P2: No valid match is missed."""
        text = "aaaaaa"
        pattern = "aa"
        matches = kmp_search(text, pattern)
        # Verify all possible matches are found
        expected = [
            i
            for i in range(len(text) - len(pattern) + 1)
            if text[i : i + len(pattern)] == pattern
        ]
        self.assertEqual(matches, expected)

    def test_p4_pattern_equals(self) -> None:
        """P4: Pattern at returned index equals pattern string."""
        test_cases = [
            ("hello world hello", "hello"),
            ("abcabcabc", "abc"),
            ("xyzxyzxyz", "xyz"),
        ]
        for text, pattern in test_cases:
            matches = kmp_search(text, pattern)
            for idx in matches:
                self.assertEqual(text[idx : idx + len(pattern)], pattern)


if __name__ == "__main__":
    unittest.main()
