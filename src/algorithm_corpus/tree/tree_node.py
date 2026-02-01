"""Tree Node data structure.

References:
    Knuth, D.E. (1997). The Art of Computer Programming, Volume 1:
    Fundamental Algorithms. Section 2.3: Trees.
"""

from __future__ import annotations


class TreeNode:
    """Binary tree node.

    Attributes:
        val: Node value.
        left: Left child node.
        right: Right child node.

    Example:
        >>> node = TreeNode(1)
        >>> node.left = TreeNode(2)
        >>> node.right = TreeNode(3)
        >>> node.val
        1
        >>> node.left.val
        2
    """

    __slots__ = ("left", "right", "val")

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        """Initialize tree node.

        Args:
            val: Node value.
            left: Left child.
            right: Right child.
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """String representation."""
        return f"TreeNode({self.val})"

    __hash__ = None  # type: ignore[assignment]  # Mutable object

    def __eq__(self, other: object) -> bool:
        """Check equality by structure and values."""
        if not isinstance(other, TreeNode):
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )
