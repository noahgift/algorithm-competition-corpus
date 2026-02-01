"""Two Pointers algorithms.

Classic two pointer techniques for array and string problems.
"""

from __future__ import annotations

from algorithm_corpus.two_pointers.container import (
    max_area,
    trap_water,
)
from algorithm_corpus.two_pointers.palindrome import (
    is_palindrome,
    longest_palindromic_substring,
)
from algorithm_corpus.two_pointers.partition import (
    dutch_national_flag,
    move_zeros,
    remove_duplicates,
)
from algorithm_corpus.two_pointers.two_sum import (
    three_sum,
    two_sum_sorted,
)

__all__: list[str] = [
    "dutch_national_flag",
    "is_palindrome",
    "longest_palindromic_substring",
    "max_area",
    "move_zeros",
    "remove_duplicates",
    "three_sum",
    "trap_water",
    "two_sum_sorted",
]
