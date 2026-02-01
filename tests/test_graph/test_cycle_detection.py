"""Tests for Cycle Detection algorithms.

Tests Popperian Falsification Invariants:
    P1: If cycle detected, returned nodes form an actual cycle
    P2: If no cycle detected, graph is acyclic
    P3: For undirected: back edge to non-parent indicates cycle
    P4: For directed: back edge (gray -> gray) indicates cycle
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.cycle_detection import (
    find_cycle_directed,
    has_cycle_directed,
    has_cycle_undirected,
)


class TestHasCycleUndirected(unittest.TestCase):
    """Unit tests for has_cycle_undirected."""

    def test_no_cycle_linear(self) -> None:
        """Test linear graph has no cycle."""
        graph = {0: [1], 1: [0, 2], 2: [1]}
        self.assertFalse(has_cycle_undirected(graph, [0, 1, 2]))

    def test_has_cycle_triangle(self) -> None:
        """Test triangle has cycle."""
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
        self.assertTrue(has_cycle_undirected(graph, [0, 1, 2]))

    def test_single_node(self) -> None:
        """Test single node has no cycle."""
        graph = {0: []}
        self.assertFalse(has_cycle_undirected(graph, [0]))

    def test_disconnected_with_cycle(self) -> None:
        """Test disconnected graph with cycle in one component."""
        graph = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
        self.assertTrue(has_cycle_undirected(graph, [0, 1, 2, 3, 4]))


class TestHasCycleDirected(unittest.TestCase):
    """Unit tests for has_cycle_directed."""

    def test_no_cycle_dag(self) -> None:
        """Test DAG has no cycle."""
        graph = {0: [1], 1: [2], 2: []}
        self.assertFalse(has_cycle_directed(graph, [0, 1, 2]))

    def test_has_cycle(self) -> None:
        """Test graph with cycle."""
        graph = {0: [1], 1: [2], 2: [0]}
        self.assertTrue(has_cycle_directed(graph, [0, 1, 2]))

    def test_single_node(self) -> None:
        """Test single node has no cycle."""
        graph = {0: []}
        self.assertFalse(has_cycle_directed(graph, [0]))

    def test_self_loop(self) -> None:
        """Test self-loop is detected as cycle."""
        graph = {0: [0]}
        self.assertTrue(has_cycle_directed(graph, [0]))


class TestFindCycleDirected(unittest.TestCase):
    """Unit tests for find_cycle_directed."""

    def test_find_cycle(self) -> None:
        """Test finding a cycle."""
        graph = {0: [1], 1: [2], 2: [0]}
        cycle = find_cycle_directed(graph, [0, 1, 2])
        self.assertEqual(len(cycle), 3)
        self.assertEqual(set(cycle), {0, 1, 2})

    def test_no_cycle(self) -> None:
        """Test when no cycle exists."""
        graph = {0: [1], 1: []}
        cycle = find_cycle_directed(graph, [0, 1])
        self.assertEqual(cycle, [])

    def test_cycle_in_larger_graph(self) -> None:
        """Test finding cycle in larger graph."""
        graph = {0: [1], 1: [2], 2: [3], 3: [1], 4: []}
        cycle = find_cycle_directed(graph, [0, 1, 2, 3, 4])
        # Cycle should be 1 -> 2 -> 3 -> 1
        self.assertGreater(len(cycle), 0)
        self.assertTrue(set(cycle).issubset({1, 2, 3}))


class TestCycleDetectionInvariants(unittest.TestCase):
    """Popperian falsification tests for cycle detection invariants."""

    def _random_undirected_graph(
        self, rng: random.Random, n: int, density: float
    ) -> dict[int, list[int]]:
        """Generate a random undirected graph."""
        graph: dict[int, list[int]] = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < density:
                    graph[i].append(j)
                    graph[j].append(i)
        return graph

    def _random_directed_graph(
        self, rng: random.Random, n: int, density: float
    ) -> dict[int, list[int]]:
        """Generate a random directed graph."""
        graph: dict[int, list[int]] = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j and rng.random() < density:
                    graph[i].append(j)
        return graph

    def _is_valid_cycle_directed(
        self, graph: dict[int, list[int]], cycle: list[int]
    ) -> bool:
        """Check if cycle is valid (each node connects to next)."""
        if len(cycle) < 2:
            return False
        for i in range(len(cycle)):
            curr = cycle[i]
            next_node = cycle[(i + 1) % len(cycle)]
            if next_node not in graph.get(curr, []):
                return False
        return True

    def test_p1_cycle_validity(self) -> None:
        """P1: If cycle detected, returned nodes form an actual cycle."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 15)
            graph = self._random_directed_graph(rng, n, density=0.3)
            nodes = list(range(n))
            cycle = find_cycle_directed(graph, nodes)
            if cycle:
                self.assertTrue(
                    self._is_valid_cycle_directed(graph, cycle),
                    f"Invalid cycle: {cycle}",
                )

    def test_p2_no_cycle_means_acyclic(self) -> None:
        """P2: If no cycle detected, graph is acyclic."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            # Generate a DAG (guaranteed acyclic)
            graph: dict[int, list[int]] = {i: [] for i in range(n)}
            for i in range(n):
                for j in range(i + 1, n):
                    if rng.random() < 0.3:
                        graph[i].append(j)
            nodes = list(range(n))
            self.assertFalse(has_cycle_directed(graph, nodes))
            self.assertEqual(find_cycle_directed(graph, nodes), [])

    def test_p3_undirected_consistency(self) -> None:
        """P3: Undirected cycle detection is consistent with theory."""
        # Tree should have no cycle
        tree = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
        self.assertFalse(has_cycle_undirected(tree, [0, 1, 2, 3]))
        # Add one edge to create cycle
        tree[2].append(3)
        tree[3].append(2)
        self.assertTrue(has_cycle_undirected(tree, [0, 1, 2, 3]))

    def test_p4_directed_vs_undirected(self) -> None:
        """P4: Directed cycles require correct edge direction."""
        # Undirected path 0 - 1 - 2 with directed edges
        # 0 -> 1 -> 2 (no cycle)
        graph_no_cycle = {0: [1], 1: [2], 2: []}
        self.assertFalse(has_cycle_directed(graph_no_cycle, [0, 1, 2]))
        # Add back edge to create cycle: 0 -> 1 -> 2 -> 0
        graph_with_cycle = {0: [1], 1: [2], 2: [0]}
        self.assertTrue(has_cycle_directed(graph_with_cycle, [0, 1, 2]))

    def test_consistency_between_has_and_find(self) -> None:
        """has_cycle and find_cycle should agree."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_directed_graph(rng, n, density=0.3)
            nodes = list(range(n))
            has_cycle = has_cycle_directed(graph, nodes)
            cycle = find_cycle_directed(graph, nodes)
            self.assertEqual(has_cycle, len(cycle) > 0)


if __name__ == "__main__":
    unittest.main()
