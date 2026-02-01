"""Classic Binary Search Algorithm.

Searches for a target value in a sorted array using divide and conquer.

Time Complexity: O(log n)
Space Complexity: O(1)

References:
    [1] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 3:
        Sorting and Searching" (2nd ed.). Addison-Wesley. Section 6.2.1.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 2.3.

Invariants (Popperian Falsification):
    P1: If found, arr[result] == target
    P2: If not found, result == -1
    P3: Search space halves each iteration (logarithmic)
    P4: Works correctly on empty arrays (returns -1)
"""

from __future__ import annotations


def binary_search(arr: list[int], target: int) -> int:
    """Find the index of target in a sorted array.

    Args:
        arr: Sorted array of integers.
        target: Value to search for.

    Returns:
        Index of target if found, -1 otherwise.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2

        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1

        >>> binary_search([], 1)
        -1

        >>> binary_search([1], 1)
        0
    """
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_leftmost(arr: list[int], target: int) -> int:
    """Find the leftmost (first) index of target.

    Args:
        arr: Sorted array of integers.
        target: Value to search for.

    Returns:
        Leftmost index of target if found, -1 otherwise.

    Examples:
        >>> binary_search_leftmost([1, 2, 2, 2, 3], 2)
        1

        >>> binary_search_leftmost([1, 2, 3], 4)
        -1

        >>> binary_search_leftmost([2, 2, 2], 2)
        0
    """
    left: int = 0
    right: int = len(arr)
    result: int = -1

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] >= target:
            if arr[mid] == target:
                result = mid
            right = mid
        else:
            left = mid + 1

    return result


def binary_search_rightmost(arr: list[int], target: int) -> int:
    """Find the rightmost (last) index of target.

    Args:
        arr: Sorted array of integers.
        target: Value to search for.

    Returns:
        Rightmost index of target if found, -1 otherwise.

    Examples:
        >>> binary_search_rightmost([1, 2, 2, 2, 3], 2)
        3

        >>> binary_search_rightmost([1, 2, 3], 4)
        -1

        >>> binary_search_rightmost([2, 2, 2], 2)
        2
    """
    left: int = 0
    right: int = len(arr)
    result: int = -1

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] <= target:
            if arr[mid] == target:
                result = mid
            left = mid + 1
        else:
            right = mid

    return result


def lower_bound(arr: list[int], target: int) -> int:
    """Find the first index where arr[i] >= target.

    Args:
        arr: Sorted array of integers.
        target: Value to search for.

    Returns:
        First index i where arr[i] >= target, or len(arr) if not found.

    Examples:
        >>> lower_bound([1, 2, 4, 5], 3)
        2

        >>> lower_bound([1, 2, 3], 2)
        1

        >>> lower_bound([1, 2, 3], 4)
        3

        >>> lower_bound([], 1)
        0
    """
    left: int = 0
    right: int = len(arr)

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr: list[int], target: int) -> int:
    """Find the first index where arr[i] > target.

    Args:
        arr: Sorted array of integers.
        target: Value to search for.

    Returns:
        First index i where arr[i] > target, or len(arr) if not found.

    Examples:
        >>> upper_bound([1, 2, 2, 3], 2)
        3

        >>> upper_bound([1, 2, 3], 3)
        3

        >>> upper_bound([1, 2, 3], 0)
        0

        >>> upper_bound([], 1)
        0
    """
    left: int = 0
    right: int = len(arr)

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
