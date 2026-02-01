"""Search Range in Sorted Array.

Find the starting and ending position of a given target value.

Time Complexity: O(log n)
Space Complexity: O(1)

References:
    [1] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 3:
        Sorting and Searching" (2nd ed.). Addison-Wesley. Section 6.2.1.

Invariants (Popperian Falsification):
    P1: If found, arr[start:end+1] all equal target
    P2: If not found, result == [-1, -1]
    P3: start <= end when found
    P4: No elements equal to target exist outside [start, end]
"""

from __future__ import annotations


def search_range(arr: list[int], target: int) -> list[int]:
    """Find the starting and ending position of target.

    Args:
        arr: Sorted array of integers.
        target: Value to search for.

    Returns:
        [start, end] indices if found, [-1, -1] otherwise.

    Examples:
        >>> search_range([5, 7, 7, 8, 8, 10], 8)
        [3, 4]

        >>> search_range([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]

        >>> search_range([], 0)
        [-1, -1]

        >>> search_range([1], 1)
        [0, 0]
    """
    start: int = _find_first(arr, target)
    if start == -1:
        return [-1, -1]
    end: int = _find_last(arr, target)
    return [start, end]


def _find_first(arr: list[int], target: int) -> int:
    """Find the first occurrence of target."""
    left: int = 0
    right: int = len(arr) - 1
    result: int = -1

    while left <= right:
        mid: int = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def _find_last(arr: list[int], target: int) -> int:
    """Find the last occurrence of target."""
    left: int = 0
    right: int = len(arr) - 1
    result: int = -1

    while left <= right:
        mid: int = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
