"""Tests for Topological Sort algorithms.

Tests Popperian Falsification Invariants:
    P1: For every edge (u,v), u appears before v in the ordering
    P2: Result contains all nodes iff graph is a DAG
    P3: Result is None iff graph contains a cycle
    P4: All nodes appear exactly once in the result
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.topological_sort import (
    all_topological_sorts,
    topological_sort_dfs,
    topological_sort_kahn,
)


class TestTopologicalSortKahn(unittest.TestCase):
    """Unit tests for topological_sort_kahn."""

    def test_simple_dag(self) -> None:
        """Test on simple DAG."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort_kahn(graph, [0, 1, 2, 3])
        self.assertIsNotNone(result)
        self.assertEqual(result, [0, 1, 2, 3])

    def test_cycle_detection(self) -> None:
        """Test cycle detection."""
        graph = {0: [1], 1: [0]}
        result = topological_sort_kahn(graph, [0, 1])
        self.assertIsNone(result)

    def test_single_node(self) -> None:
        """Test single node."""
        graph = {0: []}
        result = topological_sort_kahn(graph, [0])
        self.assertEqual(result, [0])

    def test_disconnected_dag(self) -> None:
        """Test disconnected DAG."""
        graph = {0: [1], 1: [], 2: [3], 3: []}
        result = topological_sort_kahn(graph, [0, 1, 2, 3])
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)


class TestTopologicalSortDfs(unittest.TestCase):
    """Unit tests for topological_sort_dfs."""

    def test_simple_dag(self) -> None:
        """Test on simple DAG."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort_dfs(graph, [0, 1, 2, 3])
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 3)

    def test_cycle_detection(self) -> None:
        """Test cycle detection."""
        graph = {0: [1], 1: [0]}
        result = topological_sort_dfs(graph, [0, 1])
        self.assertIsNone(result)

    def test_single_node(self) -> None:
        """Test single node."""
        graph = {0: []}
        result = topological_sort_dfs(graph, [0])
        self.assertEqual(result, [0])


class TestAllTopologicalSorts(unittest.TestCase):
    """Unit tests for all_topological_sorts."""

    def test_multiple_orderings(self) -> None:
        """Test finding all orderings."""
        graph = {0: [2], 1: [2], 2: []}
        result = all_topological_sorts(graph, [0, 1, 2])
        self.assertEqual(len(result), 2)
        sorted_result = sorted(result)
        self.assertEqual(sorted_result, [[0, 1, 2], [1, 0, 2]])

    def test_single_ordering(self) -> None:
        """Test graph with single ordering."""
        graph = {0: [1], 1: [2], 2: []}
        result = all_topological_sorts(graph, [0, 1, 2])
        self.assertEqual(result, [[0, 1, 2]])

    def test_single_node(self) -> None:
        """Test single node."""
        graph = {0: []}
        result = all_topological_sorts(graph, [0])
        self.assertEqual(result, [[0]])


class TestTopologicalSortInvariants(unittest.TestCase):
    """Popperian falsification tests for topological sort invariants."""

    def _random_dag(
        self, rng: random.Random, n: int, density: float
    ) -> dict[int, list[int]]:
        """Generate a random DAG (edges only go from lower to higher indices)."""
        graph: dict[int, list[int]] = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < density:
                    graph[i].append(j)
        return graph

    def _has_cycle(self, graph: dict[int, list[int]], nodes: list[int]) -> bool:
        """Check if graph has a cycle using DFS."""
        white, gray, black = 0, 1, 2
        color = dict.fromkeys(nodes, white)
        for start in nodes:
            if color[start] != white:
                continue
            stack = [(start, False)]
            while stack:
                node, processed = stack.pop()
                if processed:
                    color[node] = black
                    continue
                if color[node] == gray:
                    return True
                if color[node] == black:
                    continue
                color[node] = gray
                stack.append((node, True))
                for neighbor in graph.get(node, []):
                    if color.get(neighbor, white) == gray:
                        return True
                    if color.get(neighbor, white) == white:
                        stack.append((neighbor, False))
        return False

    def test_p1_edge_ordering(self) -> None:
        """P1: For every edge (u,v), u appears before v in the ordering."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_dag(rng, n, density=0.3)
            nodes = list(range(n))
            result = topological_sort_kahn(graph, nodes)
            if result is not None:
                pos = {node: i for i, node in enumerate(result)}
                for u in nodes:
                    for v in graph.get(u, []):
                        self.assertLess(
                            pos[u], pos[v], f"Edge ({u},{v}) violates ordering"
                        )

    def test_p2_result_contains_all_nodes(self) -> None:
        """P2: Result contains all nodes iff graph is a DAG."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_dag(rng, n, density=0.3)
            nodes = list(range(n))
            result = topological_sort_kahn(graph, nodes)
            # Since we generate DAGs, result should always be valid
            self.assertIsNotNone(result)
            self.assertEqual(len(result), n)
            self.assertEqual(set(result), set(nodes))

    def test_p3_cycle_implies_none(self) -> None:
        """P3: Result is None iff graph contains a cycle."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(2, 10)
            # Create graph with potential cycles
            graph: dict[int, list[int]] = {i: [] for i in range(n)}
            for _ in range(n):
                u, v = rng.randint(0, n - 1), rng.randint(0, n - 1)
                if u != v:
                    graph[u].append(v)
            nodes = list(range(n))
            result_kahn = topological_sort_kahn(graph, nodes)
            result_dfs = topological_sort_dfs(graph, nodes)
            has_cycle = self._has_cycle(graph, nodes)
            if has_cycle:
                self.assertIsNone(result_kahn)
                self.assertIsNone(result_dfs)
            else:
                self.assertIsNotNone(result_kahn)
                self.assertIsNotNone(result_dfs)

    def test_p4_no_duplicates(self) -> None:
        """P4: All nodes appear exactly once in the result."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_dag(rng, n, density=0.3)
            nodes = list(range(n))
            result = topological_sort_kahn(graph, nodes)
            if result is not None:
                self.assertEqual(len(result), len(set(result)))

    def test_kahn_dfs_consistency(self) -> None:
        """Both algorithms should agree on cycle detection."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 10)
            graph = self._random_dag(rng, n, density=0.3)
            nodes = list(range(n))
            result_kahn = topological_sort_kahn(graph, nodes)
            result_dfs = topological_sort_dfs(graph, nodes)
            # Both should succeed or fail together
            self.assertEqual(result_kahn is None, result_dfs is None)


if __name__ == "__main__":
    unittest.main()
