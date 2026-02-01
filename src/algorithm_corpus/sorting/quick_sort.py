"""Quick Sort Algorithm.

Divide and conquer sorting using partitioning.

Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n) for recursion stack

References:
    [1] Hoare, C.A.R. (1961). "Algorithm 64: Quicksort".
        Communications of the ACM. 4(7): 321. doi:10.1145/366622.366644

    [2] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 3:
        Sorting and Searching" (2nd ed.). Addison-Wesley. Section 5.2.2.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 7.

Invariants (Popperian Falsification):
    P1: Result is a permutation of input
    P2: Result is sorted in non-decreasing order
    P3: Partition places pivot in final position
    P4: All elements left of pivot are <= pivot
"""

from __future__ import annotations


def quick_sort(arr: list[int]) -> list[int]:
    """Sort array using recursive quick sort.

    Args:
        arr: Array to sort.

    Returns:
        New sorted array.

    Examples:
        >>> quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> quick_sort([])
        []

        >>> quick_sort([1])
        [1]

        >>> quick_sort([2, 1])
        [1, 2]
    """
    result: list[int] = arr[:]
    _quick_sort_recursive(result, 0, len(result) - 1)
    return result


def _quick_sort_recursive(arr: list[int], low: int, high: int) -> None:
    """Recursive quick sort helper."""
    if low < high:
        pivot_idx: int = _partition(arr, low, high)
        _quick_sort_recursive(arr, low, pivot_idx - 1)
        _quick_sort_recursive(arr, pivot_idx + 1, high)


def _partition(arr: list[int], low: int, high: int) -> int:
    """Partition array around pivot (last element)."""
    pivot: int = arr[high]
    i: int = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr: list[int]) -> list[int]:
    """Sort array using iterative quick sort with explicit stack.

    Args:
        arr: Array to sort.

    Returns:
        New sorted array.

    Examples:
        >>> quick_sort_iterative([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> quick_sort_iterative([])
        []

        >>> quick_sort_iterative([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
    """
    result: list[int] = arr[:]
    n: int = len(result)

    if n <= 1:
        return result

    stack: list[tuple[int, int]] = [(0, n - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_idx: int = _partition(result, low, high)

            # Push larger subarray first (optimization)
            if pivot_idx - low < high - pivot_idx:
                stack.append((pivot_idx + 1, high))
                stack.append((low, pivot_idx - 1))
            else:
                stack.append((low, pivot_idx - 1))
                stack.append((pivot_idx + 1, high))

    return result
