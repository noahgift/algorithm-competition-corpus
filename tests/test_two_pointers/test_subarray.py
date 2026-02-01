"""Tests for Subarray algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.two_pointers.subarray import (
    max_product_subarray,
    shortest_subarray_with_sum,
    subarray_sum_equals_k,
)


class TestSubarraySumEqualsK(unittest.TestCase):
    """Unit tests for subarray_sum_equals_k."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(subarray_sum_equals_k([1, 1, 1], 2), 2)

    def test_multiple(self) -> None:
        """Test multiple."""
        self.assertEqual(subarray_sum_equals_k([1, 2, 3], 3), 2)


class TestMaxProductSubarray(unittest.TestCase):
    """Unit tests for max_product_subarray."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(max_product_subarray([2, 3, -2, 4]), 6)

    def test_zeros(self) -> None:
        """Test with zeros."""
        self.assertEqual(max_product_subarray([-2, 0, -1]), 0)


class TestShortestSubarrayWithSum(unittest.TestCase):
    """Unit tests for shortest_subarray_with_sum."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(shortest_subarray_with_sum([2, -1, 2], 3), 3)

    def test_none(self) -> None:
        """Test no valid."""
        self.assertEqual(shortest_subarray_with_sum([1, 2], 4), -1)


if __name__ == "__main__":
    unittest.main()
