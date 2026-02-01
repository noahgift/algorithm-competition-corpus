# Algorithm Competition Corpus Specification

**Version:** 1.0.0
**Status:** Draft
**Last Updated:** 2026-02-01

## Executive Summary

This specification defines a **pure Python algorithm corpus** designed for:
1. Ground truth training data for Depyler Python-to-Rust transpilation
2. Educational reference with peer-reviewed citations
3. Benchmarking corpus with EXTREME quality standards

The corpus follows **Popperian falsification methodology**: every algorithm includes invariant properties that could disprove correctness, enabling scientific validation rather than mere verification.

---

## 1. Core Constraints

### 1.1 Absolute Requirements

| Constraint | Requirement | Rationale |
|------------|-------------|-----------|
| **A. Standard Library Only** | ZERO external dependencies | Ensures Depyler transpilation compatibility |
| **B. Fully Typed** | 100% type annotation coverage | Required for type-directed transpilation |
| **C. Toolchain** | `uv`, `ruff`, `ty`, `pytest` ONLY | Minimal, modern, fast toolchain |
| **D. PMAT Compliance** | `pmat comply` must pass | Zero technical debt tolerance |
| **E. Coverage** | 95% branch coverage minimum | EXTREME quality standard |
| **F. Project Management** | `pmat work` workflow | Ticket-driven development |

### 1.2 Forbidden Patterns

```python
# FORBIDDEN: External imports
import numpy as np           # NO
import hypothesis            # NO - use stdlib unittest
from sortedcontainers import SortedList  # NO

# FORBIDDEN: Old-style type annotations
from typing import Dict, List, Tuple  # NO - use builtins
Optional[int]                         # NO - use int | None

# FORBIDDEN: SATD comments
# TODO: fix this              # NO - create ticket
# FIXME: edge case            # NO - create ticket
# HACK: workaround            # NO - fix properly
```

### 1.3 Required Patterns

```python
# REQUIRED: Future annotations
from __future__ import annotations

# REQUIRED: Modern type syntax (PEP 585, PEP 604)
def dijkstra(graph: dict[int, list[tuple[int, int]]], start: int) -> dict[int, int]:
    distances: dict[int, int] = {start: 0}
    heap: list[tuple[int, int]] = [(0, start)]
    ...

# REQUIRED: Union with pipe operator
def find(self, x: int) -> int | None:
    ...
```

---

## 2. Corpus Structure

### 2.1 Target Size

**100+ algorithm files** organized across 14 categories:

| Category | Target Files | Description |
|----------|--------------|-------------|
| `graph/` | 10 | BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, topological sort, union-find, strongly connected components |
| `dynamic_programming/` | 12 | Fibonacci, LCS, LIS, knapsack variants, edit distance, coin change, matrix chain, house robber, palindrome partitioning, word break |
| `sliding_window/` | 6 | Max sum subarray, min window substring, longest unique substring, variable window problems |
| `two_pointers/` | 7 | Two sum, three sum, container with water, remove duplicates, palindrome checks |
| `binary_search/` | 8 | Classic, rotated array, peak element, search insert, first/last occurrence, sqrt, capacity to ship |
| `backtracking/` | 8 | N-queens, permutations, combinations, subsets, sudoku solver, word search, palindrome partitioning |
| `bit_manipulation/` | 7 | XOR tricks, counting bits, power of two, single number variants, bitmask DP |
| `sorting/` | 8 | Quicksort, mergesort, heapsort, radix, counting sort, bucket sort, insertion sort variants |
| `heap_priority_queue/` | 6 | Kth largest, merge K sorted, median stream, sliding window median, task scheduler |
| `trees/` | 8 | Traversals, BST validation, LCA, serialize/deserialize, path sum, diameter, balanced check |
| `linked_list/` | 6 | Reverse, cycle detection, reorder, merge, remove nth, palindrome check |
| `string/` | 8 | KMP, Rabin-Karp, Z-algorithm, palindrome, anagrams, longest palindromic substring, regex matching |
| `math/` | 8 | GCD, sieve of Eratosthenes, fast exponentiation, prime factorization, modular arithmetic, combinatorics |
| `intervals/` | 6 | Merge intervals, insert interval, meeting rooms, non-overlapping intervals |

