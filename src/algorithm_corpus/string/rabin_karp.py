"""Rabin-Karp String Matching Algorithm.

Hash-based pattern matching using rolling hash.

Time Complexity: O(n + m) average, O(nm) worst case
Space Complexity: O(1) extra space

References:
    [1] Karp, R.M., Rabin, M.O. (1987).
        "Efficient randomized pattern-matching algorithms".
        IBM Journal of Research and Development. 31(2): 249-260.

Invariants (Popperian Falsification):
    P1: All returned indices are valid pattern matches
    P2: No valid match is missed
    P3: Hash collisions are handled correctly
    P4: Pattern at returned index equals pattern string
"""

from __future__ import annotations

_BASE: int = 256
_MOD: int = 101


def rabin_karp_search(text: str, pattern: str) -> list[int]:
    """Find all occurrences of pattern in text using Rabin-Karp algorithm.

    Args:
        text: Text to search in.
        pattern: Pattern to search for.

    Returns:
        List of starting indices where pattern occurs.

    Examples:
        >>> rabin_karp_search("ababcababcabc", "abc")
        [2, 7, 10]

        >>> rabin_karp_search("aaaaaa", "aa")
        [0, 1, 2, 3, 4]

        >>> rabin_karp_search("hello", "xyz")
        []

        >>> rabin_karp_search("hello", "")
        []
    """
    if not pattern or not text:
        return []

    n: int = len(text)
    m: int = len(pattern)

    if m > n:
        return []

    result: list[int] = []

    # Compute hash for pattern and first window
    pattern_hash: int = 0
    text_hash: int = 0
    h: int = 1  # _BASE^(m-1) % _MOD

    for _ in range(m - 1):
        h = (h * _BASE) % _MOD

    for i in range(m):
        pattern_hash = (_BASE * pattern_hash + ord(pattern[i])) % _MOD
        text_hash = (_BASE * text_hash + ord(text[i])) % _MOD

    # Slide window and check matches
    for i in range(n - m + 1):
        # Check hash match and verify characters to handle collisions
        if pattern_hash == text_hash and text[i : i + m] == pattern:
            result.append(i)

        # Compute hash for next window
        if i < n - m:
            text_hash = (
                _BASE * (text_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % _MOD
            if text_hash < 0:
                text_hash += _MOD

    return result
