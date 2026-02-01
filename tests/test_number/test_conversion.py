"""Tests for Number conversion algorithms.

Tests Popperian Falsification Invariants:
    P1: Roman to int and back is identity
    P2: Standard cases are correct
    P3: Subtractive notation works
    P4: Edge cases handled
"""

from __future__ import annotations

import unittest

from algorithm_corpus.number.conversion import (
    int_to_roman,
    roman_to_int,
)


class TestRomanToInt(unittest.TestCase):
    """Unit tests for roman_to_int."""

    def test_simple(self) -> None:
        """Test simple numerals."""
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("LVIII"), 58)

    def test_subtractive(self) -> None:
        """Test subtractive notation."""
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    def test_large(self) -> None:
        """Test large numbers."""
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)


class TestIntToRoman(unittest.TestCase):
    """Unit tests for int_to_roman."""

    def test_simple(self) -> None:
        """Test simple numbers."""
        self.assertEqual(int_to_roman(3), "III")
        self.assertEqual(int_to_roman(58), "LVIII")

    def test_subtractive(self) -> None:
        """Test subtractive notation."""
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")

    def test_large(self) -> None:
        """Test large numbers."""
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")


class TestConversionInvariants(unittest.TestCase):
    """Popperian falsification tests for conversion invariants."""

    def test_p1_roundtrip_identity(self) -> None:
        """P1: Roman to int and back is identity."""
        for num in [1, 4, 9, 40, 90, 400, 900, 58, 1994, 3999]:
            roman = int_to_roman(num)
            back = roman_to_int(roman)
            self.assertEqual(back, num)

    def test_p2_standard_cases(self) -> None:
        """P2: Standard cases are correct."""
        cases = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for roman, expected in cases.items():
            self.assertEqual(roman_to_int(roman), expected)

    def test_p3_subtractive_notation(self) -> None:
        """P3: Subtractive notation works."""
        cases = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        for roman, expected in cases.items():
            self.assertEqual(roman_to_int(roman), expected)

    def test_p4_edge_cases(self) -> None:
        """P4: Edge cases handled."""
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")


if __name__ == "__main__":
    unittest.main()
