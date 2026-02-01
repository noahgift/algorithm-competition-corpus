# Algorithm Competition Corpus

A pure Python algorithm corpus with **EXTREME quality standards** for Depyler transpilation and education.

## Quality Standards

| Metric | Requirement |
|--------|-------------|
| **Dependencies** | Zero (stdlib only) |
| **Type Coverage** | 100% |
| **Test Coverage** | 95% branch minimum |
| **PMAT TDG Grade** | A- or higher |
| **Lint Violations** | Zero |

## Toolchain

```bash
uv      # Package management
ruff    # Linting + formatting
ty      # Type checking
pytest  # Testing
pmat    # Project management
```

## Quick Start

```bash
# Setup
uv sync
make dev-setup

# Run all quality gates
make comply

# Development
make format   # Auto-format
make fix      # Auto-fix lint issues
make test     # Run tests
make coverage # With coverage report
```

## Categories (100+ files)

| Category | Files | Description |
|----------|-------|-------------|
| `graph/` | 10 | BFS, DFS, Dijkstra, Bellman-Ford, union-find, SCC |
| `dynamic_programming/` | 12 | Knapsack, LCS, LIS, edit distance, coin change |
| `sliding_window/` | 6 | Max sum subarray, min window substring |
| `two_pointers/` | 7 | Two sum, three sum, container with water |
| `binary_search/` | 8 | Rotated array, peak element, search insert |
| `backtracking/` | 8 | N-queens, permutations, sudoku, word search |
| `bit_manipulation/` | 7 | XOR tricks, counting bits, bitmask DP |
| `sorting/` | 8 | Quicksort, mergesort, heapsort, radix |
| `heap_priority_queue/` | 6 | Kth largest, merge K sorted, median stream |
| `trees/` | 8 | Traversals, BST validation, LCA, serialize |
| `linked_list/` | 6 | Reverse, cycle detection, palindrome |
| `string/` | 8 | KMP, Rabin-Karp, Z-algorithm, palindrome |
| `math/` | 8 | GCD, sieve, fast exponentiation, combinatorics |
| `intervals/` | 6 | Merge intervals, meeting rooms |

## Type Annotation Requirements

All files use **modern Python 3.12+ syntax** (PEP 585 + PEP 604):

```python
from __future__ import annotations

import heapq


def dijkstra(
    graph: dict[int, list[tuple[int, int]]],
    start: int,
) -> dict[int, int]:
    """Find shortest paths from start to all nodes.

    References:
        [1] Dijkstra, E.W. (1959). Numerische Mathematik. 1: 269-271.

    Examples:
        >>> dijkstra({0: [(1, 4)], 1: []}, 0)
        {0: 0, 1: 4}
    """
    distances: dict[int, int] = {start: 0}
    heap: list[tuple[int, int]] = [(0, start)]
    # ... implementation
    return distances
```

## Popperian Falsification

Tests are designed to **disprove** correctness via invariant properties:

```python
def test_p1_distances_non_negative(self) -> None:
    """P1: If any d[v] < 0, Dijkstra is WRONG."""
    for _ in range(100):
        graph = random_graph()
        distances = dijkstra(graph, 0)
        for d in distances.values():
            assert d >= 0, "Invariant P1 violated"
```

## Depyler Transpilation

```bash
# Transpile a single file
depyler transpile src/algorithm_corpus/graph/dijkstra.py

# Analyze the entire corpus
depyler-corpus analyze --corpus ~/src/algorithm-competition-corpus
```

## Project Structure

```
algorithm-competition-corpus/
├── pyproject.toml          # Project config (uv)
├── ruff.toml               # EXTREME lint config
├── ty.toml                 # Type checker config
├── Makefile                # Quality gates
├── CLAUDE.md               # Development guidelines (P0)
├── src/
│   └── algorithm_corpus/
│       ├── __init__.py
│       ├── py.typed
│       ├── graph/
│       ├── dynamic_programming/
│       └── ...
└── tests/
    ├── conftest.py         # Fixtures
    ├── test_graph/
    └── ...
```

## Development Workflow

```bash
# 1. Start work
pmat work start ALGO-XXX

# 2. Create algorithm + tests

# 3. Run quality gates (ALL must pass)
make comply

# 4. Commit
git commit -m "feat: add algorithm"

# 5. Complete work
pmat work complete ALGO-XXX
```

## Design Principles

- **Stdlib only**: Zero external dependencies
- **Fully typed**: Modern syntax with `dict[K, V]`, `list[T]`, `T | None`
- **Peer-reviewed**: Every algorithm cites academic sources
- **Falsifiable**: Tests designed to disprove, not just verify
- **Iterative**: Prefer iteration over recursion for Rust translation
- **Self-contained**: Each file stands alone

## Corpus Tiers

This corpus is **Tier 4** in the Depyler ecosystem:

| Tier | Repository | Focus |
|------|------------|-------|
| 1 | reprorusted-std-only | Stdlib module mapping |
| 2 | reprorusted-python-cli | CLI tooling patterns |
| 3 | hugging-face-ground-truth-corpus | ML/AI patterns |
| **4** | **algorithm-competition-corpus** | **Algorithmic patterns** |
| 5 | jax-ground-truth-corpus | Numerical computing |

## License

MIT
