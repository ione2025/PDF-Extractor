# 💻 Local Installation Guide - PDF Extractor Pro

**Complete step-by-step guide to set up PDF Extractor Pro on your PC**

No technical experience required! Just follow these steps carefully.

---

## 📋 What You'll Need

- A computer with Windows, macOS, or Linux
- Internet connection (for downloading and initial setup)
- About 15-20 minutes

---

## 🚀 Installation Steps

### Step 1: Install Python

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 (latest stable version)
3. Run the installer
4. ⚠️ **IMPORTANT:** Check the box "Add Python to PATH" at the bottom
5. Click "Install Now"
6. Wait for installation to complete
7. Verify installation:
   - Open Command Prompt (search for "cmd" in Start menu)
   - Type: `python --version`
   - You should see: `Python 3.11.x` or `Python 3.12.x`

**macOS:**
1. Open Terminal (search for "Terminal" in Spotlight)
2. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python:
   ```bash
   brew install python@3.11
   ```
4. Verify installation:
   ```bash
   python3 --version
   ```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3-pip
python3 --version
```

### Step 2: Install System Dependencies

These are required for PDF processing and OCR (text recognition).

**Windows:**

1. **Install Tesseract OCR:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Run the installer (tesseract-ocr-w64-setup-v5.3.x.exe)
   - During installation, select "Additional Language Data"
   - Check: English, Arabic, Chinese Traditional, Chinese Simplified
   - Note the installation path (usually `C:\Program Files\Tesseract-OCR`)
   - Add to PATH:
     - Right-click "This PC" → Properties → Advanced System Settings
     - Click "Environment Variables"
     - Under "System variables", find "Path", click Edit
     - Click "New" and add: `C:\Program Files\Tesseract-OCR`
     - Click OK on all windows

2. **Install Poppler:**
   - Download from: https://github.com/oschwartz10612/poppler-windows/releases
   - Download "Release-24.02.0-0.zip" (or latest version)
   - Extract to `C:\Program Files\poppler`
   - Add to PATH (same process as Tesseract):
     - Add: `C:\Program Files\poppler\Library\bin`

3. **Verify installations:**
   - Open a NEW Command Prompt (must be new to load PATH changes)
   - Type: `tesseract --version`
   - Type: `pdftoppm -v`
   - Both should work without errors

**macOS:**
```bash
# Install Tesseract with language packs
brew install tesseract tesseract-lang

# Install Poppler
brew install poppler

# Verify installations
tesseract --version
pdftoppm -v
```

**Linux (Ubuntu/Debian):**
```bash
# Install Tesseract with language packs
sudo apt install tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-ara \
    tesseract-ocr-chi-tra \
    tesseract-ocr-chi-sim

# Install Poppler
sudo apt install poppler-utils

# Verify installations
tesseract --version
pdftoppm -v
```

### Step 3: Download PDF Extractor Pro

**Option A: Using Git (Recommended)**

1. **Install Git:**
   - Windows: Download from https://git-scm.com/download/win
   - macOS: `brew install git`
   - Linux: `sudo apt install git`

2. **Clone the repository:**
   ```bash
   git clone https://github.com/ione2025/PDF-Extractor.git
   cd PDF-Extractor
   ```

**Option B: Download ZIP**

1. Go to: https://github.com/ione2025/PDF-Extractor
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to a folder (e.g., `C:\PDF-Extractor` or `~/PDF-Extractor`)
5. Open Command Prompt/Terminal and navigate to that folder:
   ```bash
   cd C:\PDF-Extractor
   # or on Mac/Linux:
   cd ~/PDF-Extractor
   ```

### Step 4: Install Python Dependencies

**All Platforms:**

1. Make sure you're in the PDF-Extractor folder
2. Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will take 2-5 minutes and install everything needed.

**If you see errors:**
- On Windows, try: `python -m pip install -r requirements.txt`
- On Mac/Linux, try: `pip3 install -r requirements.txt`

### Step 5: Configure API Key (For AI Features)

The application works without this, but AI image analysis requires a Gemini API key.

**To get a FREE API key:**
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

**To configure:**
1. Open the folder where you extracted/cloned PDF-Extractor
2. Create a file named `.env` (note the dot at the start)
3. Add this line (replace with your actual key):
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

**Note:** The app already has a demo key configured, so this step is optional for testing.

### Step 6: Run the Application

**All Platforms:**

```bash
python app.py
```

**What you should see:**
```
============================================================
PDF Extractor Pro - Web Application
============================================================

