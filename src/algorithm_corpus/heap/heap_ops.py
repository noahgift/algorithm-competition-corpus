"""Heap Operations.

Binary min-heap operations from scratch.

Time Complexity: O(log n) for push/pop, O(n) for heapify
Space Complexity: O(1) extra space

References:
    [1] Williams, J.W.J. (1964). "Algorithm 232: Heapsort".
        Communications of the ACM. 7(6): 347-348.

    [2] Floyd, R.W. (1964). "Algorithm 245: Treesort 3".
        Communications of the ACM. 7(12): 701.

Invariants (Popperian Falsification):
    P1: Heap property maintained after operations
    P2: heap_pop returns minimum element
    P3: heap_push adds element correctly
    P4: heapify creates valid heap from array
"""

from __future__ import annotations


def _sift_down(heap: list[int], i: int, n: int) -> None:
    """Sift element at index i down to maintain heap property."""
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest


def _sift_up(heap: list[int], i: int) -> None:
    """Sift element at index i up to maintain heap property."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


def heapify(arr: list[int]) -> list[int]:
    """Convert array into a min-heap in-place.

    Args:
        arr: Array to heapify.

    Returns:
        The heapified array (modified in place).

    Examples:
        >>> h = heapify([3, 1, 4, 1, 5, 9])
        >>> h[0]  # Min element at root
        1

        >>> heapify([])
        []

        >>> heapify([1])
        [1]
    """
    n = len(arr)
    # Start from last non-leaf and sift down
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(arr, i, n)
    return arr


def heap_push(heap: list[int], val: int) -> None:
    """Push value onto heap.

    Args:
        heap: Min-heap.
        val: Value to add.

    Examples:
        >>> h = [1, 3, 5]
        >>> heap_push(h, 2)
        >>> h[0]
        1

        >>> h = []
        >>> heap_push(h, 5)
        >>> h
        [5]
    """
    heap.append(val)
    _sift_up(heap, len(heap) - 1)


def heap_pop(heap: list[int]) -> int:
    """Pop and return minimum from heap.

    Args:
        heap: Non-empty min-heap.

    Returns:
        Minimum element.

    Examples:
        >>> h = [1, 3, 5]
        >>> heap_pop(h)
        1
        >>> h
        [3, 5]

        >>> h = [5]
        >>> heap_pop(h)
        5
        >>> h
        []
    """
    if len(heap) == 1:
        return heap.pop()

    min_val = heap[0]
    heap[0] = heap.pop()
    _sift_down(heap, 0, len(heap))

    return min_val
