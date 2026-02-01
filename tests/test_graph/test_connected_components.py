"""Tests for Connected Components algorithms.

Tests Popperian Falsification Invariants:
    P1: Components partition all nodes (each node in exactly one component)
    P2: All nodes in a component are mutually reachable
    P3: No edge exists between different SCCs in condensation graph order
    P4: Number of components <= number of nodes
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.connected_components import (
    find_connected_components,
    find_connected_components_bfs,
    kosaraju_scc,
    tarjan_scc,
)


class TestFindConnectedComponents(unittest.TestCase):
    """Unit tests for find_connected_components."""

    def test_two_components(self) -> None:
        """Test finding two components."""
        graph = {0: [1], 1: [0], 2: [3], 3: [2]}
        result = find_connected_components(graph, [0, 1, 2, 3])
        self.assertEqual(len(result), 2)
        components_sorted = sorted([sorted(c) for c in result])
        self.assertEqual(components_sorted, [[0, 1], [2, 3]])

    def test_single_component(self) -> None:
        """Test single component."""
        graph = {0: [1, 2], 1: [0], 2: [0]}
        result = find_connected_components(graph, [0, 1, 2])
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), [0, 1, 2])

    def test_isolated_nodes(self) -> None:
        """Test isolated nodes."""
        graph = {0: [], 1: [], 2: []}
        result = find_connected_components(graph, [0, 1, 2])
        self.assertEqual(len(result), 3)


class TestFindConnectedComponentsBfs(unittest.TestCase):
    """Unit tests for find_connected_components_bfs."""

    def test_two_components_bfs(self) -> None:
        """Test finding two components with BFS."""
        graph = {0: [1], 1: [0], 2: []}
        result = find_connected_components_bfs(graph, [0, 1, 2])
        self.assertEqual(len(result), 2)
        components_sorted = sorted([sorted(c) for c in result])
        self.assertEqual(components_sorted, [[0, 1], [2]])

    def test_single_node(self) -> None:
        """Test single node."""
        graph = {0: []}
        result = find_connected_components_bfs(graph, [0])
        self.assertEqual(result, [[0]])


class TestKosarajuScc(unittest.TestCase):
    """Unit tests for kosaraju_scc."""

    def test_find_sccs(self) -> None:
        """Test finding SCCs."""
        graph = {0: [1], 1: [2], 2: [0], 3: [2]}
        result = kosaraju_scc(graph, [0, 1, 2, 3])
        self.assertEqual(len(result), 2)
        components_sorted = sorted([sorted(c) for c in result])
        self.assertEqual(components_sorted, [[0, 1, 2], [3]])

    def test_single_node_scc(self) -> None:
        """Test single node SCC."""
        graph = {0: []}
        result = kosaraju_scc(graph, [0])
        self.assertEqual(result, [[0]])

    def test_all_separate_sccs(self) -> None:
        """Test when all nodes are separate SCCs."""
        graph = {0: [1], 1: [2], 2: []}
        result = kosaraju_scc(graph, [0, 1, 2])
        self.assertEqual(len(result), 3)


class TestTarjanScc(unittest.TestCase):
    """Unit tests for tarjan_scc."""

    def test_find_sccs(self) -> None:
        """Test finding SCCs."""
        graph = {0: [1], 1: [2], 2: [0, 3], 3: []}
        result = tarjan_scc(graph, [0, 1, 2, 3])
        self.assertEqual(len(result), 2)
        components_sorted = sorted([sorted(c) for c in result])
        self.assertEqual(components_sorted, [[0, 1, 2], [3]])

    def test_single_node(self) -> None:
        """Test single node."""
        graph = {0: []}
        result = tarjan_scc(graph, [0])
        self.assertEqual(result, [[0]])


class TestConnectedComponentsInvariants(unittest.TestCase):
    """Popperian falsification tests for connected components invariants."""

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

    def test_p1_partition_property(self) -> None:
        """P1: Components partition all nodes."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_undirected_graph(rng, n, density=0.2)
            nodes = list(range(n))
            components = find_connected_components(graph, nodes)
            # All nodes covered
            all_nodes = set()
            for comp in components:
                all_nodes.update(comp)
            self.assertEqual(all_nodes, set(nodes))
            # No overlap
            total = sum(len(c) for c in components)
            self.assertEqual(total, n)

    def test_p2_mutual_reachability(self) -> None:
        """P2: All nodes in a component are mutually reachable."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(1, 15)
            graph = self._random_undirected_graph(rng, n, density=0.3)
            nodes = list(range(n))
            components = find_connected_components(graph, nodes)
            for comp in components:
                if len(comp) <= 1:
                    continue
                # Check that all nodes in component are reachable from each other
                for start in comp:
                    visited: set[int] = set()
                    stack = [start]
                    while stack:
                        curr = stack.pop()
                        if curr in visited:
                            continue
                        visited.add(curr)
                        stack.extend(nb for nb in graph.get(curr, []) if nb in comp)
                    self.assertEqual(visited, set(comp))

    def test_p4_component_count_bound(self) -> None:
        """P4: Number of components <= number of nodes."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_undirected_graph(rng, n, density=0.2)
            nodes = list(range(n))
            components = find_connected_components(graph, nodes)
            self.assertLessEqual(len(components), n)

    def test_dfs_bfs_consistency(self) -> None:
        """DFS and BFS should find same components."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_undirected_graph(rng, n, density=0.3)
            nodes = list(range(n))
            dfs_result = find_connected_components(graph, nodes)
            bfs_result = find_connected_components_bfs(graph, nodes)
            # Same number of components
            self.assertEqual(len(dfs_result), len(bfs_result))
            # Same sets of components
            dfs_sets = {frozenset(c) for c in dfs_result}
            bfs_sets = {frozenset(c) for c in bfs_result}
            self.assertEqual(dfs_sets, bfs_sets)

    def test_kosaraju_tarjan_consistency(self) -> None:
        """Kosaraju and Tarjan should find same SCCs."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_directed_graph(rng, n, density=0.3)
            nodes = list(range(n))
            kosaraju_result = kosaraju_scc(graph, nodes)
            tarjan_result = tarjan_scc(graph, nodes)
            # Same number of SCCs
            self.assertEqual(len(kosaraju_result), len(tarjan_result))
            # Same sets of SCCs
            kosaraju_sets = {frozenset(c) for c in kosaraju_result}
            tarjan_sets = {frozenset(c) for c in tarjan_result}
            self.assertEqual(kosaraju_sets, tarjan_sets)


if __name__ == "__main__":
    unittest.main()
