"""Word break algorithms.

Dynamic programming for string segmentation.
"""

from __future__ import annotations


def word_break(s: str, word_dict: list[str]) -> bool:
    """Check if string can be segmented into dictionary words.

    Args:
        s: Input string.
        word_dict: List of valid words.

    Returns:
        True if string can be segmented.

    Example:
        >>> word_break("leetcode", ["leet", "code"])
        True
        >>> word_break("applepenapple", ["apple", "pen"])
        True
        >>> word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
        False
    """
    if not s:
        return True

    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


def word_break_all(s: str, word_dict: list[str]) -> list[str]:
    """Find all possible segmentations of string.

    Args:
        s: Input string.
        word_dict: List of valid words.

    Returns:
        List of all possible sentence segmentations.

    Example:
        >>> sorted(
        ...     word_break_all("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        ... )
        ['cat sand dog', 'cats and dog']
    """
    word_set = set(word_dict)
    memo: dict[int, list[str]] = {}

    def backtrack(start: int) -> list[str]:
        if start in memo:
            return memo[start]

        if start == len(s):
            return [""]

        result: list[str] = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                for sentence in backtrack(end):
                    if sentence:
                        result.append(word + " " + sentence)
                    else:
                        result.append(word)

        memo[start] = result
        return result

    return backtrack(0)
