"""Tests for Union-Find (Disjoint Set Union) data structure.

Tests Popperian Falsification Invariants:
    P1: find(x) == find(y) iff x and y are in same set
    P2: After union(x,y), find(x) == find(y)
    P3: Number of components decreases by 1 after successful union
    P4: find(x) always returns a valid representative
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.union_find import (
    UnionFind,
    count_connected_components,
    find_redundant_connection,
    is_valid_tree,
)


class TestUnionFind(unittest.TestCase):
    """Unit tests for UnionFind class."""

    def test_initialization(self) -> None:
        """Test UnionFind initialization."""
        uf = UnionFind(5)
        self.assertEqual(uf.get_count(), 5)
        for i in range(5):
            self.assertEqual(uf.find(i), i)

    def test_union_basic(self) -> None:
        """Test basic union operation."""
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.connected(0, 1))
        self.assertEqual(uf.get_count(), 4)

    def test_union_already_connected(self) -> None:
        """Test union when already connected."""
        uf = UnionFind(5)
        uf.union(0, 1)
        self.assertFalse(uf.union(0, 1))
        self.assertEqual(uf.get_count(), 4)

    def test_connected(self) -> None:
        """Test connected check."""
        uf = UnionFind(5)
        self.assertFalse(uf.connected(0, 1))
        uf.union(0, 1)
        self.assertTrue(uf.connected(0, 1))

    def test_transitive_connection(self) -> None:
        """Test transitive connections."""
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        self.assertTrue(uf.connected(0, 2))


class TestCountConnectedComponents(unittest.TestCase):
    """Unit tests for count_connected_components."""

    def test_two_components(self) -> None:
        """Test counting two components."""
        result = count_connected_components(5, [[0, 1], [1, 2], [3, 4]])
        self.assertEqual(result, 2)

    def test_no_edges(self) -> None:
        """Test with no edges."""
        result = count_connected_components(3, [])
        self.assertEqual(result, 3)

    def test_single_component(self) -> None:
        """Test single connected component."""
        result = count_connected_components(4, [[0, 1], [1, 2], [2, 3]])
        self.assertEqual(result, 1)


class TestIsValidTree(unittest.TestCase):
    """Unit tests for is_valid_tree."""

    def test_valid_tree(self) -> None:
        """Test valid tree."""
        self.assertTrue(is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))

    def test_has_cycle(self) -> None:
        """Test graph with cycle."""
        self.assertFalse(is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

    def test_disconnected(self) -> None:
        """Test disconnected graph."""
        self.assertFalse(is_valid_tree(2, []))

    def test_single_node(self) -> None:
        """Test single node (valid tree)."""
        self.assertTrue(is_valid_tree(1, []))


class TestFindRedundantConnection(unittest.TestCase):
    """Unit tests for find_redundant_connection."""

    def test_simple_cycle(self) -> None:
        """Test finding redundant edge in simple cycle."""
        result = find_redundant_connection([[1, 2], [1, 3], [2, 3]])
        self.assertEqual(result, [2, 3])

    def test_larger_graph(self) -> None:
        """Test larger graph with cycle."""
        result = find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
        self.assertEqual(result, [1, 4])


class TestUnionFindInvariants(unittest.TestCase):
    """Popperian falsification tests for Union-Find invariants."""

    def test_p1_find_same_set_equivalence(self) -> None:
        """P1: find(x) == find(y) iff x and y are in same set."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 20)
            uf = UnionFind(n)
            # Track which sets are merged
            sets: list[set[int]] = [{i} for i in range(n)]
            for _ in range(rng.randint(0, n)):
                x, y = rng.randint(0, n - 1), rng.randint(0, n - 1)
                if uf.union(x, y):
                    # Merge sets
                    set_x = next(s for s in sets if x in s)
                    set_y = next(s for s in sets if y in s)
                    if set_x != set_y:
                        merged = set_x | set_y
                        sets.remove(set_x)
                        sets.remove(set_y)
                        sets.append(merged)
            # Verify invariant
            for i in range(n):
                for j in range(n):
                    same_find = uf.find(i) == uf.find(j)
                    same_set = any(i in s and j in s for s in sets)
                    self.assertEqual(same_find, same_set)

    def test_p2_union_implies_same_find(self) -> None:
        """P2: After union(x,y), find(x) == find(y)."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 20)
            uf = UnionFind(n)
            for _ in range(rng.randint(1, n)):
                x, y = rng.randint(0, n - 1), rng.randint(0, n - 1)
                uf.union(x, y)
                self.assertEqual(
                    uf.find(x), uf.find(y), f"After union({x},{y}), finds differ"
                )

    def test_p3_count_decreases_on_union(self) -> None:
        """P3: Number of components decreases by 1 after successful union."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(2, 20)
            uf = UnionFind(n)
            for _ in range(rng.randint(1, n)):
                x, y = rng.randint(0, n - 1), rng.randint(0, n - 1)
                count_before = uf.get_count()
                result = uf.union(x, y)
                count_after = uf.get_count()
                if result:
                    self.assertEqual(count_after, count_before - 1)
                else:
                    self.assertEqual(count_after, count_before)

    def test_p4_find_returns_valid_representative(self) -> None:
        """P4: find(x) always returns a valid representative."""
        rng = random.Random(42)
        for _ in range(50):
            n = rng.randint(1, 20)
            uf = UnionFind(n)
            for _ in range(rng.randint(0, n)):
                x, y = rng.randint(0, n - 1), rng.randint(0, n - 1)
                uf.union(x, y)
            for i in range(n):
                rep = uf.find(i)
                self.assertGreaterEqual(rep, 0)
                self.assertLess(rep, n)
                # Representative should be its own parent (eventually)
                self.assertEqual(uf.find(rep), rep)


if __name__ == "__main__":
    unittest.main()
