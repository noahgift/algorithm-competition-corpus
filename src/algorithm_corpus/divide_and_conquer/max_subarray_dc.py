"""Maximum Subarray using Divide and Conquer.

Find maximum sum subarray using divide and conquer approach.

Time Complexity: O(n log n)
Space Complexity: O(log n) due to recursion

References:
    [1] Bentley, J. (1984). "Programming Pearls: Algorithm Design Techniques".
        Communications of the ACM. 27(9): 865-873.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 4.1.

Invariants (Popperian Falsification):
    P1: Result is a valid subarray sum
    P2: Result equals optimal subarray sum
    P3: Works with negative numbers
    P4: Empty array returns 0
"""

from __future__ import annotations


def max_subarray_divide_conquer(arr: list[int]) -> int:
    """Find maximum subarray sum using divide and conquer.

    Args:
        arr: Array of integers.

    Returns:
        Maximum sum of any contiguous subarray.

    Examples:
        >>> max_subarray_divide_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        >>> max_subarray_divide_conquer([1, 2, 3, 4, 5])
        15

        >>> max_subarray_divide_conquer([-1, -2, -3])
        -1

        >>> max_subarray_divide_conquer([])
        0
    """
    if not arr:
        return 0

    def _max_crossing_sum(left: int, mid: int, right: int) -> int:
        # Find max sum on left side including mid
        left_sum = float("-inf")
        current = 0
        for i in range(mid, left - 1, -1):
            current += arr[i]
            left_sum = max(left_sum, current)

        # Find max sum on right side excluding mid
        right_sum = float("-inf")
        current = 0
        for i in range(mid + 1, right + 1):
            current += arr[i]
            right_sum = max(right_sum, current)

        return int(left_sum) + int(right_sum)

    def _max_subarray(left: int, right: int) -> int:
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        left_max = _max_subarray(left, mid)
        right_max = _max_subarray(mid + 1, right)
        cross_max = _max_crossing_sum(left, mid, right)

        return max(left_max, right_max, cross_max)

    return _max_subarray(0, len(arr) - 1)
