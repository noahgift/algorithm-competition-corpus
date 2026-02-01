"""Merge Sort and Inversions using Divide and Conquer.

Classic merge sort with inversion counting.

Time Complexity: O(n log n)
Space Complexity: O(n)

References:
    [1] von Neumann, J. (1945). First description of merge sort.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 2.3.

Invariants (Popperian Falsification):
    P1: Result is sorted
    P2: Result is permutation of input
    P3: Inversion count is correct
    P4: O(n log n) time complexity maintained
"""

from __future__ import annotations


def merge_sort_recursive(arr: list[int]) -> list[int]:
    """Sort array using recursive merge sort.

    Args:
        arr: Array to sort.

    Returns:
        New sorted array.

    Examples:
        >>> merge_sort_recursive([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> merge_sort_recursive([])
        []

        >>> merge_sort_recursive([1])
        [1]
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted arrays."""
    result: list[int] = []
    i = j = 0

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


def count_inversions(arr: list[int]) -> int:
    """Count inversions using merge sort.

    An inversion is a pair (i, j) where i < j and arr[i] > arr[j].

    Args:
        arr: Array of integers.

    Returns:
        Number of inversions.

    Examples:
        >>> count_inversions([2, 4, 1, 3, 5])
        3

        >>> count_inversions([1, 2, 3, 4, 5])
        0

        >>> count_inversions([5, 4, 3, 2, 1])
        10

        >>> count_inversions([])
        0
    """

    def _merge_count(arr_slice: list[int]) -> tuple[list[int], int]:
        if len(arr_slice) <= 1:
            return arr_slice[:], 0

        mid = len(arr_slice) // 2
        left, left_inv = _merge_count(arr_slice[:mid])
        right, right_inv = _merge_count(arr_slice[mid:])

        merged: list[int] = []
        inversions = left_inv + right_inv
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, count = _merge_count(arr)
    return count
