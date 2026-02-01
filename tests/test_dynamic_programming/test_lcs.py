"""Tests for Longest Common Subsequence algorithms.

Tests Popperian Falsification Invariants:
    P1: LCS is a subsequence of both strings
    P2: LCS length <= min(len(s1), len(s2))
    P3: LCS(s, s) = s (reflexivity)
    P4: LCS(s1, s2) = LCS(s2, s1) (symmetry in length)
"""

from __future__ import annotations

import random
import string
import unittest

from algorithm_corpus.dynamic_programming.lcs import (
    lcs_length,
    lcs_optimized,
    lcs_string,
    lcs_three_strings,
)


class TestLcsLength(unittest.TestCase):
    """Unit tests for lcs_length."""

    def test_common_subsequence(self) -> None:
        """Test finding common subsequence."""
        result = lcs_length("abcde", "ace")
        self.assertEqual(result, 3)

    def test_no_common(self) -> None:
        """Test with no common characters."""
        result = lcs_length("abc", "def")
        self.assertEqual(result, 0)

    def test_identical_strings(self) -> None:
        """Test identical strings."""
        result = lcs_length("abc", "abc")
        self.assertEqual(result, 3)

    def test_empty_string(self) -> None:
        """Test with empty string."""
        result = lcs_length("", "abc")
        self.assertEqual(result, 0)


class TestLcsString(unittest.TestCase):
    """Unit tests for lcs_string."""

    def test_find_lcs(self) -> None:
        """Test finding actual LCS."""
        result = lcs_string("abcde", "ace")
        self.assertEqual(result, "ace")

    def test_no_common(self) -> None:
        """Test with no common characters."""
        result = lcs_string("abc", "def")
        self.assertEqual(result, "")

    def test_identical_strings(self) -> None:
        """Test identical strings."""
        result = lcs_string("abcd", "abcd")
        self.assertEqual(result, "abcd")


class TestLcsOptimized(unittest.TestCase):
    """Unit tests for lcs_optimized."""

    def test_common_subsequence(self) -> None:
        """Test finding common subsequence length."""
        result = lcs_optimized("abcde", "ace")
        self.assertEqual(result, 3)

    def test_no_common(self) -> None:
        """Test with no common characters."""
        result = lcs_optimized("abc", "def")
        self.assertEqual(result, 0)


class TestLcsThreeStrings(unittest.TestCase):
    """Unit tests for lcs_three_strings."""

    def test_identical_strings(self) -> None:
        """Test three identical strings."""
        result = lcs_three_strings("abc", "abc", "abc")
        self.assertEqual(result, 3)

    def test_decreasing_common(self) -> None:
        """Test with decreasing common portion."""
        result = lcs_three_strings("abc", "ab", "a")
        self.assertEqual(result, 1)

    def test_no_common(self) -> None:
        """Test with no common characters."""
        result = lcs_three_strings("abc", "def", "ghi")
        self.assertEqual(result, 0)


class TestLcsInvariants(unittest.TestCase):
    """Popperian falsification tests for LCS invariants."""

    def _is_subsequence(self, sub: str, main: str) -> bool:
        """Check if sub is a subsequence of main."""
        it = iter(main)
        return all(c in it for c in sub)

    def _random_string(self, rng: random.Random, length: int) -> str:
        """Generate a random string."""
        return "".join(rng.choices(string.ascii_lowercase, k=length))

    def test_p1_is_subsequence(self) -> None:
        """P1: LCS is a subsequence of both strings."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 20)
            len2 = rng.randint(0, 20)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            lcs = lcs_string(s1, s2)
            self.assertTrue(
                self._is_subsequence(lcs, s1), f"LCS not in s1: {lcs}, {s1}"
            )
            self.assertTrue(
                self._is_subsequence(lcs, s2), f"LCS not in s2: {lcs}, {s2}"
            )

    def test_p2_length_bound(self) -> None:
        """P2: LCS length <= min(len(s1), len(s2))."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 20)
            len2 = rng.randint(0, 20)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            lcs_len = lcs_length(s1, s2)
            self.assertLessEqual(lcs_len, min(len(s1), len(s2)))

    def test_p3_reflexivity(self) -> None:
        """P3: LCS(s, s) = s."""
        rng = random.Random(42)
        for _ in range(30):
            length = rng.randint(0, 20)
            s = self._random_string(rng, length)
            lcs = lcs_string(s, s)
            self.assertEqual(lcs, s)
            self.assertEqual(lcs_length(s, s), len(s))

    def test_p4_symmetry(self) -> None:
        """P4: LCS(s1, s2) = LCS(s2, s1) in length."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 20)
            len2 = rng.randint(0, 20)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            self.assertEqual(lcs_length(s1, s2), lcs_length(s2, s1))

    def test_length_optimized_consistency(self) -> None:
        """lcs_length and lcs_optimized should give same results."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 20)
            len2 = rng.randint(0, 20)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            self.assertEqual(lcs_length(s1, s2), lcs_optimized(s1, s2))

    def test_string_length_consistency(self) -> None:
        """lcs_string length should match lcs_length."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 15)
            len2 = rng.randint(0, 15)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            self.assertEqual(len(lcs_string(s1, s2)), lcs_length(s1, s2))


if __name__ == "__main__":
    unittest.main()
