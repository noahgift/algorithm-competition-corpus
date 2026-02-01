"""Palindrome Algorithms using Two Pointers.

Check and find palindromes using two pointer technique.

Time Complexity: O(n) for is_palindrome, O(n²) for longest_palindromic_substring
Space Complexity: O(1) extra space

References:
    [1] Manacher, G. (1975). "A new linear-time on-line algorithm for
        finding the smallest initial palindrome of a string".
        Journal of the ACM.

Invariants (Popperian Falsification):
    P1: Empty string is a palindrome
    P2: Single character is a palindrome
    P3: Palindrome reads same forwards and backwards
    P4: Longest palindromic substring is actually a palindrome
"""

from __future__ import annotations


def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome.

    Only considers alphanumeric characters, case-insensitive.

    Args:
        s: Input string.

    Returns:
        True if palindrome, False otherwise.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True

        >>> is_palindrome("race a car")
        False

        >>> is_palindrome("")
        True

        >>> is_palindrome("a")
        True
    """
    left: int = 0
    right: int = len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def _expand_around_center(s: str, left: int, right: int) -> str:
    """Expand around center to find palindrome."""
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


def longest_palindromic_substring(s: str) -> str:
    """Find the longest palindromic substring.

    Args:
        s: Input string.

    Returns:
        Longest palindromic substring.

    Examples:
        >>> longest_palindromic_substring("babad") in ("bab", "aba")
        True

        >>> longest_palindromic_substring("cbbd")
        'bb'

        >>> longest_palindromic_substring("")
        ''

        >>> longest_palindromic_substring("a")
        'a'

        >>> longest_palindromic_substring("ac")
        'a'
    """
    if len(s) < 2:  # noqa: PLR2004
        return s

    result: str = s[0]

    for i in range(len(s)):
        # Odd length palindrome (center at i)
        odd: str = _expand_around_center(s, i, i)
        if len(odd) > len(result):
            result = odd

        # Even length palindrome (center between i and i+1)
        even: str = _expand_around_center(s, i, i + 1)
        if len(even) > len(result):
            result = even

    return result
