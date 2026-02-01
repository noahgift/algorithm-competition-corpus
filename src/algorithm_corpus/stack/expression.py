"""Expression evaluation algorithms.

Infix to postfix conversion and RPN evaluation.

References:
    Dijkstra, E.W. (1961). "Shunting-yard algorithm."
    ALGOL Bulletin Supplement.
"""

from __future__ import annotations


def _precedence(op: str) -> int:
    """Get operator precedence."""
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0


def infix_to_postfix(expr: str) -> str:
    """Convert infix expression to postfix (RPN).

    Uses Dijkstra's shunting-yard algorithm.

    Args:
        expr: Infix expression with single-digit operands.

    Returns:
        Postfix expression string.

    Example:
        >>> infix_to_postfix("3+4*2")
        '342*+'
        >>> infix_to_postfix("(1+2)*3")
        '12+3*'
    """
    output: list[str] = []
    stack: list[str] = []

    for char in expr:
        if char.isdigit():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('
        elif char in "+-*/":
            while stack and _precedence(stack[-1]) >= _precedence(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)


def eval_postfix(expr: str) -> int:
    """Evaluate postfix (RPN) expression.

    Args:
        expr: Postfix expression with single-digit operands.

    Returns:
        Result of evaluation.

    Example:
        >>> eval_postfix("342*+")
        11
        >>> eval_postfix("12+3*")
        9
    """
    stack: list[int] = []

    for char in expr:
        if char.isdigit():
            stack.append(int(char))
        elif char in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if char == "+":
                stack.append(a + b)
            elif char == "-":
                stack.append(a - b)
            elif char == "*":
                stack.append(a * b)
            elif char == "/":
                stack.append(int(a / b))

    return stack[0] if stack else 0


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate Reverse Polish Notation expression.

    Supports multi-digit numbers.

    Args:
        tokens: List of operands and operators.

    Returns:
        Result of evaluation.

    Example:
        >>> eval_rpn(["2", "1", "+", "3", "*"])
        9
        >>> eval_rpn(["4", "13", "5", "/", "+"])
        6
    """
    stack: list[int] = []

    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            elif tok == "/":
                # Truncate toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(tok))

    return stack[0] if stack else 0