### 2.2 Directory Layout

```
algorithm-competition-corpus/
├── pyproject.toml              # uv project config
├── ty.toml                     # ty type checker config
├── ruff.toml                   # ruff linter config
├── Makefile                    # quality gates
├── CLAUDE.md                   # P0: development guidelines
├── README.md                   # P1: corpus overview
├── .pmat/                      # PMAT configuration
│   ├── gates.toml              # quality gate thresholds
│   └── metrics.toml            # TDG scoring config
├── docs/
│   └── specifications/
│       └── competition-corpus.md
├── src/
│   └── algorithm_corpus/
│       ├── __init__.py
│       ├── py.typed            # PEP 561 marker
│       ├── graph/
│       │   ├── __init__.py
│       │   ├── dijkstra.py
│       │   ├── bfs.py
│       │   └── ...
│       ├── dynamic_programming/
│       │   ├── __init__.py
│       │   ├── knapsack.py
│       │   └── ...
│       └── ... (14 categories)
└── tests/
    ├── conftest.py             # pytest fixtures
    ├── test_graph/
    │   ├── test_dijkstra.py
    │   └── ...
    └── ... (mirror src structure)
```

---

## 3. File Template

### 3.1 Algorithm File Template

```python
"""Dijkstra's Algorithm for Single-Source Shortest Paths.

Computes the shortest path from a source vertex to all other vertices
in a weighted graph with non-negative edge weights.

Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V + E)

References:
    [1] Dijkstra, E.W. (1959). "A note on two problems in connexion with graphs".
        Numerische Mathematik. 1: 269-271. doi:10.1007/BF01386390

    [2] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009).
        "Introduction to Algorithms" (3rd ed.). MIT Press. Chapter 24.3.

Invariants (Popperian Falsification):
    P1: All computed distances are non-negative (d[v] >= 0 for all v)
    P2: Triangle inequality holds: d[u] + w(u,v) >= d[v] for all edges (u,v)
    P3: Source distance is zero: d[source] = 0
    P4: Unreachable vertices have infinite distance

Depyler Transpilation Notes:
    - Uses heapq (maps to std::collections::BinaryHeap)
    - Dict[int, int] maps to HashMap<i32, i32>
    - Iterative preferred over recursive for Rust stack safety
"""
from __future__ import annotations

import heapq


def dijkstra(
    graph: dict[int, list[tuple[int, int]]],
    source: int,
) -> dict[int, int]:
    """Compute shortest distances from source to all reachable vertices.

    Args:
        graph: Adjacency list where graph[u] contains (v, weight) pairs.
        source: The starting vertex.

    Returns:
        Dictionary mapping each reachable vertex to its shortest distance.

    Raises:
        ValueError: If source is not in graph.

    Examples:
        >>> g = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        >>> dijkstra(g, 0)
        {0: 0, 2: 1, 1: 3, 3: 4}

        >>> dijkstra({0: []}, 0)
        {0: 0}

        >>> dijkstra({0: [(1, 10)], 1: []}, 0)
        {0: 0, 1: 10}
    """
    if source not in graph:
        msg = f"Source vertex {source} not in graph"
        raise ValueError(msg)

    distances: dict[int, int] = {source: 0}
    heap: list[tuple[int, int]] = [(0, source)]

    while heap:
        dist, u = heapq.heappop(heap)

        if dist > distances.get(u, float("inf")):
            continue

        for v, weight in graph.get(u, []):
            new_dist = dist + weight
            if new_dist < distances.get(v, float("inf")):
                distances[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return distances
```

