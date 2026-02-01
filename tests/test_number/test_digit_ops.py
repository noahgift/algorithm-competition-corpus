"""Tests for Digit operations algorithms.

Tests Popperian Falsification Invariants:
    P1: Reverse of reverse is identity (for non-overflow)
    P2: Palindrome check is symmetric
    P3: Digit sum is non-negative
    P4: Overflow returns 0
"""

from __future__ import annotations

import unittest

from algorithm_corpus.number.digit_ops import (
    digit_sum,
    is_palindrome_number,
    reverse_integer,
)


class TestReverseInteger(unittest.TestCase):
    """Unit tests for reverse_integer."""

    def test_positive(self) -> None:
        """Test positive number."""
        self.assertEqual(reverse_integer(123), 321)

    def test_negative(self) -> None:
        """Test negative number."""
        self.assertEqual(reverse_integer(-123), -321)

    def test_trailing_zero(self) -> None:
        """Test trailing zero."""
        self.assertEqual(reverse_integer(120), 21)

    def test_zero(self) -> None:
        """Test zero."""
        self.assertEqual(reverse_integer(0), 0)


class TestIsPalindromeNumber(unittest.TestCase):
    """Unit tests for is_palindrome_number."""

    def test_palindrome(self) -> None:
        """Test palindrome."""
        self.assertTrue(is_palindrome_number(121))
        self.assertTrue(is_palindrome_number(1221))

    def test_negative(self) -> None:
        """Test negative number."""
        self.assertFalse(is_palindrome_number(-121))

    def test_trailing_zero(self) -> None:
        """Test trailing zero."""
        self.assertFalse(is_palindrome_number(10))

    def test_single_digit(self) -> None:
        """Test single digit."""
        self.assertTrue(is_palindrome_number(7))


class TestDigitSum(unittest.TestCase):
    """Unit tests for digit_sum."""

    def test_basic(self) -> None:
        """Test basic sum."""
        self.assertEqual(digit_sum(12345), 15)

    def test_zero(self) -> None:
        """Test zero."""
        self.assertEqual(digit_sum(0), 0)

    def test_single_digit(self) -> None:
        """Test single digit."""
        self.assertEqual(digit_sum(5), 5)


class TestDigitOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for digit ops invariants."""

    def test_p1_double_reverse_identity(self) -> None:
        """P1: Reverse of reverse is identity (for non-overflow, no trailing zeros)."""
        # Numbers with trailing zeros lose them on reverse
        for num in [123, 456, 789, 12321, 54321]:
            reversed_once = reverse_integer(num)
            if reversed_once != 0:  # Not overflow
                reversed_twice = reverse_integer(reversed_once)
                self.assertEqual(reversed_twice, num)

    def test_p2_palindrome_symmetric(self) -> None:
        """P2: Palindrome check is symmetric."""
        # If n is palindrome, reversing should give same result
        palindromes = [121, 1221, 12321, 0, 7]
        for num in palindromes:
            self.assertTrue(is_palindrome_number(num))

    def test_p3_digit_sum_non_negative(self) -> None:
        """P3: Digit sum is non-negative."""
        for num in [0, 1, 123, 999, 1000000]:
            self.assertGreaterEqual(digit_sum(num), 0)

    def test_p4_overflow_returns_zero(self) -> None:
        """P4: Overflow returns 0."""
        # 2^31 - 1 = 2147483647, reverse is 7463847412 (overflow)
        self.assertEqual(reverse_integer(1534236469), 0)


if __name__ == "__main__":
    unittest.main()
