"""Tests for Edit Distance (Levenshtein Distance) algorithms.

Tests Popperian Falsification Invariants:
    P1: edit_distance(s, s) = 0 (identity)
    P2: edit_distance(s1, s2) = edit_distance(s2, s1) (symmetry)
    P3: edit_distance(s1, s2) <= len(s1) + len(s2) (upper bound)
    P4: edit_distance >= |len(s1) - len(s2)| (lower bound)
"""

from __future__ import annotations

import random
import string
import unittest

from algorithm_corpus.dynamic_programming.edit_distance import (
    edit_distance,
    edit_distance_operations,
    edit_distance_optimized,
    edit_distance_weighted,
)


class TestEditDistance(unittest.TestCase):
    """Unit tests for edit_distance."""

    def test_horse_to_ros(self) -> None:
        """Test classic example."""
        result = edit_distance("horse", "ros")
        self.assertEqual(result, 3)

    def test_intention_to_execution(self) -> None:
        """Test another classic example."""
        result = edit_distance("intention", "execution")
        self.assertEqual(result, 5)

    def test_empty_string(self) -> None:
        """Test with empty string."""
        result = edit_distance("", "abc")
        self.assertEqual(result, 3)

    def test_identical_strings(self) -> None:
        """Test identical strings."""
        result = edit_distance("abc", "abc")
        self.assertEqual(result, 0)


class TestEditDistanceOptimized(unittest.TestCase):
    """Unit tests for edit_distance_optimized."""

    def test_horse_to_ros(self) -> None:
        """Test classic example."""
        result = edit_distance_optimized("horse", "ros")
        self.assertEqual(result, 3)

    def test_different_strings(self) -> None:
        """Test different strings."""
        result = edit_distance_optimized("abc", "def")
        self.assertEqual(result, 3)


class TestEditDistanceOperations(unittest.TestCase):
    """Unit tests for edit_distance_operations."""

    def test_single_replace(self) -> None:
        """Test single replacement."""
        result = edit_distance_operations("cat", "cut")
        self.assertEqual(len(result), 1)
        self.assertIn("Replace", result[0])

    def test_insertions(self) -> None:
        """Test insertions."""
        result = edit_distance_operations("", "ab")
        self.assertEqual(len(result), 2)
        for op in result:
            self.assertIn("Insert", op)

    def test_no_operations(self) -> None:
        """Test identical strings need no operations."""
        result = edit_distance_operations("abc", "abc")
        self.assertEqual(len(result), 0)


class TestEditDistanceWeighted(unittest.TestCase):
    """Unit tests for edit_distance_weighted."""

    def test_equal_weights(self) -> None:
        """Test with equal weights."""
        result = edit_distance_weighted("abc", "def", 1, 1, 1)
        self.assertEqual(result, 3)

    def test_higher_replace_cost(self) -> None:
        """Test with higher replacement cost."""
        result = edit_distance_weighted("abc", "def", 1, 1, 2)
        self.assertEqual(result, 6)


class TestEditDistanceInvariants(unittest.TestCase):
    """Popperian falsification tests for edit distance invariants."""

    def _random_string(self, rng: random.Random, length: int) -> str:
        """Generate a random string."""
        return "".join(rng.choices(string.ascii_lowercase, k=length))

    def test_p1_identity(self) -> None:
        """P1: edit_distance(s, s) = 0."""
        rng = random.Random(42)
        for _ in range(30):
            length = rng.randint(0, 20)
            s = self._random_string(rng, length)
            self.assertEqual(edit_distance(s, s), 0)
            self.assertEqual(edit_distance_optimized(s, s), 0)

    def test_p2_symmetry(self) -> None:
        """P2: edit_distance(s1, s2) = edit_distance(s2, s1)."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 15)
            len2 = rng.randint(0, 15)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            self.assertEqual(edit_distance(s1, s2), edit_distance(s2, s1))

    def test_p3_upper_bound(self) -> None:
        """P3: edit_distance(s1, s2) <= len(s1) + len(s2)."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 15)
            len2 = rng.randint(0, 15)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            dist = edit_distance(s1, s2)
            self.assertLessEqual(dist, len(s1) + len(s2))

    def test_p4_lower_bound(self) -> None:
        """P4: edit_distance >= |len(s1) - len(s2)|."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 15)
            len2 = rng.randint(0, 15)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            dist = edit_distance(s1, s2)
            self.assertGreaterEqual(dist, abs(len(s1) - len(s2)))

    def test_optimized_consistency(self) -> None:
        """Both implementations should give same results."""
        rng = random.Random(42)
        for _ in range(50):
            len1 = rng.randint(0, 15)
            len2 = rng.randint(0, 15)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            self.assertEqual(edit_distance(s1, s2), edit_distance_optimized(s1, s2))

    def test_operations_count_matches(self) -> None:
        """Number of operations should equal edit distance."""
        rng = random.Random(42)
        for _ in range(30):
            len1 = rng.randint(0, 10)
            len2 = rng.randint(0, 10)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            dist = edit_distance(s1, s2)
            ops = edit_distance_operations(s1, s2)
            self.assertEqual(len(ops), dist)

    def test_triangle_inequality(self) -> None:
        """Edit distance satisfies triangle inequality."""
        rng = random.Random(42)
        for _ in range(30):
            len1 = rng.randint(0, 10)
            len2 = rng.randint(0, 10)
            len3 = rng.randint(0, 10)
            s1 = self._random_string(rng, len1)
            s2 = self._random_string(rng, len2)
            s3 = self._random_string(rng, len3)
            d12 = edit_distance(s1, s2)
            d23 = edit_distance(s2, s3)
            d13 = edit_distance(s1, s3)
            self.assertLessEqual(d13, d12 + d23)


if __name__ == "__main__":
    unittest.main()
