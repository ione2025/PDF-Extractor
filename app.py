import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import PyPDF2
import pdfplumber

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'pdf'}

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_pypdf2(pdf_path):
    """Extract text from PDF using PyPDF2."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
    except Exception as e:
        raise Exception(f"PyPDF2 extraction failed: {str(e)}")
    
    return text


def extract_text_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)
            
            for page_num, page in enumerate(pdf.pages):
                text += f"\n--- Page {page_num + 1} ---\n"
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        raise Exception(f"pdfplumber extraction failed: {str(e)}")
    
    return text


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/extract', methods=['POST'])
def extract():
    """Handle PDF upload and text extraction."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400
    
    try:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Get extraction method from request (default to pdfplumber)
        method = request.form.get('method', 'pdfplumber')
        
        # Extract text based on selected method
        if method == 'pypdf2':
            extracted_text = extract_text_pypdf2(filepath)
        else:
            extracted_text = extract_text_pdfplumber(filepath)
        
        # Clean up - delete the uploaded file after extraction
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'text': extracted_text,
            'filename': filename,
            'method': method
        })
    
    except Exception as e:
        # Clean up file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
        
        return jsonify({
            'error': f'Extraction failed: {str(e)}'
        }), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
