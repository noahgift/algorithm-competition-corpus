"""Backtracking algorithms.

Systematic exploration of solution spaces with pruning.
"""

from __future__ import annotations

from algorithm_corpus.backtracking.n_queens import (
    n_queens,
    n_queens_count,
)
from algorithm_corpus.backtracking.permutations import (
    permutations,
    permutations_unique,
)
from algorithm_corpus.backtracking.subsets import (
    combinations,
    subsets,
)

__all__: list[str] = [
    "combinations",
    "n_queens",
    "n_queens_count",
    "permutations",
    "permutations_unique",
    "subsets",
]
