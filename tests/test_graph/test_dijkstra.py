"""Tests for Dijkstra's Algorithm.

Implements Popperian falsification through invariant property testing.
Each test attempts to DISPROVE the algorithm's correctness.

Test Categories:
    1. Invariant Properties (P1-P4): Could falsify the algorithm
    2. Boundary Conditions: Empty, single-node, disconnected graphs
    3. Correctness Verification: Known solutions
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.dijkstra import (
    dijkstra,
    dijkstra_k_shortest,
    dijkstra_with_path,
)


class TestDijkstraInvariants(unittest.TestCase):
    """Popperian falsification tests for Dijkstra invariants.

    These tests attempt to DISPROVE the algorithm by checking
    mathematical invariants that must hold for correctness.
    """

    def test_p1_distances_non_negative(self) -> None:
        """P1: All computed distances must be non-negative.

        Falsification: If any d[v] < 0, the algorithm is incorrect.
        """
        rng = random.Random(42)
        for _ in range(100):
            n = rng.randint(1, 20)
            graph = self._random_graph(rng, n, density=0.3)
            if graph:
                source = rng.choice(list(graph.keys()))
                distances = dijkstra(graph, source)
                for v, d in distances.items():
                    self.assertGreaterEqual(
                        d,
                        0,
                        f"Invariant P1 violated: d[{v}] = {d} < 0",
                    )

    def test_p2_triangle_inequality(self) -> None:
        """P2: Triangle inequality must hold for all edges.

        For every edge (u, v) with weight w: d[u] + w >= d[v]

        Falsification: If d[u] + w < d[v] for any edge, algorithm failed.
        """
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: [],
        }
        distances = dijkstra(graph, 0)

        for u, edges in graph.items():
            if u not in distances:
                continue
            for v, weight in edges:
                if v in distances:
                    self.assertGreaterEqual(
                        distances[u] + weight,
                        distances[v],
                        f"Triangle inequality violated: d[{u}] + w({u},{v}) < d[{v}]",
                    )

    def test_p3_source_distance_zero(self) -> None:
        """P3: Distance from source to itself must be zero.

        Falsification: If d[source] != 0, algorithm is incorrect.
        """
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 10)
            graph = self._random_graph(rng, n, density=0.5)
            if graph:
                source = rng.choice(list(graph.keys()))
                distances = dijkstra(graph, source)
                self.assertEqual(
                    distances[source],
                    0,
                    f"Invariant P3 violated: d[source] = {distances[source]} != 0",
                )

    def test_p4_optimal_substructure(self) -> None:
        """P4: Shortest paths have optimal substructure.

        If path P = (s, ..., u, v) is shortest s->v,
        then (s, ..., u) is shortest s->u.
        """
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2), (3, 6)],
            2: [(3, 3)],
            3: [],
        }
        distances = dijkstra(graph, 0)

        # Path 0->1->2 = 1+2 = 3 should be optimal
        self.assertEqual(distances[2], 3)
        # Path 0->1->2->3 = 1+2+3 = 6 should be optimal
        self.assertEqual(distances[3], 6)

    @staticmethod
    def _random_graph(
        rng: random.Random,
        n: int,
        density: float = 0.3,
    ) -> dict[int, list[tuple[int, int]]]:
        """Generate a random weighted graph for property testing."""
        graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < density:
                    weight = rng.randint(1, 100)
                    graph[u].append((v, weight))
        return graph


class TestDijkstraBoundaryConditions(unittest.TestCase):
    """Boundary condition tests for edge cases."""

    def test_single_node(self) -> None:
        """Single node graph returns only source."""
        result = dijkstra({0: []}, 0)
        self.assertEqual(result, {0: 0})

    def test_disconnected_graph(self) -> None:
        """Unreachable vertices should not appear in result."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1)],
            1: [],
            2: [(3, 1)],
            3: [],
        }
        result = dijkstra(graph, 0)
        self.assertIn(0, result)
        self.assertIn(1, result)
        self.assertNotIn(2, result)
        self.assertNotIn(3, result)

    def test_linear_path(self) -> None:
        """Linear graph should have cumulative distances."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1)],
            1: [(2, 2)],
            2: [(3, 3)],
            3: [],
        }
        result = dijkstra(graph, 0)
        self.assertEqual(result, {0: 0, 1: 1, 2: 3, 3: 6})


class TestDijkstraCorrectness(unittest.TestCase):
    """Correctness tests against known solutions."""

    def test_clrs_example(self) -> None:
        """Test against CLRS textbook example."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 10), (3, 5)],
            1: [(2, 1), (3, 2)],
            2: [(4, 4)],
            3: [(1, 3), (2, 9), (4, 2)],
            4: [(0, 7), (2, 6)],
        }
        expected = {0: 0, 1: 8, 2: 9, 3: 5, 4: 7}
        result = dijkstra(graph, 0)
        self.assertEqual(result, expected)


class TestDijkstraWithPath(unittest.TestCase):
    """Tests for path reconstruction."""

    def test_path_exists(self) -> None:
        """Should return valid path when one exists."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2)],
            2: [],
        }
        dist, path = dijkstra_with_path(graph, 0, 2)
        self.assertEqual(dist, 3)
        self.assertEqual(path, [0, 1, 2])

    def test_path_not_exists(self) -> None:
        """Should return -1 when no path exists."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [],
            1: [],
        }
        dist, path = dijkstra_with_path(graph, 0, 1)
        self.assertEqual(dist, -1)
        self.assertEqual(path, [])

    def test_same_start_end(self) -> None:
        """Should handle start == end case."""
        graph: dict[int, list[tuple[int, int]]] = {0: [(1, 5)], 1: []}
        dist, path = dijkstra_with_path(graph, 0, 0)
        self.assertEqual(dist, 0)
        self.assertEqual(path, [0])


class TestDijkstraKShortest(unittest.TestCase):
    """Tests for k-shortest paths."""

    def test_k_shortest_basic(self) -> None:
        """Should find multiple shortest paths."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1), (2, 2)],
            1: [(2, 1)],
            2: [],
        }
        result = dijkstra_k_shortest(graph, 0, 2, 2)
        self.assertEqual(sorted(result), [2, 2])

    def test_k_greater_than_paths(self) -> None:
        """Should return fewer than k if not enough paths."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1)],
            1: [],
        }
        result = dijkstra_k_shortest(graph, 0, 1, 3)
        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main()
