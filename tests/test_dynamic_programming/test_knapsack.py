"""Tests for Knapsack Problem algorithms.

Tests Popperian Falsification Invariants:
    P1: Selected items' total weight <= capacity
    P2: Solution value >= 0
    P3: Solution is optimal among all valid selections
    P4: dp[i][w] represents best value using items 0..i-1 with capacity w
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.dynamic_programming.knapsack import (
    knapsack_01,
    knapsack_01_items,
    knapsack_01_optimized,
    knapsack_bounded,
    knapsack_unbounded,
)


class TestKnapsack01(unittest.TestCase):
    """Unit tests for knapsack_01."""

    def test_simple_case(self) -> None:
        """Test simple knapsack case."""
        result = knapsack_01([1, 2, 3], [6, 10, 12], 5)
        self.assertEqual(result, 22)

    def test_larger_case(self) -> None:
        """Test larger knapsack case."""
        result = knapsack_01([10, 20, 30], [60, 100, 120], 50)
        self.assertEqual(result, 220)

    def test_empty_inputs(self) -> None:
        """Test empty inputs."""
        result = knapsack_01([], [], 10)
        self.assertEqual(result, 0)

    def test_item_too_heavy(self) -> None:
        """Test when item is too heavy."""
        result = knapsack_01([5], [10], 3)
        self.assertEqual(result, 0)


class TestKnapsack01Items(unittest.TestCase):
    """Unit tests for knapsack_01_items."""

    def test_returns_items(self) -> None:
        """Test that selected items are returned."""
        val, items = knapsack_01_items([1, 2, 3], [6, 10, 12], 5)
        self.assertEqual(val, 22)
        self.assertEqual(sorted(items), [1, 2])

    def test_item_too_heavy(self) -> None:
        """Test when item is too heavy."""
        val, items = knapsack_01_items([10], [100], 5)
        self.assertEqual(val, 0)
        self.assertEqual(items, [])

    def test_empty_inputs(self) -> None:
        """Test empty inputs."""
        val, items = knapsack_01_items([], [], 10)
        self.assertEqual(val, 0)
        self.assertEqual(items, [])


class TestKnapsack01Optimized(unittest.TestCase):
    """Unit tests for knapsack_01_optimized."""

    def test_simple_case(self) -> None:
        """Test simple knapsack case."""
        result = knapsack_01_optimized([1, 2, 3], [6, 10, 12], 5)
        self.assertEqual(result, 22)

    def test_another_case(self) -> None:
        """Test another case."""
        result = knapsack_01_optimized([2, 3, 4, 5], [3, 4, 5, 6], 5)
        self.assertEqual(result, 7)


class TestKnapsackUnbounded(unittest.TestCase):
    """Unit tests for knapsack_unbounded."""

    def test_unbounded(self) -> None:
        """Test unbounded knapsack."""
        result = knapsack_unbounded([1, 3, 4], [15, 50, 60], 8)
        self.assertEqual(result, 130)

    def test_larger_capacity(self) -> None:
        """Test with larger capacity."""
        result = knapsack_unbounded([5, 10, 15], [10, 30, 50], 100)
        self.assertEqual(result, 330)

    def test_single_item(self) -> None:
        """Test with single item type."""
        result = knapsack_unbounded([2], [10], 7)
        self.assertEqual(result, 30)


class TestKnapsackBounded(unittest.TestCase):
    """Unit tests for knapsack_bounded."""

    def test_bounded(self) -> None:
        """Test bounded knapsack."""
        result = knapsack_bounded([1, 2, 3], [6, 10, 12], [2, 2, 1], 5)
        self.assertEqual(result, 26)

    def test_limited_quantity(self) -> None:
        """Test with limited quantity."""
        result = knapsack_bounded([2], [10], [3], 5)
        self.assertEqual(result, 20)


class TestKnapsackInvariants(unittest.TestCase):
    """Popperian falsification tests for knapsack invariants."""

    def _brute_force_01(
        self, weights: list[int], values: list[int], capacity: int
    ) -> int:
        """Brute force 0/1 knapsack for verification."""
        n = len(weights)
        best = 0
        for mask in range(1 << n):
            total_weight = 0
            total_value = 0
            for i in range(n):
                if mask & (1 << i):
                    total_weight += weights[i]
                    total_value += values[i]
            if total_weight <= capacity:
                best = max(best, total_value)
        return best

    def test_p1_weight_constraint(self) -> None:
        """P1: Selected items' total weight <= capacity."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 10)
            weights = [rng.randint(1, 20) for _ in range(n)]
            values = [rng.randint(1, 100) for _ in range(n)]
            capacity = rng.randint(1, 50)
            _, items = knapsack_01_items(weights, values, capacity)
            total_weight = sum(weights[i] for i in items)
            self.assertLessEqual(total_weight, capacity)

    def test_p2_non_negative_value(self) -> None:
        """P2: Solution value >= 0."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(0, 10)
            weights = [rng.randint(1, 20) for _ in range(n)]
            values = [rng.randint(1, 100) for _ in range(n)]
            capacity = rng.randint(0, 50)
            result = knapsack_01(weights, values, capacity)
            self.assertGreaterEqual(result, 0)

    def test_p3_optimality(self) -> None:
        """P3: Solution is optimal among all valid selections."""
        rng = random.Random(42)
        for _ in range(20):
            n = rng.randint(1, 8)  # Small for brute force
            weights = [rng.randint(1, 10) for _ in range(n)]
            values = [rng.randint(1, 50) for _ in range(n)]
            capacity = rng.randint(1, 30)
            dp_result = knapsack_01(weights, values, capacity)
            brute_result = self._brute_force_01(weights, values, capacity)
            self.assertEqual(dp_result, brute_result)

    def test_implementations_consistency(self) -> None:
        """All 0/1 implementations should give same value."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 15)
            weights = [rng.randint(1, 20) for _ in range(n)]
            values = [rng.randint(1, 100) for _ in range(n)]
            capacity = rng.randint(1, 50)
            result1 = knapsack_01(weights, values, capacity)
            result2, _ = knapsack_01_items(weights, values, capacity)
            result3 = knapsack_01_optimized(weights, values, capacity)
            self.assertEqual(result1, result2)
            self.assertEqual(result1, result3)

    def test_unbounded_at_least_01(self) -> None:
        """Unbounded should be at least as good as 0/1."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 10)
            weights = [rng.randint(1, 10) for _ in range(n)]
            values = [rng.randint(1, 50) for _ in range(n)]
            capacity = rng.randint(1, 30)
            result_01 = knapsack_01(weights, values, capacity)
            result_unbounded = knapsack_unbounded(weights, values, capacity)
            self.assertGreaterEqual(result_unbounded, result_01)


if __name__ == "__main__":
    unittest.main()
