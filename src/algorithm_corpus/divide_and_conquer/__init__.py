"""Divide and Conquer algorithms.

Algorithms that solve problems by dividing them into smaller subproblems.
"""

from __future__ import annotations

from algorithm_corpus.divide_and_conquer.binary_search_dc import (
    binary_search_recursive,
    find_first_greater,
)
from algorithm_corpus.divide_and_conquer.max_subarray_dc import (
    max_subarray_divide_conquer,
)
from algorithm_corpus.divide_and_conquer.merge_sort_dc import (
    count_inversions,
    merge_sort_recursive,
)

__all__: list[str] = [
    "binary_search_recursive",
    "count_inversions",
    "find_first_greater",
    "max_subarray_divide_conquer",
    "merge_sort_recursive",
]
