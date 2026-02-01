"""Container With Most Water and Trapping Rain Water.

Classic two pointer problems for water container problems.

Time Complexity: O(n)
Space Complexity: O(1)

References:
    [1] LeetCode Problem 11: Container With Most Water
    [2] LeetCode Problem 42: Trapping Rain Water

Invariants (Popperian Falsification):
    P1: Result is non-negative
    P2: Result does not exceed theoretical maximum
    P3: Empty array returns 0
    P4: Single element array returns 0
"""

from __future__ import annotations


def max_area(heights: list[int]) -> int:
    """Find maximum water container area between vertical lines.

    Args:
        heights: Array of non-negative integers representing line heights.

    Returns:
        Maximum area of water that can be contained.

    Examples:
        >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49

        >>> max_area([1, 1])
        1

        >>> max_area([4, 3, 2, 1, 4])
        16

        >>> max_area([])
        0
    """
    if len(heights) < 2:  # noqa: PLR2004
        return 0

    left: int = 0
    right: int = len(heights) - 1
    max_water: int = 0

    while left < right:
        width: int = right - left
        height: int = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water


def trap_water(heights: list[int]) -> int:
    """Calculate total water trapped between bars.

    Args:
        heights: Array of non-negative integers representing bar heights.

    Returns:
        Total units of water trapped.

    Examples:
        >>> trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6

        >>> trap_water([4, 2, 0, 3, 2, 5])
        9

        >>> trap_water([])
        0

        >>> trap_water([1, 2, 3])
        0
    """
    if len(heights) < 3:  # noqa: PLR2004
        return 0

    left: int = 0
    right: int = len(heights) - 1
    left_max: int = heights[left]
    right_max: int = heights[right]
    water: int = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]

    return water
