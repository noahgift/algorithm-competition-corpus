"""Longest Increasing Subsequence algorithms.

Multiple approaches with different time complexities.

References:
    Cormen, T.H., et al. (2009). Introduction to Algorithms (3rd ed.).
    MIT Press. Problem 15-4: Longest Increasing Subsequence.
"""

from __future__ import annotations


def lis_dp(nums: list[int]) -> int:
    """Find length of longest increasing subsequence.

    O(n^2) DP approach.

    Args:
        nums: List of integers.

    Returns:
        Length of longest increasing subsequence.

    Example:
        >>> lis_dp([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> lis_dp([0, 1, 0, 3, 2, 3])
        4
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def _bisect_left(arr: list[int], x: int) -> int:
    """Binary search for leftmost insertion position."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def lis_binary_search(nums: list[int]) -> int:
    """Find length of longest increasing subsequence.

    O(n log n) using binary search.

    Args:
        nums: List of integers.

    Returns:
        Length of longest increasing subsequence.

    Example:
        >>> lis_binary_search([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> lis_binary_search([7, 7, 7, 7])
        1
    """
    if not nums:
        return 0

    tails: list[int] = []

    for num in nums:
        pos = _bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


def lis_with_sequence(nums: list[int]) -> list[int]:
    """Find longest increasing subsequence itself.

    O(n log n) approach that also returns the actual subsequence.

    Args:
        nums: List of integers.

    Returns:
        The longest increasing subsequence.

    Example:
        >>> lis_with_sequence([10, 9, 2, 5, 3, 7, 101, 18])
        [2, 3, 7, 18]
    """
    if not nums:
        return []

    n = len(nums)
    tails: list[int] = []
    tails_idx: list[int] = []
    parent: list[int] = [-1] * n

    for i, num in enumerate(nums):
        pos = _bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            tails_idx.append(i)
        else:
            tails[pos] = num
            tails_idx[pos] = i

        if pos > 0:
            parent[i] = tails_idx[pos - 1]

    # Reconstruct sequence
    result: list[int] = []
    idx = tails_idx[-1] if tails_idx else -1
    while idx >= 0:
        result.append(nums[idx])
        idx = parent[idx]

    return result[::-1]
