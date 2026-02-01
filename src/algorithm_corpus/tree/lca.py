"""Lowest Common Ancestor algorithms.

Find LCA in binary trees using various approaches.

References:
    Tarjan, R.E. (1979). "Applications of path compression on balanced trees."
    J. ACM 26(4): 690-715.
"""

from __future__ import annotations

from algorithm_corpus.tree.tree_node import TreeNode  # noqa: TC001


def lca_recursive(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Find lowest common ancestor of two nodes.

    Recursive approach using divide and conquer.

    Args:
        root: Root of binary tree.
        p: First node.
        q: Second node.

    Returns:
        LCA node, or None if not found.

    Example:
        >>> root = TreeNode(
        ...     3,
        ...     TreeNode(5, TreeNode(6), TreeNode(2)),
        ...     TreeNode(1, TreeNode(0), TreeNode(8)),
        ... )
        >>> p = root.left  # Node 5
        >>> q = root.right  # Node 1
        >>> lca_recursive(root, p, q).val
        3
    """
    if root is None or root is p or root is q:
        return root

    left = lca_recursive(root.left, p, q)
    right = lca_recursive(root.right, p, q)

    if left and right:
        return root
    return left if left else right


def lca_bst(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Find lowest common ancestor in BST.

    Uses BST property for O(h) time.

    Args:
        root: Root of BST.
        p: First node.
        q: Second node.

    Returns:
        LCA node.

    Example:
        >>> root = TreeNode(
        ...     6,
        ...     TreeNode(2, TreeNode(0), TreeNode(4)),
        ...     TreeNode(8, TreeNode(7), TreeNode(9)),
        ... )
        >>> p = root.left.left  # Node 0
        >>> q = root.left.right  # Node 4
        >>> lca_bst(root, p, q).val
        2
    """
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
    return None


def lca_with_parent(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Find LCA using path intersection.

    Alternative approach storing paths.

    Args:
        root: Root of binary tree.
        p: First node.
        q: Second node.

    Returns:
        LCA node.

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> lca_with_parent(root, root.left, root.right).val
        1
    """

    def find_path(node: TreeNode | None, target: TreeNode) -> list[TreeNode]:
        if node is None:
            return []
        if node is target:
            return [node]

        for child in (node.left, node.right):
            child_path = find_path(child, target)
            if child_path:
                return [node] + child_path

        return []

    path_p = find_path(root, p)
    path_q = find_path(root, q)

    # Find last common node in paths
    lca: TreeNode | None = None
    for np, nq in zip(path_p, path_q, strict=False):
        if np is nq:
            lca = np
        else:
            break

    return lca
