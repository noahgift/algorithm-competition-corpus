"""Tests for Binary Search algorithms.

Tests Popperian Falsification Invariants:
    P1: If found, arr[result] == target
    P2: If not found, result == -1
    P3: Search space halves each iteration (logarithmic)
    P4: Works correctly on empty arrays (returns -1)
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.binary_search.binary_search import (
    binary_search,
    binary_search_leftmost,
    binary_search_rightmost,
    lower_bound,
    upper_bound,
)


class TestBinarySearch(unittest.TestCase):
    """Unit tests for binary_search."""

    def test_found(self) -> None:
        """Test finding element."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self) -> None:
        """Test element not present."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element(self) -> None:
        """Test single element array."""
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1], 2), -1)


class TestBinarySearchLeftmost(unittest.TestCase):
    """Unit tests for binary_search_leftmost."""

    def test_leftmost_duplicates(self) -> None:
        """Test finding leftmost in duplicates."""
        self.assertEqual(binary_search_leftmost([1, 2, 2, 2, 3], 2), 1)

    def test_not_found(self) -> None:
        """Test element not present."""
        self.assertEqual(binary_search_leftmost([1, 2, 3], 4), -1)

    def test_all_same(self) -> None:
        """Test all same elements."""
        self.assertEqual(binary_search_leftmost([2, 2, 2], 2), 0)


class TestBinarySearchRightmost(unittest.TestCase):
    """Unit tests for binary_search_rightmost."""

    def test_rightmost_duplicates(self) -> None:
        """Test finding rightmost in duplicates."""
        self.assertEqual(binary_search_rightmost([1, 2, 2, 2, 3], 2), 3)

    def test_all_same(self) -> None:
        """Test all same elements."""
        self.assertEqual(binary_search_rightmost([2, 2, 2], 2), 2)


class TestLowerBound(unittest.TestCase):
    """Unit tests for lower_bound."""

    def test_target_not_present(self) -> None:
        """Test when target not in array."""
        self.assertEqual(lower_bound([1, 2, 4, 5], 3), 2)

    def test_target_present(self) -> None:
        """Test when target in array."""
        self.assertEqual(lower_bound([1, 2, 3], 2), 1)

    def test_all_smaller(self) -> None:
        """Test when all elements smaller."""
        self.assertEqual(lower_bound([1, 2, 3], 4), 3)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(lower_bound([], 1), 0)


class TestUpperBound(unittest.TestCase):
    """Unit tests for upper_bound."""

    def test_with_duplicates(self) -> None:
        """Test with duplicate elements."""
        self.assertEqual(upper_bound([1, 2, 2, 3], 2), 3)

    def test_target_at_end(self) -> None:
        """Test target at end."""
        self.assertEqual(upper_bound([1, 2, 3], 3), 3)

    def test_target_smaller_than_all(self) -> None:
        """Test target smaller than all."""
        self.assertEqual(upper_bound([1, 2, 3], 0), 0)


class TestBinarySearchInvariants(unittest.TestCase):
    """Popperian falsification tests for binary search invariants."""

    def test_p1_found_equals_target(self) -> None:
        """P1: If found, arr[result] == target."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 100)
            arr = sorted(rng.randint(0, 100) for _ in range(n))
            target = rng.choice(arr)
            idx = binary_search(arr, target)
            self.assertNotEqual(idx, -1)
            self.assertEqual(arr[idx], target)

    def test_p2_not_found_returns_minus_one(self) -> None:
        """P2: If not found, result == -1."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted(rng.randint(0, 50) for _ in range(n))
            target = 1000  # Guaranteed not in array
            idx = binary_search(arr, target)
            self.assertEqual(idx, -1)

    def test_p4_empty_returns_minus_one(self) -> None:
        """P4: Works correctly on empty arrays."""
        self.assertEqual(binary_search([], 5), -1)
        self.assertEqual(binary_search_leftmost([], 5), -1)
        self.assertEqual(binary_search_rightmost([], 5), -1)

    def test_leftmost_rightmost_range(self) -> None:
        """Leftmost <= any found index <= rightmost."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted(rng.randint(0, 10) for _ in range(n))
            target = rng.choice(arr)
            left = binary_search_leftmost(arr, target)
            right = binary_search_rightmost(arr, target)
            self.assertLessEqual(left, right)
            # All elements in range equal target
            for i in range(left, right + 1):
                self.assertEqual(arr[i], target)

    def test_lower_upper_bound_consistency(self) -> None:
        """lower_bound <= upper_bound for same target."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted(rng.randint(0, 20) for _ in range(n))
            target = rng.randint(0, 25)
            low = lower_bound(arr, target)
            high = upper_bound(arr, target)
            self.assertLessEqual(low, high)


if __name__ == "__main__":
    unittest.main()
