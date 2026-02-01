"""Bit Manipulation algorithms.

Bitwise operations and tricks for efficient computation.
"""

from __future__ import annotations

from algorithm_corpus.bit_manipulation.advanced_ops import (
    hamming_distance,
    reverse_bits,
    single_number,
)
from algorithm_corpus.bit_manipulation.basic_ops import (
    count_bits,
    get_bit,
    is_power_of_two,
    set_bit,
    toggle_bit,
)

__all__: list[str] = [
    "count_bits",
    "get_bit",
    "hamming_distance",
    "is_power_of_two",
    "reverse_bits",
    "set_bit",
    "single_number",
    "toggle_bit",
]
