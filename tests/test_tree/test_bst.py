"""Tests for BST algorithms.

Tests Popperian Falsification Invariants:
    P1: Search finds inserted elements
    P2: BST property maintained after insert
    P3: Valid BST correctly validated
    P4: Invalid BST correctly rejected
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.tree.bst import (
    bst_insert,
    bst_search,
    is_valid_bst,
)
from algorithm_corpus.tree.tree_node import TreeNode
from algorithm_corpus.tree.tree_traversal import inorder


class TestBstSearch(unittest.TestCase):
    """Unit tests for bst_search."""

    def test_found(self) -> None:
        """Test element found."""
        tree = TreeNode(4, TreeNode(2), TreeNode(7))
        node = bst_search(tree, 2)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 2)  # type: ignore[union-attr]

    def test_not_found(self) -> None:
        """Test element not found."""
        tree = TreeNode(4, TreeNode(2), TreeNode(7))
        self.assertIsNone(bst_search(tree, 5))

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertIsNone(bst_search(None, 1))


class TestBstInsert(unittest.TestCase):
    """Unit tests for bst_insert."""

    def test_insert_empty(self) -> None:
        """Test insert into empty tree."""
        tree = bst_insert(None, 5)
        self.assertEqual(tree.val, 5)

    def test_insert_left(self) -> None:
        """Test insert to left."""
        tree = TreeNode(5)
        tree = bst_insert(tree, 3)
        self.assertEqual(tree.left.val, 3)  # type: ignore[union-attr]

    def test_insert_right(self) -> None:
        """Test insert to right."""
        tree = TreeNode(5)
        tree = bst_insert(tree, 7)
        self.assertEqual(tree.right.val, 7)  # type: ignore[union-attr]


class TestIsValidBst(unittest.TestCase):
    """Unit tests for is_valid_bst."""

    def test_valid(self) -> None:
        """Test valid BST."""
        tree = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertTrue(is_valid_bst(tree))

    def test_invalid(self) -> None:
        """Test invalid BST."""
        tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertFalse(is_valid_bst(tree))

    def test_empty(self) -> None:
        """Test empty tree."""
        self.assertTrue(is_valid_bst(None))


class TestBstInvariants(unittest.TestCase):
    """Popperian falsification tests for BST invariants."""

    def test_p1_search_finds_inserted(self) -> None:
        """P1: Search finds inserted elements."""
        rng = random.Random(42)
        tree: TreeNode | None = None
        values = [rng.randint(0, 100) for _ in range(20)]
        for val in values:
            tree = bst_insert(tree, val)
        for val in values:
            node = bst_search(tree, val)
            self.assertIsNotNone(node)
            self.assertEqual(node.val, val)  # type: ignore[union-attr]

    def test_p2_bst_property_maintained(self) -> None:
        """P2: BST property maintained after insert."""
        rng = random.Random(42)
        tree: TreeNode | None = None
        for _ in range(30):
            tree = bst_insert(tree, rng.randint(0, 100))
        # Inorder of BST should be sorted
        result = inorder(tree)
        self.assertEqual(result, sorted(result))

    def test_p3_valid_bst_validated(self) -> None:
        """P3: Valid BST correctly validated."""
        # Build BST by insertion
        tree: TreeNode | None = None
        for val in [5, 3, 7, 1, 4, 6, 8]:
            tree = bst_insert(tree, val)
        self.assertTrue(is_valid_bst(tree))

    def test_p4_invalid_bst_rejected(self) -> None:
        """P4: Invalid BST correctly rejected."""
        # Manually construct invalid BST
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(15)
        tree.left.right = TreeNode(12)  # Invalid: 12 > 10
        self.assertFalse(is_valid_bst(tree))


if __name__ == "__main__":
    unittest.main()
