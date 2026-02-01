"""Connected Components in Graphs.

Finds all connected components in undirected graphs and
strongly connected components in directed graphs.

Time Complexity: O(V + E)
Space Complexity: O(V)

References:
    [1] Kosaraju, S.R. (1978). Unpublished manuscript.
        Described in Aho, Hopcroft, Ullman (1983).

    [2] Tarjan, R.E. (1972). "Depth-first search and linear graph algorithms".
        SIAM Journal on Computing. 1(2): 146-160. doi:10.1137/0201010

    [3] Sharir, M. (1981). "A strong-connectivity algorithm and its
        applications in data flow analysis". Computers & Mathematics
        with Applications. 7(1): 67-72.

Invariants (Popperian Falsification):
    P1: Components partition all nodes (each node in exactly one component)
    P2: All nodes in a component are mutually reachable
    P3: No edge exists between different SCCs in condensation graph order
    P4: Number of components <= number of nodes
"""

from __future__ import annotations

from collections import deque


def find_connected_components(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[list[int]]:
    """Find all connected components in an undirected graph using DFS.

    Args:
        graph: Adjacency list representation.
        nodes: List of all nodes.

    Returns:
        List of components, each component is a list of nodes.

    Examples:
        >>> sorted(
        ...     [
        ...         sorted(c)
        ...         for c in find_connected_components(
        ...             {0: [1], 1: [0], 2: [3], 3: [2]}, [0, 1, 2, 3]
        ...         )
        ...     ]
        ... )
        [[0, 1], [2, 3]]

        >>> find_connected_components({0: []}, [0])
        [[0]]

        >>> sorted(
        ...     [
        ...         sorted(c)
        ...         for c in find_connected_components(
        ...             {0: [1, 2], 1: [0], 2: [0]}, [0, 1, 2]
        ...         )
        ...     ]
        ... )
        [[0, 1, 2]]
    """
    visited: set[int] = set()
    components: list[list[int]] = []

    for start in nodes:
        if start in visited:
            continue

        component: list[int] = []
        stack: list[int] = [start]

        while stack:
            node: int = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            component.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

        components.append(component)

    return components


def find_connected_components_bfs(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[list[int]]:
    """Find all connected components in an undirected graph using BFS.

    Args:
        graph: Adjacency list representation.
        nodes: List of all nodes.

    Returns:
        List of components, each component is a list of nodes.

    Examples:
        >>> sorted(
        ...     [
        ...         sorted(c)
        ...         for c in find_connected_components_bfs(
        ...             {0: [1], 1: [0], 2: []}, [0, 1, 2]
        ...         )
        ...     ]
        ... )
        [[0, 1], [2]]

        >>> find_connected_components_bfs({0: []}, [0])
        [[0]]
    """
    visited: set[int] = set()
    components: list[list[int]] = []

    for start in nodes:
        if start in visited:
            continue

        component: list[int] = []
        queue: deque[int] = deque([start])
        visited.add(start)

        while queue:
            node: int = queue.popleft()
            component.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        components.append(component)

    return components


def kosaraju_scc(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[list[int]]:
    """Find strongly connected components using Kosaraju's algorithm.

    Uses iterative DFS for both passes.

    Args:
        graph: Adjacency list of directed graph.
        nodes: List of all nodes.

    Returns:
        List of SCCs, each SCC is a list of nodes.

    Examples:
        >>> sorted(
        ...     [
        ...         sorted(c)
        ...         for c in kosaraju_scc(
        ...             {0: [1], 1: [2], 2: [0], 3: [2]}, [0, 1, 2, 3]
        ...         )
        ...     ]
        ... )
        [[0, 1, 2], [3]]

        >>> kosaraju_scc({0: []}, [0])
        [[0]]
    """
    # First pass: get finish order
    visited: set[int] = set()
    order: list[int] = []

    for start in nodes:
        if start in visited:
            continue

        stack: list[tuple[int, bool]] = [(start, False)]

        while stack:
            node, processed = stack.pop()

            if processed:
                order.append(node)
                continue

            if node in visited:
                continue

            visited.add(node)
            stack.append((node, True))

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append((neighbor, False))

    # Build reverse graph
    reverse_graph: dict[int, list[int]] = {node: [] for node in nodes}
    for node in nodes:
        for neighbor in graph.get(node, []):
            reverse_graph[neighbor].append(node)

    # Second pass: find SCCs
    visited.clear()
    sccs: list[list[int]] = []

    for node in reversed(order):
        if node in visited:
            continue

        component: list[int] = []
        stack: list[int] = [node]

        while stack:
            curr: int = stack.pop()
            if curr in visited:
                continue

            visited.add(curr)
            component.append(curr)

            for neighbor in reverse_graph.get(curr, []):
                if neighbor not in visited:
                    stack.append(neighbor)

        sccs.append(component)

    return sccs


def tarjan_scc(
    graph: dict[int, list[int]],
    nodes: list[int],
) -> list[list[int]]:
    """Find strongly connected components using Tarjan's algorithm.

    Uses iterative implementation with explicit stack management.

    Args:
        graph: Adjacency list of directed graph.
        nodes: List of all nodes.

    Returns:
        List of SCCs, each SCC is a list of nodes.

    Examples:
        >>> sorted(
        ...     [
        ...         sorted(c)
        ...         for c in tarjan_scc(
        ...             {0: [1], 1: [2], 2: [0, 3], 3: []}, [0, 1, 2, 3]
        ...         )
        ...     ]
        ... )
        [[0, 1, 2], [3]]

        >>> tarjan_scc({0: []}, [0])
        [[0]]
    """
    index_counter: list[int] = [0]
    index: dict[int, int] = {}
    lowlink: dict[int, int] = {}
    on_stack: set[int] = set()
    stack: list[int] = []
    sccs: list[list[int]] = []

    for start in nodes:
        if start in index:
            continue

        # Work stack contains (node, neighbor_index, is_root_call)
        work_stack: list[tuple[int, int, bool]] = [(start, 0, True)]

        while work_stack:
            node, neighbor_idx, is_root = work_stack.pop()

            if is_root:
                if node in index:
                    continue

                index[node] = index_counter[0]
                lowlink[node] = index_counter[0]
                index_counter[0] += 1
                stack.append(node)
                on_stack.add(node)

            neighbors = graph.get(node, [])

            # Process neighbors starting from neighbor_idx
            while neighbor_idx < len(neighbors):
                neighbor = neighbors[neighbor_idx]
                neighbor_idx += 1

                if neighbor not in index:
                    # Save current state and process neighbor
                    work_stack.append((node, neighbor_idx, False))
                    work_stack.append((neighbor, 0, True))
                    break
                if neighbor in on_stack:
                    lowlink[node] = min(lowlink[node], index[neighbor])
            else:
                # All neighbors processed - check if root of SCC
                if lowlink[node] == index[node]:
                    component: list[int] = []
                    while True:
                        w: int = stack.pop()
                        on_stack.remove(w)
                        component.append(w)
                        if w == node:
                            break
                    sccs.append(component)

                # Update parent's lowlink if we came from a parent
                if work_stack:
                    parent_node = work_stack[-1][0]
                    if parent_node in lowlink:
                        lowlink[parent_node] = min(lowlink[parent_node], lowlink[node])

    return sccs
