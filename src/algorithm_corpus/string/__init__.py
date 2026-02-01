"""String algorithms.

Pattern matching, string manipulation, and text processing.
"""

from __future__ import annotations

from algorithm_corpus.string.kmp import (
    build_failure_function,
    kmp_search,
)
from algorithm_corpus.string.rabin_karp import (
    rabin_karp_search,
)
from algorithm_corpus.string.string_ops import (
    anagram_groups,
    is_anagram,
    reverse_words,
)

__all__: list[str] = [
    "anagram_groups",
    "build_failure_function",
    "is_anagram",
    "kmp_search",
    "rabin_karp_search",
    "reverse_words",
]
