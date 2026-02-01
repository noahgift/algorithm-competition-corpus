"""K-th element and top-K problems.

Heap-based solutions for k-th element problems.
"""

from __future__ import annotations


def _sift_down(heap: list[int], n: int, i: int, *, is_max: bool = False) -> None:
    """Sift element down in heap."""
    while True:
        extreme = i
        left = 2 * i + 1
        right = 2 * i + 2

        if is_max:
            if left < n and heap[left] > heap[extreme]:
                extreme = left
            if right < n and heap[right] > heap[extreme]:
                extreme = right
        else:
            if left < n and heap[left] < heap[extreme]:
                extreme = left
            if right < n and heap[right] < heap[extreme]:
                extreme = right

        if extreme == i:
            break

        heap[i], heap[extreme] = heap[extreme], heap[i]
        i = extreme


def find_kth_largest_quickselect(nums: list[int], k: int) -> int:
    """Find k-th largest element using quickselect.

    Average O(n), worst O(n^2) time.

    Args:
        nums: List of integers.
        k: K-th largest (1-indexed).

    Returns:
        K-th largest element.

    Example:
        >>> find_kth_largest_quickselect([3, 2, 1, 5, 6, 4], 2)
        5
        >>> find_kth_largest_quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
    """
    k = len(nums) - k  # Convert to 0-indexed for k-th smallest

    left, right = 0, len(nums) - 1

    while left < right:
        pivot_idx = _partition(nums, left, right)
        if pivot_idx == k:
            break
        if pivot_idx < k:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1

    return nums[k]


def _partition(nums: list[int], left: int, right: int) -> int:
    """Partition array around pivot."""
    pivot = nums[right]
    i = left

    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[right] = nums[right], nums[i]
    return i


def k_closest_to_origin(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    """Find k points closest to origin.

    Uses max heap of size k.

    Args:
        points: List of (x, y) coordinates.
        k: Number of closest points.

    Returns:
        K closest points.

    Example:
        >>> sorted(k_closest_to_origin([(1, 3), (-2, 2)], 1))
        [(-2, 2)]
        >>> sorted(k_closest_to_origin([(3, 3), (5, -1), (-2, 4)], 2))
        [(-2, 4), (3, 3)]
    """
    # Use quickselect on distances
    n = len(points)
    distances = [(x * x + y * y, x, y) for x, y in points]

    def partition_dist(left: int, right: int) -> int:
        pivot = distances[right]
        i = left
        for j in range(left, right):
            if distances[j][0] <= pivot[0]:
                distances[i], distances[j] = distances[j], distances[i]
                i += 1
        distances[i], distances[right] = distances[right], distances[i]
        return i

    left, right = 0, n - 1
    while left < right:
        pivot_idx = partition_dist(left, right)
        if pivot_idx == k:
            break
        if pivot_idx < k:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1

    return [(x, y) for _, x, y in distances[:k]]


def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists.

    Uses min heap.

    Args:
        lists: List of sorted lists.

    Returns:
        Merged sorted list.

    Example:
        >>> merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
        [1, 1, 2, 3, 4, 4, 5, 6]
    """
    result: list[int] = []
    # Initialize with (value, list_index, element_index)
    heap: list[tuple[int, int, int]] = []

    for i, lst in enumerate(lists):
        if lst:
            heap.append((lst[0], i, 0))

    # Build heap
    for i in range(len(heap) // 2 - 1, -1, -1):
        _sift_down_tuple(heap, len(heap), i)

    while heap:
        val, list_idx, elem_idx = heap[0]
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            heap[0] = (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            _sift_down_tuple(heap, len(heap), 0)
        else:
            heap[0] = heap[-1]
            heap.pop()
            if heap:
                _sift_down_tuple(heap, len(heap), 0)

    return result


def _sift_down_tuple(heap: list[tuple[int, int, int]], n: int, i: int) -> None:
    """Sift down for tuple heap."""
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap[left][0] < heap[smallest][0]:
            smallest = left
        if right < n and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
