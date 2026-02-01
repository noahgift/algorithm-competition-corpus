"""Basic Linked List operations.

Iterative implementations for Rust transpilation compatibility.

References:
    Knuth, D.E. (1997). The Art of Computer Programming, Volume 1:
    Fundamental Algorithms. Section 2.2: Linear Lists.
"""

from __future__ import annotations

from algorithm_corpus.linked_list.list_node import ListNode


def length(head: ListNode | None) -> int:
    """Calculate length of linked list.

    Args:
        head: Head of linked list.

    Returns:
        Number of nodes in list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> length(from_list([1, 2, 3]))
        3
        >>> length(None)
        0
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def to_list(head: ListNode | None) -> list[int]:
    """Convert linked list to Python list.

    Args:
        head: Head of linked list.

    Returns:
        List of values.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> to_list(from_list([1, 2, 3]))
        [1, 2, 3]
    """
    result: list[int] = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse linked list in place.

    Args:
        head: Head of linked list.

    Returns:
        New head of reversed list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> to_list(reverse_list(from_list([1, 2, 3])))
        [3, 2, 1]
    """
    prev: ListNode | None = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def get_middle(head: ListNode | None) -> ListNode | None:
    """Get middle node using Floyd's tortoise and hare.

    For even length, returns second middle node.

    Args:
        head: Head of linked list.

    Returns:
        Middle node.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> get_middle(from_list([1, 2, 3, 4, 5])).val  # type: ignore[union-attr]
        3
    """
    if not head:
        return None
    slow: ListNode | None = head
    fast: ListNode | None = head
    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    return slow


def insert_at(head: ListNode | None, val: int, position: int) -> ListNode:
    """Insert value at position.

    Args:
        head: Head of linked list.
        val: Value to insert.
        position: 0-indexed position.

    Returns:
        Head of modified list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> to_list(insert_at(from_list([1, 3]), 2, 1))
        [1, 2, 3]
    """
    new_node = ListNode(val)
    if position == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(position - 1):
        if current is None:
            break
        current = current.next

    if current:
        new_node.next = current.next
        current.next = new_node
        return head if head else new_node

    return head if head else new_node


def delete_node(head: ListNode | None, val: int) -> ListNode | None:
    """Delete first occurrence of value.

    Args:
        head: Head of linked list.
        val: Value to delete.

    Returns:
        Head of modified list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> to_list(delete_node(from_list([1, 2, 3]), 2))
        [1, 3]
    """
    if not head:
        return None

    if head.val == val:
        return head.next

    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            break
        current = current.next

    return head
