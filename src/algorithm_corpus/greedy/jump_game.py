"""Jump game algorithms.

Greedy solutions for jump problems.
"""

from __future__ import annotations


def can_jump(nums: list[int]) -> bool:
    """Check if you can reach the last index.

    Each element represents maximum jump length.

    Args:
        nums: List of non-negative integers.

    Returns:
        True if last index is reachable.

    Example:
        >>> can_jump([2, 3, 1, 1, 4])
        True
        >>> can_jump([3, 2, 1, 0, 4])
        False
    """
    max_reach = 0

    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
        if max_reach >= len(nums) - 1:
            return True

    return True


def min_jumps(nums: list[int]) -> int:
    """Find minimum number of jumps to reach last index.

    Greedy BFS-like approach.

    Args:
        nums: List of positive integers.

    Returns:
        Minimum number of jumps.

    Example:
        >>> min_jumps([2, 3, 1, 1, 4])
        2
        >>> min_jumps([2, 3, 0, 1, 4])
        2
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                break

    return jumps
