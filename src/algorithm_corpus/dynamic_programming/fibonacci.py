"""Fibonacci Sequence Algorithms.

Implements Fibonacci sequence using tabulation (iterative)
and space-optimized approaches (preferred for Rust transpilation).

Time Complexity: O(n)
Space Complexity: O(n) for tabulation, O(1) for optimized

References:
    [1] Bellman, R. (1954). "The theory of dynamic programming".
        Bulletin of the American Mathematical Society. 60(6): 503-515.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 15.

Invariants (Popperian Falsification):
    P1: F(n) = F(n-1) + F(n-2) for n >= 2
    P2: F(0) = 0, F(1) = 1
    P3: F(n) >= 0 for all n >= 0
    P4: F(n) < F(n+1) for n >= 1
"""

from __future__ import annotations


def fibonacci_tabulation(n: int) -> int:
    """Calculate nth Fibonacci number using tabulation.

    Args:
        n: The index of the Fibonacci number (0-indexed).

    Returns:
        The nth Fibonacci number.

    Examples:
        >>> fibonacci_tabulation(0)
        0

        >>> fibonacci_tabulation(1)
        1

        >>> fibonacci_tabulation(10)
        55

        >>> fibonacci_tabulation(20)
        6765
    """
    if n <= 1:
        return n

    dp: list[int] = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """Calculate nth Fibonacci number with O(1) space.

    Args:
        n: The index of the Fibonacci number (0-indexed).

    Returns:
        The nth Fibonacci number.

    Examples:
        >>> fibonacci_optimized(0)
        0

        >>> fibonacci_optimized(1)
        1

        >>> fibonacci_optimized(10)
        55

        >>> fibonacci_optimized(50)
        12586269025
    """
    if n <= 1:
        return n

    prev2: int = 0
    prev1: int = 1

    for _ in range(2, n + 1):
        curr: int = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def fibonacci_sequence(n: int) -> list[int]:
    """Generate first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate.

    Returns:
        List of first n Fibonacci numbers.

    Examples:
        >>> fibonacci_sequence(0)
        []

        >>> fibonacci_sequence(1)
        [0]

        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]

        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    result: list[int] = [0, 1]

    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])

    return result


def fibonacci_mod(n: int, mod: int) -> int:
    """Calculate nth Fibonacci number modulo mod.

    Useful for large Fibonacci numbers to prevent overflow.

    Args:
        n: The index of the Fibonacci number.
        mod: The modulo value.

    Returns:
        The nth Fibonacci number mod mod.

    Examples:
        >>> fibonacci_mod(10, 1000)
        55

        >>> fibonacci_mod(100, 1000000007)
        687995182

        >>> fibonacci_mod(0, 100)
        0
    """
    if n <= 1:
        return n

    prev2: int = 0
    prev1: int = 1

    for _ in range(2, n + 1):
        curr: int = (prev1 + prev2) % mod
        prev2 = prev1
        prev1 = curr

    return prev1
