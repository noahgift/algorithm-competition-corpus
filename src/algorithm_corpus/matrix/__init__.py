"""Matrix algorithms.

2D array manipulation and search algorithms.
"""

from __future__ import annotations

from algorithm_corpus.matrix.matrix_ops import (
    rotate_90,
    spiral_order,
    transpose,
)
from algorithm_corpus.matrix.matrix_search import (
    search_matrix,
    search_matrix_2d,
)

__all__: list[str] = [
    "rotate_90",
    "search_matrix",
    "search_matrix_2d",
    "spiral_order",
    "transpose",
]
