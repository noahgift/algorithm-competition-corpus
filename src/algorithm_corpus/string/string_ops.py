"""Basic String Operations.

Common string manipulation algorithms.

Time Complexity: Varies by operation
Space Complexity: Varies by operation

References:
    [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press.

Invariants (Popperian Falsification):
    P1: is_anagram returns True iff strings are permutations
    P2: anagram_groups contains all input strings
    P3: reverse_words preserves all characters
    P4: Operations handle empty strings correctly
"""

from __future__ import annotations


def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams.

    Case-sensitive, ignores spaces.

    Args:
        s1: First string.
        s2: Second string.

    Returns:
        True if s1 and s2 are anagrams.

    Examples:
        >>> is_anagram("listen", "silent")
        True

        >>> is_anagram("hello", "world")
        False

        >>> is_anagram("", "")
        True

        >>> is_anagram("a", "a")
        True
    """
    # Remove spaces and compare sorted characters
    s1_clean = s1.replace(" ", "")
    s2_clean = s2.replace(" ", "")
    return sorted(s1_clean) == sorted(s2_clean)


def anagram_groups(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other.

    Args:
        words: List of strings.

    Returns:
        List of groups, where each group contains anagrams.

    Examples:
        >>> sorted(
        ...     [
        ...         sorted(g)
        ...         for g in anagram_groups(
        ...             ["eat", "tea", "tan", "ate", "nat", "bat"]
        ...         )
        ...     ]
        ... )
        [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]

        >>> anagram_groups([])
        []

        >>> anagram_groups(["a"])
        [['a']]
    """
    if not words:
        return []

    groups: dict[str, list[str]] = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


def reverse_words(s: str) -> str:
    """Reverse the order of words in a string.

    Args:
        s: Input string with words separated by spaces.

    Returns:
        String with words in reverse order.

    Examples:
        >>> reverse_words("hello world")
        'world hello'

        >>> reverse_words("  hello   world  ")
        'world hello'

        >>> reverse_words("")
        ''

        >>> reverse_words("a")
        'a'
    """
    words = s.split()
    return " ".join(reversed(words))
