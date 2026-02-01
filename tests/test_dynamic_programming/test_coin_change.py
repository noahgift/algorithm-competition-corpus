"""Tests for Coin Change algorithms.

Tests Popperian Falsification Invariants:
    P1: If solution exists, sum of coins equals amount exactly
    P2: coin_change_min returns -1 iff no solution exists
    P3: coin_change_ways >= 0 for all valid inputs
    P4: Minimum coins <= amount (using coin of value 1 if available)
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.dynamic_programming.coin_change import (
    coin_change_coins,
    coin_change_limited,
    coin_change_min,
    coin_change_ways,
    coin_change_ways_permutations,
)


class TestCoinChangeMin(unittest.TestCase):
    """Unit tests for coin_change_min."""

    def test_standard_case(self) -> None:
        """Test standard coin change case."""
        result = coin_change_min([1, 2, 5], 11)
        self.assertEqual(result, 3)

    def test_impossible(self) -> None:
        """Test impossible case."""
        result = coin_change_min([2], 3)
        self.assertEqual(result, -1)

    def test_zero_amount(self) -> None:
        """Test zero amount."""
        result = coin_change_min([1], 0)
        self.assertEqual(result, 0)

    def test_us_coins(self) -> None:
        """Test with US coin denominations."""
        result = coin_change_min([1, 5, 10, 25], 30)
        self.assertEqual(result, 2)  # 25 + 5


class TestCoinChangeCoins(unittest.TestCase):
    """Unit tests for coin_change_coins."""

    def test_returns_coins(self) -> None:
        """Test that actual coins are returned."""
        result = coin_change_coins([1, 2, 5], 11)
        self.assertEqual(sorted(result), [1, 5, 5])

    def test_impossible(self) -> None:
        """Test impossible case returns empty."""
        result = coin_change_coins([2], 3)
        self.assertEqual(result, [])

    def test_zero_amount(self) -> None:
        """Test zero amount returns empty."""
        result = coin_change_coins([1, 5], 0)
        self.assertEqual(result, [])


class TestCoinChangeWays(unittest.TestCase):
    """Unit tests for coin_change_ways."""

    def test_count_ways(self) -> None:
        """Test counting ways."""
        result = coin_change_ways([1, 2, 5], 5)
        self.assertEqual(result, 4)

    def test_impossible(self) -> None:
        """Test impossible case returns 0."""
        result = coin_change_ways([2], 3)
        self.assertEqual(result, 0)

    def test_another_case(self) -> None:
        """Test another case."""
        result = coin_change_ways([1, 2, 3], 4)
        self.assertEqual(result, 4)


class TestCoinChangeWaysPermutations(unittest.TestCase):
    """Unit tests for coin_change_ways_permutations."""

    def test_count_permutations(self) -> None:
        """Test counting permutations."""
        result = coin_change_ways_permutations([1, 2, 5], 5)
        self.assertEqual(result, 9)

    def test_simple_case(self) -> None:
        """Test simple case."""
        result = coin_change_ways_permutations([1, 2], 3)
        self.assertEqual(result, 3)  # 1+1+1, 1+2, 2+1

    def test_impossible(self) -> None:
        """Test impossible case."""
        result = coin_change_ways_permutations([2], 3)
        self.assertEqual(result, 0)


class TestCoinChangeLimited(unittest.TestCase):
    """Unit tests for coin_change_limited."""

    def test_limited_coins(self) -> None:
        """Test with limited coins."""
        result = coin_change_limited([1, 2, 5], [5, 3, 2], 11)
        self.assertEqual(result, 3)

    def test_impossible_due_to_limits(self) -> None:
        """Test impossible due to quantity limits."""
        result = coin_change_limited([5], [1], 11)
        self.assertEqual(result, -1)


class TestCoinChangeInvariants(unittest.TestCase):
    """Popperian falsification tests for coin change invariants."""

    def test_p1_sum_equals_amount(self) -> None:
        """P1: If solution exists, sum of coins equals amount exactly."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 5)
            coins = sorted({rng.randint(1, 10) for _ in range(n)})
            if not coins:
                coins = [1]
            amount = rng.randint(0, 30)
            result_coins = coin_change_coins(coins, amount)
            if result_coins:
                self.assertEqual(sum(result_coins), amount)

    def test_p2_minus_one_iff_impossible(self) -> None:
        """P2: coin_change_min returns -1 iff no solution exists."""
        # Test known impossible cases
        self.assertEqual(coin_change_min([2], 3), -1)
        self.assertEqual(coin_change_min([3, 7], 5), -1)
        # Test known possible cases with coin 1
        for amount in range(20):
            self.assertNotEqual(coin_change_min([1], amount), -1)

    def test_p3_ways_non_negative(self) -> None:
        """P3: coin_change_ways >= 0 for all valid inputs."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 5)
            coins = [rng.randint(1, 10) for _ in range(n)]
            amount = rng.randint(0, 30)
            result = coin_change_ways(coins, amount)
            self.assertGreaterEqual(result, 0)
            result_perm = coin_change_ways_permutations(coins, amount)
            self.assertGreaterEqual(result_perm, 0)

    def test_p4_min_coins_bound(self) -> None:
        """P4: Minimum coins <= amount when coin of value 1 is available."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 5)
            coins = [1] + [rng.randint(2, 10) for _ in range(n)]
            amount = rng.randint(1, 30)
            result = coin_change_min(coins, amount)
            self.assertGreater(result, 0)
            self.assertLessEqual(result, amount)

    def test_ways_leq_permutations(self) -> None:
        """Number of combinations <= number of permutations."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 4)
            coins = sorted({rng.randint(1, 5) for _ in range(n)})
            if not coins:
                coins = [1]
            amount = rng.randint(0, 15)
            ways = coin_change_ways(coins, amount)
            perms = coin_change_ways_permutations(coins, amount)
            self.assertLessEqual(ways, perms)

    def test_coins_match_min(self) -> None:
        """Number of returned coins should match minimum count."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 4)
            coins = sorted({rng.randint(1, 10) for _ in range(n)})
            if not coins:
                coins = [1]
            amount = rng.randint(0, 20)
            min_count = coin_change_min(coins, amount)
            result_coins = coin_change_coins(coins, amount)
            if min_count in (-1, 0):
                self.assertEqual(result_coins, [])
            else:
                self.assertEqual(len(result_coins), min_count)


if __name__ == "__main__":
    unittest.main()
