"""Tests for Sliding window max/min algorithms.

Tests Popperian Falsification Invariants:
    P1: Max is actually maximum in window
    P2: Min is actually minimum in window
    P3: Result length is n - k + 1
    P4: Empty input returns empty
"""

from __future__ import annotations

import unittest

from algorithm_corpus.queue.sliding_max import (
    max_sliding_window,
    min_sliding_window,
)


class TestMaxSlidingWindow(unittest.TestCase):
    """Unit tests for max_sliding_window."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(
            max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]
        )

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(max_sliding_window([1], 1), [1])

    def test_k_equals_n(self) -> None:
        """Test window equals array size."""
        self.assertEqual(max_sliding_window([1, 2, 3], 3), [3])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(max_sliding_window([], 3), [])


class TestMinSlidingWindow(unittest.TestCase):
    """Unit tests for min_sliding_window."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(
            min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [-1, -3, -3, -3, 3, 3]
        )

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(min_sliding_window([1], 1), [1])

    def test_empty(self) -> None:
        """Test empty input."""
        self.assertEqual(min_sliding_window([], 3), [])


class TestSlidingWindowInvariants(unittest.TestCase):
    """Popperian falsification tests for sliding window invariants."""

    def test_p1_max_is_maximum(self) -> None:
        """P1: Max is actually maximum in window."""
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        result = max_sliding_window(nums, k)
        for i, max_val in enumerate(result):
            window = nums[i : i + k]
            self.assertEqual(max_val, max(window))

    def test_p2_min_is_minimum(self) -> None:
        """P2: Min is actually minimum in window."""
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        result = min_sliding_window(nums, k)
        for i, min_val in enumerate(result):
            window = nums[i : i + k]
            self.assertEqual(min_val, min(window))

    def test_p3_result_length(self) -> None:
        """P3: Result length is n - k + 1."""
        for n in [5, 8, 10]:
            for k in [1, 3, n]:
                nums = list(range(n))
                result = max_sliding_window(nums, k)
                self.assertEqual(len(result), n - k + 1)

    def test_p4_empty_returns_empty(self) -> None:
        """P4: Empty input returns empty."""
        self.assertEqual(max_sliding_window([], 1), [])
        self.assertEqual(min_sliding_window([], 1), [])


if __name__ == "__main__":
    unittest.main()
