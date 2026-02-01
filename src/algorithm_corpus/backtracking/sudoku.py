"""Sudoku solver using backtracking.

Classic constraint satisfaction problem.
"""

from __future__ import annotations


def solve_sudoku(board: list[list[str]]) -> bool:
    """Solve a Sudoku puzzle in-place.

    Args:
        board: 9x9 grid with digits '1'-'9' and '.' for empty cells.

    Returns:
        True if solution found (board is modified in-place).

    Example:
        >>> board = [
        ...     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ...     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ...     [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ...     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ...     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ...     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        ...     [".", "6", ".", ".", ".", ".", "2", "8", "."],
        ...     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ...     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ... ]
        >>> solve_sudoku(board)
        True
        >>> board[0][2]
        '4'
    """
    empty = _find_empty(board)
    if not empty:
        return True  # Solved

    row, col = empty

    for digit in "123456789":
        if _is_valid(board, row, col, digit):
            board[row][col] = digit

            if solve_sudoku(board):
                return True

            board[row][col] = "."

    return False


def _find_empty(board: list[list[str]]) -> tuple[int, int] | None:
    """Find next empty cell."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return (i, j)
    return None


def _is_valid(board: list[list[str]], row: int, col: int, digit: str) -> bool:
    """Check if digit is valid at position."""
    # Check row
    if digit in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == digit:
            return False

    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == digit:
                return False

    return True


def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Check if a Sudoku board is valid.

    Args:
        board: 9x9 grid with digits '1'-'9' and '.' for empty cells.

    Returns:
        True if current state is valid.

    Example:
        >>> board = [
        ...     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ...     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ...     [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ...     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ...     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ...     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        ...     [".", "6", ".", ".", ".", ".", "2", "8", "."],
        ...     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ...     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ... ]
        >>> is_valid_sudoku(board)
        True
    """
    # Check rows
    for row in board:
        seen: set[str] = set()
        for cell in row:
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)

    # Check columns
    for col in range(9):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)

    # Check 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    cell = board[box_row * 3 + i][box_col * 3 + j]
                    if cell != ".":
                        if cell in seen:
                            return False
                        seen.add(cell)

    return True
