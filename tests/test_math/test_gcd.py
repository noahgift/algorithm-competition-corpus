"""Tests for GCD algorithms.

Tests Popperian Falsification Invariants:
    P1: gcd(a, b) divides both a and b
    P2: gcd(a, b) is the largest such divisor
    P3: gcd(a, b) == gcd(b, a) (commutative)
    P4: gcd(a, 0) == a
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.math.gcd import (
    extended_gcd,
    gcd,
    lcm,
)


class TestGCD(unittest.TestCase):
    """Unit tests for gcd."""

    def test_basic(self) -> None:
        """Test basic GCD."""
        self.assertEqual(gcd(48, 18), 6)

    def test_coprime(self) -> None:
        """Test coprime numbers."""
        self.assertEqual(gcd(17, 5), 1)

    def test_zero(self) -> None:
        """Test with zero."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)


class TestLCM(unittest.TestCase):
    """Unit tests for lcm."""

    def test_basic(self) -> None:
        """Test basic LCM."""
        self.assertEqual(lcm(4, 6), 12)

    def test_coprime(self) -> None:
        """Test coprime numbers."""
        self.assertEqual(lcm(21, 6), 42)

    def test_zero(self) -> None:
        """Test with zero."""
        self.assertEqual(lcm(0, 5), 0)

    def test_equal(self) -> None:
        """Test equal numbers."""
        self.assertEqual(lcm(5, 5), 5)


class TestExtendedGCD(unittest.TestCase):
    """Unit tests for extended_gcd."""

    def test_basic(self) -> None:
        """Test basic extended GCD."""
        g, x, y = extended_gcd(35, 15)
        self.assertEqual(g, 5)
        self.assertEqual(35 * x + 15 * y, g)

    def test_coprime(self) -> None:
        """Test coprime numbers."""
        g, x, y = extended_gcd(120, 23)
        self.assertEqual(g, 1)
        self.assertEqual(120 * x + 23 * y, g)


class TestGCDInvariants(unittest.TestCase):
    """Popperian falsification tests for GCD invariants."""

    def test_p1_divides_both(self) -> None:
        """P1: gcd(a, b) divides both a and b."""
        rng = random.Random(42)
        for _ in range(50):
            a = rng.randint(1, 1000)
            b = rng.randint(1, 1000)
            g = gcd(a, b)
            self.assertEqual(a % g, 0)
            self.assertEqual(b % g, 0)

    def test_p2_largest_divisor(self) -> None:
        """P2: gcd is the largest common divisor."""
        rng = random.Random(42)
        for _ in range(50):
            a = rng.randint(1, 100)
            b = rng.randint(1, 100)
            g = gcd(a, b)
            # No larger divisor exists
            for d in range(g + 1, min(a, b) + 1):
                if a % d == 0 and b % d == 0:
                    self.fail(f"Found larger divisor {d} for gcd({a}, {b})")

    def test_p3_commutative(self) -> None:
        """P3: gcd(a, b) == gcd(b, a)."""
        rng = random.Random(42)
        for _ in range(50):
            a = rng.randint(0, 1000)
            b = rng.randint(0, 1000)
            self.assertEqual(gcd(a, b), gcd(b, a))

    def test_p4_identity(self) -> None:
        """P4: gcd(a, 0) == a."""
        rng = random.Random(42)
        for _ in range(50):
            a = rng.randint(0, 1000)
            self.assertEqual(gcd(a, 0), a)

    def test_extended_gcd_bezout(self) -> None:
        """Extended GCD satisfies Bezout's identity."""
        rng = random.Random(42)
        for _ in range(50):
            a = rng.randint(1, 1000)
            b = rng.randint(1, 1000)
            g, x, y = extended_gcd(a, b)
            self.assertEqual(a * x + b * y, g)

    def test_lcm_gcd_relationship(self) -> None:
        """LCM * GCD == a * b."""
        rng = random.Random(42)
        for _ in range(50):
            a = rng.randint(1, 1000)
            b = rng.randint(1, 1000)
            self.assertEqual(lcm(a, b) * gcd(a, b), a * b)


if __name__ == "__main__":
    unittest.main()
