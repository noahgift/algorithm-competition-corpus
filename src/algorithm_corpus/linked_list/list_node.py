"""Linked List Node data structure.

References:
    Knuth, D.E. (1997). The Art of Computer Programming, Volume 1:
    Fundamental Algorithms. Section 2.2: Linear Lists.
"""

from __future__ import annotations


class ListNode:
    """Singly linked list node.

    Attributes:
        val: Node value.
        next: Pointer to next node.

    Example:
        >>> node = ListNode(1)
        >>> node.next = ListNode(2)
        >>> node.val
        1
        >>> node.next.val
        2
    """

    __slots__ = ("next", "val")

    def __init__(self, val: int = 0, next_node: ListNode | None = None) -> None:
        """Initialize list node.

        Args:
            val: Node value.
            next_node: Next node in list.
        """
        self.val = val
        self.next = next_node

    def __repr__(self) -> str:
        """String representation."""
        return f"ListNode({self.val})"

    __hash__ = None  # type: ignore[assignment]  # Mutable object

    def __eq__(self, other: object) -> bool:
        """Check equality by following entire list."""
        if not isinstance(other, ListNode):
            return False
        a: ListNode | None = self
        b: ListNode | None = other
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return a is None and b is None


def from_list(values: list[int]) -> ListNode | None:
    """Create linked list from Python list.

    Args:
        values: List of values.

    Returns:
        Head of linked list, or None if empty.

    Example:
        >>> head = from_list([1, 2, 3])
        >>> head.val
        1
        >>> head.next.val
        2
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
