"""Peak Finding Algorithms.

Find peak elements in arrays using binary search.

Time Complexity: O(log n)
Space Complexity: O(1)

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 4.

Invariants (Popperian Falsification):
    P1: Peak element is greater than or equal to neighbors
    P2: At least one peak always exists (boundary elements count)
    P3: O(log n) time complexity maintained
    P4: Works on arrays with duplicates
"""

from __future__ import annotations


def find_peak_element(arr: list[int]) -> int:
    """Find a peak element and return its index.

    A peak element is an element that is strictly greater than its neighbors.
    arr[-1] and arr[n] are considered -infinity.

    Args:
        arr: Array of integers.

    Returns:
        Index of any peak element.

    Examples:
        >>> arr = [1, 2, 3, 1]
        >>> find_peak_element(arr) == 2
        True

        >>> arr = [1, 2, 1, 3, 5, 6, 4]
        >>> find_peak_element(arr) in (1, 5)
        True

        >>> find_peak_element([1])
        0

        >>> find_peak_element([1, 2])
        1
    """
    n: int = len(arr)
    if n <= 1:
        return n - 1 if n == 1 else -1

    # Check boundaries first
    if arr[0] > arr[1]:
        return 0

    left: int = 1
    right: int = n - 1

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


def find_peak_in_mountain(arr: list[int]) -> int:
    """Find the peak index in a mountain array.

    A mountain array increases then decreases.
    Guaranteed to have exactly one peak.

    Args:
        arr: Mountain array.

    Returns:
        Index of the peak element.

    Examples:
        >>> find_peak_in_mountain([0, 1, 0])
        1

        >>> find_peak_in_mountain([0, 2, 1, 0])
        1

        >>> find_peak_in_mountain([0, 10, 5, 2])
        1

        >>> find_peak_in_mountain([3, 4, 5, 1])
        2
    """
    left: int = 0
    right: int = len(arr) - 1

    while left < right:
        mid: int = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left
