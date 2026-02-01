"""Advanced bit manipulation algorithms.

Advanced bit operations and problems.
"""

from __future__ import annotations


def missing_number(nums: list[int]) -> int:
    """Find missing number in range [0, n].

    Uses XOR property: a ^ a = 0.

    Args:
        nums: List containing n distinct numbers in range [0, n].

    Returns:
        Missing number.

    Example:
        >>> missing_number([3, 0, 1])
        2
        >>> missing_number([0, 1])
        2
    """
    n = len(nums)
    result = n  # Start with n

    for i, num in enumerate(nums):
        result ^= i ^ num

    return result


def single_number_ii(nums: list[int]) -> int:
    """Find element appearing exactly once when others appear 3 times.

    Uses bit counting modulo 3.

    Args:
        nums: List where every element appears 3 times except one.

    Returns:
        Element appearing once.

    Example:
        >>> single_number_ii([2, 2, 3, 2])
        3
        >>> single_number_ii([0, 1, 0, 1, 0, 1, 99])
        99
    """
    result = 0

    for i in range(32):
        bit_sum = 0
        for num in nums:
            bit_sum += (num >> i) & 1
        result |= (bit_sum % 3) << i

    # Handle negative numbers (2's complement)
    if result >= 2**31:
        result -= 2**32

    return result


def find_two_single_numbers(nums: list[int]) -> tuple[int, int]:
    """Find two elements appearing once when others appear twice.

    Args:
        nums: List where every element appears twice except two.

    Returns:
        Tuple of two unique numbers.

    Example:
        >>> sorted(find_two_single_numbers([1, 2, 1, 3, 2, 5]))
        [3, 5]
    """
    # XOR all numbers to get a ^ b
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Find rightmost set bit (differs between a and b)
    diff_bit = xor_all & (-xor_all)

    # Partition numbers and XOR each group
    num1, num2 = 0, 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return (num1, num2)


def add_without_operator(a: int, b: int) -> int:
    """Add two integers without using + operator.

    Uses bit manipulation.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Sum of a and b.

    Example:
        >>> add_without_operator(1, 2)
        3
        >>> add_without_operator(-1, 1)
        0
    """
    mask = 0xFFFFFFFF

    while b & mask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    # Handle negative numbers
    return a if b == 0 else a & mask
