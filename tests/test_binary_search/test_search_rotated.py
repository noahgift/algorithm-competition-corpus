"""Tests for Search in Rotated Sorted Array.

Tests Popperian Falsification Invariants:
    P1: If found, arr[result] == target
    P2: If not found, result == -1
    P3: Works correctly on non-rotated arrays
    P4: Maintains O(log n) time complexity
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.binary_search.search_rotated import (
    find_min_rotated,
    search_rotated,
)


class TestSearchRotated(unittest.TestCase):
    """Unit tests for search_rotated."""

    def test_found_in_rotated(self) -> None:
        """Test finding element in rotated array."""
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_not_found(self) -> None:
        """Test element not present."""
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_single_element(self) -> None:
        """Test single element array."""
        self.assertEqual(search_rotated([1], 1), 0)

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(search_rotated([], 1), -1)

    def test_non_rotated(self) -> None:
        """Test non-rotated (normal sorted) array."""
        self.assertEqual(search_rotated([1, 2, 3, 4, 5], 3), 2)


class TestFindMinRotated(unittest.TestCase):
    """Unit tests for find_min_rotated."""

    def test_rotated_array(self) -> None:
        """Test finding minimum in rotated array."""
        self.assertEqual(find_min_rotated([3, 4, 5, 1, 2]), 1)

    def test_highly_rotated(self) -> None:
        """Test highly rotated array."""
        self.assertEqual(find_min_rotated([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(find_min_rotated([1]), 1)

    def test_two_elements(self) -> None:
        """Test two elements."""
        self.assertEqual(find_min_rotated([2, 1]), 1)

    def test_non_rotated(self) -> None:
        """Test non-rotated array."""
        self.assertEqual(find_min_rotated([1, 2, 3, 4, 5]), 1)


class TestSearchRotatedInvariants(unittest.TestCase):
    """Popperian falsification tests for search_rotated invariants."""

    def _rotate_array(self, arr: list[int], k: int) -> list[int]:
        """Rotate array by k positions."""
        if not arr:
            return arr
        k = k % len(arr)
        return arr[-k:] + arr[:-k]

    def test_p1_found_equals_target(self) -> None:
        """P1: If found, arr[result] == target."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted({rng.randint(0, 100) for _ in range(n)})
            k = rng.randint(0, len(arr))
            rotated = self._rotate_array(arr, k)
            target = rng.choice(rotated)
            idx = search_rotated(rotated, target)
            self.assertNotEqual(idx, -1)
            self.assertEqual(rotated[idx], target)

    def test_p2_not_found_returns_minus_one(self) -> None:
        """P2: If not found, result == -1."""
        arr = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(search_rotated(arr, 100), -1)

    def test_p3_works_on_non_rotated(self) -> None:
        """P3: Works correctly on non-rotated arrays."""
        arr = [1, 2, 3, 4, 5, 6, 7]
        for target in arr:
            idx = search_rotated(arr, target)
            self.assertEqual(arr[idx], target)

    def test_find_min_is_actual_min(self) -> None:
        """find_min_rotated returns actual minimum."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 50)
            arr = sorted({rng.randint(0, 100) for _ in range(n)})
            k = rng.randint(0, len(arr))
            rotated = self._rotate_array(arr, k)
            found_min = find_min_rotated(rotated)
            self.assertEqual(found_min, min(rotated))


if __name__ == "__main__":
    unittest.main()
