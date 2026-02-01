"""Matrix search algorithms.

Binary search in sorted matrices.
"""

from __future__ import annotations


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Search for target in row-sorted matrix.

    Matrix is sorted such that each row is sorted and first element
    of each row is greater than last element of previous row.

    Uses binary search treating matrix as 1D array.

    Args:
        matrix: 2D sorted matrix.
        target: Value to search for.

    Returns:
        True if target found.

    Example:
        >>> search_matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9)
        True
        >>> search_matrix([[1, 3, 5], [7, 9, 11]], 6)
        False
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = mid // cols, mid % cols
        val = matrix[row][col]

        if val == target:
            return True
        if val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_matrix_2d(matrix: list[list[int]], target: int) -> bool:
    """Search for target in row and column sorted matrix.

    Matrix has rows sorted and columns sorted independently.

    Uses staircase search from top-right corner.

    Args:
        matrix: 2D matrix sorted by rows and columns.
        target: Value to search for.

    Returns:
        True if target found.

    Example:
        >>> search_matrix_2d([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 5)
        True
        >>> search_matrix_2d([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 10)
        False
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from top-right corner
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        if val < target:
            row += 1
        else:
            col -= 1

    return False
