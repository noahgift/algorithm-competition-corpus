"""Pytest configuration and shared fixtures.

This module provides fixtures and configuration for property-based testing
using only Python standard library (no external dependencies like Hypothesis).
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable


# ============================================================================
# Random Seed Management (Reproducibility)
# ============================================================================


@pytest.fixture
def seed() -> int:
    """Provide a fixed seed for reproducible random tests.

    Returns:
        Fixed seed value for test reproducibility.
    """
    return 42


@pytest.fixture
def rng(seed: int) -> random.Random:
    """Provide a seeded random number generator.

    Args:
        seed: The seed value from the seed fixture.

    Returns:
        Seeded Random instance for deterministic test generation.
    """
    return random.Random(seed)


# ============================================================================
# Property-Based Testing Helpers (stdlib-only)
# ============================================================================


@pytest.fixture
def random_ints(rng: random.Random) -> Callable[[int, int, int], list[int]]:
    """Factory for generating random integer lists.

    Args:
        rng: Seeded random number generator.

    Returns:
        Function that generates random integer lists.
    """

    def _generate(n: int, min_val: int = -1000, max_val: int = 1000) -> list[int]:
        return [rng.randint(min_val, max_val) for _ in range(n)]

    return _generate


@pytest.fixture
def random_graph(
    rng: random.Random,
) -> Callable[[int, float], dict[int, list[tuple[int, int]]]]:
    """Factory for generating random weighted graphs.

    Args:
        rng: Seeded random number generator.

    Returns:
        Function that generates random adjacency list graphs.
    """

    def _generate(
        n: int,
        density: float = 0.3,
        max_weight: int = 100,
    ) -> dict[int, list[tuple[int, int]]]:
        graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < density:
                    weight = rng.randint(1, max_weight)
                    graph[u].append((v, weight))
        return graph

    return _generate


@pytest.fixture
def random_tree(
    rng: random.Random,
) -> Callable[[int], dict[int, list[int]]]:
    """Factory for generating random trees.

    Args:
        rng: Seeded random number generator.

    Returns:
        Function that generates random tree adjacency lists.
    """

    def _generate(n: int) -> dict[int, list[int]]:
        if n <= 0:
            return {}
        if n == 1:
            return {0: []}

        tree: dict[int, list[int]] = {i: [] for i in range(n)}
        # Build tree by connecting each node to a random earlier node
        for i in range(1, n):
            parent = rng.randint(0, i - 1)
            tree[parent].append(i)
            tree[i].append(parent)
        return tree

    return _generate


# ============================================================================
# Property Test Decorator (stdlib replacement for Hypothesis)
# ============================================================================


def property_test(
    iterations: int = 100,
) -> Callable[[Callable[..., None]], Callable[..., None]]:
    """Decorator for property-based tests using stdlib random.

    This is a stdlib-only alternative to Hypothesis @given decorator.
    Tests are marked with the 'property' marker for selective execution.

    Args:
        iterations: Number of random iterations to run.

    Returns:
        Decorator that runs the test function multiple times.

    Example:
        @property_test(iterations=100)
        def test_sort_preserves_length(self, rng: random.Random) -> None:
            data = [rng.randint(-100, 100) for _ in range(rng.randint(0, 50))]
            assert len(sorted(data)) == len(data)
    """

    def decorator(func: Callable[..., None]) -> Callable[..., None]:
        @pytest.mark.property
        def wrapper(*args: object, **kwargs: object) -> None:
            for i in range(iterations):
                # Re-seed for each iteration for variety
                if "rng" in kwargs and isinstance(kwargs["rng"], random.Random):
                    kwargs["rng"].seed(42 + i)
                func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator


# ============================================================================
# Test Markers
# ============================================================================


def pytest_configure(config: pytest.Config) -> None:
    """Register custom markers."""
    config.addinivalue_line("markers", "property: marks property-based tests")
    config.addinivalue_line("markers", "slow: marks slow tests")
    config.addinivalue_line("markers", "invariant: marks Popperian invariant tests")
