"""Kth Element Algorithms using Heaps.

Find kth largest/smallest and top-k frequent elements.

Time Complexity: O(n log k) for most operations
Space Complexity: O(k)

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: kth_largest returns kth largest element
    P2: kth_smallest returns kth smallest element
    P3: top_k_frequent returns k most frequent
    P4: Results handle edge cases correctly
"""

from __future__ import annotations

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """Find the kth largest element.

    Args:
        nums: Array of integers.
        k: Position from largest (1-indexed).

    Returns:
        The kth largest element.

    Examples:
        >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
        5

        >>> kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4

        >>> kth_largest([1], 1)
        1
    """
    # Use min-heap of size k
    min_heap: list[int] = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return min_heap[0]


def kth_smallest(nums: list[int], k: int) -> int:
    """Find the kth smallest element.

    Args:
        nums: Array of integers.
        k: Position from smallest (1-indexed).

    Returns:
        The kth smallest element.

    Examples:
        >>> kth_smallest([3, 2, 1, 5, 6, 4], 2)
        2

        >>> kth_smallest([7, 10, 4, 3, 20, 15], 3)
        7

        >>> kth_smallest([1], 1)
        1
    """
    # Use max-heap (negate values) of size k
    max_heap: list[int] = []

    for num in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -num)
        elif -num > max_heap[0]:
            heapq.heapreplace(max_heap, -num)

    return -max_heap[0]


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Find the k most frequent elements.

    Args:
        nums: Array of integers.
        k: Number of top frequent elements.

    Returns:
        List of k most frequent elements.

    Examples:
        >>> sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
        [1, 2]

        >>> top_k_frequent([1], 1)
        [1]

        >>> sorted(top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2))
        [-1, 2]
    """
    # Count frequencies
    freq: dict[int, int] = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Use min-heap of size k with (frequency, number)
    min_heap: list[tuple[int, int]] = []

    for num, count in freq.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (count, num))
        elif count > min_heap[0][0]:
            heapq.heapreplace(min_heap, (count, num))

    return [num for _, num in min_heap]
