"""Tests for List Problems algorithms.

Tests Popperian Falsification Invariants:
    P1: Cycle detection finds cycle when present
    P2: Merge preserves sorted order
    P3: Remove nth from end correct position
    P4: Intersection finds shared nodes
"""

from __future__ import annotations

import unittest

from algorithm_corpus.linked_list.list_node import ListNode, from_list
from algorithm_corpus.linked_list.list_ops import to_list
from algorithm_corpus.linked_list.list_problems import (
    detect_cycle,
    find_intersection,
    has_cycle,
    merge_two_sorted,
    remove_nth_from_end,
)


class TestHasCycle(unittest.TestCase):
    """Unit tests for has_cycle."""

    def test_no_cycle(self) -> None:
        """Test list without cycle."""
        head = from_list([1, 2, 3])
        self.assertFalse(has_cycle(head))

    def test_with_cycle(self) -> None:
        """Test list with cycle."""
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = head.next  # Cycle to node 2
        self.assertTrue(has_cycle(head))

    def test_empty(self) -> None:
        """Test empty list."""
        self.assertFalse(has_cycle(None))

    def test_single_no_cycle(self) -> None:
        """Test single node without cycle."""
        self.assertFalse(has_cycle(ListNode(1)))

    def test_single_with_cycle(self) -> None:
        """Test single node with self-loop."""
        head = ListNode(1)
        head.next = head
        self.assertTrue(has_cycle(head))


class TestDetectCycle(unittest.TestCase):
    """Unit tests for detect_cycle."""

    def test_no_cycle(self) -> None:
        """Test list without cycle."""
        head = from_list([1, 2, 3])
        self.assertIsNone(detect_cycle(head))

    def test_with_cycle(self) -> None:
        """Test list with cycle."""
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        head.next.next = ListNode(3)
        head.next.next.next = node2  # Cycle to node 2
        result = detect_cycle(head)
        self.assertIsNotNone(result)
        self.assertIs(result, node2)

    def test_empty(self) -> None:
        """Test empty list."""
        self.assertIsNone(detect_cycle(None))


class TestMergeTwoSorted(unittest.TestCase):
    """Unit tests for merge_two_sorted."""

    def test_basic(self) -> None:
        """Test basic merge."""
        l1 = from_list([1, 3, 5])
        l2 = from_list([2, 4, 6])
        result = merge_two_sorted(l1, l2)
        self.assertEqual(to_list(result), [1, 2, 3, 4, 5, 6])

    def test_one_empty(self) -> None:
        """Test one empty list."""
        l1 = from_list([1, 2, 3])
        result = merge_two_sorted(l1, None)
        self.assertEqual(to_list(result), [1, 2, 3])

    def test_both_empty(self) -> None:
        """Test both empty."""
        self.assertIsNone(merge_two_sorted(None, None))


class TestRemoveNthFromEnd(unittest.TestCase):
    """Unit tests for remove_nth_from_end."""

    def test_basic(self) -> None:
        """Test basic removal."""
        head = from_list([1, 2, 3, 4, 5])
        result = remove_nth_from_end(head, 2)
        self.assertEqual(to_list(result), [1, 2, 3, 5])

    def test_remove_head(self) -> None:
        """Test remove head (last from end)."""
        head = from_list([1, 2])
        result = remove_nth_from_end(head, 2)
        self.assertEqual(to_list(result), [2])

    def test_single(self) -> None:
        """Test single node."""
        head = ListNode(1)
        result = remove_nth_from_end(head, 1)
        self.assertIsNone(result)


class TestFindIntersection(unittest.TestCase):
    """Unit tests for find_intersection."""

    def test_intersection(self) -> None:
        """Test lists with intersection."""
        shared = ListNode(3, ListNode(4))
        a = ListNode(1, ListNode(2, shared))
        b = ListNode(5, shared)
        result = find_intersection(a, b)
        self.assertIsNotNone(result)
        self.assertIs(result, shared)

    def test_no_intersection(self) -> None:
        """Test lists without intersection."""
        a = from_list([1, 2, 3])
        b = from_list([4, 5, 6])
        self.assertIsNone(find_intersection(a, b))

    def test_empty(self) -> None:
        """Test empty lists."""
        self.assertIsNone(find_intersection(None, None))


class TestListProblemsInvariants(unittest.TestCase):
    """Popperian falsification tests for list problems invariants."""

    def test_p1_cycle_detection(self) -> None:
        """P1: Cycle detection finds cycle when present."""
        # Create cycle
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Cycle back to node2

        self.assertTrue(has_cycle(head))
        cycle_start = detect_cycle(head)
        self.assertIs(cycle_start, node2)

    def test_p2_merge_preserves_order(self) -> None:
        """P2: Merge preserves sorted order."""
        l1 = from_list([1, 4, 7, 10])
        l2 = from_list([2, 3, 8, 9])
        result = to_list(merge_two_sorted(l1, l2))
        self.assertEqual(result, sorted(result))

    def test_p3_remove_nth_correct(self) -> None:
        """P3: Remove nth from end removes correct element."""
        values = [1, 2, 3, 4, 5]
        for n in range(1, 6):
            head = from_list(values)
            result = to_list(remove_nth_from_end(head, n))
            # n=1 removes 5, n=2 removes 4, etc.
            expected = values.copy()
            expected.pop(-n)
            self.assertEqual(result, expected)

    def test_p4_intersection_is_shared(self) -> None:
        """P4: Intersection node is same object in both lists."""
        shared = ListNode(10, ListNode(20))
        a = ListNode(1, ListNode(2, shared))
        b = ListNode(5, ListNode(6, ListNode(7, shared)))

        result = find_intersection(a, b)
        self.assertIsNotNone(result)

        # Verify by walking both lists
        curr_a: ListNode | None = a
        found_in_a = False
        while curr_a:
            if curr_a is result:
                found_in_a = True
                break
            curr_a = curr_a.next

        curr_b: ListNode | None = b
        found_in_b = False
        while curr_b:
            if curr_b is result:
                found_in_b = True
                break
            curr_b = curr_b.next

        self.assertTrue(found_in_a)
        self.assertTrue(found_in_b)


if __name__ == "__main__":
    unittest.main()
