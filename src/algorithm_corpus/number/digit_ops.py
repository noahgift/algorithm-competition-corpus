"""Digit operation algorithms.

Operations on individual digits of numbers.
"""

from __future__ import annotations


def reverse_integer(x: int) -> int:
    """Reverse digits of an integer.

    Handles overflow: returns 0 if result overflows 32-bit signed integer.

    Args:
        x: Integer to reverse.

    Returns:
        Reversed integer, or 0 if overflow.

    Example:
        >>> reverse_integer(123)
        321
        >>> reverse_integer(-123)
        -321
        >>> reverse_integer(120)
        21
    """
    int_max = 2**31 - 1
    int_min = -(2**31)

    sign = 1 if x >= 0 else -1
    x = abs(x)

    result = 0
    while x > 0:
        digit = x % 10
        x //= 10

        # Check overflow before adding
        if result > (int_max - digit) // 10:
            return 0

        result = result * 10 + digit

    result *= sign

    if result < int_min or result > int_max:
        return 0

    return result


def is_palindrome_number(x: int) -> bool:
    """Check if integer is a palindrome.

    Without converting to string.

    Args:
        x: Integer to check.

    Returns:
        True if palindrome.

    Example:
        >>> is_palindrome_number(121)
        True
        >>> is_palindrome_number(-121)
        False
        >>> is_palindrome_number(10)
        False
    """
    if x < 0:
        return False

    if x != 0 and x % 10 == 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Handle both even and odd length numbers
    return x == reversed_half or x == reversed_half // 10


def digit_sum(n: int) -> int:
    """Calculate sum of digits.

    Args:
        n: Non-negative integer.

    Returns:
        Sum of all digits.

    Example:
        >>> digit_sum(12345)
        15
        >>> digit_sum(0)
        0
    """
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
