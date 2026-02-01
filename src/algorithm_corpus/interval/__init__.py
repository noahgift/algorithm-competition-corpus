"""Interval algorithms.

Algorithms for interval manipulation and scheduling.
"""

from __future__ import annotations

from algorithm_corpus.interval.interval_ops import (
    insert_interval,
    interval_intersection,
    merge_overlapping,
)
from algorithm_corpus.interval.interval_scheduling import (
    can_attend,
    min_arrows,
)

__all__: list[str] = [
    "can_attend",
    "insert_interval",
    "interval_intersection",
    "merge_overlapping",
    "min_arrows",
]
