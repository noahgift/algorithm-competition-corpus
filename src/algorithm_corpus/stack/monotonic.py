"""Monotonic stack algorithms.

Stack-based algorithms maintaining monotonic property.
"""

from __future__ import annotations


def next_greater_element(nums: list[int]) -> list[int]:
    """Find next greater element for each position.

    For circular array, wraps around.

    Args:
        nums: List of integers.

    Returns:
        List where result[i] is next greater element, or -1 if none.

    Example:
        >>> next_greater_element([2, 1, 2, 4, 3])
        [4, 2, 4, -1, 4]
        >>> next_greater_element([1, 2, 1])
        [2, -1, 2]
    """
    n = len(nums)
    result = [-1] * n
    stack: list[int] = []

    # Iterate twice for circular array behavior
    for i in range(2 * n):
        idx = i % n
        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]
        if i < n:
            stack.append(idx)

    return result


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Find days until warmer temperature.

    Uses monotonic decreasing stack.

    Args:
        temperatures: Daily temperatures.

    Returns:
        Days to wait for warmer temperature, or 0 if never.

    Example:
        >>> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> daily_temperatures([30, 40, 50, 60])
        [1, 1, 1, 0]
    """
    n = len(temperatures)
    result = [0] * n
    stack: list[int] = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)

    return result
