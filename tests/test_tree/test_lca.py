"""Tests for LCA algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.tree.lca import (
    lca_bst,
    lca_recursive,
    lca_with_parent,
)
from algorithm_corpus.tree.tree_node import TreeNode


class TestLcaRecursive(unittest.TestCase):
    """Unit tests for lca_recursive."""

    def test_basic(self) -> None:
        """Test basic case."""
        root = TreeNode(
            3,
            TreeNode(5, TreeNode(6), TreeNode(2)),
            TreeNode(1, TreeNode(0), TreeNode(8)),
        )
        p = root.left
        q = root.right
        result = lca_recursive(root, p, q)  # type: ignore[arg-type]
        self.assertEqual(result.val, 3)  # type: ignore[union-attr]


class TestLcaBst(unittest.TestCase):
    """Unit tests for lca_bst."""

    def test_basic(self) -> None:
        """Test basic case."""
        root = TreeNode(
            6,
            TreeNode(2, TreeNode(0), TreeNode(4)),
            TreeNode(8, TreeNode(7), TreeNode(9)),
        )
        p = root.left.left  # type: ignore[union-attr]
        q = root.left.right  # type: ignore[union-attr]
        result = lca_bst(root, p, q)  # type: ignore[arg-type]
        self.assertEqual(result.val, 2)  # type: ignore[union-attr]


class TestLcaWithParent(unittest.TestCase):
    """Unit tests for lca_with_parent."""

    def test_basic(self) -> None:
        """Test basic case."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = lca_with_parent(root, root.left, root.right)  # type: ignore[arg-type]
        self.assertEqual(result.val, 1)  # type: ignore[union-attr]


if __name__ == "__main__":
    unittest.main()
