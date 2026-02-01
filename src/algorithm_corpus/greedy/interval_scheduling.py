"""Interval Scheduling Algorithms.

Merge overlapping intervals and find minimum resources.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n)

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: Merged intervals don't overlap
    P2: Merged intervals cover all original intervals
    P3: min_meeting_rooms is minimum possible
    P4: Empty input returns appropriate result
"""

from __future__ import annotations


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping intervals.

    Args:
        intervals: List of (start, end) tuples.

    Returns:
        List of merged non-overlapping intervals.

    Examples:
        >>> merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)])
        [(1, 6), (8, 10), (15, 18)]

        >>> merge_intervals([(1, 4), (4, 5)])
        [(1, 5)]

        >>> merge_intervals([])
        []
    """
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    result: list[tuple[int, int]] = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_start, last_end = result[-1]
        if start <= last_end:
            # Merge overlapping intervals
            result[-1] = (last_start, max(last_end, end))
        else:
            result.append((start, end))

    return result


def min_meeting_rooms(intervals: list[tuple[int, int]]) -> int:
    """Find minimum meeting rooms required.

    Args:
        intervals: List of (start, end) meeting times.

    Returns:
        Minimum number of meeting rooms needed.

    Examples:
        >>> min_meeting_rooms([(0, 30), (5, 10), (15, 20)])
        2

        >>> min_meeting_rooms([(7, 10), (2, 4)])
        1

        >>> min_meeting_rooms([])
        0

        >>> min_meeting_rooms([(1, 5), (2, 6), (3, 7)])
        3
    """
    if not intervals:
        return 0

    # Create events: +1 for start, -1 for end
    events: list[tuple[int, int]] = []
    for start, end in intervals:
        events.append((start, 1))  # Meeting starts
        events.append((end, -1))  # Meeting ends

    # Sort by time, with ends before starts at same time
    events.sort(key=lambda x: (x[0], x[1]))

    max_rooms: int = 0
    current_rooms: int = 0

    for _, delta in events:
        current_rooms += delta
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms
