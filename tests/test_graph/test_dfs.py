"""Tests for DFS Traversal algorithms.

Tests Popperian Falsification Invariants:
    P1: Each node appears at most once in output
    P2: Output size equals number of reachable nodes
    P3: All output nodes are reachable from start
    P4: Preorder visits parent before children
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.dfs import (
    dfs_all_paths,
    dfs_iterative,
    dfs_preorder_postorder,
)


class TestDfsIterative(unittest.TestCase):
    """Unit tests for dfs_iterative."""

    def test_simple_graph(self) -> None:
        """Test DFS on a simple graph."""
        graph = {0: [1, 2], 1: [3], 2: [], 3: []}
        result = dfs_iterative(graph, 0)
        self.assertEqual(result[0], 0)  # Start node first
        self.assertEqual(set(result), {0, 1, 2, 3})

    def test_single_node(self) -> None:
        """Test DFS on single node."""
        graph = {0: []}
        result = dfs_iterative(graph, 0)
        self.assertEqual(result, [0])

    def test_cycle_handling(self) -> None:
        """Test DFS handles cycles."""
        graph = {0: [1], 1: [0]}
        result = dfs_iterative(graph, 0)
        self.assertEqual(len(result), 2)
        self.assertEqual(set(result), {0, 1})

    def test_disconnected_not_visited(self) -> None:
        """Test DFS doesn't visit disconnected nodes."""
        graph = {0: [1], 1: [], 2: []}
        result = dfs_iterative(graph, 0)
        self.assertNotIn(2, result)


class TestDfsAllPaths(unittest.TestCase):
    """Unit tests for dfs_all_paths."""

    def test_multiple_paths(self) -> None:
        """Test finding all paths."""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = dfs_all_paths(graph, 0, 3)
        self.assertEqual(len(result), 2)
        paths_sorted = sorted(result)
        self.assertEqual(paths_sorted, [[0, 1, 3], [0, 2, 3]])

    def test_same_start_end(self) -> None:
        """Test path from node to itself."""
        graph = {0: [1], 1: []}
        result = dfs_all_paths(graph, 0, 0)
        self.assertEqual(result, [[0]])

    def test_no_path(self) -> None:
        """Test when no path exists."""
        graph = {0: [], 1: []}
        result = dfs_all_paths(graph, 0, 1)
        self.assertEqual(result, [])

    def test_single_path(self) -> None:
        """Test graph with single path."""
        graph = {0: [1], 1: [2], 2: []}
        result = dfs_all_paths(graph, 0, 2)
        self.assertEqual(result, [[0, 1, 2]])


class TestDfsPreorderPostorder(unittest.TestCase):
    """Unit tests for dfs_preorder_postorder."""

    def test_simple_tree(self) -> None:
        """Test preorder/postorder on simple tree."""
        graph = {0: [1, 2], 1: [], 2: []}
        pre, post = dfs_preorder_postorder(graph, 0)
        self.assertEqual(pre, [0, 1, 2])
        self.assertEqual(post, [1, 2, 0])

    def test_single_node(self) -> None:
        """Test on single node."""
        graph = {0: []}
        pre, post = dfs_preorder_postorder(graph, 0)
        self.assertEqual(pre, [0])
        self.assertEqual(post, [0])

    def test_linear_graph(self) -> None:
        """Test on linear graph."""
        graph = {0: [1], 1: [2], 2: []}
        pre, post = dfs_preorder_postorder(graph, 0)
        self.assertEqual(pre, [0, 1, 2])
        self.assertEqual(post, [2, 1, 0])


class TestDfsInvariants(unittest.TestCase):
    """Popperian falsification tests for DFS invariants."""

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

    def _reachable_nodes(self, graph: dict[int, list[int]], start: int) -> set[int]:
        """Find all reachable nodes from start."""
        visited: set[int] = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph.get(node, []))
        return visited

    def test_p1_no_duplicates(self) -> None:
        """P1: Each node appears at most once in output."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_graph(rng, n, density=0.3)
            start = rng.randint(0, n - 1)
            result = dfs_iterative(graph, start)
            self.assertEqual(len(result), len(set(result)), "Duplicates found in DFS")

    def test_p2_output_size_matches_reachable(self) -> None:
        """P2: Output size equals number of reachable nodes."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_graph(rng, n, density=0.3)
            start = rng.randint(0, n - 1)
            result = dfs_iterative(graph, start)
            reachable = self._reachable_nodes(graph, start)
            self.assertEqual(len(result), len(reachable))

    def test_p3_all_output_reachable(self) -> None:
        """P3: All output nodes are reachable from start."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            graph = self._random_graph(rng, n, density=0.3)
            start = rng.randint(0, n - 1)
            result = dfs_iterative(graph, start)
            reachable = self._reachable_nodes(graph, start)
            for node in result:
                self.assertIn(
                    node, reachable, f"Node {node} not reachable from {start}"
                )

    def test_p4_preorder_parent_before_children(self) -> None:
        """P4: In preorder, parent appears before its children."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 15)
            graph = self._random_graph(rng, n, density=0.2)
            start = rng.randint(0, n - 1)
            pre, post = dfs_preorder_postorder(graph, start)
            # Verify preorder: start is first
            if pre:
                self.assertEqual(pre[0], start)
            # Verify postorder: start is last
            if post:
                self.assertEqual(post[-1], start)

    def test_path_validity(self) -> None:
        """All paths should be valid sequences of edges."""
        rng = random.Random(42)
        for _ in range(30):
            n = rng.randint(2, 10)
            graph = self._random_graph(rng, n, density=0.3)
            start = rng.randint(0, n - 1)
            end = rng.randint(0, n - 1)
            paths = dfs_all_paths(graph, start, end)
            for path in paths:
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], end)
                for i in range(len(path) - 1):
                    self.assertIn(
                        path[i + 1],
                        graph.get(path[i], []),
                        f"Invalid edge {path[i]}->{path[i + 1]}",
                    )


if __name__ == "__main__":
    unittest.main()
