"""Greedy Coin Change.

Greedy approach for coin change (works for canonical coin systems).

Time Complexity: O(n) where n is number of coin types
Space Complexity: O(1)

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: Total value equals target amount
    P2: Uses minimum coins for canonical systems
    P3: Returns empty for impossible amounts
    P4: Handles edge cases correctly

Note: Greedy only works for canonical coin systems (like US currency).
For non-canonical systems, use dynamic programming.
"""

from __future__ import annotations


def coin_change_greedy(coins: list[int], amount: int) -> list[int]:
    """Find coins to make amount using greedy approach.

    Note: Only works optimally for canonical coin systems.

    Args:
        coins: Available coin denominations (sorted descending).
        amount: Target amount.

    Returns:
        List of coins used, or empty if impossible.

    Examples:
        >>> coin_change_greedy([25, 10, 5, 1], 41)
        [25, 10, 5, 1]

        >>> coin_change_greedy([25, 10, 5, 1], 30)
        [25, 5]

        >>> coin_change_greedy([25, 10, 5, 1], 0)
        []

        >>> coin_change_greedy([5, 2], 3)
        []
    """
    if amount == 0:
        return []

    # Sort coins in descending order
    sorted_coins = sorted(coins, reverse=True)
    result: list[int] = []
    remaining = amount

    for coin in sorted_coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining > 0:
        return []  # Could not make exact change

    return result
