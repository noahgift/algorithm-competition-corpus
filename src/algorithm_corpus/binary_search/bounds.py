"""Binary search bounds algorithms.

Lower and upper bound searches.
"""

from __future__ import annotations


def lower_bound(arr: list[int], target: int) -> int:
    """Find index of first element >= target.

    Args:
        arr: Sorted list.
        target: Target value.

    Returns:
        Index of first element >= target, or len(arr) if none.

    Example:
        >>> lower_bound([1, 2, 4, 4, 5], 4)
        2
        >>> lower_bound([1, 2, 4, 4, 5], 3)
        2
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr: list[int], target: int) -> int:
    """Find index of first element > target.

    Args:
        arr: Sorted list.
        target: Target value.

    Returns:
        Index of first element > target, or len(arr) if none.

    Example:
        >>> upper_bound([1, 2, 4, 4, 5], 4)
        4
        >>> upper_bound([1, 2, 4, 4, 5], 3)
        2
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def count_occurrences(arr: list[int], target: int) -> int:
    """Count occurrences of target in sorted array.

    Uses lower and upper bound for O(log n) time.

    Args:
        arr: Sorted list.
        target: Target value.

    Returns:
        Number of occurrences.

    Example:
        >>> count_occurrences([1, 2, 4, 4, 4, 5], 4)
        3
        >>> count_occurrences([1, 2, 5], 4)
        0
    """
    return upper_bound(arr, target) - lower_bound(arr, target)


def search_insert_position(arr: list[int], target: int) -> int:
    """Find insert position to maintain sorted order.

    Args:
        arr: Sorted list.
        target: Target value.

    Returns:
        Index to insert target.

    Example:
        >>> search_insert_position([1, 3, 5, 6], 5)
        2
        >>> search_insert_position([1, 3, 5, 6], 2)
        1
    """
    return lower_bound(arr, target)
