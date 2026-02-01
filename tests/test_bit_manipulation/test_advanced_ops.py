"""Tests for Advanced Bit Operations.

Tests Popperian Falsification Invariants:
    P1: reverse_bits inverts bit order
    P2: hamming_distance counts differing bits
    P3: single_number finds unique element
    P4: Operations handle edge cases correctly
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.bit_manipulation.advanced_ops import (
    hamming_distance,
    reverse_bits,
    single_number,
)


class TestReverseBits(unittest.TestCase):
    """Unit tests for reverse_bits."""

    def test_basic(self) -> None:
        """Test basic reversal."""
        # 1011 -> 1101
        self.assertEqual(bin(reverse_bits(0b1011, 4)), "0b1101")

    def test_zero(self) -> None:
        """Test zero."""
        self.assertEqual(reverse_bits(0, 8), 0)

    def test_one(self) -> None:
        """Test one."""
        self.assertEqual(reverse_bits(1, 4), 8)


class TestHammingDistance(unittest.TestCase):
    """Unit tests for hamming_distance."""

    def test_basic(self) -> None:
        """Test basic distance."""
        self.assertEqual(hamming_distance(1, 4), 2)  # 001, 100

    def test_same(self) -> None:
        """Test same numbers."""
        self.assertEqual(hamming_distance(0, 0), 0)
        self.assertEqual(hamming_distance(3, 3), 0)

    def test_opposite(self) -> None:
        """Test 7 and 0."""
        self.assertEqual(hamming_distance(7, 0), 3)


class TestSingleNumber(unittest.TestCase):
    """Unit tests for single_number."""

    def test_basic(self) -> None:
        """Test basic cases."""
        self.assertEqual(single_number([2, 2, 1]), 1)
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

    def test_single_element(self) -> None:
        """Test single element."""
        self.assertEqual(single_number([1]), 1)


class TestAdvancedOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for advanced ops invariants."""

    def test_p1_reverse_inverts_order(self) -> None:
        """P1: reverse_bits inverts bit order."""
        # Reversing twice should give original
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(0, 255)
            reversed_once = reverse_bits(n, 8)
            reversed_twice = reverse_bits(reversed_once, 8)
            self.assertEqual(reversed_twice, n)

    def test_p2_hamming_counts_differences(self) -> None:
        """P2: hamming_distance counts differing bits."""
        rng = random.Random(42)
        for _ in range(50):
            x = rng.randint(0, 1000)
            y = rng.randint(0, 1000)
            # Manual count using bit_count()
            xor = x ^ y
            expected = xor.bit_count()
            self.assertEqual(hamming_distance(x, y), expected)

    def test_p3_single_number_finds_unique(self) -> None:
        """P3: single_number finds unique element."""
        rng = random.Random(42)
        for _ in range(30):
            # Create list with pairs + one single
            unique = rng.randint(0, 100)
            pairs = [rng.randint(0, 100) for _ in range(5)]
            nums = pairs + pairs + [unique]
            rng.shuffle(nums)
            self.assertEqual(single_number(nums), unique)

    def test_p4_edge_cases(self) -> None:
        """P4: Operations handle edge cases correctly."""
        self.assertEqual(reverse_bits(0, 32), 0)
        self.assertEqual(hamming_distance(0, 0), 0)
        self.assertEqual(single_number([42]), 42)


if __name__ == "__main__":
    unittest.main()
