"""Tests for BFS Shortest Path algorithms.

Tests Popperian Falsification Invariants:
    P1: All distances are non-negative integers
    P2: Distance to source is zero: d[source] = 0
    P3: For any edge (u,v): |d[u] - d[v]| <= 1
    P4: Distances represent shortest unweighted paths
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.bfs import (
    bfs_level_order,
    bfs_path,
    bfs_shortest_path,
)


class TestBfsShortestPath(unittest.TestCase):
    """Unit tests for bfs_shortest_path."""

    def test_simple_graph(self) -> None:
        """Test BFS on a simple connected graph."""
        graph = {0: [1, 2], 1: [2], 2: []}
        result = bfs_shortest_path(graph, 0)
        self.assertEqual(result, {0: 0, 1: 1, 2: 1})

    def test_single_node(self) -> None:
        """Test BFS on a single node graph."""
        graph = {0: []}
        result = bfs_shortest_path(graph, 0)
        self.assertEqual(result, {0: 0})

    def test_linear_graph(self) -> None:
        """Test BFS on a linear graph."""
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        result = bfs_shortest_path(graph, 0)
        self.assertEqual(result, {0: 0, 1: 1, 2: 2, 3: 3})

    def test_disconnected_nodes(self) -> None:
        """Test BFS doesn't reach disconnected nodes."""
        graph = {0: [1], 1: [], 2: []}
        result = bfs_shortest_path(graph, 0)
        self.assertNotIn(2, result)


class TestBfsPath(unittest.TestCase):
    """Unit tests for bfs_path."""

    def test_path_exists(self) -> None:
        """Test finding path when one exists."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = bfs_path(graph, 0, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 3)

    def test_same_start_end(self) -> None:
        """Test path when start equals end."""
        graph = {0: [1], 1: []}
        result = bfs_path(graph, 0, 0)
        self.assertEqual(result, [0])

    def test_no_path(self) -> None:
        """Test when no path exists."""
        graph = {0: [], 1: []}
        result = bfs_path(graph, 0, 1)
        self.assertIsNone(result)

    def test_path_is_shortest(self) -> None:
        """Test that returned path is shortest."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = bfs_path(graph, 0, 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)  # 0 -> 1 -> 3 or 0 -> 2 -> 3


class TestBfsLevelOrder(unittest.TestCase):
    """Unit tests for bfs_level_order."""

    def test_level_order(self) -> None:
        """Test level order traversal."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = bfs_level_order(graph, 0)
        self.assertEqual(result[0], [0])
        self.assertEqual(sorted(result[1]), [1, 2])
        self.assertEqual(result[2], [3])

    def test_single_node_level(self) -> None:
        """Test level order with single node."""
        graph = {0: []}
        result = bfs_level_order(graph, 0)
        self.assertEqual(result, [[0]])

    def test_linear_levels(self) -> None:
        """Test level order with linear graph."""
        graph = {0: [1], 1: [2], 2: []}
        result = bfs_level_order(graph, 0)
        self.assertEqual(result, [[0], [1], [2]])


class TestBfsInvariants(unittest.TestCase):
    """Popperian falsification tests for BFS invariants."""

    def _random_graph(
        self, rng: random.Random, n: int, density: float
    ) -> dict[int, list[int]]:
        """Generate a random graph."""
        graph: dict[int, list[int]] = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j and rng.random() < density:
                    graph[i].append(j)
        return graph

    def test_p1_distances_non_negative(self) -> None:
        """P1: All distances must be non-negative integers."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_graph(rng, n, density=0.3)
            source = rng.randint(0, n - 1)
            distances = bfs_shortest_path(graph, source)
            for v, d in distances.items():
                self.assertGreaterEqual(d, 0, f"Distance to {v} should be >= 0")
                self.assertIsInstance(d, int, f"Distance to {v} should be int")

    def test_p2_source_distance_zero(self) -> None:
        """P2: Distance to source must be zero."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_graph(rng, n, density=0.3)
            source = rng.randint(0, n - 1)
            distances = bfs_shortest_path(graph, source)
            self.assertEqual(distances[source], 0, "Source distance must be 0")

    def test_p3_edge_distance_relaxation(self) -> None:
        """P3: For any edge (u,v), d[v] <= d[u] + 1 (relaxation property)."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 15)
            graph = self._random_graph(rng, n, density=0.4)
            source = rng.randint(0, n - 1)
            distances = bfs_shortest_path(graph, source)
            for u, neighbors in graph.items():
                if u not in distances:
                    continue
                for v in neighbors:
                    if v in distances:
                        # If we can reach v from u, d[v] <= d[u] + 1
                        self.assertLessEqual(
                            distances[v],
                            distances[u] + 1,
                            f"Edge ({u},{v}) violates relaxation property",
                        )

    def test_p4_path_validity(self) -> None:
        """P4: Returned path must be valid and shortest."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 15)
            graph = self._random_graph(rng, n, density=0.3)
            source = rng.randint(0, n - 1)
            target = rng.randint(0, n - 1)
            path = bfs_path(graph, source, target)
            distances = bfs_shortest_path(graph, source)
            if path is not None:
                self.assertEqual(path[0], source)
                self.assertEqual(path[-1], target)
                # Verify path length matches distance
                if target in distances:
                    self.assertEqual(len(path) - 1, distances[target])
                # Verify each step is valid edge
                for i in range(len(path) - 1):
                    self.assertIn(path[i + 1], graph.get(path[i], []))


if __name__ == "__main__":
    unittest.main()
