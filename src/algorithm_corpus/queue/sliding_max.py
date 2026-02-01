"""Sliding window maximum/minimum algorithms.

Uses monotonic deque for O(n) complexity.

References:
    Cormen, T.H., et al. (2009). Introduction to Algorithms (3rd ed.).
    MIT Press. Problem 10-1: Comparisons among lists.
"""

from __future__ import annotations

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Find maximum in each sliding window of size k.

    Uses monotonic decreasing deque.

    Args:
        nums: List of integers.
        k: Window size.

    Returns:
        List of maximums for each window position.

    Example:
        >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
        >>> max_sliding_window([1], 1)
        [1]
    """
    if not nums or k == 0:
        return []

    result: list[int] = []
    dq: deque[int] = deque()

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (maintain decreasing)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add to result once we have full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def min_sliding_window(nums: list[int], k: int) -> list[int]:
    """Find minimum in each sliding window of size k.

    Uses monotonic increasing deque.

    Args:
        nums: List of integers.
        k: Window size.

    Returns:
        List of minimums for each window position.

    Example:
        >>> min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [-1, -3, -3, -3, 3, 3]
        >>> min_sliding_window([1], 1)
        [1]
    """
    if not nums or k == 0:
        return []

    result: list[int] = []
    dq: deque[int] = deque()

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove larger elements (maintain increasing)
        while dq and nums[dq[-1]] > num:
            dq.pop()

        dq.append(i)

        # Add to result once we have full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
