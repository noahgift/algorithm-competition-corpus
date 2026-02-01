"""Advanced linked list algorithms.

More complex linked list manipulations.
"""

from __future__ import annotations

from algorithm_corpus.linked_list.list_node import ListNode


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Add two numbers represented as linked lists.

    Digits are stored in reverse order.

    Args:
        l1: First number as linked list.
        l2: Second number as linked list.

    Returns:
        Sum as linked list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> from algorithm_corpus.linked_list.list_ops import to_list
        >>> l1 = from_list([2, 4, 3])  # 342
        >>> l2 = from_list([5, 6, 4])  # 465
        >>> to_list(add_two_numbers(l1, l2))  # 807
        [7, 0, 8]
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    """Rotate list to the right by k places.

    Args:
        head: Head of linked list.
        k: Number of positions to rotate.

    Returns:
        New head after rotation.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> from algorithm_corpus.linked_list.list_ops import to_list
        >>> to_list(rotate_right(from_list([1, 2, 3, 4, 5]), 2))
        [4, 5, 1, 2, 3]
    """
    if not head or not head.next or k == 0:
        return head

    # Find length and last node
    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next

    # Normalize k
    k = k % length
    if k == 0:
        return head

    # Find new tail (length - k - 1 steps from head)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next  # type: ignore[union-attr]

    # Rotate
    new_head = new_tail.next  # type: ignore[union-attr]
    new_tail.next = None  # type: ignore[union-attr]
    tail.next = head

    return new_head


def is_palindrome_list(head: ListNode | None) -> bool:
    """Check if linked list is palindrome.

    Uses slow/fast pointers to find middle, then reverses second half.

    Args:
        head: Head of linked list.

    Returns:
        True if palindrome.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> is_palindrome_list(from_list([1, 2, 2, 1]))
        True
        >>> is_palindrome_list(from_list([1, 2]))
        False
    """
    if not head or not head.next:
        return True

    # Find middle
    slow: ListNode | None = head
    fast: ListNode | None = head
    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next

    # Reverse second half
    prev: ListNode | None = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Compare halves
    first: ListNode | None = head
    second: ListNode | None = prev
    while second:
        if first is None or first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True
