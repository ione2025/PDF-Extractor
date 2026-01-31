# 🚀 PDF Extractor Pro

**The Most Powerful PDF Tool Ever Created** - A sophisticated web application for extracting text and images from PDF files with AI-powered analysis, OCR scanning, and automated Excel reporting.

![PDF Extractor Pro](https://github.com/user-attachments/assets/6a3999fe-142c-43b0-9e3f-ecfb401e8ce1)

## ✨ Features

### 📝 Text Extraction with Multi-language OCR
- **Dual Extraction Methods**: Choose between PDFPlumber (recommended) and PyPDF2
- **Multi-language OCR**: Tesseract OCR with support for:
  - 🇬🇧 **English** (eng)
  - 🇸🇦 **Arabic** (ara) - العربية
  - 🇨🇳 **Chinese Traditional** (chi_tra) - 中文繁體
  - 🇨🇳 **Chinese Simplified** (chi_sim) - 中文简体
- **Intelligent Detection**: Automatically applies OCR when minimal text is detected
- **Copy to Clipboard**: One-click text copying functionality
- **Page Markers**: Clear page separation in extracted content

### 🖼️ AI-Powered Image Analysis
- **Ultra-HD Extraction**: 300-400 DPI image quality using PyMuPDF with 4x zoom matrix
- **Google Gemini AI Integration**: Advanced image analysis using Gemini 1.5 Flash
  - Automatic SKU detection
  - Product category classification (Gate, Door, Fence, Handrail, Window Protection)
  - Detailed product descriptions
  - SVG path generation for 3D modeling
  - Primary and secondary color extraction (hex codes)
- **Smart Organization**: Automatic folder structure by product category
- **WebP Compression**: High-quality images with optimized file sizes
- **JSON Metadata**: Complete product data for each extracted image
- **Excel Export**: Comprehensive SKU report with descriptions and colors

### 🎯 Advanced Capabilities
- **Real-Time Progress Tracking**: Live progress bar with percentage and ETA
- **Batch Processing**: Handle multiple images in a single PDF
- **Error Recovery**: Robust error handling with automatic cleanup
- **Security**: File validation, secure filename handling, automatic file deletion
- **Responsive Design**: Works flawlessly on desktop, tablet, and mobile

### 🎨 Modern UI/UX
- **Sleek Dark Theme**: Professional design inspired by huly.io
- **Smooth Animations**: Polished micro-interactions and transitions
- **Card-Based Layout**: Clean, organized interface with subtle shadows
- **Custom Scrollbars**: Styled scrollbars for better aesthetics
- **Accessibility**: Focus indicators and keyboard navigation support

## 🖥️ Screenshots

### Text Extraction Mode
![Text Extraction](https://github.com/user-attachments/assets/6a3999fe-142c-43b0-9e3f-ecfb401e8ce1)

### AI Image Analysis Mode
![AI Image Analysis](https://github.com/user-attachments/assets/910ce6ca-402c-4a2b-94da-43f81ec9b9a7)

## 📦 Installation

### Prerequisites

- **Python 3.7+**
- **Tesseract OCR** (for multi-language OCR)
- **Poppler** (for pdf2image)

#### Install System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr poppler-utils

# Install language packs for multi-language support
sudo apt-get install tesseract-ocr-eng      # English
sudo apt-get install tesseract-ocr-ara      # Arabic
sudo apt-get install tesseract-ocr-chi-tra  # Chinese Traditional
sudo apt-get install tesseract-ocr-chi-sim  # Chinese Simplified
```

**macOS:**
```bash
brew install tesseract poppler

# Install language packs
brew install tesseract-lang
```

**Windows:**
- Download Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
  - During installation, select additional language packs: Arabic, Chinese Traditional, Chinese Simplified
- Download Poppler: https://github.com/oschwartz10612/poppler-windows/releases

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/ione2025/PDF-Extractor.git
cd PDF-Extractor
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set environment variable for Gemini API (recommended):**
```bash
# Linux/macOS
export GEMINI_API_KEY=your_api_key_here

# Windows
set GEMINI_API_KEY=your_api_key_here
```

5. **Verify Tesseract language packs:**
```bash
# Check installed languages
tesseract --list-langs

# Should show: eng, ara, chi_tra, chi_sim (and others)
```

## 🚀 Usage

### Starting the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Text Extraction Mode

1. Select **"📝 Text Extraction + OCR"** mode
2. Upload your PDF file
3. Choose extraction method (PDFPlumber or PyPDF2)
4. Enable/disable automatic OCR
5. Click **"Extract"**
6. Copy or save the extracted text

### AI Image Analysis Mode

1. Select **"🖼️ AI Image Analysis + Excel"** mode
2. Upload a PDF containing product images
3. Click **"Extract & Analyze"**
4. Monitor real-time progress with ETA
5. View extracted products with SKU, category, and descriptions
6. Download the Excel report with all product data

## 📊 Output Structure

When extracting images, files are organized as follows:

```
output/
└── [PDF_NAME]/
    ├── [PDF_NAME]_SKU_Report.xlsx     # Excel report
    ├── Gate/
    │   ├── SKU123.webp
    │   └── SKU123.json
    ├── Door/
    │   ├── SKU456.webp
    │   └── SKU456.json
    ├── Fence/
    ├── Handrail/
    └── Window Protection/
```

### JSON Metadata Format

```json
{
  "sku": "ABC123",
  "category": "Gate",
  "description": "Modern sliding gate with decorative panels",
  "svg_path": "M 10,10 L 100,10 L 100,100 L 10,100 Z",
  "primary_color": "#2C3E50",
  "secondary_color": "#ECF0F1"
}
```

### Excel Report Columns

- **SKU**: Product SKU number
- **Category**: Product category
- **Description**: AI-generated product description
- **Primary Color**: Hex code of primary color
- **Secondary Color**: Hex code of secondary color

## 🔌 API Endpoints

### `GET /`
Returns the main application interface.

### `POST /extract`
Extracts text from uploaded PDF with optional OCR.

**Parameters:**
- `file` (required): PDF file
- `method` (optional): `pdfplumber` or `pypdf2`
- `use_ocr` (optional): `true` or `false`

**Response:**
```json
{
  "success": true,
  "text": "Extracted text...",
  "filename": "document.pdf",
  "method": "pdfplumber",
  "ocr_used": true
}
```

### `POST /extract-images`
Extracts and analyzes images using AI.

**Parameters:**
- `file` (required): PDF file

**Response:**
```json
{
  "success": true,
  "filename": "catalog.pdf",
  "total_images": 15,
  "processed": 12,
  "skipped": 3,
  "results": [...],
  "excel_file": "catalog_SKU_Report.xlsx"
}
```

### `GET /progress/<task_id>`
Get real-time progress for a task.

**Response:**
```json
{
  "current": 5,
  "total": 10,
  "percentage": 50,
  "message": "Analyzing image 5/10...",
  "eta_seconds": 120
}
```

### `GET /download-excel/<filename>`
Download generated Excel report.

### `GET /health`
Health check endpoint.

## 🛠️ Technologies

### Backend
- **Flask 3.0**: Modern Python web framework
- **PyMuPDF (fitz)**: Ultra-HD PDF image extraction
- **PyPDF2 & pdfplumber**: Text extraction
- **Pytesseract**: OCR for scanned documents
- **pdf2image**: PDF to image conversion
- **Pillow**: Image processing
- **Google Generative AI**: Gemini 1.5 Flash for image analysis
- **openpyxl**: Excel report generation

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS variables
- **Vanilla JavaScript**: No framework dependencies
- **AJAX/Fetch API**: Asynchronous file uploads

### Design System
- **Dark Theme**: Professional color palette
- **CSS Variables**: Consistent theming
- **Responsive Grid**: Mobile-first approach
- **Custom Animations**: Smooth transitions
- **Typography**: Inter/SF font stack

## ⚙️ Configuration

Edit `app.py` to customize:

```python
UPLOAD_FOLDER = 'uploads'               # Temporary uploads
OUTPUT_FOLDER = 'output'                # Extracted files
MAX_CONTENT_LENGTH = 50 MB              # Max file size
GEMINI_API_KEY = os.environ.get(...)    # Use environment variable
TESSERACT_LANGUAGES = 'eng+ara+chi_tra+chi_sim'  # OCR languages
```

### Environment Variables

**Required:**
- `GEMINI_API_KEY`: Your Google Gemini API key

**Optional:**
- `FLASK_ENV`: Set to `production` for deployment
- `FLASK_DEBUG`: Set to `0` for production

### Supported OCR Languages

- **English** (eng)
- **Arabic** (ara) - العربية
- **Chinese Traditional** (chi_tra) - 中文繁體
- **Chinese Simplified** (chi_sim) - 中文简体

To add more languages, update `TESSERACT_LANGUAGES` and install the required language packs.

### Supported Categories

- Gate
- Door
- Fence
- Handrail
- Window Protection

## 🔒 Security Features

- **File Type Validation**: Only PDF files accepted
- **Secure Filename Handling**: Prevents path traversal
- **Automatic Cleanup**: Temporary files deleted after processing
- **File Size Limits**: Prevents DoS attacks
- **Input Sanitization**: XSS protection
- **API Rate Limiting**: (Recommended for production)

## 📈 Performance

- **Text Extraction**: ~1-5 seconds per PDF
- **Image Extraction**: ~30-60 seconds per image (includes AI analysis)
- **OCR Processing**: ~10-30 seconds per page
- **High-Resolution**: 300-400 DPI output quality
- **Efficient Processing**: Parallel operations where possible

## 🐛 Troubleshooting

### OCR Not Working

**Check Tesseract installation:**
```bash
tesseract --version
tesseract --list-langs
```

**Install missing language packs:**
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr-ara tesseract-ocr-chi-tra tesseract-ocr-chi-sim

# macOS
brew install tesseract-lang

# Verify installation
tesseract --list-langs | grep -E 'ara|chi'
```

**Common issues:**
- Language pack not found: Install the specific language pack
- OCR produces garbled text: Ensure correct language pack is installed
- Poor OCR quality: Try increasing PDF resolution or pre-processing images

### pdf2image Errors
```bash
# Verify Poppler installation
pdftoppm -v

# Add to PATH on Windows
```

### Gemini API Errors
- Verify API key is valid
- Check quota and billing status
- Ensure internet connectivity

### Memory Issues
- Reduce `MAX_CONTENT_LENGTH`
- Process PDFs with fewer pages
- Increase system RAM

## 🚀 Deployment

### Production Recommendations

1. **Use a production WSGI server:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Set up reverse proxy (Nginx):**
```nginx
location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

3. **Environment variables:**
```bash
export FLASK_ENV=production
export GEMINI_API_KEY=your_api_key
```

4. **Enable HTTPS** with Let's Encrypt

5. **Set up monitoring** and logging

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Credits

- **Google Gemini AI** for image analysis
- **PyMuPDF** for PDF processing
- **Tesseract OCR** for text recognition
- **Flask** for the web framework
- **huly.io** for design inspiration

## 📞 Support

If you encounter issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the API documentation

## 🎯 Roadmap

Future enhancements:
- [ ] Batch PDF processing
- [ ] PDF editing capabilities
- [ ] Custom AI training for specific product types
- [ ] Database integration for tracking
- [ ] User authentication
- [ ] Cloud storage integration
- [ ] PDF merging and splitting
- [ ] Watermark addition/removal
- [ ] Form field extraction
- [ ] Digital signature support

---

**Built with ❤️ to be the most powerful PDF tool on the internet**