🌐 Server starting on http://0.0.0.0:5000
📊 Debug mode: False

💡 Access the application by opening the URL in your browser
🛑 Press CTRL+C to stop the server
============================================================
```

### Step 7: Open in Browser

1. Open your web browser (Chrome, Firefox, Edge, Safari)
2. Go to: **http://localhost:5000**
3. You should see the PDF Extractor Pro interface!

🎉 **Congratulations! You're ready to use PDF Extractor Pro!**

---

## 🎯 Quick Usage Guide

### Extract Text from PDF

1. Click "Open" button in the toolbar
2. Select a PDF file from your computer
3. Click "Extract Text" button
4. Wait for processing
5. Text appears in the main area
6. Click "Copy" to copy the text

### Extract Images with AI Analysis

1. Click "Open" button in the toolbar
2. Select a PDF file with product images
3. Click "Extract Images" button
4. Watch the progress bar
5. View extracted products with SKU, category, and descriptions
6. Click "Download Excel" to get a report

---

## 🐛 Troubleshooting

### "Python not found" error

**Solution:**
- Reinstall Python and make sure to check "Add Python to PATH"
- Restart your computer after installation
- Try `python3` instead of `python`

### "Tesseract not found" error

**Solution:**
- Make sure Tesseract is installed
- Verify it's in your PATH:
  - Windows: Open new Command Prompt and type `tesseract --version`
  - Mac/Linux: Type `which tesseract`
- If not found, reinstall and add to PATH (see Step 2)

### "Module not found" error

**Solution:**
```bash
pip install -r requirements.txt
```

If still failing:
```bash
pip install Flask PyPDF2 pdfplumber Pillow google-generativeai openpyxl pytesseract pdf2image gunicorn
```

### "Port 5000 already in use" error

**Solution 1 - Use different port:**
```bash
# Windows
set PORT=8080
python app.py

# Mac/Linux
export PORT=8080
python app.py
```

Then visit: http://localhost:8080

**Solution 2 - Find and stop the process:**

Windows:
```bash
netstat -ano | findstr :5000
taskkill /PID <PID_number> /F
```

Mac/Linux:
```bash
lsof -i :5000
kill -9 <PID>
```

### Application won't start

**Check Python version:**
```bash
python --version
```
Should be 3.11 or higher.

**Reinstall dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

**Run in debug mode:**
```bash
# Windows
set FLASK_DEBUG=True
python app.py

# Mac/Linux
export FLASK_DEBUG=True
python app.py
```

### OCR not working

**Verify Tesseract installation:**
```bash
tesseract --list-langs
```

Should show: eng, ara, chi_tra, chi_sim

**If languages missing:**
- Windows: Reinstall Tesseract, select language packs
- Mac: `brew reinstall tesseract tesseract-lang`
- Linux: `sudo apt install tesseract-ocr-ara tesseract-ocr-chi-tra tesseract-ocr-chi-sim`

### Images not extracting

**Verify Poppler installation:**
```bash
pdftoppm -v
```

Should show version information.

**If not working:**
- Windows: Reinstall Poppler, add to PATH
- Mac: `brew install poppler`
- Linux: `sudo apt install poppler-utils`

---

## 🔄 Updating the Application

To get the latest features:

```bash
cd PDF-Extractor
git pull
pip install --upgrade -r requirements.txt
python app.py
```

---

## 🛑 Stopping the Application

Press **CTRL+C** in the terminal/command prompt where the app is running.

---

## 💡 Tips

1. **Create a shortcut:**
   - Windows: Create a `.bat` file with the commands
   - Mac/Linux: Create a shell script

2. **Run in background:**
   - Windows: Use `start /b python app.py`
   - Mac/Linux: Use `python app.py &`

3. **Access from other devices:**
   - Note your computer's IP address
   - Access via: `http://YOUR_IP:5000`

4. **Keep window open:**
   - Don't close the Command Prompt/Terminal while using the app

---

## 📞 Still Need Help?

1. Check if all steps were followed exactly
2. Restart your computer (solves many PATH issues)
3. Try running as Administrator (Windows)
4. Open an issue on GitHub with your error message

---

## 🎓 Video Tutorial (Coming Soon)

We're working on video tutorials for:
- Windows installation
- macOS installation
- Linux installation
- First-time usage

---

**You're all set! Enjoy using PDF Extractor Pro! 🚀**
