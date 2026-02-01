"""Tests for Basic Bit Operations.

Tests Popperian Falsification Invariants:
    P1: get_bit returns 0 or 1
    P2: set_bit only changes target bit
    P3: is_power_of_two correct for all inputs
    P4: count_bits equals number of 1s in binary
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.bit_manipulation.basic_ops import (
    count_bits,
    get_bit,
    is_power_of_two,
    set_bit,
    toggle_bit,
)


class TestGetBit(unittest.TestCase):
    """Unit tests for get_bit."""

    def test_basic(self) -> None:
        """Test basic get_bit."""
        self.assertEqual(get_bit(5, 0), 1)  # 5 = 101
        self.assertEqual(get_bit(5, 1), 0)
        self.assertEqual(get_bit(5, 2), 1)

    def test_power_of_two(self) -> None:
        """Test with power of two."""
        self.assertEqual(get_bit(8, 3), 1)  # 8 = 1000


class TestSetBit(unittest.TestCase):
    """Unit tests for set_bit."""

    def test_set_to_one(self) -> None:
        """Test setting bit to 1."""
        self.assertEqual(set_bit(5, 1, 1), 7)  # 101 -> 111

    def test_set_to_zero(self) -> None:
        """Test setting bit to 0."""
        self.assertEqual(set_bit(7, 1, 0), 5)  # 111 -> 101

    def test_from_zero(self) -> None:
        """Test setting bit in 0."""
        self.assertEqual(set_bit(0, 3, 1), 8)


class TestToggleBit(unittest.TestCase):
    """Unit tests for toggle_bit."""

    def test_toggle(self) -> None:
        """Test toggling bits."""
        self.assertEqual(toggle_bit(5, 1), 7)  # 101 -> 111
        self.assertEqual(toggle_bit(7, 1), 5)  # 111 -> 101


class TestIsPowerOfTwo(unittest.TestCase):
    """Unit tests for is_power_of_two."""

    def test_powers(self) -> None:
        """Test powers of two."""
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(2))
        self.assertTrue(is_power_of_two(4))
        self.assertTrue(is_power_of_two(1024))

    def test_non_powers(self) -> None:
        """Test non-powers of two."""
        self.assertFalse(is_power_of_two(0))
        self.assertFalse(is_power_of_two(3))
        self.assertFalse(is_power_of_two(-4))


class TestCountBits(unittest.TestCase):
    """Unit tests for count_bits."""

    def test_basic(self) -> None:
        """Test basic count."""
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(1), 1)
        self.assertEqual(count_bits(7), 3)
        self.assertEqual(count_bits(255), 8)


class TestBasicOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for basic ops invariants."""

    def test_p1_get_bit_returns_zero_or_one(self) -> None:
        """P1: get_bit returns 0 or 1."""
        rng = random.Random(42)
        for _ in range(100):
            n = rng.randint(0, 1000)
            i = rng.randint(0, 15)
            result = get_bit(n, i)
            self.assertIn(result, (0, 1))

    def test_p2_set_bit_only_changes_target(self) -> None:
        """P2: set_bit only changes target bit."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 1000)
            i = rng.randint(0, 15)
            new_val = rng.randint(0, 1)
            result = set_bit(n, i, new_val)
            # Check other bits unchanged
            for j in range(16):
                if j != i:
                    self.assertEqual(get_bit(result, j), get_bit(n, j))

    def test_p3_is_power_of_two_correct(self) -> None:
        """P3: is_power_of_two correct for all inputs."""
        powers = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}
        for n in range(-10, 1100):
            if n in powers:
                self.assertTrue(is_power_of_two(n), f"{n} should be power of 2")
            else:
                self.assertFalse(is_power_of_two(n), f"{n} should not be power of 2")

    def test_p4_count_bits_correct(self) -> None:
        """P4: count_bits equals number of 1s in binary."""
        rng = random.Random(42)
        for _ in range(100):
            n = rng.randint(0, 10000)
            expected = n.bit_count()
            self.assertEqual(count_bits(n), expected)


if __name__ == "__main__":
    unittest.main()
