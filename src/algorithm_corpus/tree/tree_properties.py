"""Tree Property algorithms.

Calculate various properties of binary trees.

References:
    Knuth, D.E. (1997). The Art of Computer Programming, Volume 1:
    Fundamental Algorithms. Section 2.3: Trees.
"""

from __future__ import annotations

from algorithm_corpus.tree.tree_node import TreeNode  # noqa: TC001


def height(root: TreeNode | None) -> int:
    """Calculate height of binary tree.

    Height is number of edges on longest path from root to leaf.
    Empty tree has height -1, single node has height 0.

    Uses iterative level-order traversal.

    Args:
        root: Root node of binary tree.

    Returns:
        Height of tree.

    Example:
        >>> tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> height(tree)
        2
        >>> height(None)
        -1
    """
    if not root:
        return -1

    h = -1
    queue: list[TreeNode] = [root]

    while queue:
        h += 1
        next_level: list[TreeNode] = []
        for node in queue:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level

    return h


def diameter(root: TreeNode | None) -> int:
    """Calculate diameter of binary tree.

    Diameter is length of longest path between any two nodes.
    Path may or may not pass through root.

    Uses iterative postorder with height tracking.

    Args:
        root: Root node of binary tree.

    Returns:
        Diameter of tree (number of edges).

    Example:
        >>> tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        >>> diameter(tree)
        3
    """
    if not root:
        return 0

    max_diameter = 0
    heights: dict[int, int] = {id(None): -1}
    stack: list[tuple[TreeNode, bool]] = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            left_h = heights.get(id(node.left), -1)
            right_h = heights.get(id(node.right), -1)
            heights[id(node)] = 1 + max(left_h, right_h)
            max_diameter = max(max_diameter, left_h + right_h + 2)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return max_diameter


def is_balanced(root: TreeNode | None) -> bool:
    """Check if tree is height-balanced.

    A height-balanced tree has height difference <= 1 for all nodes.

    Uses iterative postorder traversal.

    Args:
        root: Root node of binary tree.

    Returns:
        True if tree is balanced.

    Example:
        >>> tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> is_balanced(tree)
        True
        >>> unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        >>> is_balanced(unbalanced)
        False
    """
    if not root:
        return True

    heights: dict[int, int] = {id(None): -1}
    stack: list[tuple[TreeNode, bool]] = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            left_h = heights.get(id(node.left), -1)
            right_h = heights.get(id(node.right), -1)
            if abs(left_h - right_h) > 1:
                return False
            heights[id(node)] = 1 + max(left_h, right_h)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return True


def is_symmetric(root: TreeNode | None) -> bool:
    """Check if tree is symmetric (mirror of itself).

    Uses iterative approach with two queues.

    Args:
        root: Root node of binary tree.

    Returns:
        True if tree is symmetric.

    Example:
        >>> tree = TreeNode(
        ...     1,
        ...     TreeNode(2, TreeNode(3), TreeNode(4)),
        ...     TreeNode(2, TreeNode(4), TreeNode(3)),
        ... )
        >>> is_symmetric(tree)
        True
    """
    if not root:
        return True

    queue: list[tuple[TreeNode | None, TreeNode | None]] = [(root.left, root.right)]

    while queue:
        left, right = queue.pop(0)

        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True
