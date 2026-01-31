# Building PDF Extractor Pro Executable

This guide explains how to build a standalone executable and installer for PDF Extractor Pro.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Building on Windows](#building-on-windows)
- [Building on Linux/Mac](#building-on-linuxmac)
- [Manual Build Steps](#manual-build-steps)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### All Platforms
1. **Python 3.7 or higher**
   ```bash
   python --version
   ```

2. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

3. **Install all dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Windows Only (for installer creation)
4. **Inno Setup 6** (optional, for creating .exe installer)
   - Download from: https://jrsoftware.org/isdl.php
   - Install and add to PATH

### System Dependencies
Ensure these are installed on your system:
- **Tesseract OCR** - For text extraction
- **Poppler** - For PDF to image conversion

See main README.md for installation instructions.

---

## Building on Windows

### Option 1: Automated Build (Recommended)

1. **Run the build script:**
   ```cmd
   build.bat
   ```

2. **Output:**
   - Standalone executable: `dist\PDF_Extractor_Pro\PDF_Extractor_Pro.exe`
   - Installer (if Inno Setup installed): `installer\PDF_Extractor_Pro_Setup.exe`

### Option 2: Manual Build

1. **Build executable:**
   ```cmd
   pyinstaller pdf_extractor.spec --clean
   ```

2. **Create installer (if Inno Setup installed):**
   ```cmd
   iscc setup.iss
   ```

---

## Building on Linux/Mac

### Automated Build

1. **Make build script executable:**
   ```bash
   chmod +x build.sh
   ```

2. **Run the build script:**
   ```bash
   ./build.sh
   ```

3. **Output:**
   - Executable bundle: `dist/PDF_Extractor_Pro/`
   - Run with: `./dist/PDF_Extractor_Pro/PDF_Extractor_Pro`

### Manual Build

```bash
# Clean previous builds
rm -rf build dist

# Build with PyInstaller
pyinstaller pdf_extractor.spec --clean

# Run the application
./dist/PDF_Extractor_Pro/PDF_Extractor_Pro
```

---

## Manual Build Steps

If you prefer to build manually or need to customize:

### 1. Install Build Dependencies
```bash
pip install pyinstaller
pip install -r requirements.txt
```

### 2. Build with PyInstaller
```bash
pyinstaller pdf_extractor.spec --clean
```

This creates:
- `build/` - Temporary build files (can be deleted)
- `dist/PDF_Extractor_Pro/` - Standalone application folder

### 3. Test the Build
```bash
# Windows
dist\PDF_Extractor_Pro\PDF_Extractor_Pro.exe

# Linux/Mac
./dist/PDF_Extractor_Pro/PDF_Extractor_Pro
```

### 4. Create Installer (Windows Only)
```bash
iscc setup.iss
```

This creates `installer/PDF_Extractor_Pro_Setup.exe`

---

## Build Output Structure

### Windows
```
PDF-Extractor/
├── dist/
│   └── PDF_Extractor_Pro/
│       ├── PDF_Extractor_Pro.exe    # Main executable
│       ├── templates/                # Web templates
│       ├── static/                   # CSS, JS files
│       └── [many .dll and .pyd files]
└── installer/
    └── PDF_Extractor_Pro_Setup.exe  # Installer
```

### Linux/Mac
```
PDF-Extractor/
└── dist/
    └── PDF_Extractor_Pro/
        ├── PDF_Extractor_Pro         # Main executable
        ├── templates/                # Web templates
        ├── static/                   # CSS, JS files
        └── [many .so files]
```

---

## Distribution

### Windows Installer Method (Recommended)
1. Share `installer/PDF_Extractor_Pro_Setup.exe`
2. Users run the installer
3. Application installs to `C:\Program Files\PDF Extractor Pro\`
4. Desktop shortcut created (optional)

### Portable Executable Method
1. Zip the entire `dist/PDF_Extractor_Pro/` folder
2. Share the zip file
3. Users extract and run `PDF_Extractor_Pro.exe`

### Important Notes for Users
- **Tesseract OCR** must be installed separately for OCR functionality
- **Poppler** must be installed separately for PDF to image conversion
- **Gemini API Key** should be set via environment variable or configuration

---

## Troubleshooting

### PyInstaller Build Fails

**Problem:** Import errors or missing modules
```bash
# Solution: Add missing imports to pdf_extractor.spec
hiddenimports = [
    'your_missing_module',
]
```

**Problem:** Templates/static files not found
```bash
# Solution: Verify datas in pdf_extractor.spec
datas = [
    ('templates', 'templates'),
    ('static', 'static'),
]
```

### Executable Fails to Run

**Problem:** DLL not found (Windows)
- Install Visual C++ Redistributable
- Download: https://aka.ms/vs/17/release/vc_redist.x64.exe

**Problem:** Permission denied (Linux/Mac)
```bash
chmod +x dist/PDF_Extractor_Pro/PDF_Extractor_Pro
```

**Problem:** Port 5000 already in use
- Close other applications using port 5000
- Or modify `launcher.py` to use a different port

### Inno Setup Issues

**Problem:** `iscc` command not found
- Add Inno Setup to PATH: `C:\Program Files (x86)\Inno Setup 6\`
- Or use full path: `"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup.iss`

**Problem:** Setup script compilation errors
- Check that `dist/PDF_Extractor_Pro/` exists
- Verify all files are present

### Large Executable Size

The executable may be 200-500 MB due to:
- Python runtime
- Flask and dependencies
- PDF processing libraries
- AI libraries

To reduce size:
1. Use `upx=True` in spec file (already enabled)
2. Remove unused dependencies from requirements.txt
3. Use `--exclude-module` for unneeded packages

---

## Customization

### Change Application Icon
1. Create or obtain an `.ico` file (Windows) or `.icns` (Mac)
2. Edit `pdf_extractor.spec`:
   ```python
   exe = EXE(
       ...
       icon='path/to/your/icon.ico',
   )
   ```

### Change Application Name
Edit `setup.iss`:
```ini
#define MyAppName "Your App Name"
```

### Change Default Port
Edit `launcher.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=False)
```

---

## Advanced Configuration

### Bundle External Dependencies

To bundle Tesseract or Poppler with your executable:

1. Add binaries to spec file:
```python
binaries = [
    ('path/to/tesseract.exe', '.'),
    ('path/to/poppler/bin/*', 'poppler/bin'),
]
```

2. Update code to find bundled binaries

### Create Mac .app Bundle
```bash
pyinstaller pdf_extractor.spec --clean --windowed
```

### Create Linux .AppImage
Use `pyinstaller` with AppImage tools (requires additional setup)

---

## Build for Different Architectures

### Windows
- 32-bit: Build on 32-bit Python
- 64-bit: Build on 64-bit Python (recommended)

### Mac
- Intel: `arch -x86_64 pyinstaller pdf_extractor.spec`
- Apple Silicon: `arch -arm64 pyinstaller pdf_extractor.spec`
- Universal: Requires additional configuration

---

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Build Executable

on: [push]

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt pyinstaller
      - run: pyinstaller pdf_extractor.spec --clean
      - uses: actions/upload-artifact@v2
        with:
          name: PDF-Extractor-Windows
          path: dist/PDF_Extractor_Pro/
```

---

## Support

For build issues:
1. Check this document
2. Review PyInstaller documentation: https://pyinstaller.org
3. Check Inno Setup documentation: https://jrsoftware.org/ishelp/
4. Open an issue on GitHub

---

## License

Same as main project (MIT License)