### 3.2 Test File Template

```python
"""Tests for Dijkstra's Algorithm.

Implements Popperian falsification through invariant property testing.
Each test attempts to DISPROVE the algorithm's correctness.

Test Categories:
    1. Invariant Properties (P1-P4): Could falsify the algorithm
    2. Boundary Conditions: Empty, single-node, disconnected graphs
    3. Correctness Verification: Known solutions
"""
from __future__ import annotations

import random
import unittest

from algorithm_corpus.graph.dijkstra import dijkstra


class TestDijkstraInvariants(unittest.TestCase):
    """Popperian falsification tests for Dijkstra invariants.

    These tests attempt to DISPROVE the algorithm by checking
    mathematical invariants that must hold for correctness.
    """

    def test_p1_distances_non_negative(self) -> None:
        """P1: All computed distances must be non-negative.

        Falsification: If any d[v] < 0, the algorithm is incorrect.
        """
        # Property-based: generate random graphs
        for _ in range(100):
            n = random.randint(1, 20)
            graph = self._random_graph(n, density=0.3)
            if graph:
                source = random.choice(list(graph.keys()))
                distances = dijkstra(graph, source)
                for v, d in distances.items():
                    self.assertGreaterEqual(
                        d, 0,
                        f"Invariant P1 violated: d[{v}] = {d} < 0"
                    )

    def test_p2_triangle_inequality(self) -> None:
        """P2: Triangle inequality must hold for all edges.

        For every edge (u, v) with weight w: d[u] + w >= d[v]

        Falsification: If d[u] + w < d[v] for any edge, algorithm failed
        to find shortest path.
        """
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: [],
        }
        distances = dijkstra(graph, 0)

        for u, edges in graph.items():
            if u not in distances:
                continue
            for v, weight in edges:
                if v in distances:
                    self.assertGreaterEqual(
                        distances[u] + weight,
                        distances[v],
                        f"Triangle inequality violated: d[{u}] + w({u},{v}) < d[{v}]"
                    )

    def test_p3_source_distance_zero(self) -> None:
        """P3: Distance from source to itself must be zero.

        Falsification: If d[source] != 0, algorithm is incorrect.
        """
        for _ in range(50):
            n = random.randint(1, 10)
            graph = self._random_graph(n, density=0.5)
            if graph:
                source = random.choice(list(graph.keys()))
                distances = dijkstra(graph, source)
                self.assertEqual(
                    distances[source], 0,
                    f"Invariant P3 violated: d[source] = {distances[source]} != 0"
                )

    def test_p4_optimal_substructure(self) -> None:
        """P4: Shortest paths have optimal substructure.

        If path P = (s, ..., u, v) is shortest s->v,
        then (s, ..., u) is shortest s->u.

        Falsification: Find a shorter subpath.
        """
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1), (2, 4)],
            1: [(2, 2), (3, 6)],
            2: [(3, 3)],
            3: [],
        }
        distances = dijkstra(graph, 0)

        # d[0->1] + w[1->2] should equal d[0->2] if path goes through 1
        self.assertEqual(distances[2], 3)  # 0->1->2 = 1+2 = 3
        self.assertEqual(distances[3], 6)  # 0->1->2->3 = 1+2+3 = 6

    @staticmethod
    def _random_graph(
        n: int,
        density: float = 0.3,
    ) -> dict[int, list[tuple[int, int]]]:
        """Generate a random weighted graph for property testing."""
        graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
        for u in range(n):
            for v in range(n):
                if u != v and random.random() < density:
                    weight = random.randint(1, 100)
                    graph[u].append((v, weight))
        return graph


class TestDijkstraBoundaryConditions(unittest.TestCase):
    """Boundary condition tests for edge cases."""

    def test_empty_graph_raises(self) -> None:
        """Empty graph should raise ValueError."""
        with self.assertRaises(ValueError):
            dijkstra({}, 0)

    def test_single_node(self) -> None:
        """Single node graph returns only source."""
        result = dijkstra({0: []}, 0)
        self.assertEqual(result, {0: 0})

    def test_disconnected_graph(self) -> None:
        """Unreachable vertices should not appear in result."""
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 1)],
            1: [],
            2: [(3, 1)],  # Disconnected component
            3: [],
        }
        result = dijkstra(graph, 0)
        self.assertIn(0, result)
        self.assertIn(1, result)
        self.assertNotIn(2, result)
        self.assertNotIn(3, result)


class TestDijkstraCorrectness(unittest.TestCase):
    """Correctness tests against known solutions."""

    def test_known_solution_1(self) -> None:
        """Test against manually verified solution.

        Reference: CLRS Figure 24.6
        """
        graph: dict[int, list[tuple[int, int]]] = {
            0: [(1, 10), (3, 5)],
            1: [(2, 1), (3, 2)],
            2: [(4, 4)],
            3: [(1, 3), (2, 9), (4, 2)],
            4: [(0, 7), (2, 6)],
        }
        expected = {0: 0, 1: 8, 2: 9, 3: 5, 4: 7}
        result = dijkstra(graph, 0)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
```

