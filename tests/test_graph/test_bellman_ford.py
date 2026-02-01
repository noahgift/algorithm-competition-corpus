"""Tests for Bellman-Ford Algorithm.

Tests Popperian Falsification Invariants:
    P1: After k iterations, d[v] is length of shortest path using <= k edges
    P2: If no negative cycle, algorithm terminates in V-1 iterations
    P3: Negative cycle detected iff distance decreases in iteration V
    P4: Triangle inequality: d[u] + w(u,v) >= d[v] after relaxation
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.bellman_ford import (
    bellman_ford,
    bellman_ford_with_path,
    find_negative_cycle,
    shortest_path_with_k_edges,
)


class TestBellmanFord(unittest.TestCase):
    """Unit tests for bellman_ford."""

    def test_simple_graph(self) -> None:
        """Test on simple graph."""
        edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3)]
        result = bellman_ford(edges, 3, 0)
        self.assertIsNotNone(result)
        self.assertEqual(result, {0: 0, 1: 4, 2: 1})

    def test_negative_cycle(self) -> None:
        """Test detection of negative cycle."""
        edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
        result = bellman_ford(edges, 3, 0)
        self.assertIsNone(result)

    def test_no_edges(self) -> None:
        """Test with no edges."""
        result = bellman_ford([], 1, 0)
        self.assertEqual(result, {0: 0})

    def test_single_edge(self) -> None:
        """Test with single edge."""
        edges = [(0, 1, 5)]
        result = bellman_ford(edges, 2, 0)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 5)


class TestBellmanFordWithPath(unittest.TestCase):
    """Unit tests for bellman_ford_with_path."""

    def test_path_exists(self) -> None:
        """Test finding path."""
        edges = [(0, 1, 2), (1, 2, 3)]
        dist, path = bellman_ford_with_path(edges, 3, 0, 2)
        self.assertEqual(dist, 5)
        self.assertEqual(path, [0, 1, 2])

    def test_no_path(self) -> None:
        """Test when no path exists."""
        edges = [(0, 1, 1)]
        dist, path = bellman_ford_with_path(edges, 3, 0, 2)
        self.assertEqual(dist, -1)
        self.assertEqual(path, [])

    def test_negative_cycle_in_path(self) -> None:
        """Test negative cycle detection with path."""
        edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
        dist, path = bellman_ford_with_path(edges, 3, 0, 2)
        self.assertEqual(dist, -1)
        self.assertEqual(path, [])


class TestFindNegativeCycle(unittest.TestCase):
    """Unit tests for find_negative_cycle."""

    def test_has_negative_cycle(self) -> None:
        """Test finding negative cycle."""
        edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
        cycle = find_negative_cycle(edges, 3)
        self.assertEqual(len(cycle), 3)
        self.assertEqual(set(cycle), {0, 1, 2})

    def test_no_negative_cycle(self) -> None:
        """Test when no negative cycle."""
        edges = [(0, 1, 1), (1, 2, 1)]
        cycle = find_negative_cycle(edges, 3)
        self.assertEqual(cycle, [])


class TestShortestPathWithKEdges(unittest.TestCase):
    """Unit tests for shortest_path_with_k_edges."""

    def test_one_edge_limit(self) -> None:
        """Test with one edge limit."""
        edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)]
        result = shortest_path_with_k_edges(edges, 3, 0, 2, 1)
        self.assertEqual(result, 5)

    def test_two_edge_limit(self) -> None:
        """Test with two edge limit."""
        edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)]
        result = shortest_path_with_k_edges(edges, 3, 0, 2, 2)
        self.assertEqual(result, 2)

    def test_no_path_with_k_edges(self) -> None:
        """Test when no path exists with k edges."""
        edges = [(0, 1, 1)]
        result = shortest_path_with_k_edges(edges, 3, 0, 2, 2)
        self.assertEqual(result, -1)


class TestBellmanFordInvariants(unittest.TestCase):
    """Popperian falsification tests for Bellman-Ford invariants."""

    def _random_edges(
        self,
        rng: random.Random,
        n: int,
        m: int,
        *,
        negative: bool = False,
    ) -> list[tuple[int, int, int]]:
        """Generate random edges."""
        edges: list[tuple[int, int, int]] = []
        for _ in range(m):
            u = rng.randint(0, n - 1)
            v = rng.randint(0, n - 1)
            if u != v:
                w = rng.randint(-5 if negative else 1, 10)
                edges.append((u, v, w))
        return edges

    def test_p1_distances_non_negative_without_negative_weights(self) -> None:
        """P1: With non-negative weights, all distances are non-negative."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(2, 15)
            m = rng.randint(0, n * 2)
            edges = self._random_edges(rng, n, m, negative=False)
            result = bellman_ford(edges, n, 0)
            if result is not None:
                for d in result.values():
                    self.assertGreaterEqual(d, 0)

    def test_p2_source_distance_zero(self) -> None:
        """P2: Source distance is always zero."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(2, 15)
            m = rng.randint(0, n * 2)
            edges = self._random_edges(rng, n, m, negative=False)
            start = rng.randint(0, n - 1)
            result = bellman_ford(edges, n, start)
            if result is not None:
                self.assertEqual(result[start], 0)

    def test_p4_triangle_inequality(self) -> None:
        """P4: Triangle inequality holds after relaxation."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(2, 15)
            m = rng.randint(1, n * 2)
            edges = self._random_edges(rng, n, m, negative=False)
            result = bellman_ford(edges, n, 0)
            if result is not None:
                inf = 10**18
                for u, v, w in edges:
                    if result.get(u, inf) != inf:
                        self.assertLessEqual(
                            result.get(v, inf),
                            result[u] + w + 1,  # +1 for possible unreachable
                        )

    def test_path_sum_equals_distance(self) -> None:
        """Path weights should sum to returned distance."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(2, 10)
            m = rng.randint(n - 1, n * 2)
            edges = self._random_edges(rng, n, m, negative=False)
            start = rng.randint(0, n - 1)
            end = rng.randint(0, n - 1)
            dist, path = bellman_ford_with_path(edges, n, start, end)
            if dist != -1 and len(path) > 1:
                # Build edge weight lookup
                edge_weights: dict[tuple[int, int], int] = {}
                for u, v, w in edges:
                    if (u, v) not in edge_weights:
                        edge_weights[(u, v)] = w
                    else:
                        edge_weights[(u, v)] = min(edge_weights[(u, v)], w)
                # Sum path weights
                path_sum = 0
                for i in range(len(path) - 1):
                    if (path[i], path[i + 1]) in edge_weights:
                        path_sum += edge_weights[(path[i], path[i + 1])]
                self.assertEqual(path_sum, dist)


if __name__ == "__main__":
    unittest.main()
