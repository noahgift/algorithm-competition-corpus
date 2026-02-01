"""Activity Selection Problem.

Select maximum number of non-overlapping activities.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n)

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 16.1.

Invariants (Popperian Falsification):
    P1: Selected activities don't overlap
    P2: Number of activities is maximized
    P3: All activities in result are valid
    P4: Empty input returns empty result
"""

from __future__ import annotations


def activity_selection(
    activities: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    """Select maximum non-overlapping activities.

    Args:
        activities: List of (start, end) tuples.

    Returns:
        List of selected non-overlapping activities.

    Examples:
        >>> activity_selection(
        ...     [
        ...         (1, 4),
        ...         (3, 5),
        ...         (0, 6),
        ...         (5, 7),
        ...         (3, 8),
        ...         (5, 9),
        ...         (6, 10),
        ...         (8, 11),
        ...         (8, 12),
        ...         (2, 13),
        ...         (12, 14),
        ...     ]
        ... )
        [(1, 4), (5, 7), (8, 11), (12, 14)]

        >>> activity_selection([])
        []

        >>> activity_selection([(1, 2)])
        [(1, 2)]
    """
    if not activities:
        return []

    # Sort by end time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    result: list[tuple[int, int]] = [sorted_activities[0]]

    for activity in sorted_activities[1:]:
        # If this activity starts after the last selected one ends
        if activity[0] >= result[-1][1]:
            result.append(activity)

    return result


def max_activities(activities: list[tuple[int, int]]) -> int:
    """Count maximum number of non-overlapping activities.

    Args:
        activities: List of (start, end) tuples.

    Returns:
        Maximum number of non-overlapping activities.

    Examples:
        >>> max_activities([(1, 4), (3, 5), (0, 6), (5, 7)])
        2

        >>> max_activities([])
        0

        >>> max_activities([(1, 2), (2, 3), (3, 4)])
        3
    """
    return len(activity_selection(activities))
