"""Array Partition Algorithms using Two Pointers.

Partition and rearrange arrays in place.

Time Complexity: O(n)
Space Complexity: O(1)

References:
    [1] Dijkstra, E.W. (1976). "A Discipline of Programming".
        Prentice Hall. (Dutch National Flag problem)

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: Result is a permutation of input
    P2: Partition property is satisfied
    P3: In-place modification (no extra space)
    P4: Relative order preserved when applicable
"""

from __future__ import annotations


def dutch_national_flag(arr: list[int]) -> list[int]:
    """Sort array containing only 0s, 1s, and 2s.

    Dutch National Flag problem by Dijkstra.

    Args:
        arr: Array containing only 0, 1, 2.

    Returns:
        New sorted array.

    Examples:
        >>> dutch_national_flag([2, 0, 2, 1, 1, 0])
        [0, 0, 1, 1, 2, 2]

        >>> dutch_national_flag([2, 0, 1])
        [0, 1, 2]

        >>> dutch_national_flag([])
        []

        >>> dutch_national_flag([0])
        [0]
    """
    result: list[int] = arr[:]

    low: int = 0
    mid: int = 0
    high: int = len(result) - 1

    while mid <= high:
        if result[mid] == 0:
            result[low], result[mid] = result[mid], result[low]
            low += 1
            mid += 1
        elif result[mid] == 1:
            mid += 1
        else:
            result[mid], result[high] = result[high], result[mid]
            high -= 1

    return result


def move_zeros(arr: list[int]) -> list[int]:
    """Move all zeros to end while maintaining relative order.

    Args:
        arr: Array of integers.

    Returns:
        New array with zeros moved to end.

    Examples:
        >>> move_zeros([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]

        >>> move_zeros([0])
        [0]

        >>> move_zeros([])
        []

        >>> move_zeros([1, 2, 3])
        [1, 2, 3]
    """
    result: list[int] = arr[:]

    write_pos: int = 0

    # Move non-zeros to front
    for i in range(len(result)):
        if result[i] != 0:
            result[write_pos] = result[i]
            write_pos += 1

    # Fill remaining with zeros
    while write_pos < len(result):
        result[write_pos] = 0
        write_pos += 1

    return result


def remove_duplicates(arr: list[int]) -> int:
    """Remove duplicates from sorted array in-place.

    Returns the new length. Elements beyond new length are undefined.

    Args:
        arr: Sorted array of integers.

    Returns:
        Length of array after removing duplicates.

    Examples:
        >>> arr = [1, 1, 2]
        >>> k = remove_duplicates(arr)
        >>> k
        2
        >>> arr[:k]
        [1, 2]

        >>> arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        >>> k = remove_duplicates(arr)
        >>> k
        5
        >>> arr[:k]
        [0, 1, 2, 3, 4]

        >>> remove_duplicates([])
        0
    """
    if not arr:
        return 0

    write_pos: int = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_pos] = arr[i]
            write_pos += 1

    return write_pos
