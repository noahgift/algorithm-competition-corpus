"""Radix Sort algorithm.

Non-comparison sorting algorithm using digit-by-digit sorting.

References:
    Cormen, T.H., et al. (2009). Introduction to Algorithms (3rd ed.).
    MIT Press. Chapter 8.3: Radix Sort.

Time Complexity: O(d * (n + k)) where d is digits, k is base.
Space Complexity: O(n + k).
"""

from __future__ import annotations


def radix_sort(arr: list[int]) -> list[int]:
    """Sort non-negative integers using radix sort.

    LSD (Least Significant Digit) radix sort using base 10.

    Args:
        arr: List of non-negative integers.

    Returns:
        Sorted list.

    Example:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    if not arr:
        return []

    # Handle negatives by separating them
    negatives = [-x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    if positives:
        positives = _radix_sort_positive(positives)

    if negatives:
        negatives = _radix_sort_positive(negatives)
        negatives = [-x for x in reversed(negatives)]

    return negatives + positives


def _radix_sort_positive(arr: list[int]) -> list[int]:
    """Radix sort for non-negative integers."""
    if not arr:
        return []

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def _counting_sort_by_digit(arr: list[int], exp: int) -> list[int]:
    """Stable counting sort by specific digit."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Convert to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable sort: go backwards)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    return output


def radix_sort_strings(strings: list[str]) -> list[str]:
    """Radix sort for fixed-length strings.

    MSD (Most Significant Digit) approach for strings.

    Args:
        strings: List of strings (must be same length).

    Returns:
        Sorted list of strings.

    Example:
        >>> radix_sort_strings(["cab", "abc", "bca", "aab"])
        ['aab', 'abc', 'bca', 'cab']
    """
    if not strings:
        return []

    max_len = max(len(s) for s in strings)

    # Pad strings to equal length
    padded = [s.ljust(max_len) for s in strings]

    # LSD radix sort on characters
    for i in range(max_len - 1, -1, -1):
        # Count sort by character at position i
        padded = _counting_sort_by_char(padded, i)

    # Remove padding
    return [s.rstrip() for s in padded]


def _counting_sort_by_char(strings: list[str], pos: int) -> list[str]:
    """Stable counting sort by character at position."""
    n = len(strings)
    output = [""] * n
    count = [0] * 128  # ASCII characters

    for s in strings:
        count[ord(s[pos])] += 1

    for i in range(1, 128):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        char_idx = ord(strings[i][pos])
        count[char_idx] -= 1
        output[count[char_idx]] = strings[i]

    return output
