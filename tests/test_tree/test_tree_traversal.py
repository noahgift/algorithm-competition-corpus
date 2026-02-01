"""Tests for Tree Traversal algorithms.

Tests Popperian Falsification Invariants:
    P1: Inorder of BST is sorted
    P2: All traversals visit same nodes
    P3: Preorder first element is root
    P4: Postorder last element is root
"""

from __future__ import annotations

import unittest

from algorithm_corpus.tree.tree_node import TreeNode
from algorithm_corpus.tree.tree_traversal import (
    inorder,
    level_order,
    postorder,
    preorder,
)


class TestInorder(unittest.TestCase):
    """Unit tests for inorder traversal."""

    def test_basic(self) -> None:
        """Test basic tree."""
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(inorder(tree), [1, 3, 2])

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertEqual(inorder(None), [])

    def test_single(self) -> None:
        """Test single node."""
        self.assertEqual(inorder(TreeNode(1)), [1])


class TestPreorder(unittest.TestCase):
    """Unit tests for preorder traversal."""

    def test_basic(self) -> None:
        """Test basic tree."""
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(preorder(tree), [1, 2, 3])

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertEqual(preorder(None), [])


class TestPostorder(unittest.TestCase):
    """Unit tests for postorder traversal."""

    def test_basic(self) -> None:
        """Test basic tree."""
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(postorder(tree), [2, 3, 1])

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertEqual(postorder(None), [])


class TestLevelOrder(unittest.TestCase):
    """Unit tests for level order traversal."""

    def test_basic(self) -> None:
        """Test basic tree."""
        tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(level_order(tree), [[3], [9, 20], [15, 7]])

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertEqual(level_order(None), [])


class TestTraversalInvariants(unittest.TestCase):
    """Popperian falsification tests for traversal invariants."""

    def _build_bst(self, values: list[int]) -> TreeNode | None:
        """Build BST from values."""
        if not values:
            return None
        root = TreeNode(values[0])
        for val in values[1:]:
            self._insert_bst(root, val)
        return root

    def _insert_bst(self, root: TreeNode, val: int) -> None:
        """Insert value into BST."""
        current = root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                current = current.right

    def test_p1_inorder_bst_sorted(self) -> None:
        """P1: Inorder of BST is sorted."""
        bst = self._build_bst([5, 3, 7, 1, 4, 6, 8])
        result = inorder(bst)
        self.assertEqual(result, sorted(result))

    def test_p2_all_traversals_same_nodes(self) -> None:
        """P2: All traversals visit same nodes."""
        tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        in_nodes = sorted(inorder(tree))
        pre_nodes = sorted(preorder(tree))
        post_nodes = sorted(postorder(tree))
        level_nodes = sorted([v for level in level_order(tree) for v in level])
        self.assertEqual(in_nodes, pre_nodes)
        self.assertEqual(pre_nodes, post_nodes)
        self.assertEqual(post_nodes, level_nodes)

    def test_p3_preorder_first_is_root(self) -> None:
        """P3: Preorder first element is root."""
        tree = TreeNode(42, TreeNode(1), TreeNode(2))
        result = preorder(tree)
        self.assertEqual(result[0], 42)

    def test_p4_postorder_last_is_root(self) -> None:
        """P4: Postorder last element is root."""
        tree = TreeNode(42, TreeNode(1), TreeNode(2))
        result = postorder(tree)
        self.assertEqual(result[-1], 42)


if __name__ == "__main__":
    unittest.main()
