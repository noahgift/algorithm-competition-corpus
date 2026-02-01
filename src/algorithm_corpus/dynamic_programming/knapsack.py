"""Knapsack Problem Variants.

Solves the 0/1 knapsack and unbounded knapsack problems
using dynamic programming.

Time Complexity: O(n * W)
Space Complexity: O(n * W) or O(W) optimized

References:
    [1] Bellman, R. (1954). "The theory of dynamic programming".
        Bulletin of the American Mathematical Society. 60(6): 503-515.

    [2] Dantzig, G.B. (1957). "Discrete-variable extremum problems".
        Operations Research. 5(2): 266-288.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 16.2.

Invariants (Popperian Falsification):
    P1: Selected items' total weight <= capacity
    P2: Solution value >= 0
    P3: Solution is optimal among all valid selections
    P4: dp[i][w] represents best value using items 0..i-1 with capacity w
"""

from __future__ import annotations


def knapsack_01(
    weights: list[int],
    values: list[int],
    capacity: int,
) -> int:
    """Solve 0/1 knapsack problem.

    Args:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity.

    Returns:
        Maximum value achievable.

    Examples:
        >>> knapsack_01([1, 2, 3], [6, 10, 12], 5)
        22

        >>> knapsack_01([10, 20, 30], [60, 100, 120], 50)
        220

        >>> knapsack_01([], [], 10)
        0

        >>> knapsack_01([5], [10], 3)
        0
    """
    n: int = len(weights)
    dp: list[list[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_01_items(
    weights: list[int],
    values: list[int],
    capacity: int,
) -> tuple[int, list[int]]:
    """Solve 0/1 knapsack and return selected items.

    Args:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity.

    Returns:
        Tuple of (max_value, list of selected item indices).

    Examples:
        >>> val, items = knapsack_01_items([1, 2, 3], [6, 10, 12], 5)
        >>> val
        22
        >>> sorted(items)
        [1, 2]

        >>> knapsack_01_items([10], [100], 5)
        (0, [])

        >>> knapsack_01_items([], [], 10)
        (0, [])
    """
    n: int = len(weights)
    dp: list[list[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected: list[int] = []
    w: int = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected


def knapsack_01_optimized(
    weights: list[int],
    values: list[int],
    capacity: int,
) -> int:
    """Solve 0/1 knapsack with O(W) space.

    Args:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity.

    Returns:
        Maximum value achievable.

    Examples:
        >>> knapsack_01_optimized([1, 2, 3], [6, 10, 12], 5)
        22

        >>> knapsack_01_optimized([2, 3, 4, 5], [3, 4, 5, 6], 5)
        7
    """
    n: int = len(weights)
    dp: list[int] = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def knapsack_unbounded(
    weights: list[int],
    values: list[int],
    capacity: int,
) -> int:
    """Solve unbounded knapsack (items can be used multiple times).

    Args:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity.

    Returns:
        Maximum value achievable.

    Examples:
        >>> knapsack_unbounded([1, 3, 4], [15, 50, 60], 8)
        130

        >>> knapsack_unbounded([5, 10, 15], [10, 30, 50], 100)
        330

        >>> knapsack_unbounded([2], [10], 7)
        30
    """
    dp: list[int] = [0] * (capacity + 1)

    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def knapsack_bounded(
    weights: list[int],
    values: list[int],
    counts: list[int],
    capacity: int,
) -> int:
    """Solve bounded knapsack (limited quantity of each item).

    Args:
        weights: List of item weights.
        values: List of item values.
        counts: List of available quantities for each item.
        capacity: Maximum weight capacity.

    Returns:
        Maximum value achievable.

    Examples:
        >>> knapsack_bounded([1, 2, 3], [6, 10, 12], [2, 2, 1], 5)
        26

        >>> knapsack_bounded([2], [10], [3], 5)
        20
    """
    n: int = len(weights)
    dp: list[int] = [0] * (capacity + 1)

    for i in range(n):
        for _ in range(counts[i]):
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
