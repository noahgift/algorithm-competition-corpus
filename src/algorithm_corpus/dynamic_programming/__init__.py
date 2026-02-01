"""Dynamic programming algorithms.

This module contains classic DP algorithms for optimization problems.

Algorithms:
    - Fibonacci: Memoization and tabulation examples
    - LCS: Longest common subsequence
    - LIS: Longest increasing subsequence
    - Edit Distance: Levenshtein distance
    - Knapsack: 0/1 and unbounded variants
    - Coin Change: Minimum coins and counting ways
    - Matrix Chain: Optimal parenthesization
    - House Robber: Non-adjacent selection
"""

from __future__ import annotations

__all__: list[str] = [
    "coin_change_min",
    "coin_change_ways",
    "edit_distance",
    "fibonacci_memo",
    "fibonacci_optimized",
    "fibonacci_tabulation",
    "house_robber",
    "house_robber_circular",
    "knapsack_01",
    "knapsack_unbounded",
    "lcs_length",
    "lcs_string",
    "lis_length",
    "lis_sequence",
    "matrix_chain_order",
]
