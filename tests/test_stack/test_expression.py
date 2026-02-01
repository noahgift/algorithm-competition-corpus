"""Tests for Expression evaluation algorithms.

Tests Popperian Falsification Invariants:
    P1: Postfix of infix evaluates to same result
    P2: RPN evaluation is correct
    P3: Operator precedence is respected
    P4: Parentheses override precedence
"""

from __future__ import annotations

import unittest

from algorithm_corpus.stack.expression import (
    eval_postfix,
    eval_rpn,
    infix_to_postfix,
)


class TestInfixToPostfix(unittest.TestCase):
    """Unit tests for infix_to_postfix."""

    def test_simple(self) -> None:
        """Test simple expression."""
        self.assertEqual(infix_to_postfix("3+4"), "34+")

    def test_precedence(self) -> None:
        """Test operator precedence."""
        self.assertEqual(infix_to_postfix("3+4*2"), "342*+")

    def test_parentheses(self) -> None:
        """Test parentheses."""
        self.assertEqual(infix_to_postfix("(1+2)*3"), "12+3*")

    def test_complex(self) -> None:
        """Test complex expression."""
        self.assertEqual(infix_to_postfix("(3+4)*(5-2)"), "34+52-*")


class TestEvalPostfix(unittest.TestCase):
    """Unit tests for eval_postfix."""

    def test_addition(self) -> None:
        """Test addition."""
        self.assertEqual(eval_postfix("34+"), 7)

    def test_precedence(self) -> None:
        """Test precedence."""
        self.assertEqual(eval_postfix("342*+"), 11)

    def test_parentheses(self) -> None:
        """Test parentheses effect."""
        self.assertEqual(eval_postfix("12+3*"), 9)

    def test_empty(self) -> None:
        """Test empty expression."""
        self.assertEqual(eval_postfix(""), 0)


class TestEvalRpn(unittest.TestCase):
    """Unit tests for eval_rpn."""

    def test_simple(self) -> None:
        """Test simple expression."""
        self.assertEqual(eval_rpn(["2", "1", "+"]), 3)

    def test_complex(self) -> None:
        """Test complex expression."""
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)

    def test_division(self) -> None:
        """Test division."""
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)

    def test_negative_division(self) -> None:
        """Test division truncating toward zero."""
        self.assertEqual(eval_rpn(["10", "3", "/"]), 3)


class TestExpressionInvariants(unittest.TestCase):
    """Popperian falsification tests for expression invariants."""

    def test_p1_postfix_evaluates_correctly(self) -> None:
        """P1: Postfix of infix evaluates to same result."""
        # 3 + 4 * 2 = 3 + 8 = 11
        postfix = infix_to_postfix("3+4*2")
        result = eval_postfix(postfix)
        self.assertEqual(result, 11)

    def test_p2_rpn_is_correct(self) -> None:
        """P2: RPN evaluation matches expected."""
        # (4 + (13 / 5)) = 4 + 2 = 6
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)

    def test_p3_precedence_respected(self) -> None:
        """P3: Operator precedence is respected."""
        # 2 + 3 * 4 = 2 + 12 = 14 (not 20)
        postfix = infix_to_postfix("2+3*4")
        self.assertEqual(eval_postfix(postfix), 14)

    def test_p4_parentheses_override(self) -> None:
        """P4: Parentheses override precedence."""
        # (2 + 3) * 4 = 5 * 4 = 20
        postfix = infix_to_postfix("(2+3)*4")
        self.assertEqual(eval_postfix(postfix), 20)


if __name__ == "__main__":
    unittest.main()
