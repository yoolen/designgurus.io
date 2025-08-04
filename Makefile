# Simple Makefile for Python project

VENV = venv
BLACK = $(VENV)/bin/black
PYLINT = $(VENV)/bin/pylint
ISORT = $(VENV)/bin/isort

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements-dev.txt

format:
	@echo "Running black..."
	$(BLACK) problems/
	@echo "Running isort..."
	$(ISORT) problems/

lint:
	@echo "Running pylint..."
	$(PYLINT) problems/

fix:
	@make format
	@make lint

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete