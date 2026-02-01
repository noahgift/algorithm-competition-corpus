"""Tests for Jump Game algorithms."""

from __future__ import annotations

import unittest

from algorithm_corpus.greedy.jump_game import (
    can_jump,
    min_jumps,
)


class TestCanJump(unittest.TestCase):
    """Unit tests for can_jump."""

    def test_reachable(self) -> None:
        """Test reachable."""
        self.assertTrue(can_jump([2, 3, 1, 1, 4]))

    def test_not_reachable(self) -> None:
        """Test not reachable."""
        self.assertFalse(can_jump([3, 2, 1, 0, 4]))


class TestMinJumps(unittest.TestCase):
    """Unit tests for min_jumps."""

    def test_basic(self) -> None:
        """Test basic case."""
        self.assertEqual(min_jumps([2, 3, 1, 1, 4]), 2)

    def test_single(self) -> None:
        """Test single element."""
        self.assertEqual(min_jumps([0]), 0)


if __name__ == "__main__":
    unittest.main()
