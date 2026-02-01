# 🎯 Getting Started - PDF Extractor Pro

**The simplest way to start using PDF Extractor Pro on your computer**

---

## ⚡ Super Quick Start

### For Windows Users:

1. **Download Python:**
   - Go to: https://www.python.org/downloads/
   - Download Python 3.11 or 3.12
   - Install it (check "Add Python to PATH")

2. **Download PDF Extractor:**
   - Download this repository as ZIP
   - Extract to a folder

3. **Run the application:**
   - Double-click `start.bat` in the folder

That's it! Your browser will open automatically.

### For Mac/Linux Users:

1. **Install Python 3.11+**

2. **Download this repository**

3. **Open Terminal in the folder and run:**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

Your browser will open at http://localhost:5000

---

## 📚 What's Next?

### First Time Setup

1. **Install system tools** (needed for OCR and PDF processing):
   - **Windows:** See [INSTALL_LOCAL.md](INSTALL_LOCAL.md) - Section "Step 2"
   - **Mac:** Run `brew install tesseract poppler tesseract-lang`
   - **Linux:** Run `sudo apt install tesseract-ocr poppler-utils`

2. **Get API Key** (optional, for AI features):
   - Visit: https://makersuite.google.com/app/apikey
   - Create a free API key
   - Create `.env` file with: `GEMINI_API_KEY=your_key_here`

### Using the Application

**Extract Text from PDF:**
1. Click "Open" button
2. Select your PDF file
3. Click "Extract Text"
4. Copy or save the result

**Extract Images with AI:**
1. Click "Open" button
2. Select PDF with product images
3. Click "Extract Images"
4. Wait for AI analysis
5. Download Excel report

---

## 🆘 Need Help?

**Common Issues:**

❌ **"Python not found"**
→ Reinstall Python, check "Add to PATH"

❌ **"Module not found"**
→ Run: `pip install -r requirements.txt`

❌ **"Port already in use"**
→ Use: `set PORT=8080` then `python app.py`

❌ **OCR not working**
→ Install Tesseract (see INSTALL_LOCAL.md)

**Full Documentation:**
- [Complete Installation Guide](INSTALL_LOCAL.md) - Detailed step-by-step
- [Web Interface Guide](WEB_INTERFACE.md) - Feature documentation
- [Deployment Guide](DEPLOYMENT.md) - Production setup

---

## 💡 Quick Tips

- Keep the command window open while using the app
- Access from other devices: `http://YOUR_IP:5000`
- Stop the app: Press CTRL+C in the terminal
- Update the app: `git pull` then `pip install -r requirements.txt`

---

**Ready to extract? Run the app and visit http://localhost:5000! 🚀**
