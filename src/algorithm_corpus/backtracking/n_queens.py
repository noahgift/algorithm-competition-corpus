"""N-Queens Problem.

Place N queens on an NxN chessboard with no attacks.

Time Complexity: O(N!)
Space Complexity: O(N)

References:
    [1] Dijkstra, E.W. (1972). "Notes on Structured Programming".
        Academic Press.

Invariants (Popperian Falsification):
    P1: No two queens attack each other
    P2: Exactly N queens placed
    P3: All solutions are distinct
    P4: N=0 returns empty, N=1 returns one solution
"""

from __future__ import annotations


def n_queens(n: int) -> list[list[int]]:
    """Find all solutions to N-Queens problem.

    Args:
        n: Board size and number of queens.

    Returns:
        List of solutions. Each solution is a list of column positions.

    Examples:
        >>> n_queens(4)
        [[1, 3, 0, 2], [2, 0, 3, 1]]

        >>> n_queens(1)
        [[0]]

        >>> n_queens(0)
        [[]]
    """
    if n == 0:
        return [[]]

    result: list[list[int]] = []

    def _is_safe(queens: list[int], row: int, col: int) -> bool:
        for r in range(row):
            c = queens[r]
            # Same column or diagonal
            if c == col or abs(c - col) == row - r:
                return False
        return True

    def _backtrack(queens: list[int]) -> None:
        row = len(queens)
        if row == n:
            result.append(queens[:])
            return

        for col in range(n):
            if _is_safe(queens, row, col):
                queens.append(col)
                _backtrack(queens)
                queens.pop()

    _backtrack([])
    return result


def n_queens_count(n: int) -> int:
    """Count number of N-Queens solutions.

    Args:
        n: Board size and number of queens.

    Returns:
        Number of distinct solutions.

    Examples:
        >>> n_queens_count(4)
        2

        >>> n_queens_count(8)
        92

        >>> n_queens_count(1)
        1

        >>> n_queens_count(0)
        1
    """
    return len(n_queens(n))
