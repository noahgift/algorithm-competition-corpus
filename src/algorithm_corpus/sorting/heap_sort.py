"""Heap Sort Algorithm.

In-place sorting using a binary heap data structure.

Time Complexity: O(n log n)
Space Complexity: O(1)

References:
    [1] Williams, J.W.J. (1964). "Algorithm 232: Heapsort".
        Communications of the ACM. 7(6): 347-348.

    [2] Floyd, R.W. (1964). "Algorithm 245: Treesort 3".
        Communications of the ACM. 7(12): 701.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 6.

Invariants (Popperian Falsification):
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Heap property maintained during heapify
    P4: In-place sorting (O(1) extra space)
"""

from __future__ import annotations


def heap_sort(arr: list[int]) -> list[int]:
    """Sort array using heap sort.

    Args:
        arr: Array to sort.

    Returns:
        New sorted array.

    Examples:
        >>> heap_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> heap_sort([])
        []

        >>> heap_sort([1])
        [1]

        >>> heap_sort([2, 1])
        [1, 2]
    """
    result: list[int] = arr[:]
    n: int = len(result)

    if n <= 1:
        return result

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        _heapify(result, i, 0)

    return result


def _heapify(arr: list[int], n: int, i: int) -> None:
    """Maintain max-heap property at index i."""
    largest: int = i
    left: int = 2 * i + 1
    right: int = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)
