"""Tests for Combinatorics algorithms.

Tests Popperian Falsification Invariants:
    P1: factorial(n) == n!
    P2: binomial(n, k) == n! / (k! * (n-k)!)
    P3: binomial(n, k) == binomial(n, n-k)
    P4: permutations(n, k) == n! / (n-k)!
"""

from __future__ import annotations

import unittest

from algorithm_corpus.math.combinatorics import (
    binomial_coefficient,
    factorial,
    permutations_count,
)


class TestFactorial(unittest.TestCase):
    """Unit tests for factorial."""

    def test_zero(self) -> None:
        """Test factorial of 0."""
        self.assertEqual(factorial(0), 1)

    def test_one(self) -> None:
        """Test factorial of 1."""
        self.assertEqual(factorial(1), 1)

    def test_five(self) -> None:
        """Test factorial of 5."""
        self.assertEqual(factorial(5), 120)

    def test_ten(self) -> None:
        """Test factorial of 10."""
        self.assertEqual(factorial(10), 3628800)


class TestBinomialCoefficient(unittest.TestCase):
    """Unit tests for binomial_coefficient."""

    def test_basic(self) -> None:
        """Test basic binomial coefficients."""
        self.assertEqual(binomial_coefficient(5, 2), 10)
        self.assertEqual(binomial_coefficient(10, 3), 120)

    def test_boundary(self) -> None:
        """Test boundary cases."""
        self.assertEqual(binomial_coefficient(5, 0), 1)
        self.assertEqual(binomial_coefficient(5, 5), 1)

    def test_invalid(self) -> None:
        """Test invalid k."""
        self.assertEqual(binomial_coefficient(3, 5), 0)


class TestPermutationsCount(unittest.TestCase):
    """Unit tests for permutations_count."""

    def test_basic(self) -> None:
        """Test basic permutations."""
        self.assertEqual(permutations_count(5, 2), 20)

    def test_all(self) -> None:
        """Test P(n, n)."""
        self.assertEqual(permutations_count(5, 5), 120)

    def test_zero(self) -> None:
        """Test P(n, 0)."""
        self.assertEqual(permutations_count(5, 0), 1)

    def test_invalid(self) -> None:
        """Test invalid k."""
        self.assertEqual(permutations_count(3, 5), 0)


class TestCombinatoricsInvariants(unittest.TestCase):
    """Popperian falsification tests for combinatorics invariants."""

    def test_p1_factorial_definition(self) -> None:
        """P1: factorial(n) == n!."""
        expected = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        for n, exp in enumerate(expected):
            self.assertEqual(factorial(n), exp)

    def test_p2_binomial_formula(self) -> None:
        """P2: binomial(n, k) == n! / (k! * (n-k)!)."""
        for n in range(10):
            for k in range(n + 1):
                expected = factorial(n) // (factorial(k) * factorial(n - k))
                self.assertEqual(binomial_coefficient(n, k), expected)

    def test_p3_binomial_symmetry(self) -> None:
        """P3: binomial(n, k) == binomial(n, n-k)."""
        for n in range(15):
            for k in range(n + 1):
                self.assertEqual(
                    binomial_coefficient(n, k), binomial_coefficient(n, n - k)
                )

    def test_p4_permutations_formula(self) -> None:
        """P4: permutations(n, k) == n! / (n-k)!."""
        for n in range(10):
            for k in range(n + 1):
                expected = factorial(n) // factorial(n - k)
                self.assertEqual(permutations_count(n, k), expected)

    def test_pascals_triangle(self) -> None:
        """Binomial satisfies Pascal's triangle identity."""
        for n in range(1, 15):
            for k in range(1, n):
                self.assertEqual(
                    binomial_coefficient(n, k),
                    binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k),
                )


if __name__ == "__main__":
    unittest.main()
