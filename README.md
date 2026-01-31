# PDF Text Extractor

A modern web application for extracting text content from PDF files. Built with Flask, PyPDF2, and PDFPlumber.

## Features

- 📄 **PDF Text Extraction** - Extract text content from PDF files
- 🎯 **Multiple Extraction Methods** - Choose between PDFPlumber (recommended) and PyPDF2
- 🎨 **Modern UI** - Beautiful, responsive interface with gradient design
- 📋 **Copy to Clipboard** - Easily copy extracted text with one click
- 🔒 **Secure** - Files are automatically deleted after extraction
- 📱 **Mobile Friendly** - Works on desktop, tablet, and mobile devices

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

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

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload a PDF file and click "Extract Text" to extract the text content.

4. Choose your preferred extraction method:
   - **PDFPlumber** (Recommended) - Better handling of complex PDF layouts
   - **PyPDF2** - Faster but may struggle with some PDF formats

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
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── script.js     # Frontend JavaScript
└── uploads/              # Temporary upload directory (auto-created)
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **PDF Processing**: PyPDF2, PDFPlumber
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with gradient design

## Configuration

The application can be configured by modifying the following variables in `app.py`:

- `UPLOAD_FOLDER`: Directory for temporary file uploads (default: `uploads`)
- `MAX_CONTENT_LENGTH`: Maximum file size in bytes (default: 16MB)
- `ALLOWED_EXTENSIONS`: Allowed file extensions (default: `pdf`)

## Security Features

- File type validation
- Secure filename handling
- Automatic cleanup of uploaded files
- File size limits
- CORS protection

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.