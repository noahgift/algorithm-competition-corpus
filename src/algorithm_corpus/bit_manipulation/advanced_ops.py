"""Advanced Bit Manipulation Operations.

More complex bitwise algorithms.

Time Complexity: O(log n) for most operations
Space Complexity: O(1)

References:
    [1] Warren, H.S. (2012). "Hacker's Delight" (2nd ed.). Addison-Wesley.

Invariants (Popperian Falsification):
    P1: reverse_bits inverts bit order
    P2: hamming_distance counts differing bits
    P3: single_number finds unique element
    P4: Operations handle edge cases correctly
"""

from __future__ import annotations


def reverse_bits(n: int, bits: int = 32) -> int:
    """Reverse the bits of n.

    Args:
        n: Non-negative integer.
        bits: Number of bits to consider.

    Returns:
        Integer with bits reversed.

    Examples:
        >>> bin(reverse_bits(0b1011, 4))
        '0b1101'
        >>> reverse_bits(0, 8)
        0
        >>> reverse_bits(1, 4)
        8
    """
    result: int = 0
    for _ in range(bits):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


def hamming_distance(x: int, y: int) -> int:
    """Calculate Hamming distance between two integers.

    Hamming distance is the number of positions where bits differ.

    Args:
        x: First non-negative integer.
        y: Second non-negative integer.

    Returns:
        Number of differing bits.

    Examples:
        >>> hamming_distance(1, 4)
        2
        >>> hamming_distance(0, 0)
        0
        >>> hamming_distance(7, 0)
        3
        >>> hamming_distance(3, 3)
        0
    """
    xor: int = x ^ y
    count: int = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count


def single_number(nums: list[int]) -> int:
    """Find the element that appears only once.

    Every element appears twice except for one.
    Uses XOR property: a ^ a = 0 and a ^ 0 = a.

    Args:
        nums: List where every element appears twice except one.

    Returns:
        The single element.

    Examples:
        >>> single_number([2, 2, 1])
        1
        >>> single_number([4, 1, 2, 1, 2])
        4
        >>> single_number([1])
        1
    """
    result: int = 0
    for num in nums:
        result ^= num
    return result
