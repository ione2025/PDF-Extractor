@echo off
REM Build script for PDF Extractor Pro Windows Installer
REM This script builds the executable and creates the installer

echo ========================================
echo PDF Extractor Pro - Build Script
echo ========================================
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [ERROR] PyInstaller is not installed!
    echo Please install it using: pip install pyinstaller
    pause
    exit /b 1
)

REM Step 1: Install dependencies
echo [1/4] Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Step 2: Clean previous builds
echo [2/4] Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist installer rmdir /s /q installer
mkdir installer
echo.

REM Step 3: Build executable with PyInstaller
echo [3/4] Building executable with PyInstaller...
echo This may take several minutes...
pyinstaller pdf_extractor.spec --clean
if errorlevel 1 (
    echo [ERROR] PyInstaller build failed
    pause
    exit /b 1
)
echo.

REM Step 4: Create installer with Inno Setup (if available)
echo [4/4] Creating installer...
where iscc >nul 2>&1
if %errorlevel% equ 0 (
    echo Inno Setup found. Creating installer...
    iscc setup.iss
    if errorlevel 1 (
        echo [WARNING] Installer creation failed, but executable is ready
    ) else (
        echo.
        echo ========================================
        echo BUILD SUCCESSFUL!
        echo ========================================
        echo Installer: installer\PDF_Extractor_Pro_Setup.exe
        echo Executable: dist\PDF_Extractor_Pro\PDF_Extractor_Pro.exe
        echo ========================================
    )
) else (
    echo [INFO] Inno Setup not found - skipping installer creation
    echo The standalone executable is available at:
    echo dist\PDF_Extractor_Pro\PDF_Extractor_Pro.exe
    echo.
    echo To create an installer:
    echo 1. Download Inno Setup from https://jrsoftware.org/isdl.php
    echo 2. Install it and add to PATH
    echo 3. Run this script again
    echo ========================================
)

echo.
echo Build complete! You can now distribute the application.
pause
