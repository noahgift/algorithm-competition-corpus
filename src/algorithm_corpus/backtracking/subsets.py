"""Subset and Combination Generation.

Generate all subsets and combinations using backtracking.

Time Complexity: O(2^N * N) for subsets, O(C(N,K) * K) for combinations
Space Complexity: O(N)

References:
    [1] Knuth, D.E. (2011). "The Art of Computer Programming, Volume 4A:
        Combinatorial Algorithms, Part 1". Addison-Wesley.

Invariants (Popperian Falsification):
    P1: All subsets are valid subsets of input
    P2: Correct number of subsets (2^N)
    P3: No duplicate subsets
    P4: combinations(n, k) returns C(n, k) results
"""

from __future__ import annotations


def subsets(nums: list[int]) -> list[list[int]]:
    """Generate all subsets (power set).

    Args:
        nums: List of distinct integers.

    Returns:
        All subsets.

    Examples:
        >>> sorted([sorted(s) for s in subsets([1, 2, 3])])
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

        >>> subsets([])
        [[]]

        >>> sorted(subsets([1]))
        [[], [1]]
    """
    result: list[list[int]] = []

    def _backtrack(start: int, current: list[int]) -> None:
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            _backtrack(i + 1, current)
            current.pop()

    _backtrack(0, [])
    return result


def combinations(n: int, k: int) -> list[list[int]]:
    """Generate all k-combinations of [1, 2, ..., n].

    Args:
        n: Range of numbers (1 to n).
        k: Size of each combination.

    Returns:
        All combinations of size k.

    Examples:
        >>> combinations(4, 2)
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

        >>> combinations(3, 3)
        [[1, 2, 3]]

        >>> combinations(3, 0)
        [[]]

        >>> combinations(0, 0)
        [[]]
    """
    result: list[list[int]] = []

    def _backtrack(start: int, current: list[int]) -> None:
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)
            _backtrack(i + 1, current)
            current.pop()

    _backtrack(1, [])
    return result
