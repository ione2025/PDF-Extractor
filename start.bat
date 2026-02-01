@echo off
echo ============================================================
echo PDF Extractor Pro - Quick Start
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version

echo.
echo [2/3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [3/3] Starting PDF Extractor Pro...
echo.
echo ============================================================
echo Application will start in a few seconds...
echo Open your browser to: http://localhost:5000
echo Press CTRL+C to stop the server
echo ============================================================
echo.

python app.py

pause
