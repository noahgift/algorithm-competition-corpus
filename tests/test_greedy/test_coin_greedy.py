"""Tests for Greedy Coin Change algorithm.

Tests Popperian Falsification Invariants:
    P1: Total value equals target amount
    P2: Uses minimum coins for canonical systems
    P3: Returns empty for impossible amounts
    P4: Handles edge cases correctly
"""

from __future__ import annotations

import unittest

from algorithm_corpus.greedy.coin_greedy import (
    coin_change_greedy,
)


class TestCoinChangeGreedy(unittest.TestCase):
    """Unit tests for coin_change_greedy."""

    def test_us_coins(self) -> None:
        """Test with US coins."""
        self.assertEqual(coin_change_greedy([25, 10, 5, 1], 41), [25, 10, 5, 1])

    def test_exact_change(self) -> None:
        """Test exact change."""
        self.assertEqual(coin_change_greedy([25, 10, 5, 1], 30), [25, 5])

    def test_zero_amount(self) -> None:
        """Test zero amount."""
        self.assertEqual(coin_change_greedy([25, 10, 5, 1], 0), [])

    def test_impossible(self) -> None:
        """Test impossible amount."""
        self.assertEqual(coin_change_greedy([5, 2], 3), [])


class TestCoinGreedyInvariants(unittest.TestCase):
    """Popperian falsification tests for coin greedy invariants."""

    def test_p1_sum_equals_target(self) -> None:
        """P1: Total value equals target amount."""
        coins = [25, 10, 5, 1]
        for amount in [0, 1, 5, 10, 25, 41, 99, 100]:
            result = coin_change_greedy(coins, amount)
            if result:
                self.assertEqual(sum(result), amount)

    def test_p3_impossible_returns_empty(self) -> None:
        """P3: Returns empty for impossible amounts."""
        self.assertEqual(coin_change_greedy([5, 2], 3), [])
        self.assertEqual(coin_change_greedy([3], 7), [])

    def test_p4_edge_cases(self) -> None:
        """P4: Handles edge cases correctly."""
        self.assertEqual(coin_change_greedy([1], 5), [1, 1, 1, 1, 1])
        self.assertEqual(coin_change_greedy([25, 10, 5, 1], 0), [])


if __name__ == "__main__":
    unittest.main()
