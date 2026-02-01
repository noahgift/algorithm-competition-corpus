"""Tests for Heap Operations.

Tests Popperian Falsification Invariants:
    P1: Heap property maintained after operations
    P2: heap_pop returns minimum element
    P3: heap_push adds element correctly
    P4: heapify creates valid heap from array
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.heap.heap_ops import (
    heap_pop,
    heap_push,
    heapify,
)


def _is_min_heap(arr: list[int]) -> bool:
    """Check if array satisfies min-heap property."""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True


class TestHeapify(unittest.TestCase):
    """Unit tests for heapify."""

    def test_basic(self) -> None:
        """Test basic heapify."""
        h = heapify([3, 1, 4, 1, 5, 9])
        self.assertEqual(h[0], 1)  # Min at root

    def test_empty(self) -> None:
        """Test empty array."""
        self.assertEqual(heapify([]), [])

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(heapify([1]), [1])


class TestHeapPush(unittest.TestCase):
    """Unit tests for heap_push."""

    def test_push(self) -> None:
        """Test pushing to heap."""
        h = [1, 3, 5]
        heap_push(h, 2)
        self.assertEqual(h[0], 1)

    def test_push_to_empty(self) -> None:
        """Test pushing to empty heap."""
        h: list[int] = []
        heap_push(h, 5)
        self.assertEqual(h, [5])


class TestHeapPop(unittest.TestCase):
    """Unit tests for heap_pop."""

    def test_pop(self) -> None:
        """Test popping from heap."""
        h = [1, 3, 5]
        self.assertEqual(heap_pop(h), 1)
        self.assertEqual(h, [3, 5])

    def test_pop_single(self) -> None:
        """Test popping single element."""
        h = [5]
        self.assertEqual(heap_pop(h), 5)
        self.assertEqual(h, [])


class TestHeapOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for heap ops invariants."""

    def test_p1_heap_property_after_heapify(self) -> None:
        """P1: Heap property maintained after heapify."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(0, 100) for _ in range(rng.randint(1, 30))]
            h = heapify(arr[:])
            self.assertTrue(_is_min_heap(h))

    def test_p1_heap_property_after_push(self) -> None:
        """P1: Heap property maintained after push."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(0, 100) for _ in range(rng.randint(1, 20))]
            h = heapify(arr[:])
            heap_push(h, rng.randint(0, 100))
            self.assertTrue(_is_min_heap(h))

    def test_p2_pop_returns_minimum(self) -> None:
        """P2: heap_pop returns minimum element."""
        rng = random.Random(42)
        for _ in range(30):
            arr = [rng.randint(0, 100) for _ in range(rng.randint(1, 20))]
            h = heapify(arr[:])
            expected_min = min(h)
            self.assertEqual(heap_pop(h), expected_min)

    def test_p4_heapify_valid(self) -> None:
        """P4: heapify creates valid heap from array."""
        test_cases = [[5, 3, 8, 1, 2], [10, 9, 8, 7, 6], [1, 2, 3, 4, 5]]
        for arr in test_cases:
            h = heapify(arr[:])
            self.assertTrue(_is_min_heap(h))
            self.assertEqual(sorted(h), sorted(arr))


if __name__ == "__main__":
    unittest.main()
