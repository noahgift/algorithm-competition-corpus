"""Two Sum and Three Sum with Two Pointers.

Find pairs or triplets that sum to a target value.

Time Complexity: O(n) for two_sum_sorted, O(n²) for three_sum
Space Complexity: O(1) extra space

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: If found, elements sum to target
    P2: Indices are valid within array bounds
    P3: Works on sorted arrays (two_sum_sorted)
    P4: Three sum finds all unique triplets
"""

from __future__ import annotations


def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int] | None:
    """Find two numbers that add up to target in sorted array.

    Args:
        arr: Sorted array of integers.
        target: Target sum.

    Returns:
        Tuple of indices (i, j) where arr[i] + arr[j] == target,
        or None if no such pair exists.

    Examples:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        (0, 1)

        >>> two_sum_sorted([2, 3, 4], 6)
        (0, 2)

        >>> two_sum_sorted([1, 2, 3], 10)

        >>> two_sum_sorted([], 5)
    """
    if len(arr) < 2:  # noqa: PLR2004
        return None

    left: int = 0
    right: int = len(arr) - 1

    while left < right:
        current_sum: int = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def three_sum(arr: list[int], target: int = 0) -> list[tuple[int, int, int]]:
    """Find all unique triplets that sum to target.

    Args:
        arr: Array of integers.
        target: Target sum (default 0).

    Returns:
        List of unique triplets (a, b, c) where a + b + c == target.

    Examples:
        >>> sorted(three_sum([-1, 0, 1, 2, -1, -4]))
        [(-1, -1, 2), (-1, 0, 1)]

        >>> three_sum([0, 1, 1])
        []

        >>> three_sum([0, 0, 0])
        [(0, 0, 0)]
    """
    n: int = len(arr)
    if n < 3:  # noqa: PLR2004
        return []

    sorted_arr: list[int] = sorted(arr)
    result: list[tuple[int, int, int]] = []

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
            continue

        left: int = i + 1
        right: int = n - 1

        while left < right:
            total: int = sorted_arr[i] + sorted_arr[left] + sorted_arr[right]

            if total == target:
                result.append((sorted_arr[i], sorted_arr[left], sorted_arr[right]))
                # Skip duplicates
                while left < right and sorted_arr[left] == sorted_arr[left + 1]:
                    left += 1
                while left < right and sorted_arr[right] == sorted_arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result
