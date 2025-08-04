#!/bin/bash
# Quick script to activate the development environment

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Run 'make setup' first."
    exit 1
fi

# Activate the virtual environment
source venv/bin/activate
echo "✅ Development environment activated!"
echo ""
echo "Available commands:"
echo "  make lint    - Run pylint on your code"
echo "  make format  - Auto-format code with black and isort"
echo "  make check   - Check formatting without changes"
echo "  make fix     - Format code and run linter"
echo "  make help    - Show all available commands"
echo ""
echo "To deactivate: deactivate"