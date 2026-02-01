"""Bellman-Ford Algorithm for Shortest Paths.

Finds shortest paths from a source to all vertices, handling
negative edge weights and detecting negative cycles.

Time Complexity: O(V * E)
Space Complexity: O(V)

References:
    [1] Bellman, R. (1958). "On a routing problem".
        Quarterly of Applied Mathematics. 16: 87-90.

    [2] Ford, L.R. Jr. (1956). "Network Flow Theory".
        RAND Corporation Paper P-923.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 24.1.

Invariants (Popperian Falsification):
    P1: After k iterations, d[v] is length of shortest path using <= k edges
    P2: If no negative cycle, algorithm terminates in V-1 iterations
    P3: Negative cycle detected iff distance decreases in iteration V
    P4: Triangle inequality: d[u] + w(u,v) >= d[v] after relaxation
"""

from __future__ import annotations

INF: int = 10**18  # Large value representing infinity


def bellman_ford(
    edges: list[tuple[int, int, int]],
    n: int,
    start: int,
) -> dict[int, int] | None:
    """Find shortest distances from start to all nodes.

    Args:
        edges: List of edges as (u, v, weight).
        n: Number of nodes (0 to n-1).
        start: The starting node.

    Returns:
        Dictionary of shortest distances, or None if negative cycle exists.

    Examples:
        >>> bellman_ford([(0, 1, 4), (0, 2, 5), (1, 2, -3)], 3, 0)
        {0: 0, 1: 4, 2: 1}

        >>> bellman_ford([(0, 1, 1), (1, 2, -1), (2, 0, -1)], 3, 0) is None
        True

        >>> bellman_ford([], 1, 0)
        {0: 0}
    """
    dist: dict[int, int] = dict.fromkeys(range(n), INF)
    dist[start] = 0

    for _ in range(n - 1):
        updated: bool = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None

    return dist


def bellman_ford_with_path(
    edges: list[tuple[int, int, int]],
    n: int,
    start: int,
    end: int,
) -> tuple[int, list[int]]:
    """Find shortest path and distance from start to end.

    Args:
        edges: List of edges as (u, v, weight).
        n: Number of nodes (0 to n-1).
        start: The starting node.
        end: The target node.

    Returns:
        Tuple of (distance, path). Distance is -1 if negative cycle or no path.

    Examples:
        >>> bellman_ford_with_path([(0, 1, 2), (1, 2, 3)], 3, 0, 2)
        (5, [0, 1, 2])

        >>> bellman_ford_with_path([(0, 1, 1)], 3, 0, 2)
        (-1, [])
    """
    dist: dict[int, int] = dict.fromkeys(range(n), INF)
    parent: dict[int, int] = dict.fromkeys(range(n), -1)
    dist[start] = 0

    for _ in range(n - 1):
        updated: bool = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return -1, []

    if dist[end] == INF:
        return -1, []

    path: list[int] = []
    current: int = end
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return dist[end], path


def find_negative_cycle(
    edges: list[tuple[int, int, int]],
    n: int,
) -> list[int]:
    """Find a negative cycle in the graph if one exists.

    Args:
        edges: List of edges as (u, v, weight).
        n: Number of nodes (0 to n-1).

    Returns:
        List of nodes forming a negative cycle, or empty list if none.

    Examples:
        >>> cycle = find_negative_cycle([(0, 1, 1), (1, 2, -1), (2, 0, -1)], 3)
        >>> len(cycle)
        3
        >>> set(cycle) == {0, 1, 2}
        True

        >>> find_negative_cycle([(0, 1, 1), (1, 2, 1)], 3)
        []
    """
    dist: dict[int, int] = dict.fromkeys(range(n), 0)
    parent: dict[int, int] = dict.fromkeys(range(n), -1)

    cycle_node: int = -1

    for _ in range(n):
        cycle_node = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                cycle_node = v

    if cycle_node == -1:
        return []

    # Go back n steps to ensure we're in the cycle
    current: int = cycle_node
    for _ in range(n):
        current = parent[current]

    # Extract the cycle
    cycle: list[int] = []
    node: int = current
    while True:
        cycle.append(node)
        node = parent[node]
        if node == current:
            break

    cycle.reverse()
    return cycle


def shortest_path_with_k_edges(
    edges: list[tuple[int, int, int]],
    n: int,
    start: int,
    end: int,
    k: int,
) -> int:
    """Find shortest path using at most k edges.

    Args:
        edges: List of edges as (u, v, weight).
        n: Number of nodes (0 to n-1).
        start: The starting node.
        end: The target node.
        k: Maximum number of edges allowed.

    Returns:
        Shortest distance, or -1 if no path with at most k edges.

    Examples:
        >>> shortest_path_with_k_edges(
        ...     [(0, 1, 1), (1, 2, 1), (0, 2, 5)], 3, 0, 2, 1
        ... )
        5

        >>> shortest_path_with_k_edges(
        ...     [(0, 1, 1), (1, 2, 1), (0, 2, 5)], 3, 0, 2, 2
        ... )
        2

        >>> shortest_path_with_k_edges([(0, 1, 1)], 3, 0, 2, 2)
        -1
    """
    dist: list[int] = [INF] * n
    dist[start] = 0

    for _ in range(k):
        new_dist: list[int] = dist[:]
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w
        dist = new_dist

    if dist[end] == INF:
        return -1
    return dist[end]
