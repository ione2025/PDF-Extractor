#!/bin/bash
# Build script for PDF Extractor Pro (Linux/Mac)
# Creates a standalone executable bundle

set -e

echo "========================================"
echo "PDF Extractor Pro - Build Script"
echo "========================================"
echo ""

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "[ERROR] PyInstaller is not installed!"
    echo "Please install it using: pip install pyinstaller"
    exit 1
fi

# Step 1: Install dependencies
echo "[1/3] Installing dependencies..."
pip install -r requirements.txt
pip install pyinstaller
echo ""

# Step 2: Clean previous builds
echo "[2/3] Cleaning previous builds..."
rm -rf build dist installer
mkdir -p installer
echo ""

# Step 3: Build executable with PyInstaller
echo "[3/3] Building executable with PyInstaller..."
echo "This may take several minutes..."
pyinstaller pdf_extractor.spec --clean

echo ""
echo "========================================"
echo "BUILD SUCCESSFUL!"
echo "========================================"
echo "Executable bundle: dist/PDF_Extractor_Pro/"
echo "Run: ./dist/PDF_Extractor_Pro/PDF_Extractor_Pro"
echo "========================================"
echo ""
echo "Build complete! You can now distribute the application."
