# PDF Extractor Web Application

A powerful web application for extracting both text and images from PDF files, with AI-powered image analysis using Google's Gemini 1.5 Flash.

## Features

### 📝 Text Extraction
- Extract text content from PDF files
- Choose between PDFPlumber (recommended) and PyPDF2
- Copy extracted text to clipboard with one click
- Clean, readable output with page markers

### 🖼️ AI-Powered Image Extraction
- **Ultra-HD extraction** at 300-400 DPI using PyMuPDF
- **AI Analysis** with Google Gemini 1.5 Flash for each image:
  - Automatic SKU detection
  - Product category classification (Gate, Door, Fence, Handrail, Window Protection)
  - SVG path generation for 3D silhouettes
  - Primary and secondary color extraction
- **Smart Organization**: Automatically creates category-based folders
- **WebP Format**: Saves images as high-quality WebP with SKU filenames
- **Metadata Export**: Creates JSON files with SVG paths and color data
- **Intelligent Filtering**: Skips images without SKU numbers

### 🎨 Modern Interface
- Beautiful gradient design
- Responsive layout (works on desktop, tablet, and mobile)
- Dual-mode interface for text and image extraction
- Real-time progress indicators
- Comprehensive results dashboard

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Google Gemini API key (included in the code)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ione2025/PDF-Extractor.git
cd PDF-Extractor
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

### Text Extraction Mode

1. Click on "📝 Text Extraction" tab
2. Upload a PDF file
3. Choose your extraction method (PDFPlumber or PyPDF2)
4. Click "Extract Text"
5. Copy the extracted text or save it for your use

### Image Extraction Mode

1. Click on "🖼️ Image Extraction (AI)" tab
2. Upload a PDF file containing product images
3. Click "Extract Images"
4. Wait for AI analysis (may take a few minutes depending on PDF size)
5. View extracted products with SKU, category, and page information
6. Find your images organized in the `output/[PDF_NAME]/[CATEGORY]/` folders

## Output Structure

When extracting images, the application creates the following structure:

```
output/
└── [PDF_NAME]/
    ├── Gate/
    │   ├── SKU123.webp
    │   ├── SKU123.json
    │   ├── SKU456.webp
    │   └── SKU456.json
    ├── Door/
    │   └── ...
    ├── Fence/
    │   └── ...
    ├── Handrail/
    │   └── ...
    └── Window Protection/
        └── ...
```

Each JSON file contains:
```json
{
  "sku": "ABC123",
  "category": "Gate",
  "svg_path": "M 10,10 L 100,10 L 100,100 L 10,100 Z",
  "primary_color": "#2C3E50",
  "secondary_color": "#ECF0F1"
}
```

## API Endpoints

### `GET /`
Returns the main application interface.

### `POST /extract`
Extracts text from uploaded PDF file.

**Parameters:**
- `file` (required): PDF file to extract text from
- `method` (optional): Extraction method (`pdfplumber` or `pypdf2`, default: `pdfplumber`)

**Response:**
```json
{
  "success": true,
  "text": "Extracted text content...",
  "filename": "document.pdf",
  "method": "pdfplumber"
}
```

### `POST /extract-images`
Extracts and analyzes images from PDF using AI.

**Parameters:**
- `file` (required): PDF file to extract images from

**Response:**
```json
{
  "success": true,
  "filename": "catalog.pdf",
  "total_images": 15,
  "processed": 12,
  "skipped": 3,
  "results": [
    {
      "page": 1,
      "sku": "ABC123",
      "category": "Gate",
      "saved": true
    }
  ],
  "output_folder": "output/catalog"
}
```

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Project Structure

```
PDF-Extractor/
├── app.py                    # Flask application with all routes
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Main HTML interface
├── static/
│   ├── css/
│   │   └── style.css        # Responsive stylesheet
│   └── js/
│       └── script.js        # Frontend JavaScript logic
├── uploads/                 # Temporary upload directory (auto-created)
└── output/                  # Extracted images and metadata (auto-created)
```

## Technologies Used

### Backend
- **Flask**: Python web framework
- **PyPDF2**: PDF text extraction
- **PDFPlumber**: Advanced PDF text extraction
- **PyMuPDF (fitz)**: High-resolution image extraction
- **Pillow**: Image processing
- **Google Generative AI**: Gemini 1.5 Flash for image analysis

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with gradients and animations
- **JavaScript (Vanilla)**: Interactive functionality
- **AJAX**: Asynchronous file uploads

## Configuration

### Application Settings (app.py)

```python
UPLOAD_FOLDER = 'uploads'           # Temporary upload directory
OUTPUT_FOLDER = 'output'            # Image output directory
MAX_CONTENT_LENGTH = 50 MB          # Maximum file size
GEMINI_API_KEY = "YOUR_API_KEY"     # Google Gemini API key
```

### Supported Categories

- Gate
- Door
- Fence
- Handrail
- Window Protection

## Security Features

- File type validation (PDF only)
- Secure filename handling
- Automatic cleanup of temporary files
- File size limits (50MB)
- Input sanitization

## Performance Considerations

- **Text Extraction**: Fast (seconds)
- **Image Extraction**: Slower due to AI analysis (1-3 minutes per PDF depending on image count)
- High-resolution extraction uses 4x zoom matrix for 300-400 DPI quality
- Temporary files are cleaned up automatically

## Error Handling

- Graceful error messages for user-facing issues
- Automatic file cleanup on errors
- Skips images without SKU instead of failing
- Fallback values for AI analysis failures

## Troubleshooting

### Issue: Images not extracting
- Ensure PDF contains actual images (not just scanned pages)
- Check that API key is valid and has quota remaining

### Issue: No SKU detected
- Verify SKU is visible and readable in the PDF
- Try using higher quality PDF source

### Issue: Slow processing
- Normal for large PDFs with many images
- Each image requires AI analysis which takes time
- Consider processing PDFs in smaller batches

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## API Credits

This application uses Google's Gemini 1.5 Flash API for image analysis. Please ensure you comply with Google's terms of service and API usage policies.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.