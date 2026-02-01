"""Greatest Common Divisor and Least Common Multiple.

Euclidean algorithm implementations for GCD and LCM.

Time Complexity: O(log(min(a, b)))
Space Complexity: O(1) iterative, O(log(min(a, b))) recursive

References:
    [1] Euclid. "Elements" (c. 300 BC). Book VII, Propositions 1-2.

    [2] Knuth, D.E. (1997). "The Art of Computer Programming, Volume 2:
        Seminumerical Algorithms" (3rd ed.). Addison-Wesley. Section 4.5.2.

Invariants (Popperian Falsification):
    P1: gcd(a, b) divides both a and b
    P2: gcd(a, b) is the largest such divisor
    P3: gcd(a, b) == gcd(b, a) (commutative)
    P4: gcd(a, 0) == a
"""

from __future__ import annotations


def gcd(a: int, b: int) -> int:
    """Compute greatest common divisor using Euclidean algorithm.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        Greatest common divisor of a and b.

    Examples:
        >>> gcd(48, 18)
        6

        >>> gcd(54, 24)
        6

        >>> gcd(17, 5)
        1

        >>> gcd(0, 5)
        5

        >>> gcd(5, 0)
        5
    """
    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    """Compute least common multiple.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        Least common multiple of a and b.

    Examples:
        >>> lcm(4, 6)
        12

        >>> lcm(21, 6)
        42

        >>> lcm(0, 5)
        0

        >>> lcm(5, 5)
        5
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm.

    Finds gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b).

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Tuple (gcd, x, y) where ax + by = gcd.

    Examples:
        >>> g, x, y = extended_gcd(35, 15)
        >>> g
        5
        >>> 35 * x + 15 * y == g
        True

        >>> g, x, y = extended_gcd(120, 23)
        >>> g
        1
        >>> 120 * x + 23 * y == g
        True
    """
    if b == 0:
        return (a, 1, 0)

    g: int
    x: int
    y: int
    g, x, y = extended_gcd(b, a % b)

    return (g, y, x - (a // b) * y)
