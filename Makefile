# Algorithm Competition Corpus - PMAT Quality Gates
# All gates must pass before any commit

.PHONY: all lint format format-check typecheck test coverage doctest comply clean help dev-setup

# Default target: full compliance check
all: comply

# ============================================================================
# Individual Quality Gates
# ============================================================================

## Gate 1: Linting (zero violations)
lint:
	@echo "Gate 1: Linting..."
	uv run ruff check src tests
	@echo "Gate 1: PASSED"

## Gate 2: Formatting (no changes needed)
format:
	uv run ruff format src tests

format-check:
	@echo "Gate 2: Format check..."
	uv run ruff format --check src tests
	@echo "Gate 2: PASSED"

## Gate 3: Type checking (zero errors)
typecheck:
	@echo "Gate 3: Type checking..."
	uv run ty check src
	@echo "Gate 3: PASSED"

## Gate 4: Doctests (all pass)
doctest:
	@echo "Gate 4: Doctests..."
	uv run pytest --doctest-modules src/ -v
	@echo "Gate 4: PASSED"

## Gate 5: Unit tests (all pass)
test:
	@echo "Gate 5: Unit tests..."
	uv run pytest tests/ -v
	@echo "Gate 5: PASSED"

## Gate 6: Coverage (95% branch minimum)
coverage:
	@echo "Gate 6: Coverage..."
	uv run pytest tests/ \
		--cov=src/algorithm_corpus \
		--cov-branch \
		--cov-report=term-missing \
		--cov-fail-under=95
	@echo "Gate 6: PASSED"

# ============================================================================
# PMAT Compliance (ALL gates must pass)
# ============================================================================

## Full compliance check (run before every commit)
comply: format-check lint typecheck doctest test coverage
	@echo ""
	@echo "=============================================="
	@echo "  PMAT COMPLY: All 6 gates PASSED"
	@echo "=============================================="
	@echo ""

## Quick check (format + lint + typecheck only)
quick: format-check lint typecheck
	@echo "Quick check: PASSED"

# ============================================================================
# Development Helpers
# ============================================================================

## Set up development environment
dev-setup:
	uv sync
	uv tool install ruff
	uv tool install pytest
	uv tool install pytest-cov
	@echo "Development environment ready"

## Fix all auto-fixable issues
fix:
	uv run ruff format src tests
	uv run ruff check --fix src tests
	@echo "Auto-fixes applied"

## Generate HTML coverage report
coverage-html:
	uv run pytest tests/ \
		--cov=src/algorithm_corpus \
		--cov-branch \
		--cov-report=html \
		--cov-report=term-missing
	@echo "HTML report generated in htmlcov/"

## Run property-based tests only
property-tests:
	uv run pytest tests/ -v -m property

## Run slow tests
slow-tests:
	uv run pytest tests/ -v -m slow

# ============================================================================
# Cleanup
# ============================================================================

## Clean all generated files
clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .ruff_cache
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name ".coverage.*" -delete 2>/dev/null || true
	@echo "Cleaned"

# ============================================================================
# Help
# ============================================================================

## Show this help message
help:
	@echo "Algorithm Competition Corpus - PMAT Quality Gates"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Quality Gates:"
	@echo "  comply        Run ALL quality gates (use before commit)"
	@echo "  quick         Run format + lint + typecheck only"
	@echo "  lint          Gate 1: Check for lint violations"
	@echo "  format-check  Gate 2: Check formatting"
	@echo "  typecheck     Gate 3: Run type checker"
	@echo "  doctest       Gate 4: Run doctests"
	@echo "  test          Gate 5: Run unit tests"
	@echo "  coverage      Gate 6: Run tests with 95% coverage check"
	@echo ""
	@echo "Development:"
	@echo "  dev-setup     Install development tools"
	@echo "  format        Auto-format code"
	@echo "  fix           Auto-fix lint issues"
	@echo "  coverage-html Generate HTML coverage report"
	@echo "  clean         Remove generated files"
	@echo ""
	@echo "PMAT Workflow:"
	@echo "  1. pmat work start ALGO-XXX"
	@echo "  2. Write algorithm + tests"
	@echo "  3. make comply"
	@echo "  4. git commit"
	@echo "  5. pmat work complete ALGO-XXX"
