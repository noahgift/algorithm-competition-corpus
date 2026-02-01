"""Combinatorics Algorithms.

Factorial, binomial coefficients, and counting.

Time Complexity: O(n) for factorial, O(min(k, n-k)) for binomial
Space Complexity: O(1)

References:
    [1] Graham, R.L., Knuth, D.E., Patashnik, O. (1994).
        "Concrete Mathematics" (2nd ed.). Addison-Wesley.

Invariants (Popperian Falsification):
    P1: factorial(n) == n!
    P2: binomial(n, k) == n! / (k! * (n-k)!)
    P3: binomial(n, k) == binomial(n, n-k)
    P4: permutations(n, k) == n! / (n-k)!
"""

from __future__ import annotations


def factorial(n: int) -> int:
    """Compute n factorial.

    Args:
        n: Non-negative integer.

    Returns:
        n! = n * (n-1) * ... * 1.

    Examples:
        >>> factorial(0)
        1

        >>> factorial(1)
        1

        >>> factorial(5)
        120

        >>> factorial(10)
        3628800
    """
    if n < 0:
        msg = "Factorial not defined for negative numbers"
        raise ValueError(msg)

    result: int = 1
    for i in range(2, n + 1):
        result *= i

    return result


def binomial_coefficient(n: int, k: int) -> int:
    """Compute binomial coefficient C(n, k).

    Also known as "n choose k".

    Args:
        n: Total items.
        k: Items to choose.

    Returns:
        Number of ways to choose k items from n items.

    Examples:
        >>> binomial_coefficient(5, 2)
        10

        >>> binomial_coefficient(10, 3)
        120

        >>> binomial_coefficient(5, 0)
        1

        >>> binomial_coefficient(5, 5)
        1

        >>> binomial_coefficient(3, 5)
        0
    """
    if k < 0 or k > n:
        return 0

    # Use symmetry: C(n, k) == C(n, n-k)
    k = min(k, n - k)

    result: int = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)

    return result


def permutations_count(n: int, k: int) -> int:
    """Compute number of k-permutations of n items.

    Also known as P(n, k) = n! / (n-k)!.

    Args:
        n: Total items.
        k: Items to arrange.

    Returns:
        Number of ways to arrange k items from n items.

    Examples:
        >>> permutations_count(5, 2)
        20

        >>> permutations_count(5, 5)
        120

        >>> permutations_count(5, 0)
        1

        >>> permutations_count(3, 5)
        0
    """
    if k < 0 or k > n:
        return 0

    result: int = 1
    for i in range(k):
        result *= n - i

    return result
