# CLAUDE.md - Algorithm Competition Corpus

**Priority: P0** (Read first before any development)

## Project Overview

This is a **pure Python algorithm corpus** with EXTREME quality standards:
- **Zero external dependencies** (stdlib only)
- **100% type annotation coverage**
- **95% branch test coverage**
- **PMAT TDG grade A- or higher**

## Critical Constraints

### A. Standard Library Only

```python
# ALLOWED
import heapq
import collections
import functools
import itertools
import bisect
import math
import random

# FORBIDDEN
import numpy           # NO
import hypothesis      # NO
import networkx        # NO
```

### B. Modern Type Syntax (PEP 585 + PEP 604)

```python
# REQUIRED: Future annotations at top of every file
from __future__ import annotations

# REQUIRED: Use builtins, not typing module
def dijkstra(graph: dict[int, list[tuple[int, int]]]) -> dict[int, int]:
    distances: dict[int, int] = {}
    heap: list[tuple[int, int]] = []

# REQUIRED: Use | for unions
def find(x: int) -> int | None:

# FORBIDDEN: Old-style annotations
from typing import Dict, List, Tuple, Optional  # NO
```

### C. Toolchain

```bash
# ONLY these tools
uv          # Package management
ruff        # Linting + formatting
ty          # Type checking
pytest      # Testing
```

### D. SATD (Self-Admitted Technical Debt) - ZERO TOLERANCE

```python
# FORBIDDEN comments - create a ticket instead
# TODO: ...      # NO
# FIXME: ...     # NO
# HACK: ...      # NO
# XXX: ...       # NO
```

## Development Workflow

### Starting Work

```bash
# 1. Start work on a ticket
pmat work start ALGO-XXX

# 2. Create algorithm file
# src/algorithm_corpus/<category>/<algorithm>.py

# 3. Write doctests FIRST (TDD)
# Minimum 3 doctests per function

# 4. Implement algorithm

# 5. Create test file
# tests/test_<category>/test_<algorithm>.py

# 6. Run quality gates
make comply

# 7. Commit and complete
git add . && git commit -m "feat: add <algorithm>"
pmat work complete ALGO-XXX
```

### Quality Gates (ALL must pass)

```bash
make comply   # Runs all 6 gates:
              # 1. ruff format --check (no changes needed)
              # 2. ruff check (zero violations)
              # 3. ty check (zero type errors)
              # 4. pytest --doctest-modules (all doctests pass)
              # 5. pytest tests/ (all unit tests pass)
              # 6. coverage >=95% branch
```

## File Templates

### Algorithm File

```python
"""Algorithm Name.

Brief description of what the algorithm does.

Time Complexity: O(...)
Space Complexity: O(...)

References:
    [1] Author (Year). "Title". Journal. doi:...

Invariants (Popperian Falsification):
    P1: First invariant that must hold
    P2: Second invariant that must hold
"""
from __future__ import annotations

import heapq  # Only stdlib imports


def algorithm_name(param: list[int]) -> int:
    """One-line description.

    Args:
        param: Description of parameter.

    Returns:
        Description of return value.

    Raises:
        ValueError: When input is invalid.

    Examples:
        >>> algorithm_name([1, 2, 3])
        6

        >>> algorithm_name([])
        0

        >>> algorithm_name([-1])
        -1
    """
    # Implementation with type annotations on complex variables
    result: int = 0
    for x in param:
        result += x
    return result
```

### Test File

```python
"""Tests for algorithm_name.

Popperian falsification via invariant property testing.
"""
from __future__ import annotations

import random
import unittest

from algorithm_corpus.category.algorithm_name import algorithm_name


class TestAlgorithmInvariants(unittest.TestCase):
    """Invariant tests that could falsify the algorithm."""

    def test_p1_invariant_name(self) -> None:
        """P1: Description of invariant."""
        for _ in range(100):
            # Generate random input
            data = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
            result = algorithm_name(data)
            # Assert invariant holds
            self.assertGreaterEqual(result, 0)


class TestBoundaryConditions(unittest.TestCase):
    """Edge case tests."""

    def test_empty_input(self) -> None:
        """Empty input should return expected value."""
        self.assertEqual(algorithm_name([]), 0)


class TestCorrectness(unittest.TestCase):
    """Correctness tests against known solutions."""

    def test_known_solution(self) -> None:
        """Test against manually verified solution."""
        self.assertEqual(algorithm_name([1, 2, 3]), 6)


if __name__ == "__main__":
    unittest.main()
```

## Peer-Reviewed Citations

Every algorithm MUST include citations to peer-reviewed sources:

| Algorithm | Required Citation |
|-----------|------------------|
| Dijkstra | Dijkstra (1959). Numerische Mathematik |
| Bellman-Ford | Bellman (1958). Quarterly of Applied Mathematics |
| Union-Find | Tarjan (1975). JACM |
| KMP | Knuth, Morris, Pratt (1977). SIAM J. Comput |
| Quicksort | Hoare (1961). Computer Journal |

## Popperian Falsification

Tests are designed to **disprove** correctness, not just verify examples:

```python
# BAD: Only verification
def test_dijkstra_example(self):
    result = dijkstra(graph, 0)
    self.assertEqual(result, expected)  # Just checks one case

# GOOD: Falsification via invariant
def test_p1_distances_non_negative(self):
    """P1: If any d[v] < 0, algorithm is WRONG."""
    for _ in range(100):
        graph = random_graph()
        distances = dijkstra(graph, 0)
        for d in distances.values():
            self.assertGreaterEqual(d, 0)  # Could falsify!
```

## Depyler Transpilation Notes

This corpus is designed for Python-to-Rust transpilation:

| Python | Rust |
|--------|------|
| `list[int]` | `Vec<i32>` |
| `dict[int, int]` | `HashMap<i32, i32>` |
| `heapq` | `BinaryHeap` |
| `collections.deque` | `VecDeque` |
| `int \| None` | `Option<i32>` |

**Avoid:**
- `*args` unpacking (not supported)
- Nested functions (not supported)
- `eval()`, `exec()` (not supported)
- Recursive algorithms when iterative is possible

## Quick Reference

```bash
# Setup
uv sync && make dev-setup

# Development loop
make format        # Auto-format
make fix          # Auto-fix lint issues
make comply       # Full quality check

# Testing
make test         # Unit tests only
make doctest      # Doctests only
make coverage     # With coverage report
make coverage-html # HTML report

# Cleanup
make clean
```
