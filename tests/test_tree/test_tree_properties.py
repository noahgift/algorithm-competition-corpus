"""Tests for Tree Properties algorithms.

Tests Popperian Falsification Invariants:
    P1: Height of balanced tree is O(log n)
    P2: Diameter >= height
    P3: Balanced implies height difference <= 1
    P4: Symmetric tree is mirror of itself
"""

from __future__ import annotations

import math
import unittest

from algorithm_corpus.tree.tree_node import TreeNode
from algorithm_corpus.tree.tree_properties import (
    diameter,
    height,
    is_balanced,
    is_symmetric,
)


class TestHeight(unittest.TestCase):
    """Unit tests for height."""

    def test_basic(self) -> None:
        """Test basic tree."""
        tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(height(tree), 2)

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertEqual(height(None), -1)

    def test_single(self) -> None:
        """Test single node."""
        self.assertEqual(height(TreeNode(1)), 0)


class TestDiameter(unittest.TestCase):
    """Unit tests for diameter."""

    def test_basic(self) -> None:
        """Test basic tree."""
        tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(diameter(tree), 3)

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertEqual(diameter(None), 0)

    def test_single(self) -> None:
        """Test single node."""
        self.assertEqual(diameter(TreeNode(1)), 0)

    def test_linear(self) -> None:
        """Test linear tree."""
        tree = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(diameter(tree), 2)


class TestIsBalanced(unittest.TestCase):
    """Unit tests for is_balanced."""

    def test_balanced(self) -> None:
        """Test balanced tree."""
        tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertTrue(is_balanced(tree))

    def test_unbalanced(self) -> None:
        """Test unbalanced tree."""
        tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertFalse(is_balanced(tree))

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertTrue(is_balanced(None))


class TestIsSymmetric(unittest.TestCase):
    """Unit tests for is_symmetric."""

    def test_symmetric(self) -> None:
        """Test symmetric tree."""
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        )
        self.assertTrue(is_symmetric(tree))

    def test_asymmetric(self) -> None:
        """Test asymmetric tree."""
        tree = TreeNode(
            1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))
        )
        self.assertFalse(is_symmetric(tree))

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertTrue(is_symmetric(None))


class TestTreePropertiesInvariants(unittest.TestCase):
    """Popperian falsification tests for tree properties invariants."""

    def _build_complete_tree(self, n: int) -> TreeNode | None:
        """Build complete binary tree with n nodes."""
        if n <= 0:
            return None
        nodes = [TreeNode(i) for i in range(n)]
        for i in range(n):
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < n:
                nodes[i].left = nodes[left_idx]
            if right_idx < n:
                nodes[i].right = nodes[right_idx]
        return nodes[0]

    def test_p1_complete_tree_height(self) -> None:
        """P1: Height of complete tree with n nodes is floor(log2(n))."""
        for n in [1, 3, 7, 15, 31]:
            tree = self._build_complete_tree(n)
            h = height(tree)
            expected = int(math.log2(n))
            self.assertEqual(h, expected)

    def test_p2_diameter_gte_height(self) -> None:
        """P2: Diameter >= height."""
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        h = height(tree)
        d = diameter(tree)
        self.assertGreaterEqual(d, h)

    def test_p3_balanced_height_diff(self) -> None:
        """P3: Balanced tree has height difference <= 1 at all nodes."""

        def check_balance(node: TreeNode | None) -> tuple[bool, int]:
            if not node:
                return True, -1
            left_bal, left_h = check_balance(node.left)
            right_bal, right_h = check_balance(node.right)
            balanced = left_bal and right_bal and abs(left_h - right_h) <= 1
            return balanced, 1 + max(left_h, right_h)

        tree = self._build_complete_tree(15)
        our_result = is_balanced(tree)
        verified, _ = check_balance(tree)
        self.assertEqual(our_result, verified)

    def test_p4_symmetric_is_mirror(self) -> None:
        """P4: Symmetric tree equals its mirror."""

        def mirror(node: TreeNode | None) -> TreeNode | None:
            if not node:
                return None
            return TreeNode(node.val, mirror(node.right), mirror(node.left))

        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        )
        self.assertTrue(is_symmetric(tree))
        mirrored = mirror(tree)
        self.assertEqual(tree, mirrored)


if __name__ == "__main__":
    unittest.main()