---

## 4. Toolchain Configuration

### 4.1 pyproject.toml

```toml
[project]
name = "algorithm-competition-corpus"
version = "0.1.0"
description = "Pure Python algorithm corpus for Depyler transpilation"
requires-python = ">=3.12"
readme = "README.md"
license = { text = "MIT" }
authors = [{ name = "Noah Gift" }]
keywords = ["algorithms", "transpilation", "depyler", "education"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.12",
    "Typing :: Typed",
]

# ZERO external dependencies - stdlib only
dependencies = []

[project.optional-dependencies]
dev = []  # Tools managed via uv tool install

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/algorithm_corpus"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "-ra",
    "--doctest-modules",
    "--cov=src/algorithm_corpus",
    "--cov-branch",
    "--cov-report=term-missing",
    "--cov-fail-under=95",
]
filterwarnings = ["error"]

[tool.coverage.run]
source = ["src/algorithm_corpus"]
branch = true
parallel = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
fail_under = 95
show_missing = true
```

### 4.2 ruff.toml

```toml
# EXTREME lint configuration

target-version = "py312"
line-length = 88
src = ["src", "tests"]

[lint]
select = [
    "F",      # Pyflakes
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "C90",    # mccabe complexity
    "I",      # isort
    "N",      # pep8-naming
    "D",      # pydocstyle
    "UP",     # pyupgrade
    "YTT",    # flake8-2020
    "ANN",    # flake8-annotations
    "ASYNC",  # flake8-async
    "S",      # flake8-bandit (security)
    "BLE",    # flake8-blind-except
    "FBT",    # flake8-boolean-trap
    "B",      # flake8-bugbear
    "A",      # flake8-builtins
    "COM",    # flake8-commas
    "C4",     # flake8-comprehensions
    "DTZ",    # flake8-datetimez
    "T10",    # flake8-debugger
    "EM",     # flake8-errmsg
    "FA",     # flake8-future-annotations
    "ISC",    # flake8-implicit-str-concat
    "ICN",    # flake8-import-conventions
    "LOG",    # flake8-logging
    "G",      # flake8-logging-format
    "INP",    # flake8-no-pep420
    "PIE",    # flake8-pie
    "T20",    # flake8-print
    "PYI",    # flake8-pyi
    "PT",     # flake8-pytest-style
    "Q",      # flake8-quotes
    "RSE",    # flake8-raise
    "RET",    # flake8-return
    "SLF",    # flake8-self
    "SLOT",   # flake8-slots
    "SIM",    # flake8-simplify
    "TID",    # flake8-tidy-imports
    "TCH",    # flake8-type-checking
    "INT",    # flake8-gettext
    "ARG",    # flake8-unused-arguments
    "PTH",    # flake8-use-pathlib
    "TD",     # flake8-todos
    "FIX",    # flake8-fixme
    "ERA",    # eradicate (commented code)
    "PD",     # pandas-vet
    "PGH",    # pygrep-hooks
    "PL",     # Pylint
    "TRY",    # tryceratops
    "FLY",    # flynt
    "NPY",    # NumPy-specific (should find nothing)
    "PERF",   # Perflint
    "FURB",   # refurb
    "RUF",    # Ruff-specific
]

ignore = [
    "D100",   # Missing docstring in public module (handled by module docstring)
    "D104",   # Missing docstring in public package
    "ANN101", # Missing type annotation for self (deprecated)
    "ANN102", # Missing type annotation for cls (deprecated)
    "COM812", # Conflicts with formatter
    "ISC001", # Conflicts with formatter
]

# EXTREME: Zero tolerance for complexity
[lint.mccabe]
max-complexity = 10

[lint.pylint]
max-args = 5
max-branches = 10
max-returns = 3
max-statements = 30

[lint.pydocstyle]
convention = "google"

[lint.flake8-annotations]
allow-star-arg-any = false
mypy-init-return = true
suppress-none-returning = true

[lint.flake8-bandit]
check-typed-exception = true

[lint.per-file-ignores]
"tests/*" = [
    "S101",   # Assert allowed in tests
    "ARG001", # Unused function argument (fixtures)
    "PLR2004", # Magic value comparison
    "D103",   # Missing docstring in public function
]

[format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
docstring-code-format = true
```

