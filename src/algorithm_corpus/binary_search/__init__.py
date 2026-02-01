"""Binary Search Algorithms.

Classic binary search and variants for searching in sorted arrays.
"""

from __future__ import annotations

from algorithm_corpus.binary_search.binary_search import (
    binary_search,
    binary_search_leftmost,
    binary_search_rightmost,
    lower_bound,
    upper_bound,
)
from algorithm_corpus.binary_search.peak_finding import (
    find_peak_element,
    find_peak_in_mountain,
)
from algorithm_corpus.binary_search.search_range import (
    search_range,
)
from algorithm_corpus.binary_search.search_rotated import (
    find_min_rotated,
    search_rotated,
)

__all__ = [
    "binary_search",
    "binary_search_leftmost",
    "binary_search_rightmost",
    "find_min_rotated",
    "find_peak_element",
    "find_peak_in_mountain",
    "lower_bound",
    "search_range",
    "search_rotated",
    "upper_bound",
]
