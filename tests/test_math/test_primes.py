"""Tests for Prime algorithms.

Tests Popperian Falsification Invariants:
    P1: is_prime returns True only for primes
    P2: Sieve generates all primes up to n
    P3: prime_factors multiplied together equal n
    P4: All factors returned are prime
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.math.primes import (
    is_prime,
    prime_factors,
    sieve_of_eratosthenes,
)


class TestIsPrime(unittest.TestCase):
    """Unit tests for is_prime."""

    def test_small_primes(self) -> None:
        """Test small primes."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(97))

    def test_non_primes(self) -> None:
        """Test non-primes."""
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(100))


class TestSieve(unittest.TestCase):
    """Unit tests for sieve_of_eratosthenes."""

    def test_small(self) -> None:
        """Test small sieve."""
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])

    def test_twenty(self) -> None:
        """Test sieve up to 20."""
        self.assertEqual(sieve_of_eratosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        self.assertEqual(sieve_of_eratosthenes(1), [])
        self.assertEqual(sieve_of_eratosthenes(2), [2])


class TestPrimeFactors(unittest.TestCase):
    """Unit tests for prime_factors."""

    def test_composite(self) -> None:
        """Test composite numbers."""
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(100), [2, 2, 5, 5])

    def test_prime(self) -> None:
        """Test prime number."""
        self.assertEqual(prime_factors(17), [17])

    def test_one(self) -> None:
        """Test 1."""
        self.assertEqual(prime_factors(1), [])


class TestPrimeInvariants(unittest.TestCase):
    """Popperian falsification tests for prime invariants."""

    def test_p1_is_prime_correct(self) -> None:
        """P1: is_prime returns True only for primes."""
        known_primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
        for n in range(50):
            if n in known_primes:
                self.assertTrue(is_prime(n), f"{n} should be prime")
            else:
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_p2_sieve_complete(self) -> None:
        """P2: Sieve generates all primes up to n."""
        primes = sieve_of_eratosthenes(100)
        for p in primes:
            self.assertTrue(is_prime(p))
        # Check no primes are missing
        for n in range(2, 101):
            if is_prime(n):
                self.assertIn(n, primes)

    def test_p3_factors_product(self) -> None:
        """P3: prime_factors multiplied together equal n."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 10000)
            factors = prime_factors(n)
            product = 1
            for f in factors:
                product *= f
            self.assertEqual(product, n)

    def test_p4_all_factors_prime(self) -> None:
        """P4: All factors returned are prime."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 10000)
            factors = prime_factors(n)
            for f in factors:
                self.assertTrue(is_prime(f), f"{f} is not prime")


if __name__ == "__main__":
    unittest.main()
