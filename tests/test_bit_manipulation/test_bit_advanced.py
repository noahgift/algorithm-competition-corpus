"""Tests for Advanced Bit Manipulation algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.bit_manipulation.bit_advanced import (
    add_without_operator,
    find_two_single_numbers,
    missing_number,
    single_number_ii,
)


class TestMissingNumber(unittest.TestCase):
    """Unit tests for missing_number."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_first(self) -> None:
        """Test missing first."""
        self.assertEqual(missing_number([0, 1]), 2)


class TestSingleNumberII(unittest.TestCase):
    """Unit tests for single_number_ii."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(single_number_ii([2, 2, 3, 2]), 3)

    def test_larger(self) -> None:
        """Test larger case."""
        self.assertEqual(single_number_ii([0, 1, 0, 1, 0, 1, 99]), 99)


class TestFindTwoSingleNumbers(unittest.TestCase):
    """Unit tests for find_two_single_numbers."""

    def test_basic(self) -> None:
        """Test basic case."""
        result = find_two_single_numbers([1, 2, 1, 3, 2, 5])
        self.assertEqual(sorted(result), [3, 5])


class TestAddWithoutOperator(unittest.TestCase):
    """Unit tests for add_without_operator."""

    def test_positive(self) -> None:
        """Test positive numbers."""
        self.assertEqual(add_without_operator(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
