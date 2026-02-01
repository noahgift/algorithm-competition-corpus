"""Linked List problem algorithms.

Classic linked list interview problems with iterative solutions.

References:
    Floyd, R.W. (1967). "Nondeterministic Algorithms."
    J. ACM 14(4): 636-644. (Cycle detection)
"""

from __future__ import annotations

from algorithm_corpus.linked_list.list_node import ListNode


def has_cycle(head: ListNode | None) -> bool:
    """Detect if linked list has a cycle.

    Uses Floyd's cycle detection algorithm.

    Args:
        head: Head of linked list.

    Returns:
        True if cycle exists.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import ListNode
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> has_cycle(head)
        False
    """
    if not head:
        return False
    slow: ListNode | None = head
    fast: ListNode | None = head
    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def detect_cycle(head: ListNode | None) -> ListNode | None:
    """Find start of cycle in linked list.

    Uses Floyd's algorithm with phase 2 to find cycle start.

    Args:
        head: Head of linked list.

    Returns:
        Node where cycle begins, or None if no cycle.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import ListNode
        >>> head = ListNode(1, ListNode(2))
        >>> detect_cycle(head) is None
        True
    """
    if not head:
        return None

    slow: ListNode | None = head
    fast: ListNode | None = head

    # Phase 1: Find meeting point
    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow is not fast:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next  # type: ignore[union-attr]

    return slow


def merge_two_sorted(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Merge two sorted linked lists.

    Args:
        l1: First sorted list.
        l2: Second sorted list.

    Returns:
        Merged sorted list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> from algorithm_corpus.linked_list.list_ops import to_list
        >>> to_list(merge_two_sorted(from_list([1, 3, 5]), from_list([2, 4, 6])))
        [1, 2, 3, 4, 5, 6]
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """Remove nth node from end of list.

    Uses two-pointer technique with n-gap.

    Args:
        head: Head of linked list.
        n: Position from end (1-indexed).

    Returns:
        Head of modified list.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import from_list
        >>> from algorithm_corpus.linked_list.list_ops import to_list
        >>> to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 2))
        [1, 2, 3, 5]
    """
    dummy = ListNode(0, head)
    first: ListNode | None = dummy
    second: ListNode | None = dummy

    # Advance first pointer by n+1
    for _ in range(n + 1):
        if first:
            first = first.next

    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next  # type: ignore[union-attr]

    # Remove nth node
    if second and second.next:
        second.next = second.next.next

    return dummy.next


def find_intersection(
    head_a: ListNode | None, head_b: ListNode | None
) -> ListNode | None:
    """Find intersection node of two linked lists.

    Uses length difference technique.

    Args:
        head_a: Head of first list.
        head_b: Head of second list.

    Returns:
        Intersection node, or None if no intersection.

    Example:
        >>> from algorithm_corpus.linked_list.list_node import ListNode
        >>> shared = ListNode(3, ListNode(4))
        >>> a = ListNode(1, ListNode(2, shared))
        >>> b = ListNode(5, shared)
        >>> find_intersection(a, b).val  # type: ignore[union-attr]
        3
    """
    if not head_a or not head_b:
        return None

    # Get lengths
    len_a = 0
    len_b = 0
    curr_a: ListNode | None = head_a
    curr_b: ListNode | None = head_b

    while curr_a:
        len_a += 1
        curr_a = curr_a.next
    while curr_b:
        len_b += 1
        curr_b = curr_b.next

    # Align starting points
    curr_a = head_a
    curr_b = head_b
    if len_a > len_b:
        for _ in range(len_a - len_b):
            curr_a = curr_a.next  # type: ignore[union-attr]
    else:
        for _ in range(len_b - len_a):
            curr_b = curr_b.next  # type: ignore[union-attr]

    # Find intersection
    while curr_a and curr_b:
        if curr_a is curr_b:
            return curr_a
        curr_a = curr_a.next
        curr_b = curr_b.next

    return None
