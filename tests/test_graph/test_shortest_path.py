"""Tests for Shortest Path algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.graph.shortest_path import (
    floyd_warshall,
    has_negative_cycle,
    shortest_path_unweighted,
)


class TestFloydWarshall(unittest.TestCase):
    """Unit tests for floyd_warshall."""

    def test_basic(self) -> None:
        """Test basic case."""
        graph = [
            [0, 5, float("inf"), 10],
            [float("inf"), 0, 3, float("inf")],
            [float("inf"), float("inf"), 0, 1],
            [float("inf"), float("inf"), float("inf"), 0],
        ]
        result = floyd_warshall(graph)
        self.assertEqual(result[0][2], 8)
        self.assertEqual(result[0][3], 9)


class TestShortestPathUnweighted(unittest.TestCase):
    """Unit tests for shortest_path_unweighted."""

    def test_basic(self) -> None:
        """Test basic case."""
        graph = {0: [1, 2], 1: [2], 2: [3], 3: []}
        self.assertEqual(shortest_path_unweighted(graph, 0, 3), 2)

    def test_same_node(self) -> None:
        """Test same node."""
        self.assertEqual(shortest_path_unweighted({0: []}, 0, 0), 0)


class TestHasNegativeCycle(unittest.TestCase):
    """Unit tests for has_negative_cycle."""

    def test_has_cycle(self) -> None:
        """Test with negative cycle."""
        graph = [[(1, 1)], [(2, -2)], [(0, -1)]]
        self.assertTrue(has_negative_cycle(graph))

    def test_no_cycle(self) -> None:
        """Test without negative cycle."""
        graph = [[(1, 1)], [(2, 2)], []]
        self.assertFalse(has_negative_cycle(graph))


if __name__ == "__main__":
    unittest.main()