### 4.3 ty.toml

```toml
# ty type checker configuration

[environment]
python-version = "3.12"

[rules]
# EXTREME: All type checks enabled
strict = true

[output]
# Report all errors
error-limit = 0
```

### 4.4 Makefile

```makefile
.PHONY: all lint format typecheck test coverage comply clean

# PMAT Quality Gates
all: comply

lint:
	uv run ruff check src tests

format:
	uv run ruff format src tests

format-check:
	uv run ruff format --check src tests

typecheck:
	uv run ty check src tests

test:
	uv run pytest --doctest-modules

coverage:
	uv run pytest --cov=src/algorithm_corpus --cov-branch --cov-report=term-missing --cov-fail-under=95

# PMAT Compliance (ALL must pass)
comply: format-check lint typecheck coverage
	@echo "PMAT COMPLY: All gates passed"

# Development helpers
dev-setup:
	uv sync
	uv tool install ruff
	uv tool install ty

clean:
	rm -rf .pytest_cache .coverage htmlcov .ruff_cache __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
```

---

## 5. Quality Standards

### 5.1 PMAT Compliance Requirements

| Gate | Tool | Threshold | Validation |
|------|------|-----------|------------|
| **Gate 1** | `ruff check` | Zero violations | `uv run ruff check src tests` |
| **Gate 2** | `ruff format` | No changes needed | `uv run ruff format --check src tests` |
| **Gate 3** | `ty` | Zero type errors | `uv run ty check src tests` |
| **Gate 4** | `pytest` | All pass + doctests | `uv run pytest --doctest-modules` |
| **Gate 5** | `coverage` | 95% branch minimum | `--cov-fail-under=95` |

### 5.2 TDG Scoring Criteria

| Metric | Target | Weight |
|--------|--------|--------|
| Cyclomatic Complexity | ≤10 per function | 25% |
| Cognitive Complexity | ≤10 per function | 25% |
| Test Coverage | ≥95% branch | 20% |
| Type Annotation | 100% | 15% |
| Documentation | 100% docstrings | 15% |

**Minimum Grade: A-** (TDG ≤ 1.5)

### 5.3 Testing Strategy

**Three-Layer Testing (EXTREME Quality):**

