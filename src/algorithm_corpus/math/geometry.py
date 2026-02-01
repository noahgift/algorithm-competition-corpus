"""Geometry algorithms.

Basic computational geometry.
"""

from __future__ import annotations


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor."""
    while b:
        a, b = b, a % b
    return a


def max_points_on_line(points: list[tuple[int, int]]) -> int:
    """Find maximum points on a single line.

    Uses slope representation with GCD for precision.

    Args:
        points: List of (x, y) coordinates.

    Returns:
        Maximum number of points on one line.

    Example:
        >>> max_points_on_line([(1, 1), (2, 2), (3, 3)])
        3
        >>> max_points_on_line([(1, 1), (3, 2), (5, 3), (4, 1), (2, 3), (1, 4)])
        4
    """
    if len(points) <= 2:  # noqa: PLR2004
        return len(points)

    max_count = 1

    for i, (x1, y1) in enumerate(points):
        slopes: dict[tuple[int, int], int] = {}
        duplicates = 1

        for x2, y2 in points[i + 1 :]:
            if x1 == x2 and y1 == y2:
                duplicates += 1
            else:
                dx = x2 - x1
                dy = y2 - y1
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g

                # Normalize direction
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                slope = (dx, dy)
                slopes[slope] = slopes.get(slope, 0) + 1

        current_max = duplicates
        for count in slopes.values():
            current_max = max(current_max, count + duplicates)

        max_count = max(max_count, current_max)

    return max_count


def valid_square(
    p1: tuple[int, int],
    p2: tuple[int, int],
    p3: tuple[int, int],
    p4: tuple[int, int],
) -> bool:
    """Check if four points form a valid square.

    Args:
        p1: First point.
        p2: Second point.
        p3: Third point.
        p4: Fourth point.

    Returns:
        True if points form a square.

    Example:
        >>> valid_square((0, 0), (1, 1), (1, 0), (0, 1))
        True
        >>> valid_square((0, 0), (1, 1), (1, 0), (0, 2))
        False
    """

    def dist_sq(a: tuple[int, int], b: tuple[int, int]) -> int:
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    distances = sorted(
        [
            dist_sq(p1, p2),
            dist_sq(p1, p3),
            dist_sq(p1, p4),
            dist_sq(p2, p3),
            dist_sq(p2, p4),
            dist_sq(p3, p4),
        ]
    )

    # 4 equal sides, 2 equal diagonals, sides > 0
    return (
        distances[0] > 0
        and distances[0] == distances[1] == distances[2] == distances[3]
        and distances[4] == distances[5]
        and distances[4] == 2 * distances[0]
    )
