"""Knuth-Morris-Pratt String Matching Algorithm.

Efficient pattern matching using failure function.

Time Complexity: O(n + m) where n = text length, m = pattern length
Space Complexity: O(m) for failure function

References:
    [1] Knuth, D.E., Morris, J.H., Pratt, V.R. (1977).
        "Fast pattern matching in strings".
        SIAM Journal on Computing. 6(2): 323-350.

Invariants (Popperian Falsification):
    P1: All returned indices are valid pattern matches
    P2: No valid match is missed
    P3: O(n + m) time complexity maintained
    P4: Pattern at returned index equals pattern string
"""

from __future__ import annotations


def build_failure_function(pattern: str) -> list[int]:
    """Build the KMP failure function for a pattern.

    The failure function f[i] gives the length of the longest proper
    prefix of pattern[0:i+1] that is also a suffix.

    Args:
        pattern: Pattern string.

    Returns:
        List where f[i] = length of longest proper prefix-suffix.

    Examples:
        >>> build_failure_function("ababaca")
        [0, 0, 1, 2, 3, 0, 1]

        >>> build_failure_function("aaa")
        [0, 1, 2]

        >>> build_failure_function("abc")
        [0, 0, 0]

        >>> build_failure_function("")
        []
    """
    m: int = len(pattern)
    if m == 0:
        return []

    failure: list[int] = [0] * m
    j: int = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        failure[i] = j

    return failure


def kmp_search(text: str, pattern: str) -> list[int]:
    """Find all occurrences of pattern in text using KMP algorithm.

    Args:
        text: Text to search in.
        pattern: Pattern to search for.

    Returns:
        List of starting indices where pattern occurs.

    Examples:
        >>> kmp_search("ababcababcabc", "abc")
        [2, 7, 10]

        >>> kmp_search("aaaaaa", "aa")
        [0, 1, 2, 3, 4]

        >>> kmp_search("hello", "xyz")
        []

        >>> kmp_search("hello", "")
        []
    """
    if not pattern or not text:
        return []

    n: int = len(text)
    m: int = len(pattern)

    if m > n:
        return []

    failure: list[int] = build_failure_function(pattern)
    result: list[int] = []
    j: int = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            result.append(i - m + 1)
            j = failure[j - 1]

    return result
