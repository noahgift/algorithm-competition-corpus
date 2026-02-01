"""Queue reconstruction algorithm.

Reconstruct queue based on height and count constraints.
"""

from __future__ import annotations


def reconstruct_queue(people: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Reconstruct queue from height and count pairs.

    Each person is (height, count) where count is number of
    people in front with height >= person's height.

    Greedy approach: sort by height descending, then by count ascending.
    Insert each person at their count index.

    Args:
        people: List of (height, count) tuples.

    Returns:
        Reconstructed queue.

    Example:
        >>> reconstruct_queue([(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)])
        [(5, 0), (7, 0), (5, 2), (6, 1), (4, 4), (7, 1)]
    """
    # Sort by height descending, then count ascending
    sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))

    result: list[tuple[int, int]] = []
    for person in sorted_people:
        # Insert at index equal to count
        result.insert(person[1], person)

    return result
