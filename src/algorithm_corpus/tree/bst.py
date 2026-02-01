"""Binary Search Tree algorithms.

Iterative implementations for Rust transpilation compatibility.

References:
    Cormen, T.H., et al. (2009). Introduction to Algorithms (3rd ed.).
    MIT Press. Chapter 12: Binary Search Trees.

Time Complexity: O(h) where h is height, O(log n) for balanced trees.
"""

from __future__ import annotations

from algorithm_corpus.tree.tree_node import TreeNode


def bst_search(root: TreeNode | None, target: int) -> TreeNode | None:
    """Search for value in BST.

    Iterative implementation.

    Args:
        root: Root node of BST.
        target: Value to search for.

    Returns:
        Node containing target, or None if not found.

    Example:
        >>> tree = TreeNode(4, TreeNode(2), TreeNode(7))
        >>> node = bst_search(tree, 2)
        >>> node.val if node else None
        2
        >>> bst_search(tree, 5) is None
        True
    """
    current = root
    while current:
        if target == current.val:
            return current
        current = current.left if target < current.val else current.right
    return None


def bst_insert(root: TreeNode | None, val: int) -> TreeNode:
    """Insert value into BST.

    Iterative implementation.

    Args:
        root: Root node of BST.
        val: Value to insert.

    Returns:
        Root of modified tree.

    Example:
        >>> tree = TreeNode(4, TreeNode(2), TreeNode(7))
        >>> tree = bst_insert(tree, 5)
        >>> tree.right.left.val
        5
    """
    new_node = TreeNode(val)
    if not root:
        return new_node

    current = root
    while True:
        if val < current.val:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root


def is_valid_bst(root: TreeNode | None) -> bool:
    """Check if tree is valid BST.

    Uses inorder traversal property: inorder of BST is sorted.
    Iterative implementation.

    Args:
        root: Root node of binary tree.

    Returns:
        True if tree is valid BST.

    Example:
        >>> tree = TreeNode(2, TreeNode(1), TreeNode(3))
        >>> is_valid_bst(tree)
        True
        >>> tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        >>> is_valid_bst(tree)
        False
    """
    if not root:
        return True

    stack: list[TreeNode] = []
    current: TreeNode | None = root
    prev_val: int | None = None

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if prev_val is not None and current.val <= prev_val:
            return False
        prev_val = current.val
        current = current.right

    return True
