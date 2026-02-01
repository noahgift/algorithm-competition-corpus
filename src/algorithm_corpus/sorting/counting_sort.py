"""Counting Sort Algorithm.

Non-comparison sorting for integers in a known range.

Time Complexity: O(n + k) where k is the range of input
Space Complexity: O(k)

References:
    [1] Seward, H.H. (1954). "Information sorting in the application
        of electronic digital computers to business operations".
        Master's thesis. MIT.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 8.2.

Invariants (Popperian Falsification):
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Stable sort (preserves relative order)
    P4: Linear time for bounded integer range
"""

from __future__ import annotations


def counting_sort(arr: list[int]) -> list[int]:
    """Sort array using counting sort.

    Works for non-negative integers.

    Args:
        arr: Array of non-negative integers.

    Returns:
        New sorted array.

    Examples:
        >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]

        >>> counting_sort([])
        []

        >>> counting_sort([1])
        [1]

        >>> counting_sort([1, 1, 1])
        [1, 1, 1]
    """
    if not arr:
        return []

    max_val: int = max(arr)
    min_val: int = min(arr)
    range_size: int = max_val - min_val + 1

    count: list[int] = [0] * range_size

    # Count occurrences (shift by min_val to handle any range)
    for num in arr:
        count[num - min_val] += 1

    # Build result
    result: list[int] = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])

    return result
