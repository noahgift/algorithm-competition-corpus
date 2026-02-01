"""Topological Sort Algorithms.

Implements topological sorting for Directed Acyclic Graphs (DAGs)
using both Kahn's algorithm (BFS) and DFS-based approach.

Time Complexity: O(V + E)
Space Complexity: O(V)

References:
    [1] Kahn, A.B. (1962). "Topological sorting of large networks".
        Communications of the ACM. 5(11): 558-562. doi:10.1145/368996.369025

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 22.4.

Invariants (Popperian Falsification):
    P1: For every edge (u,v), u appears before v in the ordering
    P2: Result contains all nodes iff graph is a DAG
    P3: Result is None iff graph contains a cycle
    P4: All nodes appear exactly once in the result
"""

from __future__ import annotations

from collections import deque


def topological_sort_kahn(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[int] | None:
    """Topological sort using Kahn's algorithm (BFS-based).

    Args:
        graph: Adjacency list representation of the DAG.
        nodes: List of all nodes in the graph.

    Returns:
        Topologically sorted list of nodes, or None if cycle exists.

    Examples:
        >>> topological_sort_kahn({0: [1, 2], 1: [3], 2: [3], 3: []}, [0, 1, 2, 3])
        [0, 1, 2, 3]

        >>> topological_sort_kahn({0: [1], 1: [0]}, [0, 1]) is None
        True

        >>> topological_sort_kahn({0: []}, [0])
        [0]
    """
    in_degree: dict[int, int] = dict.fromkeys(nodes, 0)

    for node in nodes:
        for neighbor in graph.get(node, []):
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    queue: deque[int] = deque()
    for node in nodes:
        if in_degree[node] == 0:
            queue.append(node)

    result: list[int] = []

    while queue:
        node: int = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(nodes):
        return None

    return result


def topological_sort_dfs(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[int] | None:
    """Topological sort using iterative DFS-based approach.

    Args:
        graph: Adjacency list representation of the DAG.
        nodes: List of all nodes in the graph.

    Returns:
        Topologically sorted list of nodes, or None if cycle exists.

    Examples:
        >>> result = topological_sort_dfs(
        ...     {0: [1, 2], 1: [3], 2: [3], 3: []}, [0, 1, 2, 3]
        ... )
        >>> result[0]
        0
        >>> result[-1]
        3

        >>> topological_sort_dfs({0: [1], 1: [0]}, [0, 1]) is None
        True
    """
    white: int = 0
    gray: int = 1
    black: int = 2

    color: dict[int, int] = dict.fromkeys(nodes, white)
    result: list[int] = []

    for start_node in nodes:
        if color[start_node] != white:
            continue

        stack: list[tuple[int, bool]] = [(start_node, False)]

        while stack:
            node, processed = stack.pop()

            if processed:
                color[node] = black
                result.append(node)
                continue

            if color[node] == gray:
                # Cycle detected
                return None

            if color[node] == black:
                continue

            color[node] = gray
            stack.append((node, True))

            for neighbor in graph.get(node, []):
                if color.get(neighbor, white) == gray:
                    return None
                if color.get(neighbor, white) == white:
                    stack.append((neighbor, False))

    result.reverse()
    return result


def all_topological_sorts(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[list[int]]:
    """Find all valid topological orderings.

    Uses iterative approach with explicit state management.

    Args:
        graph: Adjacency list representation of the DAG.
        nodes: List of all nodes in the graph.

    Returns:
        List of all valid topological orderings.

    Examples:
        >>> sorted(all_topological_sorts({0: [2], 1: [2], 2: []}, [0, 1, 2]))
        [[0, 1, 2], [1, 0, 2]]

        >>> all_topological_sorts({0: []}, [0])
        [[0]]
    """
    in_degree: dict[int, int] = dict.fromkeys(nodes, 0)

    for node in nodes:
        for neighbor in graph.get(node, []):
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    result: list[list[int]] = []

    # Stack contains: (current_order, in_degree_snapshot, visited)
    initial_state: tuple[list[int], dict[int, int], set[int]] = (
        [],
        in_degree.copy(),
        set(),
    )
    stack: list[tuple[list[int], dict[int, int], set[int]]] = [initial_state]

    while stack:
        current, curr_in_degree, visited = stack.pop()

        if len(current) == len(nodes):
            result.append(current)
            continue

        # Find all nodes with in-degree 0 that haven't been visited
        available: list[int] = [
            node for node in nodes if node not in visited and curr_in_degree[node] == 0
        ]

        for node in available:
            new_current = current + [node]
            new_visited = visited | {node}
            new_in_degree = curr_in_degree.copy()

            for neighbor in graph.get(node, []):
                new_in_degree[neighbor] -= 1

            stack.append((new_current, new_in_degree, new_visited))

    return result
