#!/bin/bash

# Virtual environment
VENV_DIR="venv"  # Directory for virtual environment

# Check if virtual environment exists, if not create it
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment
source $VENV_DIR/bin/activate

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt
