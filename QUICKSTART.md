# Quick Start Guide - PDF Extractor Pro

## For Windows Users (Easiest Method)

### Building the Installer

1. **Install Prerequisites**:
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller
   ```

2. **Run the Build Script**:
   ```cmd
   build.bat
   ```
   This will:
   - Install all dependencies
   - Create standalone executable
   - Generate Windows installer (if Inno Setup is installed)

3. **Install the Application**:
   - Run `installer\PDF_Extractor_Pro_Setup.exe`
   - Follow the installation wizard
   - Choose installation location (default: `C:\Program Files\PDF Extractor Pro\`)
   - Optionally create desktop shortcut

4. **Launch**:
   - Double-click desktop shortcut, or
   - Find in Start Menu: "PDF Extractor Pro"
   - Application automatically opens in your default web browser

## For Linux/Mac Users

1. **Make build script executable**:
   ```bash
   chmod +x build.sh
   ```

2. **Run the build script**:
   ```bash
   ./build.sh
   ```

3. **Run the application**:
   ```bash
   ./dist/PDF_Extractor_Pro/PDF_Extractor_Pro
   ```

## For Python Developers

### Run Directly from Source

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access in browser**:
   - Open `http://localhost:5000`

### Using the Launcher Script

```bash
python launcher.py
```
- Automatically opens browser
- Shows startup messages
- Easy to stop with Ctrl+C

## System Requirements

### Minimum
- Windows 10/11, macOS 10.14+, or Linux
- 4GB RAM
- 500MB free disk space
- Python 3.7+ (if running from source)

### Required External Tools
- **Tesseract OCR**: For text extraction from images
  - Windows: https://github.com/UB-Mannheim/tesseract/wiki
  - Mac: `brew install tesseract tesseract-lang`
  - Linux: `sudo apt install tesseract-ocr tesseract-ocr-ara tesseract-ocr-chi-sim tesseract-ocr-chi-tra`

- **Poppler**: For PDF to image conversion
  - Windows: https://github.com/oschwartz10612/poppler-windows/releases
  - Mac: `brew install poppler`
  - Linux: `sudo apt install poppler-utils`

### Optional
- **Inno Setup** (Windows only): For creating installer
  - Download: https://jrsoftware.org/isdl.php
  - Add to PATH for automatic installer creation

## Using the Application

### Interface Overview

The Adobe-style interface includes:

1. **Top Toolbar**:
   - Open: Select PDF file
   - Extract Text: Extract text with OCR
   - Extract Images: AI-powered image analysis
   - Export: Download Excel reports

2. **Left Sidebar**:
   - Text & OCR: Text extraction tools
   - Images & AI: Image analysis tools
   - PDF Info: Document metadata

3. **Right Panel**:
   - Extraction method selection
   - OCR options
   - Feature descriptions

4. **Main Workspace**:
   - Welcome screen
   - Progress indicators
   - Results display

5. **Status Bar**:
   - Current operation status
   - Supported languages indicator

### Text Extraction

1. Click "Open" or use the quick action button
2. Select a PDF file
3. Choose extraction method:
   - **PDFPlumber** (Recommended): Better for formatted documents
   - **PyPDF2**: Alternative method
4. Enable/disable multi-language OCR
5. Click "Extract Text"
6. Copy results to clipboard

### Image Extraction & AI Analysis

1. Select PDF file
2. Click "Extract Images" from toolbar
3. Wait for processing (shows progress)
4. View results:
   - Total images found
   - Products with SKU detected
   - Product details (category, description, colors)
5. Download Excel report with all data

## Troubleshooting

### Application Won't Start
- **Check Python version**: `python --version` (needs 3.7+)
- **Verify dependencies**: `pip install -r requirements.txt`
- **Check port**: Ensure port 5000 is not in use

### OCR Not Working
- **Install Tesseract**: See system requirements above
- **Check installation**: `tesseract --version`
- **Verify language packs**: `tesseract --list-langs`
- Should show: eng, ara, chi_tra, chi_sim

### Build Failed
- **Missing PyInstaller**: `pip install pyinstaller`
- **Permission issues**: Run as Administrator (Windows) or with sudo (Linux/Mac)
- **Disk space**: Ensure 1GB free space for build files

### Images Not Extracting
- **Install Poppler**: See system requirements
- **Check installation**: `pdftoppm -v` (Windows/Linux) or `pdftoppm -v` (Mac)
- **Gemini API**: Verify API key is set in environment or `app.py`

## Configuration

### Setting Gemini API Key

**Environment Variable (Recommended)**:
```bash
# Windows
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY=your_api_key_here
```

**Or edit `app.py`**:
```python
GEMINI_API_KEY = "your_api_key_here"
```

### Changing Port

Edit `launcher.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=False)
```

## Support

- **Documentation**: See [BUILD.md](BUILD.md) for detailed build instructions
- **Issues**: Report on GitHub Issues
- **README**: Full feature list in [README.md](README.md)

## Tips

1. **First Use**: Start with text extraction to verify setup
2. **Large PDFs**: Image extraction takes longer (AI processing)
3. **Offline Use**: Text extraction works offline; image AI requires internet
4. **Best Results**: Use high-quality PDFs for better OCR accuracy
5. **Excel Reports**: Automatically saved in `output/` folder

---

**Built with ❤️ to be the most powerful PDF tool on the internet**
