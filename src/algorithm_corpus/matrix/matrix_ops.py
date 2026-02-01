"""Matrix operations.

Basic matrix manipulation algorithms.
"""

from __future__ import annotations


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a matrix.

    Swap rows and columns.

    Args:
        matrix: 2D list of integers.

    Returns:
        Transposed matrix.

    Example:
        >>> transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def rotate_90(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate matrix 90 degrees clockwise.

    First transpose, then reverse each row.

    Args:
        matrix: Square 2D list of integers.

    Returns:
        Rotated matrix.

    Example:
        >>> rotate_90([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
        >>> rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    if not matrix or not matrix[0]:
        return []

    # Transpose then reverse rows
    transposed = transpose(matrix)
    return [row[::-1] for row in transposed]


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return elements in spiral order.

    Start from top-left, go right, then down, left, up, repeat.

    Args:
        matrix: 2D list of integers.

    Returns:
        Elements in spiral order.

    Example:
        >>> spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> spiral_order([[1, 2], [3, 4]])
        [1, 2, 4, 3]
    """
    if not matrix or not matrix[0]:
        return []

    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
