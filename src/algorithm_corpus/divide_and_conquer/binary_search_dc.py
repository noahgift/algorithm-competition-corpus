"""Binary Search using Divide and Conquer.

Recursive binary search implementations.

Time Complexity: O(log n)
Space Complexity: O(log n) due to recursion

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 2.3.

Invariants (Popperian Falsification):
    P1: Returns correct index when element exists
    P2: Returns -1 when element doesn't exist
    P3: Works on empty arrays
    P4: O(log n) time complexity maintained
"""

from __future__ import annotations


def binary_search_recursive(arr: list[int], target: int) -> int:
    """Search for target using recursive binary search.

    Args:
        arr: Sorted array.
        target: Value to find.

    Returns:
        Index of target, or -1 if not found.

    Examples:
        >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
        2

        >>> binary_search_recursive([1, 2, 3, 4, 5], 6)
        -1

        >>> binary_search_recursive([], 1)
        -1

        >>> binary_search_recursive([1], 1)
        0
    """

    def _search(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return _search(mid + 1, right)
        return _search(left, mid - 1)

    return _search(0, len(arr) - 1)


def find_first_greater(arr: list[int], target: int) -> int:
    """Find index of first element greater than target.

    Args:
        arr: Sorted array.
        target: Value to compare.

    Returns:
        Index of first element > target, or len(arr) if none.

    Examples:
        >>> find_first_greater([1, 2, 3, 4, 5], 3)
        3

        >>> find_first_greater([1, 2, 3, 4, 5], 5)
        5

        >>> find_first_greater([1, 2, 3, 4, 5], 0)
        0

        >>> find_first_greater([], 1)
        0
    """

    def _search(left: int, right: int) -> int:
        if left == right:
            return left

        mid = left + (right - left) // 2

        if arr[mid] <= target:
            return _search(mid + 1, right)
        return _search(left, mid)

    return _search(0, len(arr))
