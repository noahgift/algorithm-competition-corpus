"""Sliding window algorithms.

This module contains algorithms using the sliding window technique.

Algorithms:
    - Max Sum Subarray: Kadane's algorithm
    - Fixed Size Window: Maximum sum of k elements
    - Circular Subarray: Maximum sum with wrap-around
    - Maximum Product: Product variant of Kadane's
"""

from __future__ import annotations

__all__: list[str] = [
    "max_circular_subarray_sum",
    "max_subarray_fixed_size",
    "max_subarray_indices",
    "max_subarray_product",
    "max_subarray_sum",
]
