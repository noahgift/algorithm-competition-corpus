"""Merge Sort Algorithm.

Divide and conquer sorting using merging of sorted subarrays.

Time Complexity: O(n log n)
Space Complexity: O(n)

References:
    [1] von Neumann, J. (1945). "First Draft of a Report on the EDVAC".
        Technical report. University of Pennsylvania.

    [2] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 3:
        Sorting and Searching" (2nd ed.). Addison-Wesley. Section 5.2.4.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 2.3.

Invariants (Popperian Falsification):
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Stable sort (preserves relative order of equal elements)
    P4: O(n log n) time complexity in all cases
"""

from __future__ import annotations


def merge_sort(arr: list[int]) -> list[int]:
    """Sort array using recursive merge sort.

    Args:
        arr: Array to sort.

    Returns:
        New sorted array.

    Examples:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> merge_sort([])
        []

        >>> merge_sort([1])
        [1]

        >>> merge_sort([2, 1])
        [1, 2]
    """
    if len(arr) <= 1:
        return arr[:]

    mid: int = len(arr) // 2
    left: list[int] = merge_sort(arr[:mid])
    right: list[int] = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted arrays."""
    result: list[int] = []
    i: int = 0
    j: int = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_iterative(arr: list[int]) -> list[int]:
    """Sort array using iterative (bottom-up) merge sort.

    Args:
        arr: Array to sort.

    Returns:
        New sorted array.

    Examples:
        >>> merge_sort_iterative([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> merge_sort_iterative([])
        []

        >>> merge_sort_iterative([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
    """
    result: list[int] = arr[:]
    n: int = len(result)

    if n <= 1:
        return result

    width: int = 1
    while width < n:
        i: int = 0
        while i < n:
            left: int = i
            mid: int = min(i + width, n)
            right: int = min(i + 2 * width, n)

            merged: list[int] = _merge(result[left:mid], result[mid:right])
            result[left:right] = merged

            i += 2 * width
        width *= 2

    return result
