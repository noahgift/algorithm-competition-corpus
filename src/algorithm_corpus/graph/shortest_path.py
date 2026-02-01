"""Shortest path algorithms.

Additional shortest path algorithms for weighted graphs.

References:
    Floyd, R.W. (1962). "Algorithm 97: Shortest Path."
    Communications of the ACM 5(6): 345.
"""

from __future__ import annotations


def floyd_warshall(graph: list[list[float]]) -> list[list[float]]:
    """Find shortest paths between all pairs of vertices.

    Floyd-Warshall algorithm using dynamic programming.

    Args:
        graph: Adjacency matrix where graph[i][j] is edge weight.
               Use float('inf') for no edge.

    Returns:
        Distance matrix with shortest paths.

    Example:
        >>> graph = [
        ...     [0, 5, float("inf"), 10],
        ...     [float("inf"), 0, 3, float("inf")],
        ...     [float("inf"), float("inf"), 0, 1],
        ...     [float("inf"), float("inf"), float("inf"), 0],
        ... ]
        >>> result = floyd_warshall(graph)
        >>> result[0][2]
        8
    """
    n = len(graph)
    dist = [row[:] for row in graph]  # Deep copy

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def shortest_path_unweighted(graph: dict[int, list[int]], start: int, end: int) -> int:
    """Find shortest path in unweighted graph.

    Uses BFS for O(V + E) complexity.

    Args:
        graph: Adjacency list representation.
        start: Starting vertex.
        end: Ending vertex.

    Returns:
        Shortest path length, or -1 if no path.

    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [3], 3: []}
        >>> shortest_path_unweighted(graph, 0, 3)
        2
    """
    if start == end:
        return 0

    visited: set[int] = {start}
    queue: list[tuple[int, int]] = [(start, 0)]  # (node, distance)

    while queue:
        node, dist = queue.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1


def has_negative_cycle(graph: list[list[tuple[int, int]]]) -> bool:
    """Detect negative cycle in weighted graph.

    Uses Bellman-Ford relaxation check.

    Args:
        graph: Adjacency list where graph[u] = [(v, weight), ...].

    Returns:
        True if negative cycle exists.

    Example:
        >>> graph = [[(1, 1)], [(2, -2)], [(0, -1)]]  # Cycle: 0->1->2->0 = -2
        >>> has_negative_cycle(graph)
        True
    """
    n = len(graph)
    if n == 0:
        return False

    dist = [0] * n  # Start with all zeros

    # Relax all edges n-1 times
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                dist[v] = min(dist[v], dist[u] + weight)

    # Check for negative cycle
    for u in range(n):
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                return True

    return False
