"""Cycle Detection in Graphs.

Detects cycles in both directed and undirected graphs using
iterative DFS-based approaches (preferred for Rust transpilation).

Time Complexity: O(V + E)
Space Complexity: O(V)

References:
    [1] Tarjan, R.E. (1972). "Depth-first search and linear graph algorithms".
        SIAM Journal on Computing. 1(2): 146-160. doi:10.1137/0201010

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 22.3.

Invariants (Popperian Falsification):
    P1: If cycle detected, returned nodes form an actual cycle
    P2: If no cycle detected, graph is acyclic
    P3: For undirected: back edge to non-parent indicates cycle
    P4: For directed: back edge (gray -> gray) indicates cycle
"""

from __future__ import annotations


def has_cycle_undirected(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> bool:
    """Detect if an undirected graph has a cycle.

    Uses iterative DFS with parent tracking.

    Args:
        graph: Adjacency list representation.
        nodes: List of all nodes.

    Returns:
        True if the graph contains a cycle.

    Examples:
        >>> has_cycle_undirected({0: [1], 1: [0, 2], 2: [1]}, [0, 1, 2])
        False

        >>> has_cycle_undirected({0: [1, 2], 1: [0, 2], 2: [0, 1]}, [0, 1, 2])
        True

        >>> has_cycle_undirected({0: []}, [0])
        False
    """
    visited: set[int] = set()

    for start in nodes:
        if start in visited:
            continue

        # Stack contains (node, parent)
        stack: list[tuple[int, int]] = [(start, -1)]

        while stack:
            node, parent = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append((neighbor, node))
                elif neighbor != parent:
                    return True

    return False


def has_cycle_directed(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> bool:
    """Detect if a directed graph has a cycle.

    Uses iterative three-color DFS: WHITE (unvisited), GRAY (in progress), BLACK (done).

    Args:
        graph: Adjacency list representation.
        nodes: List of all nodes.

    Returns:
        True if the graph contains a cycle.

    Examples:
        >>> has_cycle_directed({0: [1], 1: [2], 2: []}, [0, 1, 2])
        False

        >>> has_cycle_directed({0: [1], 1: [2], 2: [0]}, [0, 1, 2])
        True

        >>> has_cycle_directed({0: []}, [0])
        False
    """
    white: int = 0
    gray: int = 1
    black: int = 2

    color: dict[int, int] = dict.fromkeys(nodes, white)

    for start in nodes:
        if color[start] != white:
            continue

        stack: list[tuple[int, bool]] = [(start, False)]

        while stack:
            node, processed = stack.pop()

            if processed:
                color[node] = black
                continue

            if color[node] == gray:
                continue

            if color[node] == black:
                continue

            color[node] = gray
            stack.append((node, True))

            for neighbor in graph.get(node, []):
                if color.get(neighbor, white) == gray:
                    return True
                if color.get(neighbor, white) == white:
                    stack.append((neighbor, False))

    return False


def find_cycle_directed(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[int]:
    """Find and return a cycle in a directed graph.

    Args:
        graph: Adjacency list representation.
        nodes: List of all nodes.

    Returns:
        List of nodes forming a cycle, or empty list if no cycle.

    Examples:
        >>> cycle = find_cycle_directed({0: [1], 1: [2], 2: [0]}, [0, 1, 2])
        >>> len(cycle)
        3
        >>> set(cycle) == {0, 1, 2}
        True

        >>> find_cycle_directed({0: [1], 1: []}, [0, 1])
        []
    """
    white: int = 0
    gray: int = 1
    black: int = 2

    color: dict[int, int] = dict.fromkeys(nodes, white)
    parent: dict[int, int] = {}
    cycle_start: int = -1
    cycle_end: int = -1

    for start in nodes:
        if color[start] != white:
            continue

        stack: list[tuple[int, bool]] = [(start, False)]

        while stack and cycle_start == -1:
            node, processed = stack.pop()

            if processed:
                color[node] = black
                continue

            if color[node] != white:
                continue

            color[node] = gray
            stack.append((node, True))

            for neighbor in graph.get(node, []):
                if color.get(neighbor, white) == gray:
                    cycle_start = neighbor
                    cycle_end = node
                    break
                if color.get(neighbor, white) == white:
                    parent[neighbor] = node
                    stack.append((neighbor, False))

        if cycle_start != -1:
            break

    if cycle_start == -1:
        return []

    cycle: list[int] = [cycle_start]
    current: int = cycle_end
    while current != cycle_start:
        cycle.append(current)
        current = parent[current]
    cycle.reverse()

    return cycle
