"""Tests for Fibonacci Sequence algorithms.

Tests Popperian Falsification Invariants:
    P1: F(n) = F(n-1) + F(n-2) for n >= 2
    P2: F(0) = 0, F(1) = 1
    P3: F(n) >= 0 for all n >= 0
    P4: F(n) < F(n+1) for n >= 1
"""

from __future__ import annotations

import unittest

from algorithm_corpus.dynamic_programming.fibonacci import (
    fibonacci_mod,
    fibonacci_optimized,
    fibonacci_sequence,
    fibonacci_tabulation,
)


class TestFibonacciTabulation(unittest.TestCase):
    """Unit tests for fibonacci_tabulation."""

    def test_base_cases(self) -> None:
        """Test base cases."""
        self.assertEqual(fibonacci_tabulation(0), 0)
        self.assertEqual(fibonacci_tabulation(1), 1)

    def test_small_values(self) -> None:
        """Test small Fibonacci numbers."""
        self.assertEqual(fibonacci_tabulation(2), 1)
        self.assertEqual(fibonacci_tabulation(5), 5)
        self.assertEqual(fibonacci_tabulation(10), 55)

    def test_larger_value(self) -> None:
        """Test larger Fibonacci number."""
        self.assertEqual(fibonacci_tabulation(20), 6765)


class TestFibonacciOptimized(unittest.TestCase):
    """Unit tests for fibonacci_optimized."""

    def test_base_cases(self) -> None:
        """Test base cases."""
        self.assertEqual(fibonacci_optimized(0), 0)
        self.assertEqual(fibonacci_optimized(1), 1)

    def test_small_values(self) -> None:
        """Test small Fibonacci numbers."""
        self.assertEqual(fibonacci_optimized(10), 55)

    def test_large_value(self) -> None:
        """Test large Fibonacci number."""
        self.assertEqual(fibonacci_optimized(50), 12586269025)


class TestFibonacciSequence(unittest.TestCase):
    """Unit tests for fibonacci_sequence."""

    def test_empty_sequence(self) -> None:
        """Test empty sequence."""
        self.assertEqual(fibonacci_sequence(0), [])

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_multiple_elements(self) -> None:
        """Test multiple elements."""
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


class TestFibonacciMod(unittest.TestCase):
    """Unit tests for fibonacci_mod."""

    def test_small_mod(self) -> None:
        """Test with small modulus."""
        self.assertEqual(fibonacci_mod(10, 1000), 55)

    def test_large_mod(self) -> None:
        """Test with large modulus."""
        self.assertEqual(fibonacci_mod(100, 1000000007), 687995182)

    def test_base_cases(self) -> None:
        """Test base cases with mod."""
        self.assertEqual(fibonacci_mod(0, 100), 0)
        self.assertEqual(fibonacci_mod(1, 100), 1)


class TestFibonacciInvariants(unittest.TestCase):
    """Popperian falsification tests for Fibonacci invariants."""

    def test_p1_recurrence_relation(self) -> None:
        """P1: F(n) = F(n-1) + F(n-2) for n >= 2."""
        for n in range(2, 30):
            fn = fibonacci_tabulation(n)
            fn_1 = fibonacci_tabulation(n - 1)
            fn_2 = fibonacci_tabulation(n - 2)
            self.assertEqual(fn, fn_1 + fn_2, f"F({n}) != F({n - 1}) + F({n - 2})")

    def test_p2_base_cases(self) -> None:
        """P2: F(0) = 0, F(1) = 1."""
        self.assertEqual(fibonacci_tabulation(0), 0)
        self.assertEqual(fibonacci_tabulation(1), 1)
        self.assertEqual(fibonacci_optimized(0), 0)
        self.assertEqual(fibonacci_optimized(1), 1)

    def test_p3_non_negative(self) -> None:
        """P3: F(n) >= 0 for all n >= 0."""
        for n in range(50):
            self.assertGreaterEqual(fibonacci_tabulation(n), 0)
            self.assertGreaterEqual(fibonacci_optimized(n), 0)

    def test_p4_strictly_increasing_after_1(self) -> None:
        """P4: F(n) < F(n+1) for n >= 2 (F(1) = F(2) = 1)."""
        for n in range(2, 30):
            fn = fibonacci_tabulation(n)
            fn_1 = fibonacci_tabulation(n + 1)
            self.assertLess(fn, fn_1, f"F({n}) >= F({n + 1})")

    def test_tabulation_optimized_consistency(self) -> None:
        """Both implementations should give same results."""
        for n in range(50):
            self.assertEqual(
                fibonacci_tabulation(n),
                fibonacci_optimized(n),
                f"Mismatch at n={n}",
            )

    def test_sequence_consistency(self) -> None:
        """Sequence should match individual computations."""
        seq = fibonacci_sequence(20)
        for i, val in enumerate(seq):
            self.assertEqual(val, fibonacci_tabulation(i))

    def test_mod_consistency(self) -> None:
        """Mod version should equal regular version mod m."""
        mod = 1000000007
        for n in range(50):
            self.assertEqual(
                fibonacci_mod(n, mod),
                fibonacci_optimized(n) % mod,
            )


if __name__ == "__main__":
    unittest.main()
