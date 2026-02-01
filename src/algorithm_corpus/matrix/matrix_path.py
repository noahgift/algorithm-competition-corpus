"""Matrix path algorithms.

Finding paths through matrices.
"""

from __future__ import annotations


def unique_paths(m: int, n: int) -> int:
    """Count unique paths in m x n grid.

    From top-left to bottom-right, only moving right or down.

    Args:
        m: Number of rows.
        n: Number of columns.

    Returns:
        Number of unique paths.

    Example:
        >>> unique_paths(3, 7)
        28
        >>> unique_paths(3, 2)
        3
    """
    # DP: dp[j] = number of ways to reach column j
    dp = [1] * n

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[n - 1]


def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    """Count unique paths avoiding obstacles.

    Args:
        grid: 0 = empty, 1 = obstacle.

    Returns:
        Number of unique paths.

    Example:
        >>> unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        2
    """
    if not grid or not grid[0] or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]

    return dp[n - 1]


def min_path_sum(grid: list[list[int]]) -> int:
    """Find minimum path sum from top-left to bottom-right.

    Only moving right or down.

    Args:
        grid: Grid of non-negative integers.

    Returns:
        Minimum sum of path.

    Example:
        >>> min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        7
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[j] = grid[0][0]
            elif i == 0:
                dp[j] = dp[j - 1] + grid[i][j]
            elif j == 0:
                dp[j] = dp[j] + grid[i][j]
            else:
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[n - 1]


def word_search(board: list[list[str]], word: str) -> bool:
    """Check if word exists in board.

    Adjacent cells are horizontally or vertically neighboring.

    Args:
        board: 2D grid of characters.
        word: Word to search for.

    Returns:
        True if word exists in board.

    Example:
        >>> board = [
        ...     ["A", "B", "C", "E"],
        ...     ["S", "F", "C", "S"],
        ...     ["A", "D", "E", "E"],
        ... ]
        >>> word_search(board, "ABCCED")
        True
        >>> word_search(board, "SEE")
        True
        >>> word_search(board, "ABCB")
        False
    """
    if not board or not board[0] or not word:
        return False

    m, n = len(board), len(board[0])

    def dfs(i: int, j: int, k: int) -> bool:
        if k == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if board[i][j] != word[k]:
            return False

        # Mark as visited
        temp = board[i][j]
        board[i][j] = "#"

        # Try all directions
        found = (
            dfs(i + 1, j, k + 1)
            or dfs(i - 1, j, k + 1)
            or dfs(i, j + 1, k + 1)
            or dfs(i, j - 1, k + 1)
        )

        # Restore
        board[i][j] = temp
        return found

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True

    return False
