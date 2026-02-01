"""Mathematical algorithms.

Number theory, combinatorics, and computational mathematics.
"""

from __future__ import annotations

from algorithm_corpus.math.combinatorics import (
    binomial_coefficient,
    factorial,
    permutations_count,
)
from algorithm_corpus.math.gcd import (
    extended_gcd,
    gcd,
    lcm,
)
from algorithm_corpus.math.power import (
    mod_pow,
    power,
)
from algorithm_corpus.math.primes import (
    is_prime,
    prime_factors,
    sieve_of_eratosthenes,
)

__all__: list[str] = [
    "binomial_coefficient",
    "extended_gcd",
    "factorial",
    "gcd",
    "is_prime",
    "lcm",
    "mod_pow",
    "permutations_count",
    "power",
    "prime_factors",
    "sieve_of_eratosthenes",
]