1. **Inline Doctests** (Layer 1)
   - Minimum 3 examples per public function
   - Happy path, edge case, error case
   - Serve as executable documentation

2. **Unit Tests** (Layer 2)
   - One test file per source file
   - Popperian falsification via invariant properties
   - Boundary condition coverage

3. **Property-Based Testing** (Layer 3)
   - Use `random` module for test generation (stdlib only)
   - Minimum 100 random inputs per property
   - Focus on algorithm invariants

---

## 6. Popperian Falsification Methodology

### 6.1 Philosophy

> "The criterion of the scientific status of a theory is its falsifiability."
> — Karl Popper, *The Logic of Scientific Discovery* (1959)

Rather than attempting to **verify** algorithms work, we design tests that could **falsify** them. Each algorithm specifies **invariant properties** that must hold for correctness.

### 6.2 Invariant Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Structural** | Output structure properties | "Sorted output is same length as input" |
| **Ordering** | Order relationships | "Output is monotonically increasing" |
| **Boundary** | Value constraints | "All distances are non-negative" |
| **Relational** | Cross-value relationships | "Triangle inequality holds" |
| **Identity** | Self-referential properties | "Distance to self is zero" |

### 6.3 Example Invariants by Category

**Sorting Algorithms:**
- P1: Output length equals input length
- P2: Output is permutation of input
- P3: Output is monotonically ordered
- P4: Stable sort preserves relative order of equal elements

**Graph Algorithms:**
- P1: All distances non-negative (Dijkstra)
- P2: MST has exactly V-1 edges
- P3: Topological order respects all edges
- P4: Connected components partition vertices

**Dynamic Programming:**
- P1: Optimal substructure property
- P2: Overlapping subproblems cached
- P3: Solution within problem constraints

---

## 7. Peer-Reviewed Citations

### 7.1 Required Citation Format

Every algorithm file must include peer-reviewed citations in the module docstring:

```python
"""Algorithm Name.

References:
    [1] Author, A.B. (Year). "Title of Paper".
        Journal Name. Volume: Pages. doi:XX.XXXX/XXXXXXX

    [2] Author, C.D., Author, E.F. (Year).
        "Title of Book" (Edition). Publisher. Chapter X.
"""
```

### 7.2 Canonical References

| Algorithm | Primary Reference |
|-----------|-------------------|
| Dijkstra | Dijkstra, E.W. (1959). Numerische Mathematik. 1: 269-271 |
| Bellman-Ford | Bellman, R. (1958). Quarterly of Applied Mathematics. 16: 87-90 |
| Floyd-Warshall | Floyd, R.W. (1962). CACM. 5(6): 345 |
| Union-Find | Tarjan, R.E. (1975). JACM. 22(2): 215-225 |
| KMP | Knuth, D.E., Morris, J.H., Pratt, V.R. (1977). SIAM J. Comput. 6(2): 323-350 |
| Quicksort | Hoare, C.A.R. (1961). Computer Journal. 5(1): 10-16 |
| Mergesort | von Neumann, J. (1945). First Draft of EDVAC |
| Binary Heap | Williams, J.W.J. (1964). CACM. 7(6): 347-348 |
| Dynamic Programming | Bellman, R. (1954). Bull. Amer. Math. Soc. 60: 503-515 |
| Backtracking | Golomb, S.W., Baumert, L.D. (1965). JACM. 12(4): 516-524 |

---

## 8. Depyler Transpilation Compatibility

### 8.1 Supported Standard Library Modules

Only these stdlib modules are guaranteed to transpile:

| Module | Rust Mapping | Status |
|--------|--------------|--------|
| `heapq` | `std::collections::BinaryHeap` | Validated |
| `collections.deque` | `std::collections::VecDeque` | Validated |
| `collections.Counter` | `HashMap<K, usize>` | Validated |
| `collections.defaultdict` | `HashMap` with default | Validated |
| `functools.reduce` | `Iterator::fold` | Validated |
| `itertools` (limited) | `std::iter` | Partial |
| `bisect` | Binary search | Validated |
| `math` | `std::f64` methods | Validated |
| `random` | `rand` crate | Validated |

