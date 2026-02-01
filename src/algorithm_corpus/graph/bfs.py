"""BFS Shortest Path for Unweighted Graphs.

Finds the shortest path from a source node to all other nodes in an
unweighted graph using Breadth-First Search.

Time Complexity: O(V + E)
Space Complexity: O(V)

References:
    [1] Moore, E.F. (1959). "The shortest path through a maze".
        Proceedings of the International Symposium on the Theory of Switching.
        Harvard University Press. pp. 285-292.

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 22.2.

Invariants (Popperian Falsification):
    P1: All distances are non-negative integers
    P2: Distance to source is zero: d[source] = 0
    P3: For any edge (u,v): |d[u] - d[v]| <= 1
    P4: Distances represent shortest unweighted paths
"""

from __future__ import annotations

from collections import deque


def bfs_shortest_path(
    graph: dict[int, list[int]],
    start: int,
) -> dict[int, int]:
    """Find shortest distances from start to all reachable nodes.

    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.

    Returns:
        Dictionary mapping each reachable node to its distance from start.

    Examples:
        >>> bfs_shortest_path({0: [1, 2], 1: [2], 2: []}, 0)
        {0: 0, 1: 1, 2: 1}

        >>> bfs_shortest_path({0: []}, 0)
        {0: 0}

        >>> bfs_shortest_path({0: [1], 1: [2], 2: [3], 3: []}, 0)
        {0: 0, 1: 1, 2: 2, 3: 3}
    """
    distances: dict[int, int] = {start: 0}
    queue: deque[int] = deque([start])

    while queue:
        node: int = queue.popleft()
        current_dist: int = distances[node]

        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)

    return distances


def bfs_path(
    graph: dict[int, list[int]],
    start: int,
    end: int,
) -> list[int] | None:
    """Find the shortest path from start to end.

    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.
        end: The target node.

    Returns:
        List of nodes representing the path, or None if no path exists.

    Examples:
        >>> bfs_path({0: [1, 2], 1: [3], 2: [3], 3: []}, 0, 3)
        [0, 1, 3]

        >>> bfs_path({0: [1], 1: []}, 0, 0)
        [0]

        >>> bfs_path({0: [], 1: []}, 0, 1) is None
        True
    """
    if start == end:
        return [start]

    parent: dict[int, int] = {}
    visited: set[int] = {start}
    queue: deque[int] = deque([start])

    while queue:
        node: int = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node

                if neighbor == end:
                    path: list[int] = [end]
                    current: int = end
                    while current != start:
                        current = parent[current]
                        path.append(current)
                    path.reverse()
                    return path

                queue.append(neighbor)

    return None


def bfs_level_order(
    graph: dict[int, list[int]],
    start: int,
) -> list[list[int]]:
    """Return nodes grouped by their distance from start.

    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.

    Returns:
        List of lists, where each inner list contains nodes at that distance.

    Examples:
        >>> bfs_level_order({0: [1, 2], 1: [3], 2: [3], 3: []}, 0)
        [[0], [1, 2], [3]]

        >>> bfs_level_order({0: []}, 0)
        [[0]]

        >>> bfs_level_order({0: [1], 1: [2], 2: []}, 0)
        [[0], [1], [2]]
    """
    levels: list[list[int]] = [[start]]
    visited: set[int] = {start}

    while levels[-1]:
        current_level: list[int] = levels[-1]
        next_level: list[int] = []

        for node in current_level:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)

        if next_level:
            levels.append(next_level)
        else:
            break

    return levels
