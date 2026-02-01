"""Tests for List Operations algorithms.

Tests Popperian Falsification Invariants:
    P1: Reverse of reverse equals original
    P2: Length equals Python list length
    P3: Insert at position increases length by 1
    P4: Delete decreases length by 1
"""

from __future__ import annotations

import random
import unittest

from algorithm_corpus.linked_list.list_node import ListNode, from_list
from algorithm_corpus.linked_list.list_ops import (
    delete_node,
    get_middle,
    insert_at,
    length,
    reverse_list,
    to_list,
)


class TestLength(unittest.TestCase):
    """Unit tests for length."""

    def test_basic(self) -> None:
        """Test basic list."""
        head = from_list([1, 2, 3])
        self.assertEqual(length(head), 3)

    def test_empty(self) -> None:
        """Test empty list."""
        self.assertEqual(length(None), 0)

    def test_single(self) -> None:
        """Test single node."""
        self.assertEqual(length(ListNode(1)), 1)


class TestToList(unittest.TestCase):
    """Unit tests for to_list."""

    def test_basic(self) -> None:
        """Test basic list."""
        head = from_list([1, 2, 3])
        self.assertEqual(to_list(head), [1, 2, 3])

    def test_empty(self) -> None:
        """Test empty list."""
        self.assertEqual(to_list(None), [])


class TestReverseList(unittest.TestCase):
    """Unit tests for reverse_list."""

    def test_basic(self) -> None:
        """Test basic list."""
        head = from_list([1, 2, 3])
        self.assertEqual(to_list(reverse_list(head)), [3, 2, 1])

    def test_empty(self) -> None:
        """Test empty list."""
        self.assertIsNone(reverse_list(None))

    def test_single(self) -> None:
        """Test single node."""
        head = ListNode(1)
        self.assertEqual(to_list(reverse_list(head)), [1])


class TestGetMiddle(unittest.TestCase):
    """Unit tests for get_middle."""

    def test_odd(self) -> None:
        """Test odd length."""
        head = from_list([1, 2, 3, 4, 5])
        middle = get_middle(head)
        self.assertIsNotNone(middle)
        self.assertEqual(middle.val, 3)  # type: ignore[union-attr]

    def test_even(self) -> None:
        """Test even length."""
        head = from_list([1, 2, 3, 4])
        middle = get_middle(head)
        self.assertIsNotNone(middle)
        self.assertEqual(middle.val, 3)  # type: ignore[union-attr]

    def test_empty(self) -> None:
        """Test empty list."""
        self.assertIsNone(get_middle(None))


class TestInsertAt(unittest.TestCase):
    """Unit tests for insert_at."""

    def test_middle(self) -> None:
        """Test insert in middle."""
        head = from_list([1, 3])
        head = insert_at(head, 2, 1)
        self.assertEqual(to_list(head), [1, 2, 3])

    def test_beginning(self) -> None:
        """Test insert at beginning."""
        head = from_list([2, 3])
        head = insert_at(head, 1, 0)
        self.assertEqual(to_list(head), [1, 2, 3])

    def test_empty(self) -> None:
        """Test insert into empty list."""
        head = insert_at(None, 1, 0)
        self.assertEqual(to_list(head), [1])


class TestDeleteNode(unittest.TestCase):
    """Unit tests for delete_node."""

    def test_middle(self) -> None:
        """Test delete from middle."""
        head = from_list([1, 2, 3])
        head = delete_node(head, 2)
        self.assertEqual(to_list(head), [1, 3])

    def test_head(self) -> None:
        """Test delete head."""
        head = from_list([1, 2, 3])
        head = delete_node(head, 1)
        self.assertEqual(to_list(head), [2, 3])

    def test_not_found(self) -> None:
        """Test delete value not found."""
        head = from_list([1, 2, 3])
        head = delete_node(head, 5)
        self.assertEqual(to_list(head), [1, 2, 3])

    def test_empty(self) -> None:
        """Test delete from empty list."""
        self.assertIsNone(delete_node(None, 1))


class TestListOpsInvariants(unittest.TestCase):
    """Popperian falsification tests for list ops invariants."""

    def test_p1_reverse_of_reverse(self) -> None:
        """P1: Reverse of reverse equals original."""
        rng = random.Random(42)
        for _ in range(30):
            values = [rng.randint(0, 100) for _ in range(rng.randint(0, 20))]
            head = from_list(values)
            result = reverse_list(reverse_list(head))
            self.assertEqual(to_list(result), values)

    def test_p2_length_matches_python(self) -> None:
        """P2: Length equals Python list length."""
        rng = random.Random(42)
        for _ in range(30):
            values = [rng.randint(0, 100) for _ in range(rng.randint(0, 20))]
            head = from_list(values)
            self.assertEqual(length(head), len(values))

    def test_p3_insert_increases_length(self) -> None:
        """P3: Insert at position increases length by 1."""
        rng = random.Random(42)
        for _ in range(30):
            values = [rng.randint(0, 100) for _ in range(rng.randint(1, 20))]
            head = from_list(values)
            original_len = length(head)
            pos = rng.randint(0, len(values))
            head = insert_at(head, 999, pos)
            self.assertEqual(length(head), original_len + 1)

    def test_p4_delete_decreases_length(self) -> None:
        """P4: Delete decreases length by 1 when value exists."""
        values = [1, 2, 3, 4, 5]
        head = from_list(values)
        original_len = length(head)
        head = delete_node(head, 3)
        self.assertEqual(length(head), original_len - 1)


if __name__ == "__main__":
    unittest.main()