### 8.2 Type Mapping

| Python | Rust | Notes |
|--------|------|-------|
| `int` | `i64` | Default integer width |
| `float` | `f64` | Only f64 supported |
| `bool` | `bool` | Direct mapping |
| `str` | `String` | Always owned |
| `list[T]` | `Vec<T>` | Type parameter required |
| `dict[K, V]` | `HashMap<K, V>` | Type parameters required |
| `set[T]` | `HashSet<T>` | Type parameter required |
| `tuple[T, ...]` | `(T, ...)` | Fixed-size tuple |
| `T \| None` | `Option<T>` | Proper None handling |

### 8.3 Patterns to Avoid

```python
# AVOID: Star unpacking (not supported)
def foo(*args): ...           # NO
result = func(*items)         # NO

# AVOID: Nested functions (not supported)
def outer():
    def inner(): ...          # NO

# AVOID: Dynamic features
eval("code")                  # NO
getattr(obj, "attr")          # NO

# PREFER: Iterative over recursive
def factorial_recursive(n):   # Avoid
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

def factorial_iterative(n):   # Prefer
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

---

## 9. Tiered Corpus Reference

This corpus is **Tier 4** in the Depyler corpus hierarchy:

| Tier | Repository | Files | Focus |
|------|------------|-------|-------|
| **1** | reprorusted-std-only | 20 | Stdlib module mapping |
| **2** | reprorusted-python-cli | 16 | CLI tooling patterns |
| **3** | hugging-face-ground-truth-corpus | 128 | ML/AI patterns |
| **4** | algorithm-competition-corpus | 100+ | Algorithmic patterns |
| **5** | jax-ground-truth-corpus | 15 | JAX numerical patterns |

### 9.1 Complementary Focus

- **Tier 1-2**: Language fundamentals and CLI patterns
- **Tier 3**: ML/AI domain-specific patterns
- **Tier 4**: Classic CS algorithms (this corpus)
- **Tier 5**: Numerical computing and autodiff

---

## 10. Development Workflow

### 10.1 Adding a New Algorithm

```bash
# 1. Start work on ticket
pmat work start ALGO-XXX

# 2. Create algorithm file with template
# src/algorithm_corpus/<category>/<algorithm>.py

# 3. Write doctests FIRST (TDD)
# Minimum 3 doctests per function

# 4. Implement algorithm
# Follow all type annotation requirements

# 5. Create test file
# tests/test_<category>/test_<algorithm>.py

# 6. Run quality gates
make comply

# 7. Complete work
pmat work complete ALGO-XXX
```

### 10.2 Quality Gate Checklist

Before every commit:

- [ ] `uv run ruff format --check src tests` — No format changes
- [ ] `uv run ruff check src tests` — Zero lint violations
- [ ] `uv run ty check src tests` — Zero type errors
- [ ] `uv run pytest --doctest-modules` — All tests pass
- [ ] `uv run pytest --cov-fail-under=95` — 95% branch coverage

---

## Appendix A: Stdlib-Only Imports Reference

```python
# Allowed imports for this corpus
from __future__ import annotations

# Standard library (algorithm-relevant subset)
import bisect
import collections
import functools
import heapq
import itertools
import math
import operator
import random
import re
import string
import typing

# From collections
from collections import Counter, defaultdict, deque

# From typing (only TYPE_CHECKING guard)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
```

---

## Appendix B: Coverage Exclusion Patterns

```python
# These patterns are excluded from coverage requirements

if TYPE_CHECKING:    # Type-only imports
    ...

raise NotImplementedError  # Abstract methods

pragma: no cover     # Explicit exclusion (use sparingly)
```

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-01 | Initial specification |
