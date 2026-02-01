"""DFS Traversal - Iterative Implementation.

Implements Depth-First Search traversal for graphs using an
iterative approach with explicit stack (preferred for Rust transpilation).

Time Complexity: O(V + E)
Space Complexity: O(V)

References:
    [1] Tarjan, R.E. (1972). "Depth-first search and linear graph algorithms".
        SIAM Journal on Computing. 1(2): 146-160. doi:10.1137/0201010

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 22.3.

Invariants (Popperian Falsification):
    P1: Each node appears at most once in output
    P2: Output size equals number of reachable nodes
    P3: All output nodes are reachable from start
    P4: Preorder visits parent before children
"""

from __future__ import annotations


def dfs_iterative(
    graph: dict[int, list[int]],
    start: int,
) -> list[int]:
    """Perform DFS traversal iteratively using a stack.

    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.

    Returns:
        List of nodes in DFS order.

    Examples:
        >>> dfs_iterative({0: [1, 2], 1: [3], 2: [], 3: []}, 0)
        [0, 1, 3, 2]

        >>> dfs_iterative({0: []}, 0)
        [0]

        >>> dfs_iterative({0: [1], 1: [0]}, 0)
        [0, 1]
    """
    visited: set[int] = set()
    result: list[int] = []
    stack: list[int] = [start]

    while stack:
        node: int = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_all_paths(
    graph: dict[int, list[int]],
    start: int,
    end: int,
) -> list[list[int]]:
    """Find all paths from start to end using iterative DFS.

    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.
        end: The target node.

    Returns:
        List of all paths from start to end.

    Examples:
        >>> sorted(dfs_all_paths({0: [1, 2], 1: [3], 2: [3], 3: []}, 0, 3))
        [[0, 1, 3], [0, 2, 3]]

        >>> dfs_all_paths({0: [1], 1: []}, 0, 0)
        [[0]]

        >>> dfs_all_paths({0: [], 1: []}, 0, 1)
        []
    """
    if start == end:
        return [[start]]

    all_paths: list[list[int]] = []
    stack: list[tuple[int, list[int], set[int]]] = [(start, [start], {start})]

    while stack:
        node, path, visited = stack.pop()

        if node == end:
            all_paths.append(path)
            continue

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_visited = visited | {neighbor}
                stack.append((neighbor, path + [neighbor], new_visited))

    return all_paths


def dfs_preorder_postorder(
    graph: dict[int, list[int]],
    start: int,
) -> tuple[list[int], list[int]]:
    """Return both preorder and postorder DFS traversals.

    Uses iterative approach with state tracking.

    Args:
        graph: Adjacency list representation of the graph.
        start: The starting node.

    Returns:
        Tuple of (preorder, postorder) traversal lists.

    Examples:
        >>> pre, post = dfs_preorder_postorder({0: [1, 2], 1: [], 2: []}, 0)
        >>> pre
        [0, 1, 2]
        >>> post
        [1, 2, 0]

        >>> pre, post = dfs_preorder_postorder({0: []}, 0)
        >>> pre, post
        ([0], [0])
    """
    visited: set[int] = set()
    preorder: list[int] = []
    postorder: list[int] = []

    # Stack contains (node, is_processed) tuples
    stack: list[tuple[int, bool]] = [(start, False)]

    while stack:
        node, is_processed = stack.pop()

        if is_processed:
            postorder.append(node)
            continue

        if node in visited:
            continue

        visited.add(node)
        preorder.append(node)

        # Push node again for postorder processing
        stack.append((node, True))

        # Push children in reverse order for correct traversal order
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, False))

    return preorder, postorder
