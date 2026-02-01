"""Greedy algorithms.

Algorithms that make locally optimal choices at each step.
"""

from __future__ import annotations

from algorithm_corpus.greedy.activity_selection import (
    activity_selection,
    max_activities,
)
from algorithm_corpus.greedy.coin_greedy import (
    coin_change_greedy,
)
from algorithm_corpus.greedy.interval_scheduling import (
    merge_intervals,
    min_meeting_rooms,
)

__all__: list[str] = [
    "activity_selection",
    "coin_change_greedy",
    "max_activities",
    "merge_intervals",
    "min_meeting_rooms",
]
