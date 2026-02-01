"""Search in Rotated Sorted Array.

Binary search variants for arrays that have been rotated.

Time Complexity: O(log n)
Space Complexity: O(1)

References:
    [1] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 3:
        Sorting and Searching" (2nd ed.). Addison-Wesley. Section 6.2.1.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: If found, arr[result] == target
    P2: If not found, result == -1
    P3: Works correctly on non-rotated arrays
    P4: Maintains O(log n) time complexity
"""

from __future__ import annotations


def search_rotated(arr: list[int], target: int) -> int:
    """Search for target in a rotated sorted array.

    The array was originally sorted in ascending order, then rotated
    at some pivot unknown to you beforehand.

    Args:
        arr: Rotated sorted array of distinct integers.
        target: Value to search for.

    Returns:
        Index of target if found, -1 otherwise.

    Examples:
        >>> search_rotated([4, 5, 6, 7, 0, 1, 2], 0)
        4

        >>> search_rotated([4, 5, 6, 7, 0, 1, 2], 3)
        -1

        >>> search_rotated([1], 1)
        0

        >>> search_rotated([], 1)
        -1
    """
    if not arr:
        return -1

    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted, target in right half
        elif arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_min_rotated(arr: list[int]) -> int:
    """Find the minimum element in a rotated sorted array.

    Args:
        arr: Rotated sorted array of distinct integers.

    Returns:
        The minimum element.

    Examples:
        >>> find_min_rotated([3, 4, 5, 1, 2])
        1

        >>> find_min_rotated([4, 5, 6, 7, 0, 1, 2])
        0

        >>> find_min_rotated([1])
        1

        >>> find_min_rotated([2, 1])
        1
    """
    left: int = 0
    right: int = len(arr) - 1

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]
