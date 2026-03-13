# Python executable
PYTHON := .venv/bin/python
PIP := .venv/bin/pip

# Default target
DEFAULT_GOAL := help

help:
	@echo "Available commands:"
	@echo "  make install      Install dependencies"
	@echo "  make run-agent    Run the Tavily tool agent"
	@echo "  make lint         Run flake8 linter"
	@echo "  make format       Format code with black"
	@echo "  make test         Run tests"
	@echo "  make clean        Remove cache files"

install:
	$(PIP) install .
	
sync:
	uv sync

run-agent:
	uv run python -m gen_agent.agents.tavily_search_in_tool_agent

lint:
	uv run ruff check .

format:
	uv run ruff format .

fix:
	uv run ruff check --fix .


test:
	uv run pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete	