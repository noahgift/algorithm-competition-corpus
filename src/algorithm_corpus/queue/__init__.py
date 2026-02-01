"""Queue-based algorithms.

Algorithms using queue and deque data structures.
"""

from __future__ import annotations

from algorithm_corpus.queue.queue_reconstruction import (
    reconstruct_queue,
)
from algorithm_corpus.queue.sliding_max import (
    max_sliding_window,
    min_sliding_window,
)

__all__: list[str] = [
    "max_sliding_window",
    "min_sliding_window",
    "reconstruct_queue",
]
