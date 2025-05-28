#!/bin/bash

cd "$(dirname "$0")"

# Set up virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Setting up virtual environment..."
  python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install package if not installed
pip show youtube-transcript-api > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Installing required package..."
  pip install youtube-transcript-api
fi

# Run Python script
clear
echo "Launching YouTube Transcript Tool..."
python3 main.py
