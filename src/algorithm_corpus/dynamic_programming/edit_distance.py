"""Edit Distance (Levenshtein Distance).

Finds the minimum number of operations (insert, delete, replace)
to transform one string into another.

Time Complexity: O(m * n)
Space Complexity: O(m * n) or O(min(m, n)) optimized

References:
    [1] Levenshtein, V.I. (1966). "Binary codes capable of correcting deletions,
        insertions, and reversals". Soviet Physics Doklady. 10(8): 707-710.

    [2] Wagner, R.A., Fischer, M.J. (1974). "The String-to-String Correction
        Problem". Journal of the ACM. 21(1): 168-173.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 15.

Invariants (Popperian Falsification):
    P1: edit_distance(s, s) = 0 (identity)
    P2: edit_distance(s1, s2) = edit_distance(s2, s1) (symmetry)
    P3: edit_distance(s1, s2) <= len(s1) + len(s2) (upper bound)
    P4: edit_distance >= |len(s1) - len(s2)| (lower bound)
"""

from __future__ import annotations


def edit_distance(word1: str, word2: str) -> int:
    """Calculate the edit distance between two strings.

    Args:
        word1: Source string.
        word2: Target string.

    Returns:
        Minimum number of operations to transform word1 to word2.

    Examples:
        >>> edit_distance("horse", "ros")
        3

        >>> edit_distance("intention", "execution")
        5

        >>> edit_distance("", "abc")
        3

        >>> edit_distance("abc", "abc")
        0
    """
    m: int = len(word1)
    n: int = len(word2)

    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def edit_distance_optimized(word1: str, word2: str) -> int:
    """Calculate edit distance with O(min(m, n)) space.

    Args:
        word1: Source string.
        word2: Target string.

    Returns:
        Minimum number of operations.

    Examples:
        >>> edit_distance_optimized("horse", "ros")
        3

        >>> edit_distance_optimized("abc", "def")
        3
    """
    if len(word1) < len(word2):
        word1, word2 = word2, word1

    m: int = len(word1)
    n: int = len(word2)

    prev: list[int] = list(range(n + 1))
    curr: list[int] = [0] * (n + 1)

    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev

    return prev[n]


def edit_distance_operations(word1: str, word2: str) -> list[str]:
    """Find the sequence of operations to transform word1 to word2.

    Args:
        word1: Source string.
        word2: Target string.

    Returns:
        List of operations as strings.

    Examples:
        >>> edit_distance_operations("cat", "cut")
        ["Replace 'a' with 'u' at position 1"]

        >>> edit_distance_operations("", "ab")
        ["Insert 'a' at position 0", "Insert 'b' at position 0"]
    """
    m: int = len(word1)
    n: int = len(word2)

    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    operations: list[str] = []
    i: int = m
    j: int = n

    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(
                f"Replace '{word1[i - 1]}' with '{word2[j - 1]}' at position {i - 1}"
            )
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"Insert '{word2[j - 1]}' at position {i}")
            j -= 1
        else:
            operations.append(f"Delete '{word1[i - 1]}' at position {i - 1}")
            i -= 1

    operations.reverse()
    return operations


def edit_distance_weighted(
    word1: str,
    word2: str,
    insert_cost: int,
    delete_cost: int,
    replace_cost: int,
) -> int:
    """Calculate weighted edit distance.

    Args:
        word1: Source string.
        word2: Target string.
        insert_cost: Cost of insertion.
        delete_cost: Cost of deletion.
        replace_cost: Cost of replacement.

    Returns:
        Minimum weighted cost to transform word1 to word2.

    Examples:
        >>> edit_distance_weighted("abc", "def", 1, 1, 1)
        3

        >>> edit_distance_weighted("abc", "def", 1, 1, 2)
        6
    """
    m: int = len(word1)
    n: int = len(word2)

    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    for j in range(n + 1):
        dp[0][j] = j * insert_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + delete_cost,
                    dp[i][j - 1] + insert_cost,
                    dp[i - 1][j - 1] + replace_cost,
                )

    return dp[m][n]
