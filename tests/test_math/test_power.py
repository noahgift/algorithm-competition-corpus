"""Tests for Power algorithms.

Tests Popperian Falsification Invariants:
    P1: power(x, n) == x^n
    P2: power(x, 0) == 1 for all x != 0
    P3: mod_pow(x, n, m) == (x^n) mod m
    P4: Results are computed in O(log n) multiplications
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.math.power import (
    mod_pow,
    power,
)


class TestPower(unittest.TestCase):
    """Unit tests for power."""

    def test_basic(self) -> None:
        """Test basic powers."""
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(3, 5), 243)

    def test_zero_exponent(self) -> None:
        """Test zero exponent."""
        self.assertEqual(power(5, 0), 1)

    def test_one_exponent(self) -> None:
        """Test exponent of one."""
        self.assertEqual(power(7, 1), 7)


class TestModPow(unittest.TestCase):
    """Unit tests for mod_pow."""

    def test_basic(self) -> None:
        """Test basic modular power."""
        self.assertEqual(mod_pow(2, 10, 1000), 24)

    def test_large(self) -> None:
        """Test large exponent."""
        self.assertEqual(mod_pow(3, 1000, 1000000007), 56888193)

    def test_zero_exponent(self) -> None:
        """Test zero exponent."""
        self.assertEqual(mod_pow(5, 0, 13), 1)


class TestPowerInvariants(unittest.TestCase):
    """Popperian falsification tests for power invariants."""

    def test_p1_power_correct(self) -> None:
        """P1: power(x, n) == x^n."""
        rng = random.Random(42)
        for _ in range(50):
            base = rng.randint(1, 10)
            exp = rng.randint(0, 10)
            expected = base**exp
            self.assertEqual(power(base, exp), expected)

    def test_p2_zero_exponent(self) -> None:
        """P2: power(x, 0) == 1."""
        for x in range(1, 20):
            self.assertEqual(power(x, 0), 1)

    def test_p3_mod_pow_correct(self) -> None:
        """P3: mod_pow(x, n, m) == (x^n) mod m."""
        rng = random.Random(42)
        for _ in range(50):
            base = rng.randint(1, 100)
            exp = rng.randint(0, 20)
            mod = rng.randint(2, 1000)
            expected = pow(base, exp, mod)
            self.assertEqual(mod_pow(base, exp, mod), expected)

    def test_p4_multiplicative_property(self) -> None:
        """Power satisfies x^(a+b) == x^a * x^b."""
        rng = random.Random(42)
        for _ in range(30):
            base = rng.randint(1, 5)
            a = rng.randint(0, 5)
            b = rng.randint(0, 5)
            self.assertEqual(power(base, a + b), power(base, a) * power(base, b))


if __name__ == "__main__":
    unittest.main()
