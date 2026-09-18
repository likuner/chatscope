#!/bin/bash
# Friday AI Assistant Launcher
# Optimized for Apple Silicon (ARM64)

# Check if virtual environment exists and activate it
if [ -d "venv" ]; then
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
fi

arch -arm64 python3 main.py

# Deactivate virtual environment if it was activated
if [ -d "venv" ]; then
    deactivate 2>/dev/null
fi
