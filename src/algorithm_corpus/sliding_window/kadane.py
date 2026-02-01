"""Maximum Sum Subarray (Kadane's Algorithm).

Find the contiguous subarray with the largest sum.

Time Complexity: O(n)
Space Complexity: O(1)

References:
    [1] Kadane, J.B. (1984). Unpublished. Algorithm described in
        Bentley, J. (1984). "Programming Pearls: Algorithm Design Techniques".
        Communications of the ACM. 27(9): 865-871.

    [2] Gries, D. (1982). "A Note on the Standard Strategy for Developing
        Loop Invariants and Loops". Science of Computer Programming. 2: 207-214.

Invariants (Popperian Falsification):
    P1: Result >= max(nums) (at minimum, single element is valid subarray)
    P2: Result <= sum(nums) (can't exceed total sum)
    P3: For all-negative arrays, result is the maximum element
    P4: For all-positive arrays, result is the total sum
"""

from __future__ import annotations


def max_subarray_sum(nums: list[int]) -> int:
    """Find the maximum sum of any contiguous subarray.

    Uses Kadane's algorithm.

    Args:
        nums: Input array of integers.

    Returns:
        Maximum subarray sum.

    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        >>> max_subarray_sum([1])
        1

        >>> max_subarray_sum([-1, -2, -3])
        -1

        >>> max_subarray_sum([5, 4, -1, 7, 8])
        23
    """
    if not nums:
        return 0

    max_sum: int = nums[0]
    current_sum: int = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_indices(nums: list[int]) -> tuple[int, int, int]:
    """Find maximum subarray sum with start and end indices.

    Args:
        nums: Input array of integers.

    Returns:
        Tuple of (max_sum, start_index, end_index).

    Examples:
        >>> max_subarray_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        (6, 3, 6)

        >>> max_subarray_indices([1, 2, 3])
        (6, 0, 2)

        >>> max_subarray_indices([-1])
        (-1, 0, 0)
    """
    if not nums:
        return 0, -1, -1

    max_sum: int = nums[0]
    current_sum: int = nums[0]
    start: int = 0
    end: int = 0
    temp_start: int = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum = current_sum + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end


def max_subarray_fixed_size(nums: list[int], k: int) -> int:
    """Find maximum sum of subarray with exactly k elements.

    Args:
        nums: Input array of integers.
        k: Size of subarray.

    Returns:
        Maximum sum of any k-element subarray.

    Examples:
        >>> max_subarray_fixed_size([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
        39

        >>> max_subarray_fixed_size([1, 2, 3], 2)
        5

        >>> max_subarray_fixed_size([5], 1)
        5
    """
    if not nums or k <= 0 or k > len(nums):
        return 0

    window_sum: int = sum(nums[:k])
    max_sum: int = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def max_circular_subarray_sum(nums: list[int]) -> int:
    """Find maximum subarray sum in a circular array.

    The subarray can wrap around from end to beginning.

    Args:
        nums: Input array of integers.

    Returns:
        Maximum circular subarray sum.

    Examples:
        >>> max_circular_subarray_sum([1, -2, 3, -2])
        3

        >>> max_circular_subarray_sum([5, -3, 5])
        10

        >>> max_circular_subarray_sum([-3, -2, -3])
        -2
    """
    if not nums:
        return 0

    max_kadane: int = nums[0]
    min_kadane: int = nums[0]
    current_max: int = nums[0]
    current_min: int = nums[0]
    total: int = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_kadane = max(max_kadane, current_max)

        current_min = min(nums[i], current_min + nums[i])
        min_kadane = min(min_kadane, current_min)

        total += nums[i]

    if max_kadane < 0:
        return max_kadane

    return max(max_kadane, total - min_kadane)


def max_subarray_product(nums: list[int]) -> int:
    """Find the maximum product of any contiguous subarray.

    Args:
        nums: Input array of integers.

    Returns:
        Maximum subarray product.

    Examples:
        >>> max_subarray_product([2, 3, -2, 4])
        6

        >>> max_subarray_product([-2, 0, -1])
        0

        >>> max_subarray_product([-2, 3, -4])
        24
    """
    if not nums:
        return 0

    max_prod: int = nums[0]
    min_prod: int = nums[0]
    result: int = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)

    return result
