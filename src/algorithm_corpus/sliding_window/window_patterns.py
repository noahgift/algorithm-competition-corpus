"""Sliding window pattern algorithms.

Common sliding window problem patterns.
"""

from __future__ import annotations


def min_size_subarray_sum(target: int, nums: list[int]) -> int:
    """Find minimum length subarray with sum >= target.

    Args:
        target: Target sum.
        nums: List of positive integers.

    Returns:
        Minimum length, or 0 if no such subarray.

    Example:
        >>> min_size_subarray_sum(7, [2, 3, 1, 2, 4, 3])
        2
        >>> min_size_subarray_sum(11, [1, 1, 1, 1, 1])
        0
    """
    if not nums:
        return 0

    left = 0
    current_sum = 0
    min_len = len(nums) + 1

    for right, num in enumerate(nums):
        current_sum += num

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len <= len(nums) else 0


def find_anagrams(s: str, p: str) -> list[int]:
    """Find all starting indices of anagrams of p in s.

    Args:
        s: Search string.
        p: Pattern string.

    Returns:
        List of starting indices where anagrams begin.

    Example:
        >>> find_anagrams("cbaebabacd", "abc")
        [0, 6]
        >>> find_anagrams("abab", "ab")
        [0, 1, 2]
    """
    if len(p) > len(s):
        return []

    result: list[int] = []
    p_count: dict[str, int] = {}
    s_count: dict[str, int] = {}

    for char in p:
        p_count[char] = p_count.get(char, 0) + 1

    for i, char in enumerate(s):
        # Add current character
        s_count[char] = s_count.get(char, 0) + 1

        # Remove leftmost if window too large
        if i >= len(p):
            left_char = s[i - len(p)]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]

        # Check if anagram
        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result


def min_window_substring(s: str, t: str) -> str:
    """Find minimum window in s containing all characters of t.

    Args:
        s: Source string.
        t: Target characters.

    Returns:
        Minimum window substring, or empty string if none.

    Example:
        >>> min_window_substring("ADOBECODEBANC", "ABC")
        'BANC'
        >>> min_window_substring("a", "a")
        'a'
    """
    if not s or not t or len(s) < len(t):
        return ""

    # Count characters needed
    need: dict[str, int] = {}
    for char in t:
        need[char] = need.get(char, 0) + 1

    have: dict[str, int] = {}
    formed = 0
    required = len(need)

    left = 0
    min_len = len(s) + 1
    min_left = 0

    for right, char in enumerate(s):
        # Add current character
        have[char] = have.get(char, 0) + 1

        # Check if this character satisfies need
        if char in need and have[char] == need[char]:
            formed += 1

        # Contract window while valid
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            # Remove left character
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return s[min_left : min_left + min_len] if min_len <= len(s) else ""
