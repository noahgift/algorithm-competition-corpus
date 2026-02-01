"""Longest Common Subsequence (LCS).

Finds the longest subsequence common to two sequences.

Time Complexity: O(m * n)
Space Complexity: O(m * n) or O(min(m, n)) optimized

References:
    [1] Wagner, R.A., Fischer, M.J. (1974). "The String-to-String Correction
        Problem". Journal of the ACM. 21(1): 168-173.

    [2] Hirschberg, D.S. (1975). "A linear space algorithm for computing
        maximal common subsequences". Communications of the ACM. 18(6): 341-343.

    [3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 15.4.

Invariants (Popperian Falsification):
    P1: LCS is a subsequence of both strings
    P2: LCS length <= min(len(s1), len(s2))
    P3: LCS(s, s) = s (reflexivity)
    P4: LCS(s1, s2) = LCS(s2, s1) (symmetry in length)
"""

from __future__ import annotations


def lcs_length(text1: str, text2: str) -> int:
    """Find the length of the longest common subsequence.

    Args:
        text1: First string.
        text2: Second string.

    Returns:
        Length of the LCS.

    Examples:
        >>> lcs_length("abcde", "ace")
        3

        >>> lcs_length("abc", "def")
        0

        >>> lcs_length("abc", "abc")
        3

        >>> lcs_length("", "abc")
        0
    """
    m: int = len(text1)
    n: int = len(text2)

    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(text1: str, text2: str) -> str:
    """Find the actual longest common subsequence.

    Args:
        text1: First string.
        text2: Second string.

    Returns:
        The LCS string.

    Examples:
        >>> lcs_string("abcde", "ace")
        'ace'

        >>> lcs_string("abc", "def")
        ''

        >>> lcs_string("abcd", "abcd")
        'abcd'
    """
    m: int = len(text1)
    n: int = len(text2)

    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result: list[str] = []
    i: int = m
    j: int = n

    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            result.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


def lcs_optimized(text1: str, text2: str) -> int:
    """Find LCS length with O(min(m, n)) space.

    Args:
        text1: First string.
        text2: Second string.

    Returns:
        Length of the LCS.

    Examples:
        >>> lcs_optimized("abcde", "ace")
        3

        >>> lcs_optimized("abc", "def")
        0
    """
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m: int = len(text1)
    n: int = len(text2)

    prev: list[int] = [0] * (n + 1)
    curr: list[int] = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[n]


def lcs_three_strings(s1: str, s2: str, s3: str) -> int:
    """Find LCS length of three strings.

    Args:
        s1: First string.
        s2: Second string.
        s3: Third string.

    Returns:
        Length of the LCS of all three strings.

    Examples:
        >>> lcs_three_strings("abc", "abc", "abc")
        3

        >>> lcs_three_strings("abc", "ab", "a")
        1

        >>> lcs_three_strings("abc", "def", "ghi")
        0
    """
    l1: int = len(s1)
    l2: int = len(s2)
    l3: int = len(s3)

    dp: list[list[list[int]]] = [
        [[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)
    ]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            for k in range(1, l3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1],
                    )

    return dp[l1][l2][l3]
