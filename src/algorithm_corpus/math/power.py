"""Power and Exponentiation Algorithms.

Fast exponentiation using binary method.

Time Complexity: O(log n)
Space Complexity: O(1)

References:
    [1] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 2:
        Seminumerical Algorithms" (3rd ed.). Addison-Wesley. Section 4.6.3.

Invariants (Popperian Falsification):
    P1: power(x, n) == x^n
    P2: power(x, 0) == 1 for all x != 0
    P3: mod_pow(x, n, m) == (x^n) mod m
    P4: Results are computed in O(log n) multiplications
"""

from __future__ import annotations


def power(base: int, exp: int) -> int:
    """Compute base^exp using binary exponentiation.

    Args:
        base: Base integer.
        exp: Non-negative exponent.

    Returns:
        base raised to power exp.

    Examples:
        >>> power(2, 10)
        1024

        >>> power(3, 5)
        243

        >>> power(5, 0)
        1

        >>> power(7, 1)
        7
    """
    if exp == 0:
        return 1

    result: int = 1

    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1

    return result


def mod_pow(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) mod m using binary exponentiation.

    Args:
        base: Base integer.
        exp: Non-negative exponent.
        mod: Modulus (must be positive).

    Returns:
        (base^exp) mod m.

    Examples:
        >>> mod_pow(2, 10, 1000)
        24

        >>> mod_pow(3, 1000, 1000000007)
        56888193

        >>> mod_pow(5, 0, 13)
        1

        >>> mod_pow(7, 256, 13)
        9
    """
    if mod == 1:
        return 0

    result: int = 1
    base = base % mod

    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1

    return result
