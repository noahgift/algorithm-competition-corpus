"""Longest substring algorithms.

Sliding window approaches for substring problems.
"""

from __future__ import annotations


def longest_no_repeat(s: str) -> int:
    """Find length of longest substring without repeating characters.

    Uses sliding window with set.

    Args:
        s: Input string.

    Returns:
        Length of longest substring without repeating characters.

    Example:
        >>> longest_no_repeat("abcabcbb")
        3
        >>> longest_no_repeat("bbbbb")
        1
        >>> longest_no_repeat("pwwkew")
        3
    """
    char_set: set[str] = set()
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        while char in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(char)
        max_len = max(max_len, right - left + 1)

    return max_len


def longest_with_k_distinct(s: str, k: int) -> int:
    """Find length of longest substring with at most k distinct characters.

    Uses sliding window with counter.

    Args:
        s: Input string.
        k: Maximum number of distinct characters.

    Returns:
        Length of longest substring with at most k distinct characters.

    Example:
        >>> longest_with_k_distinct("eceba", 2)
        3
        >>> longest_with_k_distinct("aa", 1)
        2
    """
    if k == 0:
        return 0

    char_count: dict[str, int] = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def longest_repeating_replacement(s: str, k: int) -> int:
    """Find length of longest substring after at most k character replacements.

    Args:
        s: Input string.
        k: Maximum number of characters to replace.

    Returns:
        Length of longest substring with same character after replacements.

    Example:
        >>> longest_repeating_replacement("ABAB", 2)
        4
        >>> longest_repeating_replacement("AABABBA", 1)
        4
    """
    char_count: dict[str, int] = {}
    left = 0
    max_len = 0
    max_count = 0  # Count of most frequent character in window

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1
        max_count = max(max_count, char_count[char])

        # Window size - max_count = number of replacements needed
        window_size = right - left + 1
        if window_size - max_count > k:
            left_char = s[left]
            char_count[left_char] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
