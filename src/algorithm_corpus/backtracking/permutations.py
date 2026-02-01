"""Permutation Generation.

Generate all permutations using backtracking.

Time Complexity: O(N! * N)
Space Complexity: O(N)

References:
    [1] Sedgewick, R. (1977). "Permutation Generation Methods".
        ACM Computing Surveys. 9(2): 137-164.

Invariants (Popperian Falsification):
    P1: All permutations are valid arrangements
    P2: No duplicate permutations in result
    P3: Correct number of permutations generated
    P4: Empty input returns empty permutation
"""

from __future__ import annotations


def permutations(nums: list[int]) -> list[list[int]]:
    """Generate all permutations of nums.

    Args:
        nums: List of distinct integers.

    Returns:
        All permutations.

    Examples:
        >>> sorted(permutations([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        >>> permutations([1])
        [[1]]

        >>> permutations([])
        [[]]
    """
    if not nums:
        return [[]]

    result: list[list[int]] = []
    used: list[bool] = [False] * len(nums)

    def _backtrack(current: list[int]) -> None:
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                _backtrack(current)
                current.pop()
                used[i] = False

    _backtrack([])
    return result


def permutations_unique(nums: list[int]) -> list[list[int]]:
    """Generate all unique permutations of nums (may have duplicates).

    Args:
        nums: List of integers (may have duplicates).

    Returns:
        All unique permutations.

    Examples:
        >>> sorted(permutations_unique([1, 1, 2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

        >>> sorted(permutations_unique([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result: list[list[int]] = []
    nums_sorted = sorted(nums)
    used: list[bool] = [False] * len(nums_sorted)

    def _backtrack(current: list[int]) -> None:
        if len(current) == len(nums_sorted):
            result.append(current[:])
            return

        for i in range(len(nums_sorted)):
            if used[i]:
                continue
            # Skip duplicates
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            current.append(nums_sorted[i])
            _backtrack(current)
            current.pop()
            used[i] = False

    _backtrack([])
    return result
