"""Interval operations.

Basic interval manipulation algorithms.
"""

from __future__ import annotations


def merge_overlapping(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping intervals.

    Args:
        intervals: List of (start, end) tuples.

    Returns:
        List of merged non-overlapping intervals.

    Example:
        >>> merge_overlapping([(1, 3), (2, 6), (8, 10), (15, 18)])
        [(1, 6), (8, 10), (15, 18)]
        >>> merge_overlapping([(1, 4), (4, 5)])
        [(1, 5)]
    """
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    result: list[tuple[int, int]] = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_start, last_end = result[-1]
        if start <= last_end:
            result[-1] = (last_start, max(last_end, end))
        else:
            result.append((start, end))

    return result


def insert_interval(
    intervals: list[tuple[int, int]], new_interval: tuple[int, int]
) -> list[tuple[int, int]]:
    """Insert new interval and merge if necessary.

    Args:
        intervals: Sorted non-overlapping intervals.
        new_interval: Interval to insert.

    Returns:
        Merged result after insertion.

    Example:
        >>> insert_interval([(1, 3), (6, 9)], (2, 5))
        [(1, 5), (6, 9)]
        >>> insert_interval([(1, 2), (3, 5), (6, 7), (8, 10)], (4, 8))
        [(1, 2), (3, 10)]
    """
    result: list[tuple[int, int]] = []
    new_start, new_end = new_interval
    i = 0
    n = len(intervals)

    # Add intervals before new_interval
    while i < n and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1

    result.append((new_start, new_end))

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


def interval_intersection(
    a: list[tuple[int, int]], b: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Find intersection of two interval lists.

    Args:
        a: First sorted list of intervals.
        b: Second sorted list of intervals.

    Returns:
        List of intersection intervals.

    Example:
        >>> interval_intersection([(0, 2), (5, 10)], [(1, 5), (8, 12)])
        [(1, 2), (5, 5), (8, 10)]
    """
    result: list[tuple[int, int]] = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        # Find intersection
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])

        if start <= end:
            result.append((start, end))

        # Move pointer with smaller end
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return result
