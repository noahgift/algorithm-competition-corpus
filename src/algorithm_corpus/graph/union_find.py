"""Union-Find (Disjoint Set Union) Data Structure.

Implements Union-Find with path compression and union by rank
for efficient set operations.

Time Complexity: O(alpha(n)) amortized per operation (inverse Ackermann)
Space Complexity: O(n)

References:
    [1] Tarjan, R.E. (1975). "Efficiency of a Good But Not Linear Set Union
        Algorithm". Journal of the ACM. 22(2): 215-225. doi:10.1145/321879.321884

    [2] Tarjan, R.E., van Leeuwen, J. (1984). "Worst-case Analysis of Set Union
        Algorithms". Journal of the ACM. 31(2): 245-281.

Invariants (Popperian Falsification):
    P1: find(x) == find(y) iff x and y are in same set
    P2: After union(x,y), find(x) == find(y)
    P3: Number of components decreases by 1 after successful union
    P4: find(x) always returns a valid representative
"""

from __future__ import annotations


class UnionFind:
    """Disjoint Set Union with path compression and union by rank.

    Examples:
        >>> uf = UnionFind(5)
        >>> uf.union(0, 1)
        True
        >>> uf.connected(0, 1)
        True
        >>> uf.connected(0, 2)
        False
        >>> uf.get_count()
        4
    """

    def __init__(self, n: int) -> None:
        """Initialize n disjoint sets.

        Args:
            n: Number of elements (0 to n-1).
        """
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n
        self.count: int = n

    def find(self, x: int) -> int:
        """Find the representative of the set containing x.

        Uses path compression for efficiency.

        Args:
            x: Element to find.

        Returns:
            Representative of the set containing x.

        Examples:
            >>> uf = UnionFind(3)
            >>> uf.find(0)
            0
            >>> uf.union(0, 1)
            True
            >>> uf.find(1) == uf.find(0)
            True
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union the sets containing x and y.

        Uses union by rank for efficiency.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if union was performed, False if already in same set.

        Examples:
            >>> uf = UnionFind(3)
            >>> uf.union(0, 1)
            True
            >>> uf.union(0, 1)
            False
        """
        root_x: int = self.find(x)
        root_y: int = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if x and y are in the same set.

        Examples:
            >>> uf = UnionFind(3)
            >>> uf.connected(0, 1)
            False
            >>> uf.union(0, 1)
            True
            >>> uf.connected(0, 1)
            True
        """
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """Return the number of disjoint sets.

        Returns:
            Number of disjoint sets.

        Examples:
            >>> uf = UnionFind(5)
            >>> uf.get_count()
            5
            >>> uf.union(0, 1)
            True
            >>> uf.get_count()
            4
        """
        return self.count


def count_connected_components(n: int, edges: list[list[int]]) -> int:
    """Count connected components using Union-Find.

    Args:
        n: Number of nodes.
        edges: List of edges [u, v].

    Returns:
        Number of connected components.

    Examples:
        >>> count_connected_components(5, [[0, 1], [1, 2], [3, 4]])
        2

        >>> count_connected_components(3, [])
        3

        >>> count_connected_components(4, [[0, 1], [1, 2], [2, 3]])
        1
    """
    uf: UnionFind = UnionFind(n)

    for edge in edges:
        uf.union(edge[0], edge[1])

    return uf.get_count()


def is_valid_tree(n: int, edges: list[list[int]]) -> bool:
    """Check if the graph forms a valid tree.

    A valid tree has exactly n-1 edges and is connected.

    Args:
        n: Number of nodes.
        edges: List of edges [u, v].

    Returns:
        True if the graph is a valid tree.

    Examples:
        >>> is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
        True

        >>> is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
        False

        >>> is_valid_tree(2, [])
        False
    """
    if len(edges) != n - 1:
        return False

    uf: UnionFind = UnionFind(n)

    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return False

    return uf.get_count() == 1


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    """Find the edge that creates a cycle.

    Given edges of an undirected graph with n nodes and n edges,
    find the edge that, if removed, would make it a tree.

    Args:
        edges: List of edges [u, v] (1-indexed).

    Returns:
        The redundant edge.

    Examples:
        >>> find_redundant_connection([[1, 2], [1, 3], [2, 3]])
        [2, 3]

        >>> find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
        [1, 4]
    """
    n: int = len(edges)
    uf: UnionFind = UnionFind(n + 1)

    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return edge

    return []
