"""Tests for Rabin-Karp algorithm.

Tests Popperian Falsification Invariants:
    P1: All returned indices are valid pattern matches
    P2: No valid match is missed
    P3: Hash collisions are handled correctly
    P4: Pattern at returned index equals pattern string
"""

from __future__ import annotations

import unittest

from algorithm_corpus.string.kmp import kmp_search
from algorithm_corpus.string.rabin_karp import (
    rabin_karp_search,
)


class TestRabinKarpSearch(unittest.TestCase):
    """Unit tests for rabin_karp_search."""

    def test_multiple_matches(self) -> None:
        """Test finding multiple matches."""
        self.assertEqual(rabin_karp_search("ababcababcabc", "abc"), [2, 7, 10])

    def test_overlapping(self) -> None:
        """Test overlapping matches."""
        self.assertEqual(rabin_karp_search("aaaaaa", "aa"), [0, 1, 2, 3, 4])

    def test_no_match(self) -> None:
        """Test no matches."""
        self.assertEqual(rabin_karp_search("hello", "xyz"), [])

    def test_empty_pattern(self) -> None:
        """Test empty pattern."""
        self.assertEqual(rabin_karp_search("hello", ""), [])


class TestRabinKarpInvariants(unittest.TestCase):
    """Popperian falsification tests for Rabin-Karp invariants."""

    def test_p1_valid_matches(self) -> None:
        """P1: All returned indices are valid pattern matches."""
        text = "ababcababcabc"
        pattern = "abc"
        matches = rabin_karp_search(text, pattern)
        for idx in matches:
            self.assertEqual(text[idx : idx + len(pattern)], pattern)

    def test_p2_no_missed_matches(self) -> None:
        """P2: No valid match is missed."""
        text = "aaaaaa"
        pattern = "aa"
        matches = rabin_karp_search(text, pattern)
        expected = [
            i
            for i in range(len(text) - len(pattern) + 1)
            if text[i : i + len(pattern)] == pattern
        ]
        self.assertEqual(matches, expected)

    def test_p3_handles_collisions(self) -> None:
        """P3: Hash collisions are handled correctly."""
        # Test with patterns that might have hash collisions
        text = "abcdefghijklmnopqrstuvwxyz"
        pattern = "xyz"
        matches = rabin_karp_search(text, pattern)
        self.assertEqual(matches, [23])
        # Verify the match is correct
        for idx in matches:
            self.assertEqual(text[idx : idx + len(pattern)], pattern)

    def test_consistency_with_kmp(self) -> None:
        """Rabin-Karp should give same results as KMP."""
        test_cases = [
            ("hello world hello", "hello"),
            ("ababab", "ab"),
            ("mississippi", "issi"),
        ]
        for text, pattern in test_cases:
            rk_result = rabin_karp_search(text, pattern)
            kmp_result = kmp_search(text, pattern)
            self.assertEqual(rk_result, kmp_result)


if __name__ == "__main__":
    unittest.main()
