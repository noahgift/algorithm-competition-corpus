"""Prime Number Algorithms.

Primality testing and prime generation.

Time Complexity: O(sqrt(n)) for is_prime, O(n log log n) for sieve
Space Complexity: O(1) for is_prime, O(n) for sieve

References:
    [1] Eratosthenes (c. 276-194 BC). Sieve algorithm.

    [2] Miller, G.L. (1976). "Riemann's Hypothesis and Tests for Primality".
        Journal of Computer and System Sciences.

Invariants (Popperian Falsification):
    P1: is_prime returns True only for primes
    P2: Sieve generates all primes up to n
    P3: prime_factors multiplied together equal n
    P4: All factors returned are prime
"""

from __future__ import annotations


def _has_odd_divisor(n: int) -> bool:
    """Check if n has an odd divisor other than 1."""
    i: int = 3
    while i * i <= n:
        if n % i == 0:
            return True
        i += 2
    return False


def is_prime(n: int) -> bool:
    """Check if n is prime using trial division.

    Args:
        n: Integer to check.

    Returns:
        True if n is prime, False otherwise.

    Examples:
        >>> is_prime(2)
        True

        >>> is_prime(17)
        True

        >>> is_prime(1)
        False

        >>> is_prime(4)
        False

        >>> is_prime(97)
        True
    """
    if n < 2:  # noqa: PLR2004
        return False
    if n == 2:  # noqa: PLR2004
        return True
    if n % 2 == 0:
        return False
    return not _has_odd_divisor(n)


def sieve_of_eratosthenes(n: int) -> list[int]:
    """Generate all primes up to n using Sieve of Eratosthenes.

    Args:
        n: Upper bound (inclusive).

    Returns:
        List of all primes <= n.

    Examples:
        >>> sieve_of_eratosthenes(10)
        [2, 3, 5, 7]

        >>> sieve_of_eratosthenes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]

        >>> sieve_of_eratosthenes(1)
        []

        >>> sieve_of_eratosthenes(2)
        [2]
    """
    if n < 2:  # noqa: PLR2004
        return []

    is_prime_arr: list[bool] = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    i: int = 2
    while i * i <= n:
        if is_prime_arr[i]:
            j: int = i * i
            while j <= n:
                is_prime_arr[j] = False
                j += i
        i += 1

    return [i for i in range(n + 1) if is_prime_arr[i]]


def prime_factors(n: int) -> list[int]:
    """Find all prime factors of n with multiplicity.

    Args:
        n: Positive integer to factorize.

    Returns:
        List of prime factors (with repetition).

    Examples:
        >>> prime_factors(12)
        [2, 2, 3]

        >>> prime_factors(100)
        [2, 2, 5, 5]

        >>> prime_factors(17)
        [17]

        >>> prime_factors(1)
        []
    """
    if n <= 1:
        return []

    factors: list[int] = []

    # Factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Factor out odd numbers
    i: int = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # n is prime if greater than 1
    if n > 1:
        factors.append(n)

    return factors
