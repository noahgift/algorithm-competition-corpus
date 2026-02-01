"""Basic Bit Manipulation Operations.

Fundamental bitwise operations.

Time Complexity: O(1) for most operations, O(log n) for count_bits
Space Complexity: O(1)

References:
    [1] Warren, H.S. (2012). "Hacker's Delight" (2nd ed.). Addison-Wesley.

Invariants (Popperian Falsification):
    P1: get_bit returns 0 or 1
    P2: set_bit only changes target bit
    P3: is_power_of_two correct for all inputs
    P4: count_bits equals number of 1s in binary
"""

from __future__ import annotations


def get_bit(n: int, i: int) -> int:
    """Get the i-th bit of n (0-indexed from right).

    Args:
        n: Integer.
        i: Bit position (0 = rightmost).

    Returns:
        0 or 1.

    Examples:
        >>> get_bit(5, 0)
        1
        >>> get_bit(5, 1)
        0
        >>> get_bit(5, 2)
        1
        >>> get_bit(8, 3)
        1
    """
    return (n >> i) & 1


def set_bit(n: int, i: int, value: int) -> int:
    """Set the i-th bit of n to value.

    Args:
        n: Integer.
        i: Bit position (0 = rightmost).
        value: 0 or 1.

    Returns:
        Modified integer.

    Examples:
        >>> set_bit(5, 1, 1)
        7
        >>> set_bit(7, 1, 0)
        5
        >>> set_bit(0, 3, 1)
        8
    """
    if value:
        return n | (1 << i)
    return n & ~(1 << i)


def toggle_bit(n: int, i: int) -> int:
    """Toggle the i-th bit of n.

    Args:
        n: Integer.
        i: Bit position (0 = rightmost).

    Returns:
        Modified integer.

    Examples:
        >>> toggle_bit(5, 1)
        7
        >>> toggle_bit(7, 1)
        5
        >>> toggle_bit(0, 0)
        1
    """
    return n ^ (1 << i)


def is_power_of_two(n: int) -> bool:
    """Check if n is a power of two.

    Args:
        n: Integer.

    Returns:
        True if n is a power of two.

    Examples:
        >>> is_power_of_two(1)
        True
        >>> is_power_of_two(2)
        True
        >>> is_power_of_two(4)
        True
        >>> is_power_of_two(3)
        False
        >>> is_power_of_two(0)
        False
        >>> is_power_of_two(-4)
        False
    """
    return n > 0 and (n & (n - 1)) == 0


def count_bits(n: int) -> int:
    """Count the number of 1 bits in n (population count).

    Args:
        n: Non-negative integer.

    Returns:
        Number of 1 bits.

    Examples:
        >>> count_bits(0)
        0
        >>> count_bits(1)
        1
        >>> count_bits(7)
        3
        >>> count_bits(255)
        8
    """
    count: int = 0
    while n:
        count += n & 1
        n >>= 1
    return count
