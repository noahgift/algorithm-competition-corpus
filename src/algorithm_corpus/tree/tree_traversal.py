"""Tree Traversal algorithms.

Iterative implementations for Rust transpilation compatibility.

References:
    Knuth, D.E. (1997). The Art of Computer Programming, Volume 1:
    Fundamental Algorithms. Section 2.3.1: Traversing Binary Trees.

Time Complexity: O(n) for all traversals.
Space Complexity: O(n) worst case for unbalanced trees.
"""

from __future__ import annotations

from algorithm_corpus.tree.tree_node import TreeNode  # noqa: TC001


def inorder(root: TreeNode | None) -> list[int]:
    """Inorder traversal (left, root, right).

    Uses iterative approach with explicit stack.

    Args:
        root: Root node of binary tree.

    Returns:
        List of node values in inorder.

    Example:
        >>> tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        >>> inorder(tree)
        [1, 3, 2]
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def preorder(root: TreeNode | None) -> list[int]:
    """Preorder traversal (root, left, right).

    Uses iterative approach with explicit stack.

    Args:
        root: Root node of binary tree.

    Returns:
        List of node values in preorder.

    Example:
        >>> tree = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> preorder(tree)
        [1, 2, 3]
    """
    if not root:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorder(root: TreeNode | None) -> list[int]:
    """Postorder traversal (left, right, root).

    Uses two-stack approach for iterative implementation.

    Args:
        root: Root node of binary tree.

    Returns:
        List of node values in postorder.

    Example:
        >>> tree = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> postorder(tree)
        [2, 3, 1]
    """
    if not root:
        return []

    result: list[int] = []
    stack1: list[TreeNode] = [root]
    stack2: list[TreeNode] = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().val)

    return result


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Level order (BFS) traversal.

    Returns nodes grouped by level.

    Args:
        root: Root node of binary tree.

    Returns:
        List of levels, each level is a list of node values.

    Example:
        >>> tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> level_order(tree)
        [[3], [9, 20], [15, 7]]
    """
    if not root:
        return []

    result: list[list[int]] = []
    queue: list[TreeNode] = [root]

    while queue:
        level_size = len(queue)
        level: list[int] = []

        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
