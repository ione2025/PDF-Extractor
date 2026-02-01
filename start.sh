#!/bin/bash

echo "============================================================"
echo "PDF Extractor Pro - Quick Start"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.11 or higher"
    echo ""
    echo "macOS: brew install python@3.11"
    echo "Linux: sudo apt install python3.11"
    exit 1
fi

echo "[1/3] Checking Python installation..."
python3 --version

echo ""
echo "[2/3] Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

echo ""
echo "[3/3] Starting PDF Extractor Pro..."
echo ""
echo "============================================================"
echo "Application will start in a few seconds..."
echo "Open your browser to: http://localhost:5000"
echo "Press CTRL+C to stop the server"
echo "============================================================"
echo ""

python3 app.py
