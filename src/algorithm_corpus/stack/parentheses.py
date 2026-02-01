"""Parentheses validation algorithms.

Stack-based bracket matching problems.
"""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    """Check if string has valid parentheses.

    Supports (), [], {}.

    Args:
        s: String containing brackets.

    Returns:
        True if valid.

    Example:
        >>> is_valid_parentheses("()[]{}")
        True
        >>> is_valid_parentheses("(]")
        False
        >>> is_valid_parentheses("([)]")
        False
    """
    stack: list[str] = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in ")]}" and (not stack or pairs[stack.pop()] != char):
            return False

    return len(stack) == 0


def longest_valid_parentheses(s: str) -> int:
    """Find length of longest valid parentheses substring.

    Uses stack to track indices.

    Args:
        s: String containing only '(' and ')'.

    Returns:
        Length of longest valid substring.

    Example:
        >>> longest_valid_parentheses("(()")
        2
        >>> longest_valid_parentheses(")()())")
        4
        >>> longest_valid_parentheses("")
        0
    """
    stack: list[int] = [-1]
    max_len = 0

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


def min_add_to_make_valid(s: str) -> int:
    """Find minimum additions to make parentheses valid.

    Args:
        s: String containing only '(' and ')'.

    Returns:
        Minimum number of '(' or ')' to add.

    Example:
        >>> min_add_to_make_valid("())")
        1
        >>> min_add_to_make_valid("(((")
        3
        >>> min_add_to_make_valid("()")
        0
    """
    open_count = 0
    close_needed = 0

    for char in s:
        if char == "(":
            open_count += 1
        elif char == ")":
            if open_count > 0:
                open_count -= 1
            else:
                close_needed += 1

    return open_count + close_needed
