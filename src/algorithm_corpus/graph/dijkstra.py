"""Dijkstra's Algorithm for Single-Source Shortest Paths.

Finds the shortest path from a source node to all other nodes in a
weighted graph with non-negative edge weights.

Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V)

References:
    [1] Dijkstra, E.W. (1959). "A note on two problems in connexion with graphs".
        Numerische Mathematik. 1: 269-271. doi:10.1007/BF01386390

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 24.3.

Invariants (Popperian Falsification):
    P1: All computed distances are non-negative (d[v] >= 0 for all v)
    P2: Triangle inequality holds: d[u] + w(u,v) >= d[v] for relaxed edges
    P3: Source distance is zero: d[source] = 0
    P4: Distances are optimal: no shorter path exists
"""

from __future__ import annotations

import heapq


def dijkstra(
    graph: dict[int, list[tuple[int, int]]],
    start: int,
) -> dict[int, int]:
    """Find shortest distances from start to all reachable nodes.

    Args:
        graph: Adjacency list where graph[u] = [(v, weight), ...].
        start: The starting node.

    Returns:
        Dictionary mapping each reachable node to its shortest distance.

    Examples:
        >>> result = dijkstra(
        ...     {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}, 0
        ... )
        >>> result[0], result[1], result[2], result[3]
        (0, 3, 1, 4)

        >>> dijkstra({0: []}, 0)
        {0: 0}

        >>> dijkstra({0: [(1, 10)], 1: []}, 0)
        {0: 0, 1: 10}
    """
    distances: dict[int, int] = {start: 0}
    heap: list[tuple[int, int]] = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distances.get(node, float("inf")):
            continue

        for neighbor, weight in graph.get(node, []):
            new_dist: int = dist + weight

            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


def dijkstra_with_path(
    graph: dict[int, list[tuple[int, int]]],
    start: int,
    end: int,
) -> tuple[int, list[int]]:
    """Find shortest path and its distance from start to end.

    Args:
        graph: Adjacency list where graph[u] = [(v, weight), ...].
        start: The starting node.
        end: The target node.

    Returns:
        Tuple of (distance, path). Distance is -1 if no path exists.

    Examples:
        >>> dijkstra_with_path({0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}, 0, 2)
        (3, [0, 1, 2])

        >>> dijkstra_with_path({0: [], 1: []}, 0, 1)
        (-1, [])

        >>> dijkstra_with_path({0: [(1, 5)], 1: []}, 0, 0)
        (0, [0])
    """
    if start == end:
        return 0, [start]

    distances: dict[int, int] = {start: 0}
    parent: dict[int, int] = {}
    heap: list[tuple[int, int]] = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if node == end:
            path: list[int] = []
            current: int = end
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return dist, path

        if dist > distances.get(node, float("inf")):
            continue

        for neighbor, weight in graph.get(node, []):
            new_dist: int = dist + weight

            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    return -1, []


def dijkstra_k_shortest(
    graph: dict[int, list[tuple[int, int]]],
    start: int,
    end: int,
    k: int,
) -> list[int]:
    """Find the k shortest path distances from start to end.

    Uses a modified Dijkstra that allows revisiting nodes.

    Args:
        graph: Adjacency list where graph[u] = [(v, weight), ...].
        start: The starting node.
        end: The target node.
        k: Number of shortest paths to find.

    Returns:
        List of k shortest distances (may be fewer if not enough paths exist).

    Examples:
        >>> dijkstra_k_shortest({0: [(1, 1), (2, 2)], 1: [(2, 1)], 2: []}, 0, 2, 2)
        [2, 2]

        >>> dijkstra_k_shortest({0: [(1, 1)], 1: []}, 0, 1, 3)
        [1]

        >>> dijkstra_k_shortest({0: []}, 0, 1, 1)
        []
    """
    counts: dict[int, int] = {}
    result: list[int] = []
    heap: list[tuple[int, int]] = [(0, start)]

    while heap and len(result) < k:
        dist, node = heapq.heappop(heap)

        counts[node] = counts.get(node, 0) + 1

        if node == end:
            result.append(dist)

        if counts[node] <= k:
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(heap, (dist + weight, neighbor))

    return result
