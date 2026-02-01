"""Subarray algorithms using two pointers.

Finding subarrays with specific properties.
"""

from __future__ import annotations


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """Count subarrays with sum equal to k.

    Uses prefix sum with hash map.

    Args:
        nums: List of integers.
        k: Target sum.

    Returns:
        Number of subarrays with sum k.

    Example:
        >>> subarray_sum_equals_k([1, 1, 1], 2)
        2
        >>> subarray_sum_equals_k([1, 2, 3], 3)
        2
    """
    count = 0
    prefix_sum = 0
    prefix_counts: dict[int, int] = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum - k]

        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    return count


def max_product_subarray(nums: list[int]) -> int:
    """Find maximum product of a contiguous subarray.

    Tracks both max and min due to negative numbers.

    Args:
        nums: List of integers.

    Returns:
        Maximum product.

    Example:
        >>> max_product_subarray([2, 3, -2, 4])
        6
        >>> max_product_subarray([-2, 0, -1])
        0
    """
    if not nums:
        return 0

    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)

    return result


def shortest_subarray_with_sum(nums: list[int], k: int) -> int:
    """Find shortest subarray with sum >= k.

    Uses monotonic deque for handling negative numbers.

    Args:
        nums: List of integers (may be negative).
        k: Target sum.

    Returns:
        Length of shortest subarray, or -1 if none.

    Example:
        >>> shortest_subarray_with_sum([2, -1, 2], 3)
        3
        >>> shortest_subarray_with_sum([1, 2], 4)
        -1
    """
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] + num

    result = n + 1
    deque: list[int] = []

    for i in range(n + 1):
        # Remove indices with larger prefix sums
        while deque and prefix[i] <= prefix[deque[-1]]:
            deque.pop()

        # Check if valid subarray found
        while deque and prefix[i] - prefix[deque[0]] >= k:
            result = min(result, i - deque[0])
            deque.pop(0)

        deque.append(i)

    return result if result <= n else -1
