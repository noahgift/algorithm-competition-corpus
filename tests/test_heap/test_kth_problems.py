"""Tests for K-th Problems algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.heap.kth_problems import (
    find_kth_largest_quickselect,
    k_closest_to_origin,
    merge_k_sorted_lists,
)


class TestFindKthLargestQuickselect(unittest.TestCase):
    """Unit tests for find_kth_largest_quickselect."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(find_kth_largest_quickselect([3, 2, 1, 5, 6, 4], 2), 5)

    def test_duplicates(self) -> None:
        """Test with duplicates."""
        self.assertEqual(
            find_kth_largest_quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4
        )


class TestKClosestToOrigin(unittest.TestCase):
    """Unit tests for k_closest_to_origin."""

    def test_basic(self) -> None:
        """Test basic case."""
        result = k_closest_to_origin([(1, 3), (-2, 2)], 1)
        self.assertEqual(sorted(result), [(-2, 2)])

    def test_multiple(self) -> None:
        """Test multiple points."""
        result = k_closest_to_origin([(3, 3), (5, -1), (-2, 4)], 2)
        self.assertEqual(len(result), 2)


class TestMergeKSortedLists(unittest.TestCase):
    """Unit tests for merge_k_sorted_lists."""

    def test_basic(self) -> None:
        """Test basic case."""
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        self.assertEqual(merge_k_sorted_lists(lists), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_empty(self) -> None:
        """Test empty lists."""
        self.assertEqual(merge_k_sorted_lists([]), [])


if __name__ == "__main__":
    unittest.main()
