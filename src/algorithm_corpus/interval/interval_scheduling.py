"""Interval scheduling algorithms.

Greedy interval scheduling problems.
"""

from __future__ import annotations


def can_attend(intervals: list[tuple[int, int]]) -> bool:
    """Check if a person can attend all meetings.

    Args:
        intervals: List of (start, end) meeting times.

    Returns:
        True if no meetings overlap.

    Example:
        >>> can_attend([(0, 30), (5, 10), (15, 20)])
        False
        >>> can_attend([(7, 10), (2, 4)])
        True
    """
    if len(intervals) <= 1:
        return True

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i - 1][1]:
            return False

    return True


def min_arrows(points: list[tuple[int, int]]) -> int:
    """Find minimum arrows to burst all balloons.

    Each balloon is represented as (start, end) on x-axis.
    An arrow at x bursts balloon if start <= x <= end.

    Greedy: sort by end, shoot at each unpopped balloon's end.

    Args:
        points: List of (start, end) balloon positions.

    Returns:
        Minimum number of arrows needed.

    Example:
        >>> min_arrows([(10, 16), (2, 8), (1, 6), (7, 12)])
        2
        >>> min_arrows([(1, 2), (3, 4), (5, 6)])
        3
    """
    if not points:
        return 0

    # Sort by end position
    sorted_points = sorted(points, key=lambda x: x[1])
    arrows = 1
    current_end = sorted_points[0][1]

    for start, end in sorted_points[1:]:
        if start > current_end:
            arrows += 1
            current_end = end

    return arrows
