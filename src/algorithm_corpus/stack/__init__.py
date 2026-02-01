"""Stack-based algorithms.

Algorithms using stack data structure for expression parsing and more.
"""

from __future__ import annotations

from algorithm_corpus.stack.expression import (
    eval_postfix,
    eval_rpn,
    infix_to_postfix,
)
from algorithm_corpus.stack.monotonic import (
    daily_temperatures,
    next_greater_element,
)
from algorithm_corpus.stack.parentheses import (
    is_valid_parentheses,
    longest_valid_parentheses,
    min_add_to_make_valid,
)

__all__: list[str] = [
    "daily_temperatures",
    "eval_postfix",
    "eval_rpn",
    "infix_to_postfix",
    "is_valid_parentheses",
    "longest_valid_parentheses",
    "min_add_to_make_valid",
    "next_greater_element",
]
