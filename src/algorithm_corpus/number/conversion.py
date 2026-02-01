"""Number conversion algorithms.

Roman numeral and other number system conversions.
"""

from __future__ import annotations


def roman_to_int(s: str) -> int:
    """Convert Roman numeral to integer.

    Args:
        s: Roman numeral string.

    Returns:
        Integer value.

    Example:
        >>> roman_to_int("III")
        3
        >>> roman_to_int("LVIII")
        58
        >>> roman_to_int("MCMXCIV")
        1994
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0

    for char in reversed(s):
        curr = values[char]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr

    return result


def int_to_roman(num: int) -> str:
    """Convert integer to Roman numeral.

    Args:
        num: Integer between 1 and 3999.

    Returns:
        Roman numeral string.

    Example:
        >>> int_to_roman(3)
        'III'
        >>> int_to_roman(58)
        'LVIII'
        >>> int_to_roman(1994)
        'MCMXCIV'
    """
    value_symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result: list[str] = []
    for value, symbol in value_symbols:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)
