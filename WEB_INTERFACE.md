# 🌐 Web Interface Guide - PDF Extractor Pro

## Overview

PDF Extractor Pro features a professional Adobe Acrobat-style web interface that provides a powerful and intuitive way to extract text and images from PDF files with AI-powered analysis.

![Web Interface](https://github.com/user-attachments/assets/24da9158-c6f0-4033-9065-d994063d12ce)

## 🚀 Quick Start

### Starting the Web Interface

**Option 1: Using the Launcher (Recommended)**
```bash
python launcher.py
```
This will:
- Start the Flask web server
- Automatically open your default browser
- Navigate to http://localhost:5000

**Option 2: Direct Flask Start**
```bash
python app.py
```
Then manually open your browser and go to: http://localhost:5000

**Option 3: Windows Executable**
- Double-click the desktop shortcut after installation
- Or launch from Start Menu: "PDF Extractor Pro"

## 🎨 Interface Overview

### Main Components

#### 1. **Top Header Bar**
Located at the top of the screen with quick access buttons:
- **📂 Open**: Upload PDF files
- **📝 Extract Text**: Quick text extraction
- **🖼️ Extract Images**: AI-powered image analysis
- **💾 Export**: Download results (enabled after processing)
- **⚙️ Settings**: Configuration options

#### 2. **Left Sidebar - Tools Panel**
Organized tool categories:

**EXTRACTION**
- **Text & OCR**: Text extraction with multi-language OCR support
- **Images & AI**: Image extraction with AI analysis

**ANALYSIS**
- **PDF Info**: Document metadata and properties

#### 3. **Main Content Area**
The central workspace that displays:
- Welcome screen when no file is loaded
- Progress indicators during processing
- Extracted text results
- Image analysis results
- Product information and statistics

#### 4. **Right Sidebar - Properties Panel**
Context-sensitive options:

**For Text Extraction:**
- Extraction Method selection (PDFPlumber/PyPDF2)
- OCR options (Enable/Disable multi-language OCR)
- Language support indicator

**For Image Analysis:**
- AI feature information
- Processing details

#### 5. **Status Bar**
Bottom bar showing:
- Current operation status
- Supported languages: English • العربية • 中文

## 📝 Using Text Extraction

### Step-by-Step Guide

1. **Select the Tool**
   - Click "Text & OCR" in the left sidebar (selected by default)

2. **Configure Options** (Right Panel)
   - Choose extraction method:
     - **PDFPlumber** (Recommended) - Better for formatted documents
     - **PyPDF2** - Alternative method for simple PDFs
   - Enable/Disable Multi-language OCR
     - Supports English, Arabic, Chinese Traditional, and Chinese Simplified

3. **Upload PDF**
   - Click "Open" in the top toolbar, or
   - Click "Open PDF File" button in the center

4. **Extract Text**
   - Click "Extract Text" button
   - Watch the progress indicator
   - Wait for extraction to complete

5. **View & Copy Results**
   - Extracted text appears in the main content area
   - Review text organized by page numbers
   - Click "Copy" button to copy all text to clipboard
   - OCR results (if applicable) appear after standard extraction

### Features

- **Page Markers**: Clear page separation (`--- Page 1 ---`)
- **OCR Integration**: Automatic OCR when minimal text is detected
- **Multi-language Support**: English, Arabic, Chinese Traditional/Simplified
- **Copy to Clipboard**: One-click copy functionality
- **Method Comparison**: Try different extraction methods for best results

## 🖼️ Using Image Analysis & AI

### Step-by-Step Guide

1. **Select the Tool**
   - Click "Images & AI" in the left sidebar

2. **Review Features** (Right Panel)
   - Ultra-HD extraction (300-400 DPI)
   - Gemini AI for SKU detection
   - Auto product categorization
   - Color extraction & SVG paths
   - Excel report generation

3. **Upload PDF**
   - Click "Open" in the top toolbar
   - Select a PDF containing product images

4. **Start Extraction**
   - Click "Extract Images" button
   - Monitor real-time progress with:
     - Progress bar
     - Percentage completed
     - Estimated time remaining (ETA)
     - Current processing step

5. **View Results**
   - **Statistics Dashboard**: 
     - Total images found
     - Products with SKU detected
     - Skipped images
   - **Product Cards**: Each extracted product shows:
     - Page number
     - SKU code
     - Product category
     - Description
   - **Output Location**: Files saved in `output/` folder

6. **Download Excel Report**
   - Click "Download Excel" button
   - Excel file contains:
     - SKU codes
     - Categories
     - Descriptions
     - Primary and secondary colors

### AI Analysis Features

For each product image, the AI extracts:
- **SKU Number**: Product identifier from the image
- **Category**: Auto-classified (Gate, Door, Fence, Handrail, Window Protection)
- **Description**: AI-generated product description
- **SVG Path**: Silhouette path for 3D modeling
- **Colors**: Primary and secondary hex colors

### Output Structure

```
output/
└── [PDF_NAME]/
    ├── [PDF_NAME]_SKU_Report.xlsx    # Excel report
    ├── Gate/
    │   ├── SKU001.webp              # High-quality image
    │   └── SKU001.json              # Product metadata
    ├── Door/
    ├── Fence/
    ├── Handrail/
    └── Window Protection/
```

## 🎯 Advanced Features

### Progress Tracking

The interface provides real-time feedback:
- **Animated spinner** during processing
- **Progress bar** with percentage
- **Detailed messages** about current operation
- **ETA calculation** for image analysis
- **Status updates** in the bottom status bar

### Error Handling

If errors occur:
- Clear error messages displayed in red banner
- Automatic file cleanup
- Guidance on how to resolve issues
- No corrupted files left behind

### Responsive Design

The interface adapts to different screen sizes:
- **Desktop**: Full three-panel layout
- **Tablet**: Collapsible sidebars
- **Mobile**: Stacked layout with slide-out panels

## ⚙️ Configuration

### Port Configuration

Change the default port (5000) in `launcher.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=False)
```

### API Key Configuration

Set Gemini API key for image analysis:

**Environment Variable (Recommended):**
```bash
# Windows
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY=your_api_key_here
```

**Direct Edit in app.py:**
```python
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'your_api_key_here')
```

### Upload Limits

Modify file size limits in `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB default
```

## 🔒 Security Features

The web interface includes:
- **File Type Validation**: Only PDF files accepted
- **Secure Filename Handling**: Prevents path traversal attacks
- **Automatic Cleanup**: Temporary files deleted after processing
- **File Size Limits**: Prevents DoS attacks
- **XSS Protection**: Input sanitization

## 🐛 Troubleshooting

### Interface Won't Load

**Problem**: Browser shows "Cannot connect to localhost:5000"

**Solutions**:
1. Check if Flask is running: `ps aux | grep python`
2. Verify port 5000 is not in use: `lsof -i :5000` (Mac/Linux) or `netstat -ano | findstr :5000` (Windows)
3. Check firewall settings
4. Try restarting the application

### Upload Fails

**Problem**: File upload returns error

**Solutions**:
1. Verify file is a PDF: Check file extension
2. Check file size: Must be under 50MB by default
3. Ensure sufficient disk space in uploads folder
4. Verify file is not corrupted

### OCR Not Working

**Problem**: OCR shows "OCR failed" message

**Solutions**:
1. Install Tesseract OCR:
   ```bash
   # Ubuntu/Debian
   sudo apt install tesseract-ocr tesseract-ocr-ara tesseract-ocr-chi-tra tesseract-ocr-chi-sim
   
   # macOS
   brew install tesseract tesseract-lang
   
   # Windows
   Download from: https://github.com/UB-Mannheim/tesseract/wiki
   ```

2. Verify installation:
   ```bash
   tesseract --version
   tesseract --list-langs
   ```

3. Install Poppler (for pdf2image):
   ```bash
   # Ubuntu/Debian
   sudo apt install poppler-utils
   
   # macOS
   brew install poppler
   
   # Windows
   Download from: https://github.com/oschwartz10612/poppler-windows/releases
   ```

### Image Analysis Not Working

**Problem**: Image extraction fails or returns "Unknown" for all SKUs

**Solutions**:
1. Verify Gemini API key is set
2. Check internet connection (AI analysis requires online access)
3. Verify API quota/billing status
4. Try with a different PDF

### Slow Performance

**Problem**: Extraction takes too long

**Reasons & Solutions**:
- **Large PDFs**: Image analysis is intensive (30-60 sec per image)
- **OCR Processing**: Can take 10-30 seconds per page
- **Network**: Gemini AI requires internet - check connection speed
- **System Resources**: Ensure adequate RAM (4GB minimum)

## 📊 Performance Tips

1. **Text Extraction**: Usually completes in 1-5 seconds per PDF
2. **Image Analysis**: Expect 30-60 seconds per image (AI processing time)
3. **OCR**: 10-30 seconds per page depending on complexity
4. **Batch Processing**: Process multiple PDFs separately for better performance
5. **Large Files**: Consider splitting very large PDFs before processing

## 🌐 Network Access

### Local Network Access

To access from other devices on your network:

1. Find your local IP address:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Start with host `0.0.0.0` (already default):
   ```bash
   python app.py
   ```

3. Access from other devices:
   ```
   http://[YOUR_LOCAL_IP]:5000
   ```

### Production Deployment

For production deployment, use a WSGI server:

```bash
# Install Gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Important for Production**:
- Set `FLASK_ENV=production`
- Use HTTPS with SSL certificates
- Set up reverse proxy (Nginx/Apache)
- Configure proper file upload limits
- Enable rate limiting
- Set up proper logging and monitoring

## 🎨 Customization

### Theming

The interface uses CSS variables for theming. Edit `static/css/style.css`:

```css
:root {
    --primary-color: #667EEA;
    --secondary-color: #764BA2;
    --background: #1a1a1a;
    --surface: #252525;
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
}
```

### Language Support

To add more OCR languages, edit `app.py`:

```python
TESSERACT_LANGUAGES = 'eng+ara+chi_tra+chi_sim+fra+deu'  # Add French and German
```

Then install language packs:
```bash
sudo apt install tesseract-ocr-fra tesseract-ocr-deu
```

### Product Categories

Modify categories in `app.py`:

```python
CATEGORIES = ['Gate', 'Door', 'Fence', 'Handrail', 'Window Protection', 'Custom Category']
```

## 📱 Mobile Usage

The interface is mobile-responsive:
- Tap "☰" to open/close sidebars
- Swipe left/right to navigate panels
- Tap and hold to copy text
- Pinch to zoom on results

## 🔗 API Endpoints

The web interface uses these REST API endpoints:

- `GET /` - Main interface
- `POST /extract` - Text extraction endpoint
- `POST /extract-images` - Image analysis endpoint
- `GET /progress/<task_id>` - Progress tracking
- `GET /download-excel/<filename>` - Excel download
- `GET /health` - Health check

See [README.md](README.md) for detailed API documentation.

## 💡 Tips & Best Practices

1. **Start Simple**: Test with text extraction first
2. **High Quality PDFs**: Better results with clear, high-resolution PDFs
3. **Internet Required**: Image AI analysis needs online access
4. **Offline Mode**: Text extraction and OCR work offline
5. **Excel Reports**: Auto-saved in `output/` folder with timestamp
6. **Browser Compatibility**: Works best in Chrome, Firefox, Edge, Safari
7. **Keyboard Shortcuts**: Ctrl+C to stop server when running in terminal
8. **File Organization**: Check `output/` folder for all extracted files

## 🎓 Learning Resources

- **Quick Start**: See [QUICKSTART.md](QUICKSTART.md)
- **Full Documentation**: See [README.md](README.md)
- **Build Instructions**: See [BUILD.md](BUILD.md)
- **GitHub Issues**: Report bugs or request features

## 📞 Support

If you encounter issues:
1. Check this guide first
2. Review the troubleshooting section
3. Check [README.md](README.md) for system requirements
4. Open an issue on GitHub with:
   - Browser version
   - Operating system
   - Error messages
   - Steps to reproduce

---

**🎯 The web interface is production-ready and includes all professional features needed for PDF extraction and AI-powered analysis.**

Built with ❤️ to provide the best PDF extraction experience.
