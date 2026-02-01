"""Coin Change Problem.

Find the minimum number of coins needed to make a given amount,
or count the number of ways to make the amount.

Time Complexity: O(n * amount)
Space Complexity: O(amount)

References:
    [1] Bellman, R. (1954). "The theory of dynamic programming".
        Bulletin of the American Mathematical Society. 60(6): 503-515.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 15.

Invariants (Popperian Falsification):
    P1: If solution exists, sum of coins equals amount exactly
    P2: coin_change_min returns -1 iff no solution exists
    P3: coin_change_ways >= 0 for all valid inputs
    P4: Minimum coins <= amount (using coin of value 1 if available)
"""

from __future__ import annotations


def coin_change_min(coins: list[int], amount: int) -> int:
    """Find minimum number of coins to make the amount.

    Args:
        coins: Available coin denominations.
        amount: Target amount.

    Returns:
        Minimum number of coins, or -1 if impossible.

    Examples:
        >>> coin_change_min([1, 2, 5], 11)
        3

        >>> coin_change_min([2], 3)
        -1

        >>> coin_change_min([1], 0)
        0

        >>> coin_change_min([1, 5, 10, 25], 30)
        2
    """
    dp: list[int] = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] > amount:
        return -1
    return dp[amount]


def coin_change_coins(coins: list[int], amount: int) -> list[int]:
    """Find the actual coins used to make the amount.

    Args:
        coins: Available coin denominations.
        amount: Target amount.

    Returns:
        List of coins used, or empty list if impossible.

    Examples:
        >>> sorted(coin_change_coins([1, 2, 5], 11))
        [1, 5, 5]

        >>> coin_change_coins([2], 3)
        []

        >>> coin_change_coins([1, 5], 0)
        []
    """
    dp: list[int] = [amount + 1] * (amount + 1)
    dp[0] = 0
    parent: list[int] = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] > amount:
        return []

    result: list[int] = []
    current: int = amount
    while current > 0:
        result.append(parent[current])
        current -= parent[current]

    return result


def coin_change_ways(coins: list[int], amount: int) -> int:
    """Count the number of ways to make the amount.

    Args:
        coins: Available coin denominations.
        amount: Target amount.

    Returns:
        Number of distinct ways to make the amount.

    Examples:
        >>> coin_change_ways([1, 2, 5], 5)
        4

        >>> coin_change_ways([2], 3)
        0

        >>> coin_change_ways([1, 2, 3], 4)
        4
    """
    dp: list[int] = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


def coin_change_ways_permutations(coins: list[int], amount: int) -> int:
    """Count ways considering order (permutations).

    Unlike coin_change_ways, [1,2] and [2,1] are counted separately.

    Args:
        coins: Available coin denominations.
        amount: Target amount.

    Returns:
        Number of permutations to make the amount.

    Examples:
        >>> coin_change_ways_permutations([1, 2, 5], 5)
        9

        >>> coin_change_ways_permutations([1, 2], 3)
        3

        >>> coin_change_ways_permutations([2], 3)
        0
    """
    dp: list[int] = [0] * (amount + 1)
    dp[0] = 1

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] += dp[i - coin]

    return dp[amount]


def coin_change_limited(
    coins: list[int],
    counts: list[int],
    amount: int,
) -> int:
    """Find minimum coins with limited quantities.

    Args:
        coins: Available coin denominations.
        counts: Available quantity of each coin.
        amount: Target amount.

    Returns:
        Minimum number of coins, or -1 if impossible.

    Examples:
        >>> coin_change_limited([1, 2, 5], [5, 3, 2], 11)
        3

        >>> coin_change_limited([5], [1], 11)
        -1
    """
    dp: list[int] = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(len(coins)):
        for _ in range(counts[i]):
            for j in range(amount, coins[i] - 1, -1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    if dp[amount] > amount:
        return -1
    return dp[amount]
