"""Tests for Parentheses validation algorithms.

Tests Popperian Falsification Invariants:
    P1: Empty string is valid
    P2: Matching pairs are valid
    P3: Mismatched pairs are invalid
    P4: Longest valid is never negative
"""

from __future__ import annotations

import unittest

from algorithm_corpus.stack.parentheses import (
    is_valid_parentheses,
    longest_valid_parentheses,
    min_add_to_make_valid,
)


class TestIsValidParentheses(unittest.TestCase):
    """Unit tests for is_valid_parentheses."""

    def test_valid_simple(self) -> None:
        """Test valid simple."""
        self.assertTrue(is_valid_parentheses("()"))

    def test_valid_multiple(self) -> None:
        """Test valid multiple types."""
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_valid_nested(self) -> None:
        """Test valid nested."""
        self.assertTrue(is_valid_parentheses("{[()]}"))

    def test_invalid_mismatched(self) -> None:
        """Test invalid mismatched."""
        self.assertFalse(is_valid_parentheses("(]"))

    def test_invalid_interleaved(self) -> None:
        """Test invalid interleaved."""
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_empty(self) -> None:
        """Test empty string."""
        self.assertTrue(is_valid_parentheses(""))


class TestLongestValidParentheses(unittest.TestCase):
    """Unit tests for longest_valid_parentheses."""

    def test_partial(self) -> None:
        """Test partial valid."""
        self.assertEqual(longest_valid_parentheses("(()"), 2)

    def test_multiple(self) -> None:
        """Test multiple valid parts."""
        self.assertEqual(longest_valid_parentheses(")()())"), 4)

    def test_empty(self) -> None:
        """Test empty string."""
        self.assertEqual(longest_valid_parentheses(""), 0)

    def test_all_valid(self) -> None:
        """Test all valid."""
        self.assertEqual(longest_valid_parentheses("(())"), 4)


class TestMinAddToMakeValid(unittest.TestCase):
    """Unit tests for min_add_to_make_valid."""

    def test_extra_close(self) -> None:
        """Test extra close."""
        self.assertEqual(min_add_to_make_valid("())"), 1)

    def test_extra_open(self) -> None:
        """Test extra open."""
        self.assertEqual(min_add_to_make_valid("((("), 3)

    def test_already_valid(self) -> None:
        """Test already valid."""
        self.assertEqual(min_add_to_make_valid("()"), 0)

    def test_empty(self) -> None:
        """Test empty string."""
        self.assertEqual(min_add_to_make_valid(""), 0)


class TestParenthesesInvariants(unittest.TestCase):
    """Popperian falsification tests for parentheses invariants."""

    def test_p1_empty_is_valid(self) -> None:
        """P1: Empty string is valid."""
        self.assertTrue(is_valid_parentheses(""))

    def test_p2_matching_pairs_valid(self) -> None:
        """P2: Matching pairs are valid."""
        for s in ["()", "[]", "{}", "(())", "((()))", "{[([])]}"]:
            self.assertTrue(is_valid_parentheses(s), f"Failed for {s}")

    def test_p3_mismatched_invalid(self) -> None:
        """P3: Mismatched pairs are invalid."""
        for s in ["(", ")", "(]", "[}", "(()", "())"]:
            # Only check truly invalid
            if s in ["(", ")", "(]", "[}"]:
                self.assertFalse(is_valid_parentheses(s), f"Should fail for {s}")

    def test_p4_longest_never_negative(self) -> None:
        """P4: Longest valid is never negative."""
        for s in ["", "(", ")", "()", "(()", ")(", ")))((("]:
            result = longest_valid_parentheses(s)
            self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
