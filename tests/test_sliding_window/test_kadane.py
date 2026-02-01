"""Tests for Maximum Sum Subarray (Kadane's Algorithm).

Tests Popperian Falsification Invariants:
    P1: Result >= max(nums) (at minimum, single element is valid subarray)
    P2: Result <= sum(nums) (can't exceed total sum)
    P3: For all-negative arrays, result is the maximum element
    P4: For all-positive arrays, result is the total sum
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.sliding_window.kadane import (
    max_circular_subarray_sum,
    max_subarray_fixed_size,
    max_subarray_indices,
    max_subarray_product,
    max_subarray_sum,
)


class TestMaxSubarraySum(unittest.TestCase):
    """Unit tests for max_subarray_sum."""

    def test_standard_case(self) -> None:
        """Test standard Kadane case."""
        result = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(result, 6)

    def test_single_element(self) -> None:
        """Test single element."""
        result = max_subarray_sum([1])
        self.assertEqual(result, 1)

    def test_all_negative(self) -> None:
        """Test all negative numbers."""
        result = max_subarray_sum([-1, -2, -3])
        self.assertEqual(result, -1)

    def test_all_positive(self) -> None:
        """Test all positive numbers."""
        result = max_subarray_sum([5, 4, -1, 7, 8])
        self.assertEqual(result, 23)

    def test_empty_array(self) -> None:
        """Test empty array."""
        result = max_subarray_sum([])
        self.assertEqual(result, 0)


class TestMaxSubarrayIndices(unittest.TestCase):
    """Unit tests for max_subarray_indices."""

    def test_returns_indices(self) -> None:
        """Test that indices are returned."""
        max_sum, start, end = max_subarray_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(max_sum, 6)
        self.assertEqual(start, 3)
        self.assertEqual(end, 6)

    def test_full_array(self) -> None:
        """Test when full array is max."""
        max_sum, start, end = max_subarray_indices([1, 2, 3])
        self.assertEqual(max_sum, 6)
        self.assertEqual(start, 0)
        self.assertEqual(end, 2)

    def test_single_element(self) -> None:
        """Test single element."""
        max_sum, start, end = max_subarray_indices([-1])
        self.assertEqual(max_sum, -1)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)


class TestMaxSubarrayFixedSize(unittest.TestCase):
    """Unit tests for max_subarray_fixed_size."""

    def test_fixed_size(self) -> None:
        """Test fixed size window."""
        result = max_subarray_fixed_size([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
        self.assertEqual(result, 39)

    def test_small_window(self) -> None:
        """Test small window."""
        result = max_subarray_fixed_size([1, 2, 3], 2)
        self.assertEqual(result, 5)

    def test_single_element_window(self) -> None:
        """Test single element window."""
        result = max_subarray_fixed_size([5], 1)
        self.assertEqual(result, 5)

    def test_invalid_window(self) -> None:
        """Test invalid window size."""
        result = max_subarray_fixed_size([1, 2], 5)
        self.assertEqual(result, 0)


class TestMaxCircularSubarraySum(unittest.TestCase):
    """Unit tests for max_circular_subarray_sum."""

    def test_non_circular_max(self) -> None:
        """Test when max is non-circular."""
        result = max_circular_subarray_sum([1, -2, 3, -2])
        self.assertEqual(result, 3)

    def test_circular_max(self) -> None:
        """Test when max wraps around."""
        result = max_circular_subarray_sum([5, -3, 5])
        self.assertEqual(result, 10)

    def test_all_negative(self) -> None:
        """Test all negative."""
        result = max_circular_subarray_sum([-3, -2, -3])
        self.assertEqual(result, -2)


class TestMaxSubarrayProduct(unittest.TestCase):
    """Unit tests for max_subarray_product."""

    def test_positive_product(self) -> None:
        """Test positive product."""
        result = max_subarray_product([2, 3, -2, 4])
        self.assertEqual(result, 6)

    def test_with_zero(self) -> None:
        """Test with zero."""
        result = max_subarray_product([-2, 0, -1])
        self.assertEqual(result, 0)

    def test_two_negatives(self) -> None:
        """Test two negatives make positive."""
        result = max_subarray_product([-2, 3, -4])
        self.assertEqual(result, 24)


class TestKadaneInvariants(unittest.TestCase):
    """Popperian falsification tests for Kadane invariants."""

    def _brute_force_max_subarray(self, nums: list[int]) -> int:
        """Brute force max subarray sum."""
        if not nums:
            return 0
        best = nums[0]
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                best = max(best, sum(nums[i : j + 1]))
        return best

    def test_p1_at_least_max_element(self) -> None:
        """P1: Result >= max(nums)."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            nums = [rng.randint(-10, 10) for _ in range(n)]
            result = max_subarray_sum(nums)
            self.assertGreaterEqual(result, max(nums))

    def test_p2_result_leq_sum_all_nonneg(self) -> None:
        """P2: When all elements are non-negative, result equals sum."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            nums = [rng.randint(0, 10) for _ in range(n)]
            result = max_subarray_sum(nums)
            total = sum(nums)
            self.assertEqual(result, total)

    def test_p3_all_negative(self) -> None:
        """P3: For all-negative arrays, result is the maximum element."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 20)
            nums = [-rng.randint(1, 20) for _ in range(n)]
            result = max_subarray_sum(nums)
            self.assertEqual(result, max(nums))

    def test_p4_all_positive(self) -> None:
        """P4: For all-positive arrays, result is the total sum."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 20)
            nums = [rng.randint(1, 20) for _ in range(n)]
            result = max_subarray_sum(nums)
            self.assertEqual(result, sum(nums))

    def test_optimality(self) -> None:
        """Result should match brute force."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 15)
            nums = [rng.randint(-10, 10) for _ in range(n)]
            kadane_result = max_subarray_sum(nums)
            brute_result = self._brute_force_max_subarray(nums)
            self.assertEqual(kadane_result, brute_result)

    def test_indices_validity(self) -> None:
        """Returned indices should produce the max sum."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            nums = [rng.randint(-10, 10) for _ in range(n)]
            max_sum, start, end = max_subarray_indices(nums)
            if nums:
                self.assertEqual(sum(nums[start : end + 1]), max_sum)

    def test_fixed_size_validity(self) -> None:
        """Fixed size result should be achievable."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 20)
            nums = [rng.randint(-10, 10) for _ in range(n)]
            k = rng.randint(1, n)
            result = max_subarray_fixed_size(nums, k)
            # Verify by checking all windows
            expected = max(sum(nums[i : i + k]) for i in range(n - k + 1))
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